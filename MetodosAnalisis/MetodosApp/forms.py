from django import forms


metodos = ((1,"Busqueda Incremental"),(2,"Biseccion"),(3,"Regla Falsa"),(4,"Punto fijo"),
           (5,"Newton"),(6,"Secante"),(7,"Raices Multiples"),(8,"Gaussiana Simple"),
           (9,"Gaussiana Pivoteo Parcial"),(10,"Gaussiana Pivoteo Total"),(11,"Factorización LU con eliminación gaussiana simple"),(12,"Factorización LU con pivoteo parcial"),
           (13,"Factorización directa (CROUT)"),(14,"Factorización directa (Doolittle)"),(15,"Factorización directa (Cholesky)"),(16,"Jacobi"),
           (17,"Gauss Seidel"),(18,"S.O.R."),(19,"Vandermonde"),(20,"Diferencias divididas"),(21,"Lagrange"),(22,"Trazadores lineales"),
           (23,"Trazadores cuadraticos"),
)

class SelectorMetodos(forms.Form):
    metodo: int = forms.ChoiceField(label='Metodo: ',widget=forms.Select,choices=metodos)
    

class BusquedaIncrementalF(forms.Form):
    funcion: str = forms.CharField(label='Función: ')
    x0: float = forms.FloatField(label='Punto inicial: ' )
    h: float = forms.FloatField(label='Paso: ')
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
    
class BiseccionF(forms.Form):
    funcion: str = forms.CharField(label='Función: ' )
    a: float = forms.FloatField(label='Inicio del intervalo: ' )
    b: float = forms.FloatField(label='Fin del intervalo: ' )
    t: float = forms.FloatField(label='Tolerancia: ' )
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
class ReglaFalsaF(forms.Form):
    funcion: str = forms.CharField(label='Función: ' )
    a: float = forms.FloatField(label='Inicio del intervalo: ' )
    b: float = forms.FloatField(label='Fin del intervalo: ' )
    t: float = forms.FloatField(label='Tolerancia: ' )
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
class PuntoFijoF(forms.Form):
    funcion: str = forms.CharField(label='Función: ' )
    funcionG: str = forms.CharField(label='Función: ' )
    x0: float = forms.FloatField(label='Punto inicial: ' )
    t: float = forms.FloatField(label='Tolerancia: ' )
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
class NewtonF(forms.Form):
    funcion: str = forms.CharField(label='Función: ' )
    funcionD: str = forms.CharField(label='Primera derivada de la función: ' )
    x0: float = forms.FloatField(label='Punto inicial: ' )
    t: float = forms.FloatField(label='Tolerancia: ' )
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
class SecanteF(forms.Form):
    funcion: str = forms.CharField(label='Función: ' )
    X0: float = forms.FloatField(label='Punto inicial: ' )
    X1: float = forms.FloatField(label='Segundo punto: ' )
    t: float = forms.FloatField(label='Tolerancia: ' )
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
class RaicesMLTF(forms.Form):
    funcion: str = forms.CharField(label='Función: ' )
    funcionD: str = forms.CharField(label='Primera derivada de la función: ' )
    funcion2D: str = forms.CharField(label='Segunda derivada de la función: ' )
    x0: float = forms.FloatField(label='Punto inicial: ' )
    t: float = forms.FloatField(label='Tolerancia: ' )
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
class GaussianaSimpleF(forms.Form):
    matriz: str = forms.CharField(label='Matriz de coeficientes (en formato de python): ' )
    vector: str = forms.CharField(label='Vector de terminos independientes (en formato de python): ' )
    

class MatrizVectorF(forms.Form):
    matriz: str = forms.CharField(label='Matriz de coeficientes (en formato de python): ' )
    vector: str = forms.CharField(label='Vector de terminos independientes (en formato de python): ' )
    

    
class MatrizVectorAproximacionF(forms.Form):
    matriz: str = forms.CharField(label='Matriz de coeficientes (en formato de python): ' )
    vector: str = forms.CharField(label='Vector de terminos independientes (en formato de python): ' )
    vectorAprox: str = forms.CharField(label='Vector de aproximaciones iniciales (en formato de python): ' )
    t: float = forms.FloatField(label='Tolerancia: ' )
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
    
class SORF(forms.Form):
    matriz: str = forms.CharField(label='Matriz de coeficientes (en formato de python): ' )
    vector: str = forms.CharField(label='Vector de terminos independientes (en formato de python): ' )
    vectorAprox: str = forms.CharField(label='Vector de aproximaciones iniciales (en formato de python): ' )
    relajacion: float = forms.FloatField(label='Factor de relajación: ')
    t: float = forms.FloatField(label='Tolerancia: ')
    n: int = forms.IntegerField(label='Iteraciones maximas: ' )
    
    
class interpolacionF(forms.Form):
    vectorX: str = forms.CharField(label='Vector de abscisas (en formato de python): ' )
    vectorY: str = forms.CharField(label='Vector de ordenadas (en formato de python): ')