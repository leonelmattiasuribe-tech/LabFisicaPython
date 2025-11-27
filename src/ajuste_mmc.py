import numpy as np

def calcular_coeficientes_mmc(X, Y):
    """
    Calcula los coeficientes A, B y sus errores (sigma_A y sigma_B) 
    usando Mínimos Cuadrados (MMC).
    """
    N = len(X)
    
    # 1. CÁLCULO DE SUMATORIAS
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X * Y)
    # Usamos multiplicación directa X * X para asegurar la potencia al cuadrado
    sum_X_sq = np.sum(X * X) 
    
    # 2. CÁLCULO DE COEFICIENTES (A y B)
    
    # Denominador (Delta)
    Delta = (N * sum_X_sq) - (sum_X * sum_X)
    
    if Delta == 0:
        return np.nan, np.nan, np.nan, np.nan

    # Coeficiente B (Pendiente)
    B = ((N * sum_XY) - (sum_X * sum_Y)) / Delta
    
    # Coeficiente A (Intercepto)
    A = ((sum_Y * sum_X_sq) - (sum_X * sum_XY)) / Delta
    
    # 3. CÁLCULO DE ERRORES
    
    # Residuos: Y_i - (A + B * X_i)
    residuos = Y - (A + B * X)
    
    # Desviación estándar de Y (sy)
    sy = np.sqrt(np.sum(residuos * residuos) / (N - 2)) 
    
    # Errores estándar de A y B
    sigma_B = sy * np.sqrt(N / Delta)
    sigma_A = sy * np.sqrt(sum_X_sq / Delta)
    
    # 4. RETORNO DE TODOS LOS VALORES
    return A, B, sigma_A, sigma_B
