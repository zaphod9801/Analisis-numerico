from Evaluar import Evaluador

class Metodos:
    
    def BusquedaIncremental(funcion: str, x0: float, paso: float, Nmax: int):
        try:
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
        except ZeroDivisionError:
            return "|| División por cero, uno de los argumentos no es valido ||"
                
    
    def Biseccion(funcion: str, a: float, b: float, tol: float, Nmax : int):
        try:
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
        except ZeroDivisionError:
            return "|| División por cero, uno de los argumentos no es valido ||"

    
    def ReglaFalsa(funcion: str, a: float, b: float, tol: float, Nmax: int):
        try:
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
        except ZeroDivisionError:
            return "|| División por cero, uno de los argumentos no es valido ||"
    
    
    def PuntoFijo(funcion: str, g: str, x0: float, tol: float, Nmax: int):
        try:
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
        except ZeroDivisionError:
            return "|| División por cero, uno de los argumentos no es valido ||"
        
    def Newton(funcion: str, funcionD: str, x0: float, tol: float, Nmax: int):
        try:
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
        except ZeroDivisionError:
            return "|| División por cero, uno de los argumentos no es valido ||"
    
    def Secante(funcion: str, x0: float, x1: float, tol: float, Nmax: int):
        try:
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
        except ZeroDivisionError:
            return "|| División por cero, uno de los argumentos no es valido ||"
            
    def RaicesMLT(funcion: str, funcionD: str, funcion2D: str, x0: float, tol: float, Nmax: int):
        try:
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
        except ZeroDivisionError:
            return "|| División por cero, uno de los argumentos no es valido ||"
    
    def gaussiana_simple(matrix: list, vector_ind: list):
        vector_soluc: list = []
        print(matrix)
        for a in range(len(matrix)):
            if matrix[a][a] == 0:
                for b in range(a + 1, len(matrix)):
                    if matrix[b][a] != 0:
                        swap: list = matrix[a]
                        matrix[a] = matrix[b]
                        matrix[b] = swap
                        swap2: int = vector_ind[a]
                        vector_ind[a] = vector_ind[b]
                        vector_ind[b] = swap2
                        print(matrix)
                        break
                if matrix[a][a] == 0:
                    return "|| Esta matriz no tiene solución logica o tiene infinitas soluciones. ||"
            for b in range(a + 1, len(matrix)):
                if matrix[b][a] == 0:
                    continue
                m = matrix[a][a] / matrix[b][a]
                for c in range(a, len(matrix)):
                    matrix[b][c] *= m
                    matrix[b][c] -= matrix[a][c]
                vector_ind[b] *= m
                vector_ind[b] -= vector_ind[a]
        for a in range(len(matrix) - 1, -1, -1):
            x = matrix[a][a]
            for b in range(a):
                if matrix[b][a] == 0:
                    continue
                m = matrix[a][a] / matrix[b][a]
                for c in range(a + 1):
                    matrix[b][c] *= m
                    matrix[b][c] -= matrix[a][c]
                vector_ind[b] *= m
                vector_ind[b] -= vector_ind[a]
            vector_soluc.append(vector_ind[a]/x)
        
        result:str = ""
        for x in range(0, len(vector_soluc)):
            result += "X" + str(x) + "= " + str(vector_soluc[-(x + 1)]) + "\n"
        return result
    
    def gaussiana_piv_parcial(matrix: list, vector_ind: list):
        vector_soluc: list = []
        print(matrix)
        for a in range(len(matrix)):
            piv_supremo: float = abs(matrix[a][a])
            pos_supremo: int = a
            for b in range(a + 1, len(matrix)):
                if abs(matrix[b][a]) > piv_supremo:
                    piv_supremo = abs(matrix[b][a])
                    pos_supremo = b
            if piv_supremo > abs(matrix[a][a]):
                swap: list = matrix[a]
                matrix[a] = matrix[pos_supremo]
                matrix[pos_supremo] = swap
                swap2: float = vector_ind[a]
                vector_ind[a] = vector_ind[pos_supremo]
                vector_ind[pos_supremo] = swap2
                print(matrix)
            if piv_supremo == 0:
                return "|| Esta matriz no tiene solución logica o tiene infinitas soluciones. ||"
            for b in range(a + 1, len(matrix)):
                if matrix[b][a] == 0:
                    continue
                m = matrix[a][a] / matrix[b][a]
                for c in range(a, len(matrix)):
                    matrix[b][c] *= m
                    matrix[b][c] -= matrix[a][c]
                vector_ind[b] *= m
                vector_ind[b] -= vector_ind[a]
        for a in range(len(matrix) - 1, -1, -1):
            x = matrix[a][a]
            for b in range(a):
                if matrix[b][a] == 0:
                    continue
                m = matrix[a][a] / matrix[b][a]
                for c in range(a + 1):
                    matrix[b][c] *= m
                    matrix[b][c] -= matrix[a][c]
                vector_ind[b] *= m
                vector_ind[b] -= vector_ind[a]
            vector_soluc.append(vector_ind[a]/x)
        
        result:str = ""
        for x in range(0, len(vector_soluc)):
            result += "X" + str(x) + "= " + str(vector_soluc[-(x + 1)]) + "\n"
        return result
    
    def gaussiana_piv_total(matrix: list, vector_ind: list):
        vector_soluc: list = []
        print(matrix)
        column_operations: list = []
        for a in range(len(matrix)):            
            piv_supremo: float = abs(matrix[a][a])
            pos_supremo_x: int = a
            pos_supremo_y: int = a
            for b in range(a, len(matrix)):
                for c in range(a, len(matrix)):
                    if abs(matrix[b][c]) > piv_supremo:
                        piv_supremo = abs(matrix[b][c])
                        pos_supremo_x = b
                        pos_supremo_y = c
            if piv_supremo > abs(matrix[a][a]):
                swap: list = matrix[a]
                matrix[a] = matrix[pos_supremo_x]
                matrix[pos_supremo_x] = swap
                swap2: float = vector_ind[a]
                vector_ind[a] = vector_ind[pos_supremo_x]
                vector_ind[pos_supremo_x] = swap2
                if pos_supremo_y != a:
                    for b in range(len(matrix)):
                        swap2 = matrix[b][a]
                        matrix[b][a] = matrix[b][pos_supremo_y]
                        matrix[b][pos_supremo_y] = swap2
                    column_operations.append(pos_supremo_y)
                    column_operations.append(a)
                print(matrix)
            if piv_supremo == 0:
                return "|| Esta matriz no tiene solución logica o tiene infinitas soluciones. ||"
            for b in range(a + 1, len(matrix)):
                if matrix[b][a] == 0:
                    continue
                m = matrix[a][a] / matrix[b][a]
                for c in range(a, len(matrix)):
                    matrix[b][c] *= m
                    matrix[b][c] -= matrix[a][c]
                vector_ind[b] *= m
                vector_ind[b] -= vector_ind[a]
        for a in range(len(matrix) - 1, -1, -1):
            x = matrix[a][a]
            for b in range(a):
                if matrix[b][a] == 0:
                    continue
                m = matrix[a][a] / matrix[b][a]
                for c in range(a + 1):
                    matrix[b][c] *= m
                    matrix[b][c] -= matrix[a][c]
                vector_ind[b] *= m
                vector_ind[b] -= vector_ind[a]
            vector_soluc.append(vector_ind[a]/x)
        
        vector_soluc2: list = []
        for x in range(0, len(vector_soluc)):
            vector_soluc2.append(vector_soluc[-(x + 1)])
        
        while len(column_operations) != 0:
            col1: int = column_operations.pop()
            col2: int = column_operations.pop()
            swap2: float = vector_soluc2[col1]
            vector_soluc2[col1] = vector_soluc2[col2]
            vector_soluc2[col2] = swap2

        result:str = ""
        for x in range(0, len(vector_soluc2)):
            result += "X" + str(x) + "= " + str(vector_soluc2[x]) + "\n"
        return result