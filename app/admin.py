from django.contrib import admin
from .models import  User, MemorialPage, Tribute, Photo, VisitorComment, MemorialPageSettings, Notification
admin.site.register(User)
admin.site.register(MemorialPage)
admin.site.register(Tribute)
admin.site.register(Photo)
admin.site.register(VisitorComment)
admin.site.register(MemorialPageSettings)
admin.site.register(Notification)