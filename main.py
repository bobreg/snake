import tkinter
import random
from tkinter import messagebox

'''
Как змейка движеться
Змейка располагается на двухмерном поле, с координатами Х, У
Все координаты тела змейки находятся в массиве telo[...]
движение осуществляется по шагам с периодом 300 мс.
Главная функция движения - niam_niam()
движение осуществляется следующим образом:
- в хвосте змейки перекрашивается в цвет поля последняя клетка
- в зависимости от вектора движения (w,a,s,d) следующая клетка по пути движения проверяется на 
  наличие мыши (black). Если мыши нет, то клетка проверяется на наличие стенки или собственного тела и в конце 
  в массив координат добавляется в начало новый элемент с координатами головы и впереди идущая клетка 
  перекрашивается в цвет змейки (gray1). Затем из массива удаляется последний элемент с коорлинатами хвоста змейки
- если по пути встречается мышь, то на этом шаге не удаляется из массива последний элемент и вся змейка удлинняется

'''

def vektorw(event):
    global vektor, last_vektor
    last_vektor = vektor
    if last_vektor != 's':
        vektor = 'w'


def vektora(event):
    global vektor, last_vektor
    last_vektor = vektor
    if last_vektor != 'd':
        vektor = 'a'


def vektors(event):
    global vektor, last_vektor
    last_vektor = vektor
    if last_vektor != 'w':
        vektor = 's'


def vektord(event):
    global vektor, last_vektor
    last_vektor = vektor
    if last_vektor != 'a':
        vektor = 'd'


def pause(event):
    global a
    pole_game.after_cancel(a)


def add_mouse():
    global vektor, telo
    if vektor == 'w':
        if globals()['label{}*{}'.format(telo[0][0] - 1, telo[0][1])]['bg'] == 'black':
            while True:
                x = random.randrange(1, 40, 1)
                y = random.randrange(1, 40, 1)
                if [y, x] not in telo:
                    break
            globals()['label{}*{}'.format(y, x)]['bg'] = 'black'
            shet['text'] = len(telo) - 4
        else:
            telo.pop(-1)
    elif vektor == 'a':
        if globals()['label{}*{}'.format(telo[0][0], telo[0][1]-1)]['bg'] == 'black':
            while True:
                x = random.randrange(1, 40, 1)
                y = random.randrange(1, 40, 1)
                if [y, x] not in telo:
                    break
            globals()['label{}*{}'.format(y, x)]['bg'] = 'black'
            shet['text'] = len(telo) - 4
        else:
            telo.pop(-1)
    elif vektor == 's':
        if globals()['label{}*{}'.format(telo[0][0] + 1, telo[0][1])]['bg'] == 'black':
            while True:
                x = random.randrange(1, 40, 1)
                y = random.randrange(1, 40, 1)
                if [y, x] not in telo:
                    break
            globals()['label{}*{}'.format(y, x)]['bg'] = 'black'
            shet['text'] = len(telo) - 4
        else:
            telo.pop(-1)
    elif vektor == 'd':
        if globals()['label{}*{}'.format(telo[0][0], telo[0][1]+1)]['bg'] == 'black':
            while True:
                x = random.randrange(1, 40, 1)
                y = random.randrange(1, 40, 1)
                if [y, x] not in telo:
                    break
            globals()['label{}*{}'.format(y, x)]['bg'] = 'black'
            shet['text'] = len(telo) - 4
        else:
            telo.pop(-1)


def start():
    global a
    text_motivation['text'] = 'Ну давай\nещё разок'
    a = pole_game.after(300, niam_niam)


def niam_niam():  # главная функция движения
    global vektor, last_vektor, a, telo, last_len_telo
    a = pole_game.after(100, niam_niam)  # повтор этой функции через 100 мс
    globals()['label{}*{}'.format(telo[-1][0], telo[-1][1])]['bg'] = 'linen'  # перекрасим клетку хвоста в цвет поля

    # участок кода с выводом тупых фразочек в зависимости от длинны змейки------------
    len_telo = len(telo)

    if 10 <= len_telo < 15:
        text_motivation['text'] = 'Молодец.\nУже что-то.'
    elif 15 <= len_telo < 20:
        text_motivation['text'] = 'Давай.\nПродолжай.'
    elif 20 <= len_telo < 25:
        text_motivation['text'] = 'Блестяще!.'
    elif 25 <= len_telo < 30:
        text_motivation['text'] = 'Аплодисменты\nтвоему терпению!'
    elif len_telo >= 30 and len_telo % 5 == 0 and last_len_telo != len_telo:
        text_motivation['text'] = random.choice(phrases)
    last_len_telo = len_telo
    # --------------------------------------------------------------------
    # обработка впереди стоящей клетки в зависимости от вектора движения
    if vektor == 'w':
        add_mouse()
        telo.insert(0, [telo[0][0] - 1, telo[0][1]])
    elif vektor == 'd':
        add_mouse()
        telo.insert(0, [telo[0][0], telo[0][1]+1])
    elif vektor == 'a':
        add_mouse()
        telo.insert(0, [telo[0][0], telo[0][1]-1])
    elif vektor == 's':
        add_mouse()
        telo.insert(0, [telo[0][0] + 1, telo[0][1]])

    if globals()['label{}*{}'.format(telo[0][0], telo[0][1])]['bg'] == 'linen' or globals()['label{}*{}'.format(telo[0][0], telo[0][1])]['bg'] == 'black':
        globals()['label{}*{}'.format(telo[0][0], telo[0][1])]['bg'] = 'gray1'
    else:
        text_motivation['text'] = random.choice(['Лошара!','Тебя на долго не хватило\nкак полторашки пива'])
        pole_game.after_cancel(a)
        messagebox.showinfo('Ахтунг!', message='You lose (.Y.)')
        telo = [[20, 25], [19, 25], [18, 25], [17, 25], [16, 25]]
        telo.reverse()
        vektor = 'w'
        last_vektor = 's'
        for i in range(1, 40):
            for j in range(1 ,40):
                globals()['label{}*{}'.format(i, j)]['bg'] = 'linen'
        globals()['label{}*{}'.format(random.randrange(1, 40, 1), random.randrange(1, 40, 1))]['bg'] = 'black'


pole_game = tkinter.Tk()
pole_game.title('Змейка от Alex_chel_man')
pole_game.geometry('1200x900')
# ------------создадим поле и надписи----------------
for i in range(41):
    for j in range(41):
        globals()['label{}*{}'.format(i, j)] = tkinter.Label(text='     ', bg='linen', relief='groove')
        globals()['label{}*{}'.format(i, j)].grid(row=i, column=j)

label_name = tkinter.Label(text='Змейка', font='Arial 14')
label_name.place(x=900, y=250)
button_start = tkinter.Button(text='Старт', font='Arial 20', command=start)
button_start.place(x=900, y=400)
text_motivation = tkinter.Label(text='Ну покажи на\nчто ты способен!', font='Arial 15')
text_motivation.place(x=900, y=150)
label_shet = tkinter.Label(text='Счёт:           ', font='Arial 15', relief='groove')
label_shet.place(x=900, y=70)
shet = tkinter.Label(text=0, font='Arial 13')
shet.place(x=952, y=72)
info = tkinter.Label(text='По пробелу пауза\nУправление движением -\n w a s d (англ)', font='Arial 15')
info.place(x=900, y=500)
#--------------------------------------------------------------------
telo = [[20, 25], [19, 25], [18, 25], [17, 25], [16, 25]]  # создаём начальное тело змейки
telo.reverse()  # перевернём массив, ибо я его в начале не правильно записал
vektor = 'w'  # начальное положение вектора движения
last_vektor = 's'  # положение противоположного вектора движения (это что бы не пустить змейку саму в себя)
last_len_telo = 0  # переменная для сравнения длинн змейки (нужна для фразочек)
phrases = ['охуеть',
           'эмм...',
           '29 см отращиваешь?',
           'Мамку позови',
           'Терминатор, блядь',
           'Ну теперь\nдлиннее чем\nу лысого',
           'Не моргай',
           'В упортве сила',
           'Сила воли\nплюс характер',
           'Ъуъ, сука!',
           'Один вдох\nи ты подох']  # набор тупых фразочек

for i in telo:
    globals()['label{}*{}'.format(i[0], i[1])]['bg'] = 'gray1'  # нарисуем начальную змейку по координатам тела на поле

for i in range(41):  # покрасим границы поля
    globals()['label{}*{}'.format(i, 0)]['bg'] = 'gray2'
for i in range(41):
    globals()['label{}*{}'.format(i, 40)]['bg'] = 'gray2'
for i in range(41):
    globals()['label{}*{}'.format(0, i)]['bg'] = 'gray2'
for i in range(41):
    globals()['label{}*{}'.format(40, i)]['bg'] = 'gray2'

globals()['label{}*{}'.format(12, 25)]['bg'] = 'black'  # нарисуем первую мышь


a = pole_game.after_idle(niam_niam)  # старт циклического процесса движения
pole_game.bind('w', vektorw)  # обработка нажатий кнопок для управления вектором движения и паузы
pole_game.bind('a', vektora)
pole_game.bind('s', vektors)
pole_game.bind('d', vektord)
pole_game.bind('<space>', pause)

pole_game.mainloop()
