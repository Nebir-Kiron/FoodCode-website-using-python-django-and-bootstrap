from django.shortcuts import redirect,render
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!  you have loggedin successfully')
            return redirect('login')
    else:
        form = RegistrationForm()
    contex = {
        'form':form,
        }
    return render(request,'users/register.html',contex)

@login_required
def profile_page(request):
    return render(request,'users/profile.html')