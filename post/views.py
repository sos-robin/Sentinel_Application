
from django.shortcuts import render , get_list_or_404,HttpResponseRedirect,redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from.forms import NewCommentForm , ContactForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def home(request):
    latest_featured_post = Post.objects.filter(featured=True).order_by('-timestamp').first()
    queryset = Post.objects.filter(featured=True)
    latest_posts = Post.objects.order_by('-timestamp')[:6]
    trending_posts = Post.objects.order_by('comment_count','timestamp')[:5]
    
    
    
    context = {
        'latest_featured_post': latest_featured_post,
        'object_list': queryset,
        'latest_posts': latest_posts,
        'trending_posts':trending_posts,
    }

    return render(request, 'Sentinel_App/index.html', context)

def homepage_slider_view(request):
    slider_posts = Homepage_slider.objects.order_by('-timestamp')[:5]
    context = {
        'slider_posts': slider_posts
    }
    return render(request, 'Sentinel_App/index.html', context)

#this is a generic class view
class CatListView(ListView):
    template_name = 'Sentinel_App/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content ={
            'cat':self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs
            ['category'] ).filter(featured=True)
        }
        return content
    
# this is the section to dispay posts in all the pages dont mind the name
def category_list(request):
    categorys_list = Category.objects.all() 
    category_posts =Post.objects.all() 
    recent_posts = Post.objects.order_by('-timestamp')[:6]
    about_ministry = About.objects.all()
    latest_posts = Post.objects.order_by('-timestamp')[:6]
    

    context = {
        'category_list':categorys_list,
        'category_posts': category_posts,
        'recent_posts':recent_posts,
        'about_ministry':about_ministry,
        'latest_posts':latest_posts,
        
    }
    return context
def all_blogs_view(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts,
    }

    return render(request, 'Sentinel_App/all_post.html', context)

def Single_Post(request, slug):
    
    post = get_list_or_404(Post, slug=slug, featured=True)
    
    context = {
        'posts': post,
    }
    
    return render(request, 'Sentinel_App/single-post.html', context)


def comment_view(request, slug):
    newcommentform = NewCommentForm()

    if request.method == 'POST':
        newcommentform = NewCommentForm(request.POST)
        if newcommentform.is_valid():
            cd = newcommentform.cleaned_data
            print(cd)
            new_comment = newcommentform.save(commit=False)
            new_comment.post = Post.objects.get(slug=slug)
            new_comment.save()
            
            return HttpResponseRedirect(reverse('single_post', kwargs={'slug': slug}))
    
    return render(request, 'Sentinel_App/comment.html', {'newcommentform': newcommentform})


def about_view(request):
    about_us =About.objects.all()
    team_member =TeamMember.objects.all()
    context = {
        'about_us':about_us,
        'team_member':team_member
    }
    return render(request,'Sentinel_App/about.html',context)

def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent. Thank you!")  
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'Sentinel_App/contact.html', {'form': form})



