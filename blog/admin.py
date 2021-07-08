from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Category)





class CommentAdmin(admin.ModelAdmin):
    list_display=['post','name','email','content']
admin.site.register(models.Comment, CommentAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ['post','user','vote']
    list_per_page = 20
admin.site.register(models.Vote,VoteAdmin)