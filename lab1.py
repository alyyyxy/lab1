#вариант 3
import os
import time

BLUE = '\u001b[44m '   
RED = '\u001b[41m '
WHITE = '\u001b[47m '
BLACK = '\u001b[40m '
RESET = '\u001b[0m'

def draw_flag():
    print("Задание 1:")
    width = 30
    
    for f1 in range(2):
        print(RED * width + RESET)
    for f2 in range(2):
        print(WHITE * width + RESET)
    for f3 in range(2):
        print(BLUE * width + RESET)

def draw_pattern():
    pattern_template = [
        "X   XX   X",
        " X X  X X ",
        "  X    X  ",
        " X X  X X ",
        "X   XX   X"
    ]

    for line in pattern_template:
        full_line = ""
        for char in line:
            if char == 'X':
                full_line += BLACK * 2 + RESET  
            else:
                full_line += WHITE * 2 + RESET  
        print(full_line)

def draw_patternfull(u):
    print("Задание 2:")
    for y in range(u):
        draw_pattern()

def animate():
    clear_cmd = "cls" if os.name == "nt" else "clear"
    frames = [
        [RED, WHITE, WHITE, WHITE],
        [WHITE, RED, WHITE, WHITE],
        [WHITE, WHITE, RED, WHITE],
        [WHITE, WHITE, WHITE, RED]
    ]

    for frame in frames:
        os.system(clear_cmd)
        print("Задание 3:")
        print("".join(frame) + RESET)
        time.sleep(0.2)
    
def draw_diagram():
    print("Задание 4:")
    
    odds = []   
    evens = []  
    
    try:
        file = open('sequence.txt', 'r')
        for line in file:
            val = float(line.strip())
            if val >= 0:
                odds.append(val)
            else:
                evens.append(val)
        file.close()
    except FileNotFoundError:
        print("Ошибка: файл sequence.txt не найден!")
        return

    total = len(odds) + len(evens)
    if total == 0:
        print("Файл пуст.")
        return

    p_odds = (len(odds) / total) * 100
    p_evens = (len(evens) / total) * 100

    bar_odds = ' ' * int(p_odds / 2)
    bar_evens = ' ' * int(p_evens / 2)

    print(f"Положительные: {BLUE}{bar_odds}{RESET} {p_odds:.1f}% ({len(odds)} шт.)")
    print(f"Отрицательные: {RED}{bar_evens}{RESET} {p_evens:.1f}% ({len(evens)} шт.)")

#draw_flag()
#draw_patternfull(3)
#animate()
#raw_diagram()