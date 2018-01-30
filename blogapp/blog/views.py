from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import BlogCreateForm
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.

def home(request):
    return render(request,"home.html",{})

class BlogList(ListView):
    #template_name ="blog/post_list.html"
    queryset = Post.objects.all()

def MyBlogList(request):
    template_name ="blog/post_mylist.html"
    queryset = Post.objects.filter(owner=request.user)
    context = {"object_list" : queryset}
    return render(request,template_name,context)


class BlogDetail(DetailView):
    #template_name = "blog/post_detail.html"
    queryset = Post.objects.all()

class BlogCreate(LoginRequiredMixin,CreateView):
    form_class = BlogCreateForm
    login_url = '/login/'                  #after adding login mixins library do this
    template_name = "blog/forms.html"
    success_url = "/blogs/"

    def form_valid(self, form):         #not understood if user is logged in automatically it will get connected to him
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(BlogCreate,self).form_valid(form)


