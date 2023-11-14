
from django.urls import path
from post.views import *
from post import views


urlpatterns = [
    path('',home, name ="home"), 
    path('blogs/',views.all_blogs_view, name="all_posts"),
    path('single-post/<slug:slug>/', views.Single_Post, name='single_post'),
    path('single-post/<slug:slug>/comment',views.comment_view, name ='commentview'),
    path('category/<category>',views.CatListView.as_view(),name='category'),
    path('about/', about_view, name = "about"),
    path('contact/', Contact, name = "contact"),

]