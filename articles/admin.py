from django.contrib import admin

# Register your models here.
from .models import Articles , Comment



class CommentInline(admin.TabularInline):
    model = Comment
    
class ArticleAdmin(admin.ModelAdmin): 
    inlines = [
            CommentInline,
]
    
    
admin.site.register(Articles, ArticleAdmin)
admin.site.register(Comment)