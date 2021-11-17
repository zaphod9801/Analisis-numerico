from django.shortcuts import render, redirect
from MetodosApp.forms import *
from MetodosApp.Metodos import *
from MetodosApp.Evaluar import Evaluador

metodo = 0

# Create your views here.
def SelectorMetodo(request):
    if request.method == 'POST':
        formulario = SelectorMetodos(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            metodo = info['metodo']
            
            if metodo == "1":
                return redirect('/busquedaIncremental/')
            if metodo == "2":
                return redirect('/biseccion/')
            if metodo == "3":
                return redirect('/reglaFalsa/')
            if metodo == "4":
                return redirect('/puntoFijo/')
            if metodo == "5":
                return redirect('/newton/')
            if metodo == "6":
                return redirect('/secante/')
            if metodo == "7":
                return redirect('/raicesMLT/')
            if metodo == "8":
                return redirect('/gaussianaSimple/')
            if metodo == "9":
                return redirect('/gaussianaPivoteoParcial/')
            if metodo == "10":
                return redirect('/gaussianaPivoteoTotal/')
            if metodo == "11":
                return redirect('/LUsimple/')
            if metodo == "12":
                return redirect('/LUpivoteo/')
            if metodo == "13":
                return redirect('/crout/')
            if metodo == "14":
                return redirect('/doolittle/')
            if metodo == "15":
                return redirect('/cholesky/')
            if metodo == "16":
                return redirect('/jacobi/')
            if metodo == "17":
                return redirect('/seidel/')
            if metodo == "18":
                return redirect('/sor/')
            if metodo == "19":
                return redirect('/vandermonde/')
            if metodo == "20":
                return redirect('/newtonDiv/')
            if metodo == "21":
                return redirect('/lagrange/')
            if metodo == "22":
                return redirect('/trazaLineal/')
            if metodo == "23":
                return redirect('/trazaCuadro/')
            
    else:
        formulario = SelectorMetodos()
            
    contexto = {
        "formulario":formulario
    }        
                  
    return render(request,"Inicio.html",contexto)



def BusquedaIncrementalGUI(request):
    if request.method == 'POST':
        formulario = BusquedaIncrementalF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try: 
                f: str = info['funcion']
                x0: float = info['x0']
                h: float = info['h']
                n: int = info['n']
                
                resultado = Metodos.BusquedaIncremental(str(f),float(x0),float(h),int(n))
                
            except:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string, escribela normal usando formato de Python sin comillas 
                - El punto inicial es un entero o un decimal
                - El paso es un entero o un decimal
                - Las iteraciones maximas son un entero"""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Busqueda Incremental"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = BusquedaIncrementalF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Busqueda Incremental"
    }        
                     
    return render(request,"metodo.html",contexto)
  
  
def BiseccionGUI(request):
    if request.method == 'POST':
        formulario = BiseccionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                f: str = info['funcion']
                a: float = info['a']
                b: float = info['b'] 
                t: float = info['t']
                n: int = info['n']
                
                resultado = Metodos.Biseccion(str(f),float(a),float(b),float(t),int(n))
                
            except:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string, escribela normal usando formato de Python sin comillas
                - El inicio del intervalo es un entero o un decimal
                - El final del intervalo es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Bisección"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = BiseccionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Bisección"
    }        
                     
    return render(request,"metodo.html",contexto)

def ReglaFalseGUI(request):
    if request.method == 'POST':
        formulario = ReglaFalsaF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                f: str = info['funcion']
                a: float = info['a']
                b: float = info['b'] 
                t: float = info['t'] 
                n: int = info['n']
                
                resultado = Metodos.ReglaFalsa(str(f),float(a),float(b),float(t),int(n))
            
            except:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string, escribela normal usando formato de Python sin comillas
                - El inicio del intervalo es un entero o un decimal
                - El final del intervalo es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Regla Falsa"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = ReglaFalsaF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Regla Falsa"
    }        
                     
    return render(request,"metodo.html",contexto)

def PuntoFijoGUI(request):
    if request.method == 'POST':
        formulario = PuntoFijoF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                f: str = info['funcion']
                g: str = info['funcionG']
                x0: float = info['x0']
                t: float = info['t']
                n: int = info['n']
                
                resultado = Metodos.PuntoFijo(str(f),str(g),float(x0),float(t),int(n))
            
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función y la función G son un string cada una, escribelas normal usando formato de Python sin comillas
                - El punto inicial es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Punto Fijo"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = PuntoFijoF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Punto Fijo"
    }        
                     
    return render(request,"metodo.html",contexto)


def NewtonGUI(request):
    if request.method == 'POST':
        formulario = NewtonF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                f: str = info['funcion']
                f2: str = info['funcionD']
                x0: float = info['x0']
                t: float = info['t']
                n: int = info['n']
                
                resultado = Metodos.Newton(str(f),str(f2),float(x0),float(t),int(n))
            
            except:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función y su primera derivada son un string cada una, escribelas normal usando formato de Python sin comillas
                - El punto inicial es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Newton"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = NewtonF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Newton"
    }        
                     
    return render(request,"metodo.html",contexto)

def SecanteGUI(request):
    if request.method == 'POST':
        formulario = SecanteF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                f: str = info['funcion']
                x0: float = info['x0']
                x1: float = info['x1']
                t: float = info['t']
                n: int = info['n']
                              
                resultado = Metodos.Secante(str(f),float(x0),float(x1),float(t),int(n))
                
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string cada una, escribela normal usando formato de Python sin comillas
                - El punto inicial y segundo son un entero o un decimal cada uno
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Secante"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = SecanteF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Secante"
    }        
                     
    return render(request,"metodo.html",contexto)

def RaicesMLTGUI(request):
    if request.method == 'POST':
        formulario = RaicesMLTF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                f: str = info['funcion']
                f2: str = info['funcionD']
                f3: str = info['funcion2D']
                x0: float = info['x0']
                t: float = info['t']
                n: int = info['n']
                
                resultado = Metodos.RaicesMLT(str(f),str(f2),str(f3),float(x0),float(t),int(n))
            
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función, su primera derivada y segunda derivada son un string cada una, escribelas normal usando formato de Python sin comillas
                - El punto inicial es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Raices multiples"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = RaicesMLTF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Raices multiples"
    }        
                     
    return render(request,"metodo.html",contexto)


def GaussianaSimpleGUI(request):
    if request.method == 'POST':
        formulario = GaussianaSimpleF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la eliminación gaussiana simple solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.gaussiana_simple(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Eliminación Gaussiana simple"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = GaussianaSimpleF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Eliminación Gaussiana simple"
    }        
                     
    return render(request,"metodo.html",contexto)

def GaussianaPivoteoParcialGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la eliminación gaussiana solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.gaussiana_piv_parcial(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Eliminación Gaussiana con Pivoteo Parcial"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Eliminación Gaussiana con Pivoteo Parcial"
    }        
                     
    return render(request,"metodo.html",contexto)

def GaussianaPivoteoTotalGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la eliminación gaussiana solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.gaussiana_piv_total(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Eliminación Gaussiana con Pivoteo Total"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Eliminación Gaussiana con Pivoteo Total"
    }        
                     
    return render(request,"metodo.html",contexto)

def FactorLUSimpleGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la factorización LU solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.factorizacionLU_gaussiana_simple(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Factorización LU con Eliminación Gaussiana Simple"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Factorización LU con Eliminación Gaussiana Simple"
    }        
                     
    return render(request,"metodo.html",contexto)

def FactorLUPivoteoGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la factorización LU solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.factorizacionLU_gaussiana_piv_parcial(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Factorización LU con Eliminación Gaussiana con Pivoteo Parcial"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Factorización LU con Eliminación Gaussiana con Pivoteo Parcial"
    }        
                     
    return render(request,"metodo.html",contexto)

def CroutGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la factorización directa de CROUT solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.crout_decomposition(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Factorización Directa por CROUT"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Factorización Directa por CROUT"
    }        
                     
    return render(request,"metodo.html",contexto)

def DoolittleGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la factorización directa de DOOLITTLE solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.doolittle_decomposition(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Factorización Directa por DOOLITTLE"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Factorización Directa por DOOLITTLE"
    }        
                     
    return render(request,"metodo.html",contexto)

def CholeskyGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la factorización directa de CHOLESKY solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.cholesky_decomposition(matrix, terminos_ind)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Factorización Directa por CHOLESKY"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Factorización Directa por CHOLESKY"
    }        
                     
    return render(request,"metodo.html",contexto)

def JacobiGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorAproximacionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de Jacobi solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        aprox: str = info['vectorAprox']
                        vector_aprox: list = Evaluador.CrearMatriz(aprox)
                        if len(vector_aprox) != x:
                            resultado = """Las dimensiones del vector de aproximaciones no corresponde a las esperadas"""
                        else:
                            tol: float = float(info['t'])
                            iters: int = int(info['n'])
                            resultado = Metodos.jacobi_iterative(matrix, terminos_ind, vector_aprox, tol, iters)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Jacobi"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorAproximacionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Jacobi"
    }        
                     
    return render(request,"metodo.html",contexto)

def GaussSeidelGUI(request):
    if request.method == 'POST':
        formulario = MatrizVectorAproximacionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de Gauss-Seidel solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        aprox: str = info['vectorAprox']
                        vector_aprox: list = Evaluador.CrearMatriz(aprox)
                        if len(vector_aprox) != x:
                            resultado = """Las dimensiones del vector de aproximaciones no corresponde a las esperadas"""
                        else:
                            tol: float = float(info['t'])
                            iters: int = int(info['n'])
                            resultado = Metodos.gauss_seidel_iterative(matrix, terminos_ind, vector_aprox, tol, iters)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Gauss-Seidel"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = MatrizVectorAproximacionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Gauss-Seidel"
    }        
                     
    return render(request,"metodo.html",contexto)


def SORGUI(request):
    if request.method == 'POST':
        formulario = SORF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                m: str = info['matriz']
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de S.O.R solo sirve con matrices cuadradas"""
                else:
                    t: str = info['vector']
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        aprox: str = info['vectorAprox']
                        vector_aprox: list = Evaluador.CrearMatriz(aprox)
                        if len(vector_aprox) != x:
                            resultado = """Las dimensiones del vector de aproximaciones no corresponde a las esperadas"""
                        else:
                            w: float = float(info['relajacion'])
                            if w == 0:
                                resultado = """El factor de relajación debe de ser superior a cero"""
                            else:
                                tol: float = float(info['t'])
                                iters: int = int(info['n'])
                                resultado = Metodos.SOR_iterative(matrix, terminos_ind, vector_aprox, tol, iters, w)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"S.O.R"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = SORF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"S.O.R"
    }        
                     
    return render(request,"metodo.html",contexto)


def vandermondeGUI(request):
    if request.method == 'POST':
        formulario = interpolacionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                abscisas: list = Evaluador.CrearMatriz(info['vectorX'])
                ordenadas: list = Evaluador.CrearMatriz(info['vectorY'])
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.vandermonde_interpolation(abscisas, ordenadas)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Vandermonde"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = interpolacionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Vandermonde"
    }        
                     
    return render(request,"metodo.html",contexto)


def newtonDivGUI(request):
    if request.method == 'POST':
        formulario = interpolacionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                abscisas: list = Evaluador.CrearMatriz(info['vectorX'])
                ordenadas: list = Evaluador.CrearMatriz(info['vectorY'])
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.newton_diferencias_divididas(abscisas, ordenadas)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Newton Diferencias Divididas"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = interpolacionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Newton Diferencias Divididas"
    }        
                     
    return render(request,"metodo.html",contexto)

def lagrangeGUI(request):
    if request.method == 'POST':
        formulario = interpolacionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                abscisas: list = Evaluador.CrearMatriz(info['vectorX'])
                ordenadas: list = Evaluador.CrearMatriz(info['vectorY'])
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.Lagrange_interpolation(abscisas, ordenadas)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Lagrange"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = interpolacionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Lagrange"
    }        
                     
    return render(request,"metodo.html",contexto)

def trazaLinealGUI(request):
    if request.method == 'POST':
        formulario = interpolacionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                abscisas: list = Evaluador.CrearMatriz(info['vectorX'])
                ordenadas: list = Evaluador.CrearMatriz(info['vectorY'])
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.lineal_spline(abscisas, ordenadas)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Trazadores Lineales"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = interpolacionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Trazzadores Lineales"
    }        
                     
    return render(request,"metodo.html",contexto)


def trazaCuadraGUI(request):
    if request.method == 'POST':
        formulario = interpolacionF(request.POST)
        
        if formulario.is_valid():
            info = formulario.cleaned_data
            try:
                abscisas: list = Evaluador.CrearMatriz(info['vectorX'])
                ordenadas: list = Evaluador.CrearMatriz(info['vectorY'])
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.quadratic_spline(abscisas, ordenadas)
            except:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
                
            contexto = {
                "resultado":resultado,
                "titulo":"Trazadores Cuadráticos"
            } 
            
            return render(request,"resultado.html",contexto)
            
    else:
        formulario = interpolacionF()
            
    contexto = {
        "formulario":formulario,
        "titulo":"Trazzadores Cuadráticos"
    }        
                     
    return render(request,"metodo.html",contexto)