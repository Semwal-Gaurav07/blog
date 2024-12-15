from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blog.models import Profile

# User Registration View
def user_register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

# Edit User Profile View
@login_required
def user_edit_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})

# Create Profile Page View
@login_required
def create_profile_page_view(request):
    if request.method == 'POST':
        form = ProfilePageForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = ProfilePageForm()
    return render(request, 'registration/create_user_profile_page.html', {'form': form})

# Edit Profile Page View
@login_required
def edit_profile_page_view(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    if request.method == 'POST':
        form = ProfilePageForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfilePageForm(instance=profile)
    return render(request, 'registration/edit_profile_page.html', {'form': form})

# Show Profile Page View
def show_profile_page_view(request, pk):
    page_user = get_object_or_404(Profile, id=pk)
    return render(request, 'registration/user_profile.html', {'page_user': page_user})

# Password Change View
@login_required
def passwords_change_view(request):
    if request.method == 'POST':
        form = PasswordChangingForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevents user from being logged out after password change
            return redirect('password_success')
    else:
        form = PasswordChangingForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

# Password Success View
def password_success(request):
    return render(request, 'registration/password_success.html', {})
