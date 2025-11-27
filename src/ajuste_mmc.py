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
