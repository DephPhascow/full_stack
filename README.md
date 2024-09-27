# Backend template

Если модель должна поддерживать Импорт экспорт, то нужно admin.py наследоваться от ImportExportModelAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

```python
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
```
