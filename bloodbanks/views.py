from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from bloodbanks.forms import DonorUpdateForm
from bloodbanks.models import Donor
from django.contrib.auth import get_user_model

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'index.html'


@login_required(login_url='login')
def donor_view(request):
    context = {
        'donors': Donor.objects.all().filter(will_donate='Yes, I will Donate')
    }
    return render(request, 'donors.html', context)


@login_required()
def donor_public_detail_view(request):
    try:
        donor = request.user.donor
    except Donor.DoesNotExist:
        donor = Donor(user=request.user)
    context = {
        'donor': donor,
    }
    return render(request, 'donors_details.html', context)


@login_required()
def donor_detail_view(request):
    try:
        donor = request.user.donor
    except Donor.DoesNotExist:
        donor = Donor(user=request.user)
    context = {
        'donor': donor,
    }
    return render(request, 'donors_pdetails.html', context)


@login_required()
def donor_update(request):
    if request.method == 'POST':
        d_form = DonorUpdateForm(request.POST or None, instance=request.user.donor)
        if d_form.is_valid():
            d_form.save()
            messages.success(request, f'Donor Details Updated ! ')
            return redirect('profile')
        else:
            return HttpResponse('D_Form not updated')
    else:
        d_form = DonorUpdateForm(instance=request.user.donor)
    context = {
            'form': d_form,
        }
    return render(request, 'donor_form.html', context)


