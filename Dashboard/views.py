from django.shortcuts import render

def get_profile(request):
    return render(request, 'profile.html')