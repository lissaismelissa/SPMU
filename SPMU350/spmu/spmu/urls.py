from django.contrib import admin
from django.urls import path, include
from main_page import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('columns_list/', include('columns_list.urls')),
    path('columns/', views.columns),
    path('columns/add_column/', views.add_column),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
