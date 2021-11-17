from django.urls import path
from .views import SelectorMetodo, BusquedaIncrementalGUI, BiseccionGUI, ReglaFalseGUI, PuntoFijoGUI, NewtonGUI, SecanteGUI, RaicesMLTGUI, GaussianaSimpleGUI, GaussianaPivoteoParcialGUI, GaussianaPivoteoTotalGUI, FactorLUSimpleGUI, FactorLUPivoteoGUI, CroutGUI, DoolittleGUI, CholeskyGUI, JacobiGUI, GaussSeidelGUI, SORGUI, vandermondeGUI, newtonDivGUI, lagrangeGUI, trazaLinealGUI, trazaCuadraGUI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',SelectorMetodo,name = "selector"),
    path('busquedaIncremental/',BusquedaIncrementalGUI,name = "busquedaIncremental"),
    path('biseccion/',BiseccionGUI,name = "biseccion"),
    path('reglaFalsa/',ReglaFalseGUI,name = "reglaFalsa"),
    path('puntoFijo/',PuntoFijoGUI,name = "puntoFijo"),
    path('newton/',NewtonGUI,name = "newton"),
    path('secante/',SecanteGUI,name = "secante"),
    path('raicesMLT/',RaicesMLTGUI,name = "raicesMLT"),
    path('gaussianaSimple/',GaussianaSimpleGUI,name = "gaussianaSimple"),
    path('gaussianaPivoteoParcial/',GaussianaPivoteoParcialGUI,name = "gaussianaPivoteoParcial"),
    path('gaussianaPivoteoTotal/',GaussianaPivoteoTotalGUI,name = "gaussianaPivoteoTotal"),
    path('LUsimple/',FactorLUSimpleGUI,name = "LUsimple"),
    path('LUpivoteo/',FactorLUPivoteoGUI,name = "LUpivoteo"),
    path('crout/',CroutGUI,name = "crout"),
    path('doolittle/',DoolittleGUI,name = "doolittle"),
    path('cholesky/',CholeskyGUI,name = "cholesky"),
    path('jacobi/',JacobiGUI,name = "jacobi"),
    path('seidel/',GaussSeidelGUI,name = "seidel"),
    path('sor/',SORGUI,name = "sor"),
    path('vandermonde/',vandermondeGUI,name = "vandermonde"),
    path('newtonDiv/',newtonDivGUI,name = "newtonDiv"),
    path('lagrange/',lagrangeGUI,name = "lagrange"),
    path('trazaLineal/',trazaLinealGUI,name = "trazaLineal"),
    path('trazaCuadro/',trazaCuadraGUI,name = "trazaCuadro"),
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)