from django.contrib import admin
from .models import UploadQuota, Quota

admin.site.register(UploadQuota)
admin.site.register(Quota)
