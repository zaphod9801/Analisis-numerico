from pybigparser import evaluator

class Metodos:
    
    def BusquedaIncremental(funcion: str, x0: int, paso: int, Nmax: int):
        f = evaluator.bigFunction()
        f.setFunction(funcion)
        i = 0
        xant = x0
        
        #Función evaluada en xant
        f.addSub("x",str(xant))
        f.evaluate()
        x = f.getSubValue("x")
        
        fant = x
        xact = xant + paso

        #Función evaluada en xact
        f.addSub("x",str(xact))
        f.evaluate()
        x2 = f.getSubValue("x")
        
        fact = x2
        
        for i in range(Nmax):
            if ((fant*fact)<0):
                break
            else:
                xant = xact
                fant = fact
                xact = xant + paso
                
                #Función evaluada en xact
                f.addSub("x",str(xact))
                f.evaluate()
                x3 = f.getSubValue("x")
                
                fact = x3
                
        a = xant
        b = xact
        iter = i
        
        return a, b, iter
                
            