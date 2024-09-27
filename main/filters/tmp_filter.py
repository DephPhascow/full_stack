from django.contrib import admin

class TmpFilter(admin.SimpleListFilter):
    title ='Выбрать tmp'
    parameter_name = 'choice_tmp'
    def lookups(self, request, model_admin):
        return (
            ('A', 'A'),
            ('B', 'B'),
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        return queryset.filter(name__icontains=self.value())