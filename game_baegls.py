import random

message_hello = """
    Игра 'Beagls'
    Цель игры: Угадать число, которое загадал Beagls.
    Реакции на попытки: Pico - если игрок угадал цифру на неправильном месте
                        Fermi - если в догадке есть цифра на правильном месте
                        Bagels - если в догадке нет правильных цифр
    Настройки игры: NUM_DIGITS - размер загаданного числа
                    MAX_GUESSES - количество попыток
"""

NUM_DIGITS = 3 
MAX_GUESSES = 10


def main():
    print(message_hello)

    while True:
        # Загадываемое число
        secretNum = getSecretNum()
        print(f'''Я загадал секретное число
У тебя есть {MAX_GUESSES} попыток,
что бы угадать число.\nЧто бы выйти, введи exit''')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до получения правильной догадки:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Попытка #{numGuesses}')
                guess = input('> ')
                if guess == 'exit':
                    break

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # Правильно, выходим из цикла
            if numGuesses > MAX_GUESSES:
                print('У тебя закончились попытки.')
                print(f'Правильный ответ был: {secretNum}')

        # Спрашиваем игрока, хочет ли он сыграть еще раз.
        print('Желаешь сыграть еще разок? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Спасибо за игру!')


def getSecretNum():
    '''Возвращает строку из NUM_DIGITS уникальных случайных чисел'''
    
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    print(secretNum)
    return secretNum


def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, femi и bagels
    для получения на входе пары из догадки и секретного числа."""
    
    if guess == secretNum:
        return 'Поздравляю, ты угадал'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # Правильных цифр нет вообще
    else:
        # Сортируем подсказки в алфавитном порядке, что бы их исходный
        # порядок ничего не выдавал
        clues.sort()
        # Склеиваем список подсказок в одно строковое значение.
        return ' '.join(clues)


# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()
