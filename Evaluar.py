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
    
    def matriz_dominante_diagonalmente(matriz: list, vector_ind: list):
        max_term: float = 0
        max_pos: float = 0
        for a in range(len(matriz)):
            max_term = abs(matriz[a][a])
            max_pos = a
            for b in range(a + 1, len(matriz)):
                if abs(matriz[b][a]) > max_term:
                    max_term = abs(matriz[b][a])
                    max_pos = b
            if max_pos != a:
                swap: list = matriz[a]
                matriz[a] = matriz[max_pos]
                matriz[max_pos] = swap
                swap = vector_ind[a]
                vector_ind[a] = vector_ind[max_pos]
                vector_ind[max_pos] = swap

if __name__=='__main__':
    print(Evaluador.CrearMatriz("[[4,5,8],[6,1,2],[1,2,3]]"))