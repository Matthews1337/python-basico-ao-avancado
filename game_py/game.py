from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)



def jogar(pontos: int) -> None:
    dificuldade: int = int(input("Informe o nível de dificuldade [1, 2, 3 ou 4]: "))
    calc: Calcular = Calcular(dificuldade)

    print("Informe o resultado para a seguinte informação: ")

    calc.mostrar_operacao()
    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f"Voce tem {pontos} ponto(s).")

    continuar: int = int(input("Deseja continuar no jogo? [1 - sim, 0 -não ]")) # numeros diferentes de 0 sao considerados True, enquanto 0 é considerado False

    if continuar:
        jogar(pontos)
    else:
        print(f"Você finalizou o jogo com {pontos} ponto(s).")





if __name__ == "__main__":
    main()