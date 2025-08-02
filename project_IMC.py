while True:
    try:
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite o altura: "))

        resultado_Imc = peso / (altura * altura)
        
        
        if peso and altura > 0: 
            break
        else:
            print("Peso e altura invalidos. Digite um valor positivo")
    except ValueError:
        print("Entrada invalida! Digite um número.")

print(f"O peso digitado foi {peso} Kg. ")
print(f"a altura digitada foi {altura} Kg. ")

print("O seu Imc é:  ", resultado_Imc)


