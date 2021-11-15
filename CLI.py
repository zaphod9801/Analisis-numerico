from Metodos import *
from Evaluar import Evaluador

class CLI:
    
    def EjecutarMetodo(metodo: int) -> str:
        resultado = ""
        
        if (metodo==1):
            print("-"*23+"Busqueda Incremental: "+"-"*24)
            try: 
                f: str = input("Función? ")
                x0: float = input("Punto inicial? ")
                h: float = input("Paso? ")
                n: int = input("Iteraciones maximas? ")
                print("")
                
                resultado = Metodos.BusquedaIncremental(str(f),float(x0),float(h),int(n))
                
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string, escribela normal usando formato de Python sin comillas 
                - El punto inicial es un entero o un decimal
                - El paso es un entero o un decimal
                - Las iteraciones maximas son un entero"""
            
        elif(metodo==2):
            try:
                print("-"*29+"Biseccion: "+"-"*29)
                f: str = input("Función? ")
                a: float = input("Inicio del intervalo? ")
                b: float = input("Final del intervalo? ") 
                t: float = input("Tolerancia? ")
                n: int = input("Iteraciones maximas? ")
                print("")
                
                resultado = Metodos.Biseccion(str(f),float(a),float(b),float(t),int(n))
                
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string, escribela normal usando formato de Python sin comillas
                - El inicio del intervalo es un entero o un decimal
                - El final del intervalo es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
            
        elif(metodo==3):
            try:
                print("-"*28+"Regla Falsa: "+"-"*28)
                f: str = input("Función? ")
                a: float = input("Inicio del intervalo? ")
                b: float = input("Final del intervalo? ") 
                t: float = input("Tolerancia? ")
                n: int = input("Iteraciones maximas? ")
                print("")
                
                resultado = Metodos.ReglaFalsa(str(f),float(a),float(b),float(t),int(n))
            
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string, escribela normal usando formato de Python sin comillas
                - El inicio del intervalo es un entero o un decimal
                - El final del intervalo es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
            
        elif(metodo==4):
            try:
                print("-"*28+"Punto Fijo: "+"-"*29)
                f: str = input("Función? ")
                g: str = input("Función G? ")
                x0: float = input("Punto inicial? ")
                t: float = input("Tolerancia? ")
                n: int = input("Iteraciones maximas? ")
                print("")
                
                resultado = Metodos.PuntoFijo(str(f),str(g),float(x0),float(t),int(n))
            
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función y la función G son un string cada una, escribelas normal usando formato de Python sin comillas
                - El punto inicial es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
            
        elif(metodo==5):
            try:
                print("-"*31+"Newton: "+"-"*31)
                f: str = input("Función? ")
                f2: str = input("Primera derivada de la función? ")
                x0: float = input("Punto inicial? ")
                t: float = input("Tolerancia? ")
                n: int = input("Iteraciones maximas? ")
                print("")
                
                resultado = Metodos.Newton(str(f),str(f2),float(x0),float(t),int(n))
            
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función y su primera derivada son un string cada una, escribelas normal usando formato de Python sin comillas
                - El punto inicial es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
            
        elif(metodo==6):
            try:
                print("-"*30+"Secante: "+"-"*30)
                f: str = input("Función? ")
                x0: float = input("Punto inicial? ")
                x1: float = input("Segundo punto? ")
                t: float = input("Tolerancia? ")
                n: int = input("Iteraciones maximas? ")
                print("")
                              
                resultado = Metodos.Secante(str(f),float(x0),float(x1),float(t),int(n))
                
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función es un string cada una, escribela normal usando formato de Python sin comillas
                - El punto inicial y segundo son un entero o un decimal cada uno
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
            
        elif(metodo==7):
            try:
                print("-"*28+"Raices MLT: "+"-"*29)
                f: str = input("Función? ")
                f2: str = input("Primera derivada de la función? ")
                f3: str = input("Segunda derivada de la función? ")
                x0: float = input("Punto inicial? ")
                t: float = input("Tolerancia? ")
                n: int = input("Iteraciones maximas? ")
                print("")
                
                resultado = Metodos.RaicesMLT(str(f),str(f2),str(f3),float(x0),float(t),int(n))
            
            except ValueError:
                resultado = """Un dato introducido no fue valido, recordar que: 
                - La función, su primera derivada y segunda derivada son un string cada una, escribelas normal usando formato de Python sin comillas
                - El punto inicial es un entero o un decimal
                - La toleracia es un entero o un decimal
                - Las iteraciones maximas son un entero"""
        
        elif(metodo==8):
            try:
                print("-"*28+"Eliminación Gaussiana Simple: "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)
                
                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y): 
                    resultado = """Weon, la eliminación gaussiana simple solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato de python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.gaussiana_simple(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==9):
            try:
                print("-"*28+"Eliminación Gaussiana con pivoteo parcial: "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, la eliminación gaussiana simple solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.gaussiana_piv_parcial(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==10):
            try:
                print("-"*28+"Eliminación Gaussiana con pivoteo total: "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, la elimineación gaussiana simple solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.gaussiana_piv_total(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==11):
            try:
                print("-"*28+"Factorización LU con eliminación gaussiana simple: "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, la eliminación gaussiana simple solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.factorizacionLU_gaussiana_simple(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==12):
            try:
                print("-"*28+"Factorización LU con pivoteo parcial: "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, la eliminación gaussiana simple solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.factorizacionLU_gaussiana_piv_parcial(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==13):
            try:
                print("-"*28+"Factorización directa (CROUT): "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de crout solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.crout_decomposition(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==14):
            try:
                print("-"*28+"Factorización directa (DOOLITTLE): "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de doolittle solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.doolittle_decomposition(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""

        elif(metodo==15):
            try:
                print("-"*28+"Factorización directa (CHOLESKY): "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de cholesky solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        resultado = Metodos.cholesky_decomposition(matrix, terminos_ind)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==16):
            try:
                print("-"*28+"Metodo iterativo (JACOBI): "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de cholesky solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        aprox: str = input("Vector de aproximaciones iniciales? (en formato python)")
                        vector_aprox: list = Evaluador.CrearMatriz(aprox)
                        if len(vector_aprox) != x:
                            resultado = """Las dimensiones del vector de aproximaciones no corresponde a las esperadas"""
                        else:
                            tol: float = float(input("Tolerancia minima de error? "))
                            iters: int = int(input("Numero maximo de iteraciones? "))
                            resultado = Metodos.jacobi_iterative(matrix, terminos_ind, vector_aprox, tol, iters)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""

        elif(metodo==17):
            try:
                print("-"*28+"Metodo iterativo (GAUSS-SEIDEL): "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de cholesky solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        aprox: str = input("Vector de aproximaciones iniciales? (en formato python)")
                        vector_aprox: list = Evaluador.CrearMatriz(aprox)
                        if len(vector_aprox) != x:
                            resultado = """Las dimensiones del vector de aproximaciones no corresponde a las esperadas"""
                        else:
                            tol: float = float(input("Tolerancia minima de error? "))
                            iters: int = int(input("Numero maximo de iteraciones? "))
                            resultado = Metodos.gauss_seidel_iterative(matrix, terminos_ind, vector_aprox, tol, iters)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==18):
            try:
                print("-"*28+"Metodo iterativo (S.O.R): "+"-"*29)
                m: str = input("Matriz de coeficientes? (en formato de python)")
                matrix: list = Evaluador.CrearMatriz(m)

                x: int = len(matrix)
                y: int = len(matrix[0])
                if(x != y):
                    resultado = """Weon, el algoritmo de cholesky solo sirve con matrices cuadradas"""
                else:
                    t: str = input("Vector de terminos independientes? (en formato python)")
                    terminos_ind: list = Evaluador.CrearMatriz(t)
                    if len(terminos_ind) != x:
                        resultado = """Es imposible resolver esta matriz con el vector de terminos independientes dado"""
                    else:
                        aprox: str = input("Vector de aproximaciones iniciales? (en formato python)")
                        vector_aprox: list = Evaluador.CrearMatriz(aprox)
                        if len(vector_aprox) != x:
                            resultado = """Las dimensiones del vector de aproximaciones no corresponde a las esperadas"""
                        else:
                            w: float = float(input("Factor de relajación? "))
                            if w == 0:
                                resultado = """El factor de relajación debe de ser superior a cero"""
                            else:
                                tol: float = float(input("Tolerancia minima de error? "))
                                iters: int = int(input("Numero maximo de iteraciones? "))
                                resultado = Metodos.SOR_iterative(matrix, terminos_ind, vector_aprox, tol, iters, w)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==19):
            try:
                print("-"*28+"Interpolación de VANDERMONDE: "+"-"*29)
                abscisas: list = Evaluador.CrearMatriz(input("Vector de abscisas? [En formato python]"))
                ordenadas: list = Evaluador.CrearMatriz(input("Vector de ordenadas? [En formato python]"))
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.vandermonde_interpolation(abscisas, ordenadas)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""

        elif(metodo==20):
            try:
                print("-"*28+"Interpolación de NEWTON con diferencias divididas: "+"-"*29)
                abscisas: list = Evaluador.CrearMatriz(input("Vector de abscisas? [En formato python]"))
                ordenadas: list = Evaluador.CrearMatriz(input("Vector de ordenadas? [En formato python]"))
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.newton_diferencias_divididas(abscisas, ordenadas)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==21):
            try:
                print("-"*28+"Interpolación de LAGRANGE: "+"-"*29)
                abscisas: list = Evaluador.CrearMatriz(input("Vector de abscisas? [En formato python]"))
                ordenadas: list = Evaluador.CrearMatriz(input("Vector de ordenadas? [En formato python]"))
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.Lagrange_interpolation(abscisas, ordenadas)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==22):
            try:
                print("-"*28+"Trazadores lineales: "+"-"*29)
                abscisas: list = Evaluador.CrearMatriz(input("Vector de abscisas? [En formato python]"))
                ordenadas: list = Evaluador.CrearMatriz(input("Vector de ordenadas? [En formato python]"))
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.lineal_spline(abscisas, ordenadas)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
        
        elif(metodo==23):
            try:
                print("-"*28+"Trazadores cuadraticos: "+"-"*29)
                abscisas: list = Evaluador.CrearMatriz(input("Vector de abscisas? [En formato python]"))
                ordenadas: list = Evaluador.CrearMatriz(input("Vector de ordenadas? [En formato python]"))
                if len(abscisas) != len(ordenadas):
                    resultado = "El número de abscisas dadas no concuerda con el número de ordenadas"
                else:
                    resultado = Metodos.quadratic_spline(abscisas, ordenadas)
            except ValueError:
                resultado = """Weon, algo de lo que introdujiste estaba mal."""
            
        else:
            resultado = "Opción no valida, recuerda que la opción debe ser un número del 1 al 8"
        
        return resultado
            
            
        
    def interface() -> None:
        print("-"*70)
        m: int = input("""Hola, que metodo deseas probar? Escribe el número correspondiente
              - 1: Busquedas incrementales
              - 2: Bisección
              - 3: Regla falsa
              - 4: Punto fijo
              - 5: Newton
              - 6: Secante
              - 7: Raices multiples
              - 8: Eliminación Gaussiana Simple
              - 9: Eliminación Gaussiana con pivoteo parcial
              - 10: Eliminación Gaussiana con pivoteo total
              - 11: Factorización LU con gaussiana simple
              - 12: Factorización LU con pivoteo parcial
              - 13: Factorización directa (Crout)
              - 14: Factorización directa (Doolittle)
              - 15: Factorización directa (Cholesky)
              - 16: Metodo iterativo (Jacobi)
              - 17: Metodo iterativo (Gauss-seidel)
              - 18: Metodo iterativo (S.O.R)
              - 19: Interpolación usando matriz de Vandermonde
              - 20: Interpolación de Newton con Diferencias Divididas
              - 21: Interpolación de Lagrange
              - 22: Trazadores lineales
              - 23: Trazadores cuadraticos
              """)
        try: 
            print(CLI.EjecutarMetodo(int(m)))
            print("-"*70)
            print("")
        except ValueError:
            print("Opción no valida, recuerda que la opción debe ser un número del 1 al 7")
            
if __name__=='__main__':
        CLI.interface()
            