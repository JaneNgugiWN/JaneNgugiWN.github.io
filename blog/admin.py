from django.contrib import admin
from .models import Author,Post,Tag

class PostAdmin(admin.ModelAdmin):
    list_filter=("title","author","date","tags")
    list_display=("title","date","author")
    prepopulated_fields={"slug":("title",)}
    
class AuthorAdmin(admin.ModelAdmin):
    list_filter=("firstname","email")
    list_display=("firstname","lastname","email")
    
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author,AuthorAdmin)
