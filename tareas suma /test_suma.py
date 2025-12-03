from sum import sum

print("🔍 Probando sum A+B...")

# Test 1
resultado1 = sum(3, 5)
print(f"3 + 5 = {resultado1} {'✅' if resultado1 == 8 else '❌'}")

# Test 2
resultado2 = sum(-2, 7)
print(f"-2 + 7 = {resultado2} {'✅' if resultado2 == 5 else '❌'}")

# Test 3
resultado3 = sum(0, 0)
print(f"0 + 0 = {resultado3} {'✅' if resultado3 == 0 else '❌'}")

print("🎯 ¡Tests completados!")
