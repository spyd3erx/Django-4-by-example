from django.contrib import admin
from .models import Post

# Custom model admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] #fields to show
    list_filter = ['title', 'author', 'publish', 'status'] #list of filter
    search_fields = ['title', 'body'] #searchable fields
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']