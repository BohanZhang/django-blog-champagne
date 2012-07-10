from django.contrib import admin
from blog.models import Posts

class PostsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, PostsAdmin)
