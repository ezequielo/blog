from django.contrib import admin
from blog_app.models import Comment, Post

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['body']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
 
admin.site.register(Post, PostAdmin)

