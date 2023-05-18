nota1, nota2, nota3 = map(int, input().split()) #NOTAS
razao = input()
if razao == "P":
    peso1, peso2, peso3 = map(int, input().split())  # PESOS
    notaFinal = ((nota1 * peso1)+ (nota2 * peso2) + (nota3 * peso3) ) /  (peso2 + peso3 + peso1)
    print(f"Ponderada \n{notaFinal:.2f}")
elif razao == "H":
    soma_inversos = ((1 / nota1) + (1 / nota2) + (1 / nota3)) / 3
    media_harmonica = 1 / soma_inversos
    print(f"Harmonica \n{media_harmonica:.2f}")
elif razao == "A":
    print(f"Aritmetica \n{(nota1 + nota2 + nota3) / 3:.2f}")
else:
    print("Operacao inexistente")