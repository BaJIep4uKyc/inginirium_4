import random as r
r1 = 'Записал!'
r2 = 'Харош!'
r3 = 'Запомнил!'
r4 = 'Давай, хуячь этот пробел!'
r5 = 'Есть!'


button_press = 0
class Button:
    def click(self):
        global button_press
        button_press = button_press + 1

    def click_count(self):
        print(f"Твой счёт уже аж: {button_press}")

    def reset(self):
        global button_press
        button_press = 0


clicks = Button()

print('Нажми Enter, или введи: Сколько/Сначала')
while True:
    global a
    a = input('')
    if a == '':
        clicks.click()

        i = r.randint(1, 5)
        if i == 1:
            print(r1)
        elif i == 2:
            print(r2)
        elif i == 3:
            print(r3)
        elif i == 4:
            print(r4)
        elif i == 5:
            print(r5)

    elif a == 'сколько':
        clicks.click_count()

    elif a == 'сначала':
        clicks.reset()
        print('Хуячь пробел по новой!')
