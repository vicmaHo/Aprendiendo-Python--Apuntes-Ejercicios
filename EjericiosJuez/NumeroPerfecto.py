n = int(input())

def numero_perfecto(n):
    acc_num = 0
    for i in range(1, n):
        print(f"I: {i}")
        if n % i == 0:
            acc_num+= i
    if acc_num == n:
        return True
    else:
        return False

print(numero_perfecto(n))