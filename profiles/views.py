from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.forms import ProfileUpdateForm
from profiles.models import Profile
from accounts.forms import CustomUserChangeForm


@login_required()
def profile(request):
    try:
        profiles = request.user.profile
    except Profile.DoesNotExist:
        profiles = Profile(user=request.user)
    context = {
        'profile': profiles,
    }
    return render(request, 'profile.html', context)


@login_required()
def profile_update(request):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'Profile Updated ! ')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = CustomUserChangeForm(request.POST, instance=request.user)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'profile_form.html', context)

