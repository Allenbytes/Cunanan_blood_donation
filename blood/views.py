from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import BloodDonationRequestForm, BloodDonationRequestUpdateForm
from .models import BloodDonationRequest
from accounts.models import Profile

@login_required
def blood_request_list(request):
    blood_requests = BloodDonationRequest.objects.all()
    return render(request, 'blood/blood_request_list.html', {'blood_requests': blood_requests})

@login_required
def blood_request_detail(request, id):
    blood_request = get_object_or_404(BloodDonationRequest, id=id)
    return render(request, 'blood/blood_request_detail.html', {'blood_request': blood_request})

@login_required
def blood_request_create(request):
    if request.method == 'POST':
        form = BloodDonationRequestForm(request.POST, user_profile=request.user.profile)
        if form.is_valid():
            blood_request = form.save(commit=False)
            if blood_request.request_type == 'donation':
                blood_request.user = request.user
                blood_request.blood_type = request.user.profile.blood_type
                blood_request.region = request.user.profile.region
                blood_request.province = request.user.profile.province
                blood_request.municipality = request.user.profile.municipality
                blood_request.save()
            else:
                blood_request.user = request.user
                blood_request.save()
            return redirect('blood_request_list')
    else:
        form = BloodDonationRequestForm(user_profile=request.user.profile)
    return render(request, 'blood/blood_request_form.html', {'form': form})

@login_required
def blood_request_update(request, id):
    blood_request = get_object_or_404(BloodDonationRequest, id=id)
    if request.method == 'POST':
        form = BloodDonationRequestUpdateForm(request.POST, instance=blood_request)
        if form.is_valid():
            form.save()
            return redirect('blood_request_detail', id=blood_request.id)
    else:
        form = BloodDonationRequestUpdateForm(instance=blood_request)
    return render(request, 'blood/blood_request_form.html', {'form': form})

@login_required
def blood_request_delete(request, id):
    blood_request = get_object_or_404(BloodDonationRequest, id=id)
    if request.method == 'POST':
        blood_request.delete()
        return redirect('blood_request_list')
    return render(request, 'blood/blood_request_confirm_delete.html', {'blood_request': blood_request})
