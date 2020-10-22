from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Set)

# Photo 클래스를 inline으로 나타낸다.
class PhotoInline(admin.TabularInline):
    model = Photo

# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

# Register your models here.
admin.site.register(Post, PostAdmin)