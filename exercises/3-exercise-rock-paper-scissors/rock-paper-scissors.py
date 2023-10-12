import random
from colorama import Fore

rounds_to_win = 2
user_wins = 0
computer_wins = 0


def get_user_choice():
    while True:
        choice = input(
            "Elige 'piedra', 'papel' o 'tijeras' (o escribe 'salir' para salir): ")
        if choice in ['piedra', 'papel', 'tijeras', 'salir']:
            return choice
        else:
            print("Selección no válida. Por favor, elige 'piedra', 'papel' o 'tijeras', o escribe 'salir' para salir.")


def get_computer_choice():
    options = ['piedra', 'papel', 'tijeras']
    computer_choice = random.choice(options)
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == 'salir':
        return "Gracias por jugar. ¡Hasta la próxima!"

    if user_choice == computer_choice:
        return Fore.YELLOW + "Empate" + Fore.RESET
    elif (user_choice == 'piedra' and computer_choice == 'tijeras') or \
         (user_choice == 'papel' and computer_choice == 'piedra') or \
         (user_choice == 'tijeras' and computer_choice == 'papel'):
        return Fore.GREEN + "¡Ganaste!" + Fore.RESET
    else:
        return Fore.RED + "La computadora gana." + Fore.RESET


def draw_score(user_wins, computer_wins):
    print(f"[Marcador] Tú: {user_wins} - Computadora: {computer_wins}")


def main():
    global user_wins, computer_wins
    round = 1
    print("Juguemos a Piedra, Papel y Tijeras. Escribe 'salir' para terminar el juego.")

    while True:
        print(Fore.BLUE + '*' * 40 + Fore.RESET)
        print(Fore.BLUE + 'RONDA', round)
        print(Fore.BLUE + '*' * 40 + Fore.RESET)

        user_choice = get_user_choice()
        if user_choice == 'salir':
            break

        computer_choice = get_computer_choice()

        print(f"Elegiste: {user_choice}")
        print(f"La computadora eligió: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if 'Ganaste' in result:
            user_wins += 1
        elif 'computadora gana' in result:
            computer_wins += 1

        draw_score(user_wins, computer_wins)

        if user_wins == rounds_to_win:
            print(
                Fore.GREEN + "¡Felicidades! Has ganado 2 rondas de 3. ¡Ganaste el juego!" + Fore.RESET)
            break
        elif computer_wins == rounds_to_win:
            print(
                Fore.RED + "La computadora ha ganado 2 rondas de 3. ¡La computadora gana el juego!" + Fore.RESET)
            break

        round += 1


if __name__ == "__main__":
    main()
