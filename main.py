import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from create_figure import *
from pyqtui import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()


def radio_signal():
    figures = []
    ui.combo_figures.clear()
    ui.combo_operations.clear()
    if ui.radioButton_2D.isChecked():
        figures = flat_figures.keys()
        ui.combo_operations.addItem("S - площадь фигуры")
        CreateFigure.set_type("2D")

    elif ui.radioButton_3D.isChecked():
        figures = volume_figures.keys()
        ui.combo_operations.addItem("S - площадь фигуры")
        ui.combo_operations.addItem("V - обьем фигуры")
        CreateFigure.set_type("3D")

    for item in figures:
        ui.combo_figures.addItem(item)


def button_signal():
    args = []
    all_figures = {**flat_figures, **volume_figures}
    selected_figure = all_figures[ui.combo_figures.currentText()]
    CreateFigure.set_figure(ui.combo_figures.currentText())
    CreateFigure.set_operation(ui.combo_operations.currentText())

    i = 0
    for item in FIELD_TUPLE:
        if item.text() and item.text().isdigit():
            if CreateFigure.get_figure() == "пирамида":
                if int(item.text()) == 3 or int(item.text()) == 4 and i == 1:
                    args.append(int(item.text()))
                    item.setStyleSheet("color: black")
                elif item.text() and item.text().isdigit():
                    args.append(int(item.text()))
                    item.setStyleSheet("color: black")
                else:
                    item.setStyleSheet("color: red")
            else:
                args.append(int(item.text()))
                item.setStyleSheet("color: black")
        else:
            item.setStyleSheet("color: red")
        i += 1
    CreateFigure.set_params(args)

    if selected_figure._param_len == len(args):
        ui.output.setText(str(CreateFigure.get_result()))
        figure = CreateFigure.get_figure()
        params = CreateFigure.get_params()
        ui.MatPlotWidgetWindow.update_screen(figure, params)


def combo_figures_signal():
    layout_cleared()
    if ui.combo_figures.currentText() in {"прямоугольник", "ромб", "цилиндр", "конус"}:
        ui.field_a.setHidden(False)
        ui.label_a.setHidden(False)
        ui.field_b.setHidden(False)
        ui.label_b.setHidden(False)
        if ui.combo_figures.currentText() in {"цилиндр", "конус"}:
            ui.label_a.setText("радиус R, мм:")
            ui.label_b.setText("высота h, мм:")
        elif ui.combo_figures.currentText() in {"прямоугольник"}:
            ui.label_a.setText("сторона a, мм:")
            ui.label_b.setText("сторона b, мм:")
        elif ui.combo_figures.currentText() in {"ромб"}:
            ui.label_a.setText("сторона a, мм:")
            ui.label_b.setText("угол, º:")
    elif ui.combo_figures.currentText() in {"круг", "сфера", "квадрат", "куб"}:
        ui.field_a.setHidden(False)
        ui.label_a.setHidden(False)
        if ui.combo_figures.currentText() in {"круг", "сфера"}:
            ui.label_a.setText("радиус R, мм:")
        else:
            ui.label_a.setText("сторона a, мм:")
    elif ui.combo_figures.currentText() in {
        "треугольник",
        "трапеция",
        "параллелепипед",
        "пирамида",
    }:
        ui.field_a.setHidden(False)
        ui.label_a.setHidden(False)
        ui.field_b.setHidden(False)
        ui.label_b.setHidden(False)
        ui.field_c.setHidden(False)
        ui.label_c.setHidden(False)
        if ui.combo_figures.currentText() in {"параллелепипед", "трапеция"}:
            ui.label_a.setText("сторона a, мм:")
            ui.label_b.setText("сторона b, мм:")
            ui.label_c.setText("высота h,  мм:")
        elif ui.combo_figures.currentText() == "треугольник":
            ui.label_a.setText("сторона a, мм:")
            ui.label_b.setText("сторона b, мм:")
            ui.label_c.setText("угол, º:")
        elif ui.combo_figures.currentText() == "пирамида":
            ui.label_a.setText("сторона a, мм:")
            ui.label_b.setText("кол-во граней, шт:")
            ui.label_c.setText("высота, мм:")


ui.radioButton_2D.toggled.connect(radio_signal)
ui.radioButton_3D.toggled.connect(radio_signal)
ui.combo_figures.currentTextChanged.connect(combo_figures_signal)
ui.pushButton.clicked.connect(button_signal)

FIELD_TUPLE = (ui.field_a, ui.field_b, ui.field_c)
LABLE_TUPLE = (ui.label_a, ui.label_b, ui.label_c)


def layout_cleared(pol=FIELD_TUPLE, lab=LABLE_TUPLE):
    for i in pol + lab:
        i.setHidden(True)
        i.setText("")


layout_cleared()
app.exec()
