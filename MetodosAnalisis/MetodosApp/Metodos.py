import abc
from re import A
import re
from numpy.core import numerictypes
from numpy.linalg.linalg import _multi_dot_matrix_chain_order
from MetodosApp.Evaluar import Evaluador
from math import sqrt
from MetodosApp.term import term
import numpy as np

class Metodos:
    
    def BusquedaIncremental(funcion: str, x0: float, paso: float, Nmax: int):
        try:
            i = 0
            xant = x0
            
            #Función evaluada en xant
            print(funcion)
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
        for a in range(len(matrix)):
            if matrix[a][a] == 0:
                return "|| Esta matriz no tiene solución usando eliminación gaussiana simple ||"
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
        
        result:str = ""
        for x in range(0, len(vector_soluc)):
            result += "X" + str(x) + "= " + str(vector_soluc[-(x + 1)]) + "\n"
        return result
    
    def gaussiana_piv_parcial(matrix: list, vector_ind: list):
        vector_soluc: list = []
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
        
        result:str = ""
        for x in range(0, len(vector_soluc)):
            result += "X" + str(x) + "= " + str(vector_soluc[-(x + 1)]) + "\n"
        return result
    
    def gaussiana_piv_total(matrix: list, vector_ind: list):
        return Evaluador.gaussiana_piv_total_aux(matrix, vector_ind, 0)
    
    def factorizacionLU_gaussiana_simple(matrix: list, vector_ind: list):
        result: str = ""
        mult_matrix: list = []
        for a in range(len(matrix)):
            mult_matrix.append([])
        for a in range(len(matrix)):
            if matrix[a][a] == 0:
                return "|| Esta matriz no tiene solución usando eliminación gaussiana simple ||"
            for b in range(a + 1, len(matrix)):
                if matrix[b][a] == 0:
                    mult_matrix[b].append(0)
                    continue
                m = matrix[b][a] / matrix[a][a]
                mult_matrix[b].append(m)
                for c in range(a, len(matrix)):
                    matrix[b][c] -= matrix[a][c] * m
            mult_matrix[a].append(1)
            while(len(mult_matrix[a]) < len(matrix)):
                mult_matrix[a].append(0)
        u_list = matrix
        l_list = mult_matrix
        result += "L = " + str(l_list) + "\n"
        result += "U = " + str(u_list) + "\n"
        result += Evaluador.LUx_equals_b(l_list, u_list, vector_ind)
        return result
    
    def factorizacionLU_gaussiana_piv_parcial(matrix: list, vector_ind: list):
        result = ""
        p_matrix: list = []
        l_matrix: list = []
        for a in range(len(matrix)):
            p_matrix.append([])
            l_matrix.append([])
            for b in range(len(matrix)):
                p_matrix[a].append(1 if a == b else 0)
                l_matrix[a].append(1 if a == b else 0)
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
                swap = p_matrix[a]
                p_matrix[a] = p_matrix[pos_supremo]
                p_matrix[pos_supremo] = swap
                swap = l_matrix[a]
                l_matrix[a] = l_matrix[pos_supremo]
                l_matrix[pos_supremo] = swap
            if piv_supremo == 0:
                return "|| Esta matriz no tiene solución logica o tiene infinitas soluciones. ||"
            for b in range(a + 1, len(matrix)):
                if matrix[b][a] == 0:
                    continue
                m = matrix[b][a] / matrix[a][a]
                for c in range(len(matrix)):
                    matrix[b][c] -= matrix[a][c] * m
                    l_matrix[b][c] -= l_matrix[a][c] * m
        u_list = matrix
        l_list = np.matmul(p_matrix, np.linalg.inv(l_matrix)).tolist()
        result += "L = " + str(l_list) + "\n"
        result += "U = " + str(u_list) + "\n"
        result += "Permutation Matrix: " + str(p_matrix) + "\n"
        vector_ind = np.matmul(p_matrix, vector_ind).tolist()
        result += Evaluador.LUx_equals_b(l_list, u_list, vector_ind)
        return result
    
    def crout_decomposition(matrix: list, vector_ind: list):
        result: str = ""
        l_matrix: list = []
        u_matrix: list = []
        for a in range(len(matrix)):
            l_matrix.append([])
            u_matrix.append([])
            for b in range(len(matrix)):
                u_matrix[a].append(1 if a == b else 0)
                l_matrix[a].append(0)
        for a in range(len(matrix)):
            for b in range(a, len(matrix)):
                sum: float = 0
                for c in range(a):
                    sum += l_matrix[b][c] * u_matrix[c][a]
                l_matrix[b][a] = (matrix[b][a] - sum)
            if a + 1 < len(matrix):
                for b in range(a + 1):
                    sum: float = 0
                    for c in range(a):
                        sum += l_matrix[b][c] * u_matrix[c][a + 1]
                    if l_matrix[b][b] == 0:
                        return "|| Division entre 0 :P ||"
                    u_matrix[b][a + 1] = (matrix[b][a + 1] - sum) / l_matrix[b][b]
        result += "L = " + str(l_matrix) + "\n"
        result += "U = " + str(u_matrix) + '\n'
        result += Evaluador.LUx_equals_b(l_matrix, u_matrix, vector_ind)
        return result
    
    def doolittle_decomposition(matrix: list, vector_ind : list):
        result: str = ""
        l_matrix: list = []
        u_matrix: list = []
        for a in range(len(matrix)):
            l_matrix.append([])
            u_matrix.append([])
            for b in range(len(matrix)):
                l_matrix[a].append(1 if a == b else 0)
                u_matrix[a].append(0)
        for a in range(len(matrix)):
            for b in range(a, len(matrix)):
                sum: float = 0
                for c in range(a):
                    sum += l_matrix[a][c] * u_matrix[c][b]
                u_matrix[a][b] = (matrix[a][b] - sum)
            if a + 1 < len(matrix):
                for b in range(a + 1):
                    sum: float = 0
                    for c in range(a):
                        sum += l_matrix[a + 1][c] * u_matrix[c][b]
                    if u_matrix[b][b] == 0:
                        return "|| Division entre 0 :P ||"
                    l_matrix[a + 1][b] = (matrix[a + 1][b] - sum) / u_matrix[b][b]
        result += "L = " + str(l_matrix) + "\n"
        result += "U = " + str(u_matrix) + '\n'
        result += Evaluador.LUx_equals_b(l_matrix, u_matrix, vector_ind)
        return result
    
    def cholesky_decomposition(matrix: list, vector_ind: list):
        result: str = ""
        l_matrix: list = []
        u_matrix: list = []
        for a in range(len(matrix)):
            l_matrix.append([])
            u_matrix.append([])
            for b in range(len(matrix)):
                l_matrix[a].append(0)
                u_matrix[a].append(0)
        for a in range(len(matrix)):
            sum: float = 0
            for b in range(a):
                sum += l_matrix[a][b] * u_matrix[b][a]
            if matrix[a][a] - sum < 0:
                return "|| Raiz cuadrada de un número negativo, este programa no soporta números imaginarios :P ||"
            u_matrix[a][a] = sqrt(matrix[a][a] - sum)
            l_matrix[a][a] = u_matrix[a][a]
            for b in range(a + 1, len(matrix)):
                sum: float = 0
                for c in range(a):
                    sum += l_matrix[a][c] * u_matrix[c][b]
                if l_matrix[a][a] == 0:
                    return " || Division entre 0 :P || "
                u_matrix[a][b] = (matrix[a][b] - sum) / l_matrix[a][a]
            for b in range(a + 1, len(matrix)):
                sum: float = 0
                for c in range(a):
                    sum += l_matrix[b][c] * u_matrix[c][a]
                if u_matrix[a][a] == 0:
                    return " || Division entre 0 :P || "
                l_matrix[b][a] = (matrix[b][a] - sum) / u_matrix[a][a]
        result += "L = " + str(l_matrix) + "\n"
        result += "U = " + str(u_matrix) + '\n'
        result += Evaluador.LUx_equals_b(l_matrix, u_matrix, vector_ind)
        return result

    def jacobi_iterative(matrix: list, vector_ind: list, vector_aprox: list, tol: float, iter_max: int):
        return Evaluador.jacobi_plus_gauss_seidel(matrix, vector_ind, vector_aprox, tol, iter_max, 0, 0)
    
    def gauss_seidel_iterative(matrix: list, vector_ind: list, vector_aprox: list, tol: float, iter_max: int):
        return Evaluador.jacobi_plus_gauss_seidel(matrix, vector_ind, vector_aprox, tol, iter_max, 1, 0)
    
    def SOR_iterative(matrix: list, vector_ind: list, vector_aprox: list, tol: float, iter_max: int, w: float):
        return Evaluador.jacobi_plus_gauss_seidel(matrix, vector_ind, vector_aprox, tol, iter_max, 2, w)
    
    def vandermonde_interpolation(abscisas: list, ordenadas: list):
        result: str = ""
        for x in range(len(abscisas)):
            n: float = abscisas[x]
            for y in range(x + 1, len(abscisas)):
                if n == abscisas[y]:
                    return "|| Es imposible interpolar estos puntos con este metodo, hay puntos repetidos en las abscisas ||"
        vandermonde: list = []
        for x in range(len(abscisas)):
            vandermonde.append([])
            for y in range(len(abscisas)):
                vandermonde[x].append(abscisas[x]**y)
        vect_resultados: list = Evaluador.gaussiana_piv_total_aux(vandermonde, ordenadas, 1)
        for x in range(len(vect_resultados) - 1, -1, -1):
            result += "(" + str(vect_resultados[x]) + " * X^" + str(x) + ") "
            if x != 0:
                result += "+ "
        return result
    
    def newton_diferencias_divididas(abscisas: list, ordenadas: list):
        result: str = ""
        for x in range(len(abscisas)):
            n: float = abscisas[x]
            for y in range(x + 1, len(abscisas)):
                if n == abscisas[y]:
                    return "|| Es imposible interpolar estos puntos con este metodo, hay puntos repetidos en las abscisas ||"
        dif_divididas: list = []
        for x in range(len(abscisas)):
            dif_divididas.append([])
            dif_divididas[x].append(ordenadas[x])
        for x in range(1, len(abscisas)):
            for y in range(x, len(abscisas)):
                dif_divididas[y].append((dif_divididas[y][x - 1] - dif_divididas[y - 1][x - 1]) / (abscisas[y] - abscisas[y - x]))
        b_vector: list = []
        for x in range(len(abscisas)):
            b_vector.append(dif_divididas[x][x])
        result += "Coeficientes del polinomio interpolante de Newton: " + str(b_vector) + '\n'
        return result
    
    def Lagrange_interpolation(abscisas: list, ordenadas: list):
        result: str = ""
        for x in range(len(abscisas)):
            n: float = abscisas[x]
            for y in range(x + 1, len(abscisas)):
                if n == abscisas[y]:
                    return "|| Es imposible interpolar estos puntos con este metodo, hay puntos repetidos en las abscisas ||"
        lagrange_polys: list = []
        x_arg: term = term(1, 1)
        n_term_1: term
        n_term_2: term
        for x in range(len(abscisas)):
            lagrange_polys.append([])
            prod_num: list = [[term(1, 0)]]
            for y in range(len(abscisas)):
                if x == y:
                    continue
                prod_num.append([])
                for a in range(len(prod_num) - 1):
                    n_term_1 = prod_num[a][0] * x_arg
                    n_term_2 = prod_num[a][0] * term(- abscisas[y], 0)
                    prod_num[n_term_1.term_exp].append(n_term_1)
                    prod_num[a][0] = n_term_2
                for a in range(len(prod_num)):
                    if len(prod_num[a]) > 1:
                        prod_num[a][0] = prod_num[a][0] + prod_num[a][1]
                        prod_num[a].pop()
            lagrange_polys[x] = prod_num
        for x in range(len(abscisas)):
            prod_den: float = 1
            for y in range(len(abscisas)):
                if x == y:
                    continue
                prod_den *= abscisas[x] - abscisas[y]
            for y in range(len(lagrange_polys[x])):
                lagrange_polys[x][y][0] *= term(1/prod_den, 0)
        for x in range(len(lagrange_polys)):
            result += "L" + str(x) + " = "
            for y in range(len(lagrange_polys[x]) - 1, -1, -1):
                result += str(lagrange_polys[x][y][0])
                result += '\n' if y == 0 else ' + '
        vector_soluc: list = []
        for x in range(len(abscisas)):
            vector_soluc.append(term(0, x))
        for x in range(len(ordenadas)):
            for y in range(len(lagrange_polys[x])):
                vector_soluc[y] += lagrange_polys[x][y][0] * term(ordenadas[x], 0)
        result += 'P(x) = '
        for x in range(len(vector_soluc) - 1, -1, -1):
            result += str(vector_soluc[x])
            result += '\n' if x == 0 else ' + '
        return result
    
    def lineal_spline(abscisas: list, ordenadas: list):
        result: str = "f(x) =\n"
        for x in range(len(abscisas)):
            n: float = abscisas[x]
            for y in range(x + 1, len(abscisas)):
                if n == abscisas[y]:
                    return "|| Es imposible interpolar estos puntos con este metodo, hay puntos repetidos en las abscisas ||"
        Evaluador.abscisa_sort(abscisas, ordenadas)
        for x in range(len(abscisas) - 1):
            matrix: list = [[abscisas[x], 1], [abscisas[x + 1], 1]]
            vector_ind: list = [ordenadas[x], ordenadas[x + 1]]
            form_result: list = Evaluador.gaussiana_piv_total_aux(matrix, vector_ind, 1)
            result += "     (" + str(form_result[0]) + " * X) + (" + str(form_result[1]) + ") | " + str(abscisas[x]) + " <= x <= " + str(abscisas[x + 1]) + '\n'
        return result
    
    def quadratic_spline(abscisas: list, ordenadas: list):
        result: str = "f(x) =\n"
        for x in range(len(abscisas)):
            n: float = abscisas[x]
            for y in range(x + 1, len(abscisas)):
                if n == abscisas[y]:
                    return "|| Es imposible interpolar estos puntos con este metodo, hay puntos repetidos en las abscisas ||"
        Evaluador.abscisa_sort(abscisas, ordenadas)
        matrix: list = []
        vector_ind: list = []
        for x in range((len(abscisas) - 1) * 3):
            matrix.append([])
            for y in range((len(abscisas) - 1) * 3):
                matrix[x].append(0)
            vector_ind.append(0)
        for x in range(len(abscisas) - 1):
            matrix[2*x][3*x] = abscisas[x]**2
            matrix[2*x][3*x + 1] = abscisas[x]
            matrix[2*x][3*x + 2] = 1
            matrix[2*x + 1][3*x] = abscisas[x+1]**2
            matrix[2*x + 1][3*x + 1] = abscisas[x + 1]
            matrix[2*x + 1][3*x + 2] = 1
            vector_ind[2*x] = ordenadas[x]
            vector_ind[2*x + 1] = ordenadas[x + 1]
        for x in range(len(abscisas) - 2):
            matrix[2*len(abscisas) + x - 2][3*x] = abscisas[x + 1]*2
            matrix[2*len(abscisas) + x - 2][3*x + 1] = 1
            matrix[2*len(abscisas) + x - 2][3*x + 3] = -abscisas[x + 1]*2
            matrix[2*len(abscisas) + x - 2][3*x + 4] = - 1
        matrix[-1][0] = 2
        form_result: list = Evaluador.gaussiana_piv_total_aux(matrix, vector_ind, 1)
        for x in range(len(abscisas) - 1):
            result += "     (" + str(form_result[x*3]) + " * X^2) + (" + str(form_result[x*3 + 1]) + " * X) + (" + str(form_result[x*3 + 2]) + ") | " + str(abscisas[x]) + " <= x <= " + str(abscisas[x + 1]) + '\n'
        return result