from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from blogapp.models import Post
import markdown
from django.utils.safestring import mark_safe



# Create your views here.
def home(request):
    post = Post.objects.all()
    for p in post:
        p.content = mark_safe(markdown.markdown(p.content)) 
    return render(request, 'home.html', {'post': post})



def profile(request):
    return render(request,'profile.html',{})

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print("Redirecting to home")
        login(request, form.get_user())
        return redirect('home')  # or your target page
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

