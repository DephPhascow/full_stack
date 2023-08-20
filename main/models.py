from django.db import models
from simple_history.models import HistoricalRecords
from ool import VersionField, VersionedMixin
from tinymce.models import HTMLField

gettext = lambda s: s

class TmpRoleEnum(models.TextChoices):
    SIMPLE = "SIMPLE", gettext("Simple")
    ADVANCED = "ADVANCED", gettext("Advanced")

class TmpModel(VersionedMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name=gettext("Название"))
    description = HTMLField(max_length=100, verbose_name=gettext("Описание"))
    role = models.CharField(max_length=100, choices=TmpRoleEnum.choices, verbose_name=gettext("Роль"), default=TmpRoleEnum.SIMPLE)
    history = HistoricalRecords()
    version = VersionField()
    class Meta:
        verbose_name = "TmpModel"
        verbose_name_plural = "TmpModels"
    def __str__(self):
        return self.name