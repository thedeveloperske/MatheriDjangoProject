from django.shortcuts import render, redirect
from .models import MyUsers


# Create your views here.
def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        MyUsers.objects.create(name=name, email=email)
        return redirect('success')
    return render(request, 'form.html')

