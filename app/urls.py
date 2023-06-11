from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.index, name="home"),
                  path('produtos', views.produtos, name="produtos"),
                  path('sobre', views.sobre, name="sobre"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
