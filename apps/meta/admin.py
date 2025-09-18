from django.contrib import admin

from apps.meta.models import WatchSession,Comment,Like


admin.site.register(WatchSession)
admin.site.register(Comment)
admin.site.register(Like)