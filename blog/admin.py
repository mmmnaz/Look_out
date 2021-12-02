from django.contrib import admin
from blog.models import Post, Comment, Photo, Youtube
from embed_video.admin import AdminVideoMixin


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')


admin.site.register(Post, AuthorAdmin)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(Youtube)

