print("\n=== VELON Auto APP ===")
print("Bem-vindo ao sistema de compra de carros!")

modelo = input("Digite o modelo: ")
marca = input("Digite a marca: ")
ano = int(input("Digite o ano do modelo: "))
cor = input("Digite a cor do carro: ")
kms = int(input("Digite a quilometragem: "))
valor = float(input("Digite o valor: "))
cam = input("Digite o tipo de câmbio (Manual ou Automático): ")

print("\n=== Dados do Veículo ===")

print("Modelo:", modelo)
print("Marca:", marca)
print("Ano:", ano)
print("Cor:", cor)
print("Quilometragem:", kms, "km")
print("Valor: R$", valor)
print("Câmbio:", cam)

print("\n=== Análise do Veículo ===")

# Situação do veículo
if ano >= 2026:
    print("Situação: Veículo Novo")
else:
    print("Situação: Seminovo")

# Quilometragem
if kms < 30000:
    print("Baixa quilometragem")
else:
    print("Uso médio/alto")

# Mensagens das marcas
if marca == "BMW":
    print("Veículo de luxo selecionado!")

elif marca == "Toyota":
    print("Veículo conhecido pela confiabilidade!")

elif marca == "Volkswagen":
    print("Veículo popular no mercado brasileiro!")

elif marca == "BYD":
    print("Marca referência em carros elétricos!")

elif marca == "GWM":
    print("Tecnologia e inovação em destaque!")

elif marca == "Chery":
    print("Ótimo custo-benefício selecionado!")

elif marca == "Omoda":
    print("Design futurista e moderno!")

elif marca == "Jaecoo":
    print("SUV premium com estilo sofisticado!")

elif marca == "Honda":
    print("Veículo conhecido pela durabilidade!")

elif marca == "Hyundai":
    print("Tecnologia e conforto selecionados!")

elif marca == "Chevrolet":
    print("Marca tradicional no mercado!")

elif marca == "Ford":
    print("Potência e robustez selecionadas!")

elif marca == "Fiat":
    print("Veículo econômico e popular!")

elif marca == "Audi":
    print("Modelo premium e tecnológico!")

elif marca == "Mercedes":
    print("Luxo e conforto em destaque!")

elif marca == "Porsche":
    print("Esportivo de alto desempenho!")

else:
    print("Marca cadastrada com sucesso!")

# Sistema de desconto
if valor > 100000:
    desconto = valor * 0.05
    novo_valor = valor - desconto

    print("\nDesconto aplicado de 5%")
    print("Novo valor: R$", novo_valor)

print("\n=== Simulação de Financiamento ===")

salario = float(input("Digite seu salário: R$ "))

if salario >= valor / 20:
    print("Financiamento pré-aprovado!")
else:
    print("Financiamento em análise.")

print("\nObrigado por usar o VELON Auto APP!")