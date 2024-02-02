
from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-member/',views.add_member),
    path('get-member/',views.get_member),
    path('update-member/',views.update_member),
    path('get-all-member/',views.get_all_member),
    #Family Member
    path('add-family-member/',views.add_family_member),
    path('get-family-member/',views.get_family_member),
    path('update-family-member/',views.update_family_member),
    path('get-all-family-member/',views.get_all_family_member),
    path('login-family-member/',views.login_family_member),
    path('send-notification/',views.send),
    path('view-notification/',views.view_notification),
    path('update-notification/',views.update_notification),
    
    #Path
    path('add-longlat/',views.add_longlat),
    path('update-longlat/',views.update_longlat),
    path('get-longlat/',views.get_longlat),
    path('delete-family-member/',views.delete_family_member),

    path('new-update/',views.new_update),
    path('get-single-update/',views.get_single_update),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
