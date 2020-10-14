from django.contrib import admin
from blog.models import blog_model, Comment
admin.site.register(blog_model)
admin.site.register(Comment)
