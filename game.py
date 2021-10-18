from models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    df: int = int(input('Informe o nivel de dificuldade desejado [1, 2, 3]: '))
    calc: Calculate = Calculate(df)

    print('Informe o resultado para a seguinte operação: ')
    calc.show_operation()
    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'Você tem {points} ponto(s).')

    continue1: int = int(input('Deseja continuar o jogo? [1 - sim / 0 - não] '))

    if continue1:
        play(points)
    else:
        print(f'Voce finalizou com {points} ponto(s). Até a próxima!')


if __name__ == '__main__':
    main()

