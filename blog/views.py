from django.shortcuts import render
from django.views.generic import DetailView, CreateView , UpdateView ,DeleteView
from django.urls import reverse
from .models import Post
# from django.contrib.auth.decorators import user_passes_test

def home(request):
    context = {
        'posts': Post.objects.order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Post

# @user_passes_test(lambda u: u.is_superuser)
class PostCreateView(CreateView):
    model = Post
    fields=['title','content','author','image']

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

# @user_passes_test(lambda u: u.is_superuser)
class PostUpdateView(UpdateView):
    model = Post
    fields=['title','content','author','image']

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

# @user_passes_test(lambda u: u.is_superuser)
class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog-home')
