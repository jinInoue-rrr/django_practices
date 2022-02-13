from django.contrib import admin
from .models import Post

# Register your models here.
# models.pyからPostを持ってくる

admin.site.register(Post)


