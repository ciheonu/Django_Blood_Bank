
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as user_views
from django.contrib.auth import views as auth_views
from profiles import views as profile_views

admin.site.site_header = 'Blood Bank Admin'
admin.site.site_title = 'Blood Bank Admin'
admin.site.index_title = 'Blood Bank Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bloodbanks.urls')),
    path('profile/', profile_views.profile, name='profile'),
    path('profile_update/', profile_views.profile_update, name='profile-update'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
