from math import pow, sqrt, log, log10, log2, sin, cos, tan, sinh, cosh, tanh, e, pi, factorial, acos, asin, atan, asinh, acosh, atanh, tau

class Evaluador():
    
    def Evaluar(funcion: str, x: float) -> float:
        verificador = 0
        
        try: 
            y = eval(funcion)
            verificador =  y / 10
            return y
            
        except:
            print("Función no valida")
            exit()
               
  
    def CrearMatriz(matriz: str) -> list:
        verificador = 0
        
        try:
            Matriz = eval(matriz)
            verificador = Matriz * 2
            return Matriz
        except:
            print("Matriz no valida")
            exit()
    
if __name__=='__main__':
    print(Evaluador.CrearMatriz("[[4,5,8],[6,1,2],[1,2,3]]"))