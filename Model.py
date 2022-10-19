import Controller
import View

first = 0
second = 0
ops = ''
total = 0

def init_first():
    global first
    first = Controller.input_integer('Введите число: ')

def init_second():
    global second
    second = Controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = Controller.input_operation('Введите операцию(+ cложение, - вычитание, / деление, * умножение, ** возведение в степень)')
    if ops == '=':
        View.print_total()
        return True