
# 1. Separar el número en dígitos
num = input()
digitos = [int(d) for d in str(num)]

# 2. Contar cuántos dígitos son 4 o 7
num_lucky = digitos.count(4) + digitos.count(7)

if num_lucky == 4 or num_lucky == 7:
    print("YES")
else:
    print("NO")