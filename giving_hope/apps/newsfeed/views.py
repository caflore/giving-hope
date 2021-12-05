from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

organizations = [
    {
        'author': "Red Cross",
        'title': "Donate for a better cause",
        'content': 'First cause in newsfeed',
        'date_posted': 'December 1, 2021'
    },
    {
        'author': "UNICEF",
        'title': "Donate for a better cause",
        'content': 'Second cause in newsfeed',
        'date_posted': 'December 1, 2021'
    },
    {
        'author': "World Food Programe",
        'title': "Donate for a better cause",
        'content': 'Third cause in newsfeed',
        'date_posted': 'December 1, 2021'
    },
]

# Create your views here.
def home(request):
    context = {
        'organizations': Post.objects.all()
        
    }
    return render(request, 'newsfeed/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'newsfeed/home.html'
    context_object_name = 'organizations'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['organization', 'title', 'subtitle', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['organization', 'title', 'subtitle', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/newsfeed/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'newsfeed/about.html', {'title':'About'})
