from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
import adminactions.actions as actions
from main import models

@admin.register(models.TmpModel)
class TmpAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ('name', 'description', 'role', 'version', )
    history_list_display = ["date", "change_reason", "type", "user_id", "status"]
    list_display_links = ('name', )
    list_filter = ('role', )
    search_fields = ('name', 'description', )
    readonly_fields = ('version', )


admin.site.site_header = "Django Admin"
admin.site.site_title = "Django Admin Portal"
admin.site.index_title = "Welcome to Django Admin Portal"
admin.site.site_url = "/admin/"

actions.add_to_site(admin.site)