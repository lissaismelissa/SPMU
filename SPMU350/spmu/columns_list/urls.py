from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.columns_list_home, name='columns_list_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ColumsDetailView.as_view(), name='column_detail'),
    path('<int:pk>/update', views.ColumsUpdateView.as_view(), name='column_update'),
    path('<int:pk>/delete', views.ColumsDeleteView.as_view(), name='column_delete')
]

#if settings.DEBUG:
  #  urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)