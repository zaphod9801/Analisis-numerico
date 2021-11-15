from math import pow, sqrt, log, log10, log2, sin, cos, tan, sinh, cosh, tanh, e, pi, factorial, acos, asin, atan, asinh, acosh, atanh, tau
from re import S

from numpy import matrix, result_type

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
    
    def gaussiana_piv_total_aux(matrix: list, vector_ind: list, interpol: int):
        vector_soluc: list = []
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
            if piv_supremo == 0:
                return "|| Esta matriz no tiene solución logica o tiene infinitas soluciones. ||"
            for b in range(a + 1, len(matrix)):
                if matrix[b][a] == 0:
                    continue
                m = matrix[b][a] / matrix[a][a]
                for c in range(a, len(matrix)):
                    matrix[b][c] -= matrix[a][c] * m
                vector_ind[b] -= vector_ind[a] * m
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
        if interpol == 1:
            return vector_soluc2
        for x in range(0, len(vector_soluc2)):
            result += "X" + str(x) + "= " + str(vector_soluc2[x]) + "\n"
        return result

    def LUx_equals_b(l_list: list, u_list: list, vector_ind: list):
        result = ""
        z_solve: list = []
        for a in range(len(l_list)):
            z: float = l_list[a][a]
            for b in range(a + 1, len(l_list)):
                if l_list[b][a] == 0:
                    continue
                m = l_list[a][a] / l_list[b][a]
                for c in range(a, len(l_list)):
                    l_list[b][c] *= m
                    l_list[b][c] -= l_list[a][c]
                vector_ind[b] *= m
                vector_ind[b] -= vector_ind[a]
            z_solve.append(vector_ind[a]/z)
        x_solve: list = []
        for a in range(len(u_list) - 1, -1, -1):
            x = u_list[a][a]
            for b in range(a):
                if u_list[b][a] == 0:
                    continue
                m = u_list[a][a] / u_list[b][a]
                for c in range(a + 1):
                    u_list[b][c] *= m
                z_solve[b] *= m
                z_solve[b] -= z_solve[a]
            x_solve.append(z_solve[a]/x)
        x_solve2: list = []
        for x in range(len(x_solve) - 1, -1, -1):
            x_solve2.append(x_solve[x])
        result += "vector resultados: " + str(x_solve2) + "\n"
        return result

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