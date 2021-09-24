from math import pow, sqrt, log, log10, log2, sin, cos, tan, sinh, cosh, tanh, e

class Evaluador():
    
    def Evaluar(funcion: str, x: int) -> int:
        verificador = 10
        
        try: 
            y = eval(funcion)
            verificador =  y * 10
            return y
            
        except:
            print("Función no valida")
            exit()
               
  
    