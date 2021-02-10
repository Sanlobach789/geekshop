from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from mainapp import views as mainapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('baskets/', include('basketapp.urls', namespace='baskets')),
    path('admin-staff/', include('adminapp.urls', namespace='admin_staff')),
    path('avatar/', include('avatar.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
   import debug_toolbar

   urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
