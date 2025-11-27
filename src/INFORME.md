#INFORME DE FISICA
#Nombre:Leonel Mattias Uribe Escobar
#Grupo:D6
##Datos
# Ejemplo: Sustituye con los números que obtienes de tu terminal.
A = 0.0512
sigma_A = 0.0105
B = 0.9987
sigma_B = 0.0050
k = 39.4784
sigma_k = 0.1983

# 1. VALOR FINAL DEL COEFICIENTE B (PENDIENTE)
valor_medio_B = f"{B:.4f}"
desviacion_estandar_B = f"{sigma_B:.4f}"
# Asume la precisión del instrumento de tiempo es 0.001s
precision_instrumento = "0.001 [s]" 
valor_final_B = f"({valor_medio_B} +/- {desviacion_estandar_B}) [s^2/m]"

# 2. VALOR FINAL DE LA CONSTANTE DEL RESORTE (k)
valor_medio_k = f"{k:.4f}"
desviacion_estandar_k = f"{sigma_k:.4f}"
valor_final_k = f"({valor_medio_k} +/- {desviacion_estandar_k}) [N/m]"

# RESULTADOS 

print("## Resultados")
print(f"| Parámetro | Fórmula del ajuste | Valor |")
print("| :--- | :--- | :--- |")
print(f"| **A** (Intercepto) | $A$ | {A:.4f} +/- {sigma_A:.4f} |")
print(f"| **B** (Pendiente) | $B$ | {B:.4f} +/- {sigma_B:.4f} |")
print("")
print("### Resultados Detallados del Coeficiente B")
print(f"valor medio t = {valor_medio_B}")
print(f"desviacion estandard t = {desviacion_estandar_B}")
print(f"presicion instrumento de t = {precision_instrumento}")
print(f"valor final t = {valor_final_B}")

print("\n### Valor Final de la Constante del Resorte (k)")
print(f"valor final k = {valor_final_k}")
