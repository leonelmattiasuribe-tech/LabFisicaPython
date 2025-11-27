import numpy as np

def calcular_coeficientes_mmc(X, Y):
    '''
    Calcula los coeficientes A (intercepto) y B (pendiente)
    y sus respectivos errores sigma_A y sigma_B usando Mínimos Cuadrados.
    '''
    N = len(X)
    
    # 1 CÁLCULO DE SUMATORIAS
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X * Y)
    sum_X2 = np.sum(X**2)
    
    # 2 CÁLCULO DE COEFICIENTES (A y B)
    
    # Denominador (Delta)
    Delta = (N * sum_X2) - (sum_X)**2 
    
    # Coeficiente B (Pendiente)
    B = ((N * sum_XY) - (sum_X * sum_Y)) / Delta
    
    # Coeficiente A (Intercepto)
    A = ((sum_Y * sum_X2) - (sum_X * sum_XY)) / Delta
    
    # 3 CÁLCULO DE ERRORES
    
    # Desviación estándar de Y (sy)
    sy = np.sqrt(np.sum((Y - (A + B * X))**2) / (N - 2)) 
    
    # Errores estándar de A y B
    sigma_B = sy * np.sqrt(N / Delta)
    sigma_A = sy * np.sqrt(sum_X2 / Delta)
    
    #  4 DE TODOS LOS VALORES
    return A, B, sigma_A, sigma_B 

if __name__ == '__main__':
    # Bloque de prueba (opcional)
    X_test = np.array([1.0, 2.0, 3.0, 4.0])
    Y_test = np.array([2.1, 3.9, 6.2, 7.8])
    A_r, B_r, sA_r, sB_r = calcular_coeficientes_mmc(X_test, Y_test)
    print(f"Test A: {A_r:.2f}, Test B: {B_r:.2f}")
