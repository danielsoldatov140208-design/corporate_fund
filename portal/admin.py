from django.contrib import admin
from portal.models import News,Document

class NewsAdmin(admin.ModelAdmin):
    list_display = ("id","title","created_at","is_published")
    search_fields = ("title","content","short_description")
    list_filter = ("is_published","created_at")
    ordering = ("is_published",)
    list_display_links = ("title","created_at","is_published")

admin.site.register(News,NewsAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id","title","created_at","is_published")
    search_fields = ("title","description")
    list_filter = ("is_published","created_at")
    list_display_links = ("title","created_at","is_published")


admin.site.register(Document,DocumentAdmin)