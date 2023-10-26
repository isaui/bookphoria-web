from django.shortcuts import render

def get_profile(request, username):
    user = username
    context = {'user': user}
    return render(request, 'profile.html', context)