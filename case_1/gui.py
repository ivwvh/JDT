from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
import calculator


"""
TODO:
Раздел с алгеброй и матрицами
Применение тригонометрических тождеств, нахождение корней

"""


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(270, 210)
        layout = (
            QVBoxLayout()
        )  # создаем объект описывающей расположение элементов в окне
        tabs = QTabWidget()  # создаем виджет для вкладок
        # создаем вкладки для разделов
        tabs.addTab(self.algebraTabUi(), "Algebra")
        tabs.addTab(self.trigonometryTabUi(), "Trigonometry")
        tabs.addTab(self.matrixTabUi(), "Matrices")
        # добавляем вкладки в лейаут
        layout.addWidget(tabs)
        # устанавливаем лейаут для окна
        self.setLayout(layout)

    def algebraTabUi(self) -> QWidget:
        # заготовка для раздела с алгеброй
        algebraTab = QWidget()
        layout = QVBoxLayout()
        field = QLineEdit(algebraTab)
        layout.addWidget(field)
        algebraTab.setLayout(layout)
        return algebraTab

    def trigonometryTabUi(self) -> QWidget:
        # создаем окно
        trigTab = QWidget()
        layout = QVBoxLayout()
        # создаем поля ввода
        self.sin_qle = QLineEdit(trigTab)
        self.cos_qle = QLineEdit(trigTab)
        self.tan_qle = QLineEdit(trigTab)
        self.ctg_qle = QLineEdit(trigTab)
        # создаем лейблы
        self.sin_lbl = QLabel(trigTab)
        self.cos_lbl = QLabel(trigTab)
        self.tan_lbl = QLabel(trigTab)
        self.ctg_lbl = QLabel(trigTab)
        # устанавливаем текст лейблов
        self.sin_lbl.setText("Sin:")
        self.cos_lbl.setText("Cos:")
        self.tan_lbl.setText("Tan:")
        self.ctg_lbl.setText("Ctg:")
        # создаем кнопки
        self.sin_btn = QPushButton(trigTab)
        self.cos_btn = QPushButton(trigTab)
        self.tan_btn = QPushButton(trigTab)
        self.ctg_btn = QPushButton(trigTab)
        # устанавливаем имена для кнопок
        self.sin_btn.setText("Calculate")
        self.cos_btn.setText("Calculate")
        self.tan_btn.setText("Calculate")
        self.ctg_btn.setText("Calculate")
        # привязываем к кнопкам функции которые сработают при нажатии
        self.sin_btn.clicked.connect(self.show_sin_result)
        self.cos_btn.clicked.connect(self.show_cos_result)
        self.tan_btn.clicked.connect(self.show_tan_result)
        self.ctg_btn.clicked.connect(self.show_ctg_result)
        # распределяем элементы по экрану
        self.sin_qle.move(40, 0)
        self.cos_qle.move(40, 40)
        self.tan_qle.move(40, 80)
        self.ctg_qle.move(40, 120)
        self.cos_lbl.move(0, 40)
        self.tan_lbl.move(0, 80)
        self.ctg_lbl.move(0, 120)
        self.sin_btn.move(140, 0)
        self.cos_btn.move(140, 40)
        self.tan_btn.move(140, 80)
        self.ctg_btn.move(140, 120)
        trigTab.setLayout(layout)
        return trigTab

    def matrixTabUi(self) -> QWidget:
        # заготовка для раздела с матрицами
        matrixTab = QWidget()
        layout = QVBoxLayout()
        field = QLineEdit(self)
        layout.addWidget(field)
        matrixTab.setLayout(layout)
        return matrixTab

    def show_sin_result(self) -> None:
        pop_up = QMessageBox(self)  # создаем новое окно
        radians = int(
            self.sin_qle.text()
        )  # считываем введенное в поле значение FIXME: программа крашнется при пустом поле
        result = calculator.calculate_sin(radians)  # получаем значение функции
        text = f"Sin of {radians} rad is {str(result)}"  # создаем строку с текстом который будем выводить в окне
        pop_up.setText(text)  # добавляем её в окно
        button = pop_up.exec()

    def show_cos_result(self) -> None:
        pop_up = QMessageBox(self)
        radians = int(self.cos_qle.text())
        result = str(calculator.calculate_cos(radians))
        text = f"Cos of {radians} rad is {result}"
        pop_up.setText(text)
        button = pop_up.exec()

    def show_tan_result(self) -> None:
        pop_up = QMessageBox(self)
        radians = int(self.tan_qle.text())
        result = str(calculator.calculate_tan(radians))
        text = f"Tan of {radians} rad is {result}"
        pop_up.setText(text)
        button = pop_up.exec()

    def show_ctg_result(self) -> None:
        pop_up = QMessageBox(self)
        radians = int(self.ctg_qle.text())
        result = str(calculator.calculate_ctg(radians))
        text = f"Ctg of {radians} rad is {result}"
        pop_up.setText(text)
        button = pop_up.exec()
