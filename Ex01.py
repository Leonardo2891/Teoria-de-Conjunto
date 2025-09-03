#Dados dos Conjuntos A, B, C 
A = input("Digite os números do conjunto A: ")
B = input("Digite os números do conjunto B: ")
C = input("Digite os números do conjunto C: ")

set_A = set(map(int, A.split(",")))
set_B = set(map(int, B.split(",")))
set_C = set(map(int, C.split(",")))

uniao = sorted(set_A.union(set_B).union(set_C))
print("A união entre os conjuntos:", uniao)
 
diferenca = sorted(set_A.difference(set_B).difference(set_C))
print("A diferença entre os conjuntos:", diferenca)

intersecao = sorted((set_A.intersection(set_B)).intersection(set_C))
print("A interseção entre os conjuntos:", intersecao)
