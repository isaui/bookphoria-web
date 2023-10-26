import datetime
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from Bookphoria.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from Bookphoria.models import Product, UserProfile, UserProfileForm
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Bookphoria.models import Review
from Bookphoria.forms import ReviewForm

from Homepage.models import Book

@login_required(login_url='/login')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def view_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def add_review(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']
            product = Product.objects.get(pk=product_id)  # Gantilah Product dengan model yang sesuai

            # Simpan review ke basis data
            review = Review(user=request.user, product=product, rating=rating, text=text)
            review.save()
            return redirect('review_list')  # Redirect ke halaman daftar review
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})

