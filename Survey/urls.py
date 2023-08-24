from django.contrib import admin
from django.urls import path
from Survey import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('test',views.test),
    path('data_test',views.data_test),
    path('Form_Data',views.Form_Data),
    path('PDF_FILE',views.PDF_FILE)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)