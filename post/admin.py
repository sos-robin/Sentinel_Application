from django.contrib import admin
from .models import Author, Category , Post, About,TeamMember, Contact ,Homepage_slider
from . import models
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(About)
admin.site.register(TeamMember)
admin.site.register(Contact)
admin.site.register(Homepage_slider)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email',  'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')