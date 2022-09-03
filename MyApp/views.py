from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (DetailView, ListView, UpdateView,
                                    DeleteView, CreateView, TemplateView)

from .forms import BlogCreateViewForm, BlogUpdateViewForm
# Create your views here.
class IndexListView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'post'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    
@login_required
def BlogUpdateView(request, pk):
    post = Post.objects.get(id=pk)
    form = BlogUpdateViewForm(instance=post)
    if request.method == 'POST':
        form = BlogUpdateViewForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('Xato')
    context = {'form':form}
    return render(request, 'blog/update_post.html', context)


# class BlogUpdateView(LoginRequiredMixin, UpdateView):
#     model = Post
#     fields = ['title', 'body']
#     template_name = 'blog/update_post.html'
@login_required
def BlogCreateView(request):
    form = BlogCreateViewForm()
    if request.method == 'POST':
        form = BlogCreateViewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('xato')
    context = {'form':form}
    return render(request, 'blog/create_blog.html', context)

# class BlogCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['author','title','body']
#     body = forms.CharField(widget=SummernoteWidget)
#     template_name = 'blog/create_blog.html'

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('index')



class  CommentCreateView(CreateView):
    model = Comment
    fields = ['text']
    template_name = 'blog/add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('index')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Account is NOT active")
        else:
            return HttpResponse('INVALID LOGIN REQUIRED')
    else:
        return render(request, 'registration/login.html', {})





# def base(request):
#     return render(request, 'blog/base.html')

# def blog_detail(request):
#     return render(request, 'blog/blog_detail.html')

# def index(request):
#     return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def project(request):
    return render(request, 'blog/projects.html')
