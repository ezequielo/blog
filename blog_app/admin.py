from django.contrib import admin
from blog_app.models import Comment, Post

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

    fieldsets = [
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Post',               {'fields': ['title','body']}),
#          None,               {'fields': ['body']}),
        
    ]
    inlines = [CommentInline]
    
admin.site.register(Post, PostAdmin)
