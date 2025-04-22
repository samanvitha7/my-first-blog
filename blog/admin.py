from django.contrib import admin
from .models import Post

admin.site.register(Post)

#site is an object defined in admin module . we are basiclly using default admin interface (site) to register Post models