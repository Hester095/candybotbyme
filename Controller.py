import logger
import Model
import View


def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            View.error_value()


def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=', '**']:
            return a
        else:
            View.error_value()

def operation():
    match (Model.ops):
        case '+':
            Model.total = Model.first + Model.second
        case '-':
            Model.total = Model.first - Model.second
        case '*':
            Model.total = Model.first * Model.second
        case '/':
            while Model.second == 0:
                print('На ноль делить нельзя!')
                Model.init_second()
            Model.total = int(Model.first / Model.second)
        case '**':
            Model.total = Model.first ** Model.second
        case _:
            View.error_value()
    logger.logger(f'{Model.first} {Model.ops} {Model.second} = {Model.total}')
