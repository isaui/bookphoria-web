import datetime
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from Bookphoria.forms import ReviewForm
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from Bookphoria.models import EditProfileForm, Review, UserProfile, UserProfileForm
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Bookphoria.models import Review
from Bookphoria.forms import ReviewForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

import json


from Homepage.models import Book

def register(request):
    form = UserProfileForm()
    if request.method == "POST":
        username= request.POST['username']
        fullname = request.POST['fullname']
        age =int(request.POST['age'])
        country = request.POST['country']
        city = request.POST['city']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']#validasi password
        if password1 != password2:
            error_message = "Password yang dimasukkan tidak cocok. Silakan coba lagi."
            return form
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        user_profile = UserProfile(user=user,fullname = fullname, username=username, age=age, country=country, city=city, phone_number=phone_number, password= password1)
        user_profile.save() 
        messages.success(request, 'Your account has been successfully created!')
        return redirect('/login')
    context = {'form':form}
    return render(request, 'register.html', context)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("Homepage:home")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login'))
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
    return render(request, 'user.html', {'form': form})

@login_required
def view_profile(request):
    user = request.user
    userProfile = UserProfile.objects.get(user=user)
    print(userProfile.country)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'user.html', {'form': form, 'userProfile':userProfile})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'user.html', {'reviews': reviews})

def add_review(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            text = form.cleaned_data['text']
            book = Book.objects.get(pk=product_id)  # Gantilah Product dengan model yang sesuai

            # Simpan review ke basis data
            review = Review(user=request.user, product=book, rating=rating, text=text)
            review.save()
            return redirect('review_list')  # Redirect ke halaman daftar review
    else:
        form = ReviewForm()

    return render(request, 'user.html', {'form': form})

def edit_profile(request):
    form = EditProfileForm(instance=request.user)
    userProfile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  # Ganti 'profile' dengan URL profil pengguna
    return render(request, 'edituser.html', {'form': form, 'userProfile':userProfile})

@csrf_exempt
def get_previous_edit_data_json(request):
    data = json.loads(request.body)
    print(data)
    userId = data['id']
    userProfile = UserProfile.objects.get(pk=userId)
    userProfileData = {
        'username': userProfile.username,
        'password': userProfile.password,
        'fullname': userProfile.fullname,
        'age': userProfile.age,
        'country': userProfile.country,
        'city': userProfile.city,
        'phoneNumber':userProfile.phone_number

    }
    return JsonResponse(userProfileData)