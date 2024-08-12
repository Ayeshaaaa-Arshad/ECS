from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from orders import views

app_name = 'orders'

urlpatterns = [
    path('create_order', views.create_order, name = 'create_order'),
    path('delete_order', views.delete_order, name='delete_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

