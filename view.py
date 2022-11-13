from telebot import types
import model,controller

def get_button():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton(text='Правила игры')
    btn2=types.KeyboardButton(text='Игра')
    kb.add(btn1,btn2)

def view_rules_game():
    message_rules='Игра с конфетами\nНа столе лежит 150 конфет.\n'\
        'Первый ход определяется жеребьёвкой(бот или вы).За один ход можно забрать не более чем 28 конфет.\n'\
        'Все конфеты оппонента достаются сделавшему последний ход.\n'\
            
    return message_rules

def game():
    message="привет. Предлагаю поиграть в игру 'Конфетки'"
    return message
def lets_go():
    message='сыграем в "Конфетки"\n''Первый ход определяем жеребьевкой.\n'
    return message

def print_sweet_on_table(sweetsOnTable):
    message=(f'На столе {sweetsOnTable} конфет(ы)')
    return message

def error_input():
    message='За один ход можно забрать не более чем 28 конфет или не больше, чем осталось на столе \nПопробуй еще раз'
    return message
def game_false():
    message="Конфеток не осталось. Игра окончена!!!\nЗапустите игру заново"
    return message

