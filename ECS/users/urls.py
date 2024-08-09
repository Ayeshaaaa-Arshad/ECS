from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views

app_name = 'users'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('logout/', views.logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

