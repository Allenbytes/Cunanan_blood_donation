from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from .forms import AdminUserForm, AdminProfileForm, AdminBloodDonationRequestForm
from .models import BloodDonationRequest
from accounts.models import Profile

User = get_user_model()

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_view(request):
    return render(request, 'admin_dashboard/admin_dashboard.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_blood_request_list(request):
    blood_requests = BloodDonationRequest.objects.all()
    return render(request, 'admin_dashboard/blood_request_list.html', {'blood_requests': blood_requests})

@user_passes_test(lambda u: u.is_superuser)
def admin_blood_request_detail(request, id):
    blood_request = get_object_or_404(BloodDonationRequest, id=id)
    return render(request, 'admin_dashboard/blood_request_detail.html', {'blood_request': blood_request})

@user_passes_test(lambda u: u.is_superuser)
def admin_delete_blood_request(request, id):
    blood_request = get_object_or_404(BloodDonationRequest, id=id)
    if request.method == 'POST':
        blood_request.delete()
        return redirect('admin_blood_request_list')
    return render(request, 'admin_dashboard/blood_request_confirm_delete.html', {'blood_request': blood_request})

@user_passes_test(lambda u: u.is_superuser)
def admin_user_list(request):
    users = User.objects.all()
    return render(request, 'admin_dashboard/user_list.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser)
def admin_edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = AdminUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_user_list')
    else:
        form = AdminUserForm(instance=user)
    return render(request, 'admin_dashboard/user_form.html', {'form': form, 'user': user})

@user_passes_test(lambda u: u.is_superuser)
def admin_delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('admin_user_list')
    return render(request, 'admin_dashboard/user_confirm_delete.html', {'user': user})
