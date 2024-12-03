def calcula_area(largura, comprimento):
    return largura * comprimento

def calcular_lampadas(area, potencia_watts, lampada_watts=60):
    potencia_necessaria = area * potencia_watts
    return (potencia_necessaria // lampada_watts) + (1 if potencia_necessaria % lampada_watts > 0 else 0)

def main():
    tipos_potencia = {
        0: 12,
        1: 15,
        2: 18,
        3: 20,
        4: 22
    }
    
    while True:
        tipo_comodo = int(input("Digite o tipo do cômodo (0, 2, 3, 4; 5 para terminar): "))
        if tipo_comodo == 5:
            print("Programa terminado.")
            break
        if tipo_comodo not in tipos_potencia:
            print("Tipo de cômodo inválido. Tente novamente.")
            continue
        
        largura = float(input("Digite a largura do cômodo (em metros): "))
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))
        
        area = calcula_area(largura, comprimento)
        potencia_watts = tipos_potencia[tipo_comodo]
        
        num_lampadas = calcular_lampadas(area, potencia_watts)
        
        print(f"O número de lâmpadas de 60 watts necessárias para o cômodo é: {num_lampadas}")

if __name__ == "__main__":
    main()
