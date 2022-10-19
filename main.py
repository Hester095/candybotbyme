import Controller
import Model
import View

Model.init_first()
while True:
    if Model.init_ops():
        break
    Model.init_second()
    Controller.operation()
    View.print_total()
    Model.first = Model.total