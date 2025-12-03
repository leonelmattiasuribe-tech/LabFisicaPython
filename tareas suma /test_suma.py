import suma

# Test 1
if suma.suma(1, 2) == 3:
    print("Test 1: ✓ 1 + 2 = 3")
else:
    print("Test 1: ✗ Falló")

# Test 2  
if suma.suma(-1, -1) == -2:
    print("Test 2: ✓ -1 + (-1) = -2")
else:
    print("Test 2: ✗ Falló")

# Test 3
if suma.suma(0, 0) == 0:
    print("Test 3: ✓ 0 + 0 = 0")
else:
    print("Test 3: ✗ Falló")

print("Fin de pruebas")
