from django.shortcuts import render, redirect
from .models import Contribution
from .forms import RegisterForm, LoginForm, SearchForm
from django.urls import reverse
from django.contrib.auth import logout
from django.db.models import Q
# Create your views here.

def top(request):
    if request.method == 'POST':
        loginform = LoginForm(request, data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            searchform = SearchForm()
            contributions = Contribution.objects.order_by('-created_at')
            form = RegisterForm()
            return render(request, 'top.html', {'contributions':contributions,'form':form,'loginform':loginform,'searchform':searchform,'user': user})

    searchform = SearchForm()
    loginform = LoginForm()
    contributions = Contribution.objects.order_by('-created_at')
    form = RegisterForm()
    return render(request, 'top.html',{'contributions':contributions,'form':form,'loginform':loginform,'searchform':searchform,'user': request.user})

def registration(request):
    if request.method == "POST":
        registration = RegisterForm(request.POST)
        if registration.is_valid():
            registration.save()
    
    return redirect(reverse("app:top"))

def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    
    if delete_ids:
        Contribution.objects.filter(id__in = delete_ids).delete()
    
    return redirect(reverse("app:top"))


def userlogout(request):
    logout(request)
    return redirect(reverse("app:top"))

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        search_result = Contribution.objects.all()
        if form.is_valid():
            results = search_result.filter(Q(theme__contains = form.cleaned_data['keyword'])|Q(memo__contains = form.cleaned_data['keyword']))
            
            return render(request, 'search.html', {'form':form, 'results':results})

































