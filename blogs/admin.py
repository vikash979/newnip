from django.contrib import admin
from blogs.models import blog_model, Comment
admin.site.register(blog_model)
admin.site.register(Comment)