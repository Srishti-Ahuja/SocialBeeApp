from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import decorators
from users.forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm
from users.models import Profile

# Create your views here.
def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Logged In')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='/users/login/')
def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            return render(request, 'users/registration_done.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
        user = UserEditForm(request.POST, instance=request.user)
        profile = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if user.is_valid() and profile.is_valid():
            user.save()
            profile.save()
    else:
        user = UserEditForm(instance=request.user)
        profile = ProfileEditForm(instance=request.user.profile)
        return render(request, 'users/edit_profile.html', {'user_form': user, 'profile_form': profile})
