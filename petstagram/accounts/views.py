from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login-page.html')

def register(request):
    return render(request, 'accounts/register-page.html')

def delete_page(request):
    return render(request, 'accounts/profile-delete-page.html')

def profile_details(request):
    return render(request, 'accounts/profile-details-page.html')

def profile_edit(request):
    return render(request, 'accounts/profile-edit-page.html')
