from django.shortcuts import HttpResponse,get_object_or_404
from .forms import *
from blog_app.models import BlogModel
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , logout


def Home(request):
    context={'blogs':BlogModel.objects.all()}
    return render(request, 'home.html', context)

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'register.html', {'form': form})

def login_view(request):
    n=''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log in the user
            auth_login(request, user)
            
            return redirect('home')  # Redirect to a success page or home page
        else:
            n= 'Invalid username or password.'
    
    # Render login.html for both GET and POST requests
    return render(request, 'login.html',{'n':n})

def logout_view(request):
    if request.method == 'GET':
        logout(request) 
        return redirect('home')

def add_blog(request):
    context = {'form': BlogForm()}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            title = request.POST.get('title')
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']
                image = request.FILES['image']
                blog_obj = BlogModel.objects.create(
                    user=user,
                    title=title,
                    content=content,
                    image=image
                )
                print(blog_obj)
                return redirect('home')
    except Exception as e:
        print(e)
    return render(request, 'add_blog.html', context)



def blog_detail(request, slug):
    context={}
    try:
        blog_obj=BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)


def see_blog(request):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(user=request.user)
        context['blog_obj'] = blog_obj
        if not blog_obj:
            context['message'] = "No blogs found."
    except Exception as e:
        print(e)
    return render(request, 'see_blog.html', context)


def blog_delete(request, id):
    blog_obj = get_object_or_404(BlogModel, id=id)
    
    if blog_obj.user == request.user:
        blog_obj.delete()
    else:
        return redirect('/')
    
    return redirect('see_blog')

def blog_update(request,slug):

    context={}
    try:
        
        blog_obj = BlogModel.objects.get(slug=slug)
        if blog_obj.user!=request.user:
            return redirect('/')
        initial_dict={'content':blog_obj.content}
        form=BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            title = request.POST.get('title')
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']
                image = request.FILES['image']
                blog_obj = BlogModel.objects.create(
                    user=user,
                    title=title,
                    content=content,
                    image=image
                )
                
        context['blog_obj']=blog_obj   
        context['form']=form 
    except Exception as e:
        print(e)
    return render(request, 'updateblog.html',context)