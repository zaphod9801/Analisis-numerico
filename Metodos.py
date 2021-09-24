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
                
        a = xant
        b = xact
        iter = i
        
        return a, b, iter
                
    
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
            
        return pm, i+1, E

    
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
            
        return pm, i, E
    
    
    def PuntoFijo(funcion: str, g: str, x0: int, tol: int, Nmax: int):
        xant = x0
        E = 1000
        i = 0
        
        while (E>tol and i<Nmax):
            xact =Evaluador.Evaluar(g, xant)
            E = abs(xact- xant)
            i = i+1
            xant = xact
            
        return xact, i, E
        
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
            
        return xact, i, E
    
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
            
            
        return xact, i, E
        
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
            
        return xact, i, E
             
             
if __name__ == '__main__':
    print(Metodos.Secante("x**2 + 3*x - 1",0.5,2,200,200))
        
        