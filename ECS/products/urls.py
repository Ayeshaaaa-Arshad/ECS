from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products import views

app_name = 'products'

urlpatterns = [

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

