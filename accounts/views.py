from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return HttpResponse("Welcome to AuthApp!")
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Grab the data from form submission
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # After registration, send user to login page (we’ll create it soon)
    else:
        form = UserCreationForm()  # Show an empty registration form if GET request
    return render(request, 'accounts/register.html', {'form': form})