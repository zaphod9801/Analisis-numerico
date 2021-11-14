from math import pow, sqrt, log, log10, log2, sin, cos, tan, sinh, cosh, tanh, e, pi, factorial, acos, asin, atan, asinh, acosh, atanh, tau
from re import S

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
    
    def jacobi_plus_gauss_seidel(matrix: list, vector_ind: list, vector_aprox: list, tol: float, iter_max: int, alg: int, w: float):
    # alg == 0 == Jacobi, alg == 1 == gauss seidel, alg == 2 == S.O.R
        result: str  = ""
        cur_iter : int = 0
        error: float = 0
        for x in range(len(matrix)):
            if matrix[x][x] == 0:
                return "|| Division entre cero :P esta matriz tiene un cero en la diagonal ||"
        for x in range(iter_max):
            new_aprox: list = []
            error = 0
            error_denom: float = 0
            if alg == 0:
                for a in range(len(vector_aprox)):
                    sum: float = vector_ind[a]
                    for b in range(len(matrix)):
                        if a != b:
                            sum -= vector_aprox[b] * matrix[a][b]
                    new_aprox.append(sum / matrix[a][a])
            elif alg == 1:
                for a in range(len(vector_aprox)):
                    sum: float = vector_ind[a]
                    for b in range(len(matrix)):
                        if a < b:
                            sum -= vector_aprox[b] * matrix[a][b]
                        elif a > b:
                            sum -= new_aprox[b] * matrix[a][b]
                    new_aprox.append(sum / matrix[a][a])
            elif alg == 2:
                for a in range(len(vector_aprox)):
                    sum: float = vector_ind[a]
                    for b in range(len(matrix)):
                        if a < b:
                            sum -= vector_aprox[b] * matrix[a][b]
                        elif a > b:
                            sum -= new_aprox[b] * matrix[a][b]
                    new_aprox.append((w * sum / matrix[a][a]) + ((1 - w) * vector_aprox[a]))
                print(new_aprox)
            for a in range(len(vector_aprox)):
                error += (new_aprox[a] - vector_aprox[a])**2
                error_denom += new_aprox[a]**2
            error = sqrt(error) / sqrt(error_denom)
            vector_aprox = new_aprox
            if(error < tol):
                result += "Se alcanzo la tolerancia esperada :D \n"
                cur_iter = x + 1
                break
            if x == iter_max - 1:
                result += "Se alcanzo el número maximo de iteraciones :( \n"
                cur_iter = x + 1
        result += "Vector solución alcanzado: " + str(vector_aprox) + '\n'
        result += "Número de iteraciones completadas: " + str(cur_iter) + '\n'
        result += "Error en la ultima iteracion: " + str(error) + '\n'
        return result

if __name__=='__main__':
    print(Evaluador.CrearMatriz("[[4,5,8],[6,1,2],[1,2,3]]"))