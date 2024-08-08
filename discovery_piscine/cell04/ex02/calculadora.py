def obter_numero(prompt: str) -> float:
    """Obtém um número do usuário, garantindo que a entrada seja válida."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def realizar_operacoes(num1: float, num2: float) -> tuple[float, float, float, float]:
    """Realiza operações matemáticas básicas entre dois números."""
    return (num1 + num2, num1 - num2, num1 * num2, num1 / num2 if num2 != 0 else float('inf'))

def main() -> None:
    """Função principal para executar as operações e mostrar os resultados."""
    primeiro_numero = obter_numero("Diga o primeiro número: ")
    segundo_numero = obter_numero("Diga o segundo número: ")

    soma, subtracao, multiplicacao, divisao = realizar_operacoes(primeiro_numero, segundo_numero)
    
    if segundo_numero == 0:
        print("Não é possível dividir por zero.")
        print(f"{primeiro_numero} / {segundo_numero} = Indefinido")
    else:
        print(f"{primeiro_numero} + {segundo_numero} = {soma}")
        print(f"{primeiro_numero} - {segundo_numero} = {subtracao}")
        print(f"{primeiro_numero} * {segundo_numero} = {multiplicacao}")
        print(f"{primeiro_numero} / {segundo_numero} = {divisao}")

if __name__ == "__main__":
    main()
