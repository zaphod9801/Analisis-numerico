from django.urls import path
from .views import SelectorMetodo, BusquedaIncrementalGUI, BiseccionGUI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',SelectorMetodo,name = "selector"),
    path('busquedaIncremental/',BusquedaIncrementalGUI,name = "busquedaIncremental"),
    path('biseccion/',BiseccionGUI,name = "biseccion"),
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)