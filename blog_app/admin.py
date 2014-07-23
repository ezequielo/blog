from django.contrib import admin
from blog_app.models import Comment, Post, Category


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'fk_cat')
    fieldsets = [
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Categoria',               {'fields': ['fk_cat']}),
        ('Post',               {'fields': ['title','body']}),
    ]
    inlines = [CommentInline]



class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['name']}),
    ]    
    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


