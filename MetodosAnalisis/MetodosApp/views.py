from django.shortcuts import render, redirect
from MetodosApp.forms import *
from MetodosApp.Metodos import *

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
