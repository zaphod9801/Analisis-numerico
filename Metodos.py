from Evaluar import Evaluador

class Metodos:
    
    def BusquedaIncremental(funcion: str, x0: int, paso: int, Nmax: int):
        i = 0
        xant = x0
        
        #Función evaluada en xant
        x = Evaluador.Evaluar(funcion, xant)
        
        fant = x
        xact = xant + paso

        #Función evaluada en xact
        x2 = Evaluador.Evaluar(funcion, xact)
        
        fact = x2
        
        for i in range(Nmax):
            if ((fant*fact)<0):
                break
            else:
                xant = xact
                fant = fact
                xact = xant + paso
                
                #Función evaluada en xact
                x3 = Evaluador.Evaluar(funcion, xact)
                
                fact = x3
                

        
        respuesta = "|| Extremo izquierdo: "+str(xant)+" || Extremo derecho: "+str(xact)+" || Iteraciones: "+str(i+1)+" ||"
        return respuesta
                
    
    def Biseccion(funcion: str, a: int, b: int, tol: int, Nmax : int):
        i = 0
        fa = Evaluador.Evaluar(funcion, a)
        pm = (a+b)/2
        fpm = Evaluador.Evaluar(funcion, pm)
        E = 1000
        
        while (E>tol and i<Nmax):
            if(fa*fpm)<0:
                 b = pm
            else:
                a = pm
            
            p0 = pm
            pm = (a+b)/2
            fpm = Evaluador.Evaluar(funcion, pm)
            E = abs(pm - p0)
            i = i + 1
        
        respuesta = "|| Solución: "+str(pm)+" || Número de iteraciones: "+str(i+1)+" || Error: "+str(E)+" ||"    
        return respuesta

    
    def ReglaFalsa(funcion: str, a: int, b: int, tol: int, Nmax: int):
        fa = Evaluador.Evaluar(funcion, a)
        fb = Evaluador.Evaluar(funcion, b)
        
        pm = (fb*a - fa*b)/(fb - fa)
        
        fpm = Evaluador.Evaluar(funcion, pm)
        E = 1000
        
        i = 1
        
        while (E>tol and i<Nmax):
            if (fa*fpm) < 0:
                b = pm
            
            else:
                a = pm
                
            p0 = pm
            pm = (fb*a - fa*b)/(fb-fa)
            fpm = Evaluador.Evaluar(funcion, pm)
            E = abs(pm-p0)
            
            i = i+1
            
        respuesta = "|| Solución: "+str(pm)+" || Número de iteraciones: "+str(i+1)+" || Error: "+str(E)+" ||"     
        return respuesta
    
    
    def PuntoFijo(funcion: str, g: str, x0: int, tol: int, Nmax: int):
        xant = x0
        E = 1000
        i = 0
        
        while (E>tol and i<Nmax):
            xact =Evaluador.Evaluar(g, xant)
            E = abs(xact- xant)
            i = i+1
            xant = xact
        
        respuesta = "|| Solución: "+str(xact)+" || Número de iteraciones: "+str(i+1)+" || Error: "+str(E)+" ||"     
        return respuesta
        
    def Newton(funcion: str, funcionD: str, x0: int, tol: int, Nmax: int):
        xant = x0
        fant = Evaluador.Evaluar(funcion, xant)
        E = 1000
        i = 0
        while (E>tol and i<Nmax):
            xact = xant - fant/(Evaluador.Evaluar(funcionD, xant))
            fact = Evaluador.Evaluar(funcion,xact)
            E = abs(xact-xant)
            i = i + 1 
            xant = xact
            fant = fact
            
        respuesta = "|| Solución: "+str(xact)+" || Número de iteraciones: "+str(i+1)+" || Error: "+str(E)+" ||"     
        return respuesta
    
    def Secante(funcion: str, x0: int, x1: int, tol: int, Nmax: int):
        f0 = Evaluador.Evaluar(funcion,x0)
        f1 = Evaluador.Evaluar(funcion,x1)
        E = 1000
        i = 1
        
        while (E>tol and i<Nmax):
            xact = x1 - f1 * ((x1-x0)/(f1-f0))
            fact = Evaluador.Evaluar(funcion,xact)
            E = abs(xact-x1)
            i = i + 1 
            x0 = x1
            f0 = f1
            x1 = xact
            f1 = fact
            
        respuesta = "|| Solución: "+str(xact)+" || Número de iteraciones: "+str(i+1)+" || Error: "+str(E)+" ||"     
        return respuesta
        
    def RaicesMLT(funcion: str, funcionD: str, funcion2D: str, x0: int, tol: int, Nmax: int):
        xant = x0
        fant = Evaluador.Evaluar(funcion, xant)
        E = 1000
        i = 0
        
        while (E>tol and i<Nmax):
            fd = Evaluador.Evaluar(funcionD,xant)
            fd2 = Evaluador.Evaluar(funcion2D,xant)
            xact = xant - fant*(fd/(fd**2-fant*fd2)) 
            fact = Evaluador.Evaluar(funcion,xact)
            E = abs(xact-xant)
            i = i + 1
            xant = xact
            fant = fact
        respuesta = "|| Solución: "+str(xact)+" || Número de iteraciones: "+str(i+1)+" || Error: "+str(E)+" ||"   
        return respuesta
             
             
if __name__ == '__main__':
    
    print("-"*30+"Secante: "+"-"*30)
    print(Metodos.Secante("x**2 + 3*x - 1",0.5,2,200,200))
    print("-"*70)
    print("")
    
    print("-"*29+"Biseccion: "+"-"*29)
    print(Metodos.Biseccion("x**2 + 3*x - 1",0.5,2,200,200))
    print("-"*70)
    print("")
    
    print("-"*23+"Busqueda Incremental: "+"-"*24)
    print(Metodos.BusquedaIncremental("x**2 + 3*x - 1",0.5,0.5,200))
    print("-"*70)
    print("")
    
    print("-"*31+"Newton: "+"-"*31)
    print(Metodos.Newton("x**2 + 3*x - 1","2*x+3",0.5,200,200))
    print("-"*70)
    print("")
    
    print("-"*28+"Punto Fijo: "+"-"*29)
    print(Metodos.PuntoFijo("x**2 + 3*x - 1","2*x+3",0.5,200,200))
    print("-"*70)
    print("")
    
    print("-"*28+"Raices MLT: "+"-"*29)
    print(Metodos.RaicesMLT("x**2 + 3*x - 1","2*x+3","2",0.5,200,200))
    print("-"*70)
    print("")
    
    print("-"*28+"Regla Falsa: "+"-"*28)
    print(Metodos.ReglaFalsa("x**2 + 3*x - 1",0.5,2,200,200))
    print("-"*70)
    print("")
        
        