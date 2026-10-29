S = input("Scrivi la string: ")
l = list(S)
v = "$"

l_esteso = l
l_esteso.append(v)
l_parole = list(l_esteso)
for i in reversed(l_esteso):
    l_parole[i] = l_esteso[i]

print(l_esteso)


print("BWT")