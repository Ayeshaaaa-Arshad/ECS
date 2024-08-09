from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from orders import views

app_name = 'orders'

urlpatterns = [

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

