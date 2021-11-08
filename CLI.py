from Metodos import *

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
                x: int = int(input("Número de filas de la matriz?"))
                y: int = int(input("Número de columnas de la matriz?"))
                if(x != y): 
                    resultado = """Weon, la reducción gaussiana simple solo sirve con matrices cuadradas"""
                else:
                    matrix: list = []
                    for a in range(x):
                        matrix.append([])
                        for b in range(y):
                            matrix[a].append(float(input("Valor de la posición [" + str(a) + "," + str(b) + "]")))
                    terminos_ind: list = []
                    for a in range(x):
                        terminos_ind.append(float(input("Valor del termino independiente " + str(a))))
                    resultado = Metodos.gaussiana_simple(matrix, terminos_ind)
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
              """)
        try: 
            print(CLI.EjecutarMetodo(int(m)))
            print("-"*70)
            print("")
        except ValueError:
            print("Opción no valida, recuerda que la opción debe ser un número del 1 al 7")
            
if __name__=='__main__':
        CLI.interface()
            