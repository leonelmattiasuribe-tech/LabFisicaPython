import numpy as np

def calcular_coeficientes_mmc(X, Y):
    """
    Calcula los coeficientes A (pendiente) y B (intercepto) 
    para el ajuste lineal Y = A*X + B usando Mínimos Cuadrados.
    """
    N = len(X)
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X * Y)
    sum_X2 = np.sum(X**2)

    A = (N * sum_XY - sum_X * sum_Y) / (N * sum_X2 - sum_X**2)

    B = (sum_Y - A * sum_X) / N

    return A, B


if __name__ == "__main__":
    X_test = np.array([1.0, 2.0, 3.0, 4.0])
    Y_test = np.array([3.0, 5.0, 7.0, 9.0])
    
    A_calc, B_calc = calcular_coeficientes_mmc(X_test, Y_test)
    
    print(f"Resultado de prueba: A={A_calc:.2f}, B={B_calc:.2f}")

calcular_coeficientes_mmc

def calcular_errores_mmc(X, Y, A, B):

    Calcula los errores estándar (delta) de los coeficientes A y B.
    
    N = len(X)
    
    # 1  Valores predichos y residuos
    Y_modelo = A * X + B
    residuos = Y - Y_modelo
    
    # 2 Desviación estándar de los residuos (Sr)
    Sr_cuadrado = np.sum(residuos**2) / (N - 2)
    Sr = np.sqrt(Sr_cuadrado)
    
    # 3 Denominador común
    sum_X2 = np.sum(X**2)
    sum_X = np.sum(X)
    Den = N * sum_X2 - sum_X**2
    
    # 4 Error de la Pendiente (Delta A)
    delta_A = Sr * np.sqrt(N / Den)
    
    # 5 Error del Intercepto (Delta B)
    delta_B = Sr * np.sqrt(sum_X2 / Den)
    
    return delta_A, delta_B
