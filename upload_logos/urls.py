from django.conf.urls import url
from upload_logos.views import upload

urlpatterns = [
    url(r'^$', upload, name='ajax-upload'),
]
