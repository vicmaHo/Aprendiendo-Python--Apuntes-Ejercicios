# Desarrollar un programa Python que permita generar y visualizar la
# siguiente figura:
# *
# **
# ***
# ****
# *****
# ******
# *******

n = int(input("Enter the number of lines: "))

line = "*"

for i in range(1, n+1):
    line = "*"
    line *= i
    print(line)
for i in range(n, 0, -1):
    line = "*"
    line *= i
    print(line)