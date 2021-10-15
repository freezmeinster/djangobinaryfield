from django.db import models

class Quota(models.Model):
    user = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.IntegerField()

class UploadQuota(models.Model):
    quotafile = models.BinaryField()
