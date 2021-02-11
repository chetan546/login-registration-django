from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import UserForm,UserProfileInfoForm
from django.urls import reverse_lazy
from django.views.generic import View,DetailView,ListView,DeleteView,UpdateView,CreateView,TemplateView
from . import models

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return render(request, 'index.html')

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')



def logoutUser(request):
    logout(request)
    return redirect('/login')


def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'register.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})





class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    fields = ("Title","Text_description")
    model = models.Post

class PostUpdateView(UpdateView):
    fields = ("Title","Text_description")
    model = models.Post

class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy('app:list')







