from django.shortcuts import render
from .models import UploadQuota
from .tasks import process_quota

def upload(request):
    if request.method == "POST":
        upload_file = request.FILES['quota']
        qt = UploadQuota.objects.create(quotafile=upload_file.read())
        process_quota(qt.id)

    return render(request, "index.html")
