from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from pulp import *
import math
import sys


def main():
	# Создаем само приложение
	app = QApplication(sys.argv)

	# Создаем главное окно
	window = QWidget()

	# Настраиваем окно
	window.setFixedSize(650, 200)
	window.setWindowTitle("Очагов Данил Олегович ИЦТМС 3-3 Вариант 16")

  # Добавляем сетку для GUI
	layout = QVBoxLayout()

	# Устанавливаем заголовочный текст в окне приложения
	label = QLabel(window)
	label.setText("Решение комплекса задач, моделирующих деятельность предприятия")
	label.setFont(QFont("Arial", 13))
	label.move(25, 20)

	# Рисуем кнопки для каждой задачи
	button1 = QPushButton("Задача распределения людей по работам проекта")
	button2 = QPushButton("Задача распределения денежных средств на пиар кампанию")
	button3 = QPushButton("Задача маршрутизации")
	button4 = QPushButton("Задача раскроя и упаковки")
	button5 = QPushButton("Задача теории игр")

	# Привязываем слушатель (event) к каждой кнопке при ее нажатии
	button1.clicked.connect(on_button1_clicked)
	button2.clicked.connect(on_button2_clicked)
	button3.clicked.connect(on_button3_clicked)
	button4.clicked.connect(on_button4_clicked)
	button5.clicked.connect(on_button5_clicked)

	# Добавляем элементы в сетку
	layout.addWidget(label)
	layout.addWidget(button1)
	layout.addWidget(button2)
	layout.addWidget(button3)
	layout.addWidget(button4)
	layout.addWidget(button5)

	window.setLayout(layout)

	# Показываем окно и запускаем приложение
	window.show()
	sys.exit(app.exec_())

""" Выводит сообщение в виде диалогового окна """
def show_message(msg):
	message = QMessageBox()
	message.setWindowTitle('Получено решение!')
	message.setText(msg)
	message.exec_()

""" Задача распределения людей по работам проекта """
def on_button1_clicked():
	# Задаем неизвестные
	x11 = LpVariable('x11', 0, cat='Integer')
	x12 = LpVariable('x12', 0, cat='Integer')
	x13 = LpVariable('x13', 0, cat='Integer')
	x21 = LpVariable('x21', 0, cat='Integer')
	x22 = LpVariable('x22', 0, cat='Integer')
	x23 = LpVariable('x23', 0, cat='Integer')
	x31 = LpVariable('x31', 0, cat='Integer')
	x32 = LpVariable('x32', 0, cat='Integer')
	x33 = LpVariable('x33', 0, cat='Integer')

	# Задаем кол-во часов на выполнение определенной работы
	a11 = 5
	a12 = 8
	a13 = 6
	a21 = 6
	a22 = 4
	a23 = 7
	a31 = 6
	a32 = 5
	a33 = 7

	# Задачем доход от каждого вида продукции
	income1 = 500
	income2 = 700
	income3 = 600

	# Целевая функция будет искать максимум дохода
	prob = LpProblem('myProblem', LpMaximize)

	# Прописываем целевую функцию
	profit = x11 * income1 + x21 * income1 + x31 * income1 + x12 * income2 + x22 * income2 + x32 * income2 + x13 * income3 + x23 * income3 + x33 * income3

	prob += profit, "Function"

	# Указываем ограничения
	prob += x11 + x12 + x13 == 6
	prob += x21 + x22 + x23 == 7
	prob += x31 + x32 + x33 == 5
	prob += x11 * a11 + x12 * a12 + x13 * a13 + x21 * a21 + x22 * a22 + x23 * a23 + x31 * a31 + x32 * a32 + x33 * a33 <= 84

	# Решаем
	prob.solve()

	# Форматируем вывод на экран
	output = '№  шпона:  1 | 2 | 3\n'
	output += 'Бригада 1: ' + str(math.floor(x11.value())) + ' | ' + str(math.floor(x12.value())) + ' | ' + str(math.floor(x13.value())) + '\n'
	output += 'Бригада 2: ' + str(math.floor(x21.value())) + ' | ' + str(math.floor(x22.value())) + ' | ' + str(math.floor(x23.value())) + '\n'
	output += 'Бригада 3: ' + str(math.floor(x31.value())) + ' | ' + str(math.floor(x32.value())) + ' | ' + str(math.floor(x33.value())) + '\n'
	output += '-----------------------------\n'
	totalTime = x11.value() * a11 + x12.value() * a12 + x13.value() * a13 + x21.value() * a21 + x22.value() * a22 + x23.value() * a23 + x31.value() * a31 + x32.value() * a32 + x33.value() * a33
	output += 'Затраченное время = ' + str(math.floor(totalTime)) + 'ч.\n'
	totalIncome = x11.value() * income1 + x21.value() * income1 + x31.value() * income1 + x12.value() * income2 + x22.value() * income2 + x32.value() * income2 + x13.value() * income3 + x23.value() * income3 + x33.value() * income3
	output += 'Конечный доход = ' + str(math.floor(totalIncome)) + 'ден.ед.'

	# Показываем сообщение пользователю
	show_message(output)

""" Задача распределения денежных средств на пиар кампанию """
def on_button2_clicked():
	# Задаем неизвестные
	xInternet = LpVariable('xInternet', 0, cat='Integer')
	xTV = LpVariable('xTV', 0, cat='Integer')

	# Целевая функция будет искать максимум сбыта продукции
	prob = LpProblem('myProblem', LpMaximize)

	# Прописываем целевую функцию
	profit = xInternet + xTV * 25

	prob += profit, "Function"

	# Указываем ограничения
	prob += xInternet * 50 + xTV * 1_000 <= 50_000
	prob += xInternet - xTV * 2 >= 0

	# Решаем
	prob.solve()

	# Форматируем вывод на экран
	output = 'Сбыт продукции составляет: ' + str(math.floor(xInternet.value() + xTV.value() * 25)) + ' единиц\n'
	output += 'Оптимальная интернет реклама: ' + str(math.floor(xInternet.value())) + 'мин.\n'
	output += 'Оптимальная ТВ реклама: ' + str(math.floor(xTV.value())) + 'мин.\n'
	output += 'Затрачено денег: ' + str(math.floor(xInternet.value() * 50 + xTV.value() * 1_000)) + 'руб.'

	# Показываем сообщение пользователю
	show_message(output)

""" Задача маршрутизации """
def on_button3_clicked():
	# Задаем неизвестные
	x11 = LpVariable('x11', 0, cat='Integer')
	x12 = LpVariable('x12', 0, cat='Integer')
	x13 = LpVariable('x13', 0, cat='Integer')
	x21 = LpVariable('x21', 0, cat='Integer')
	x22 = LpVariable('x22', 0, cat='Integer')
	x23 = LpVariable('x23', 0, cat='Integer')
	x31 = LpVariable('x31', 0, cat='Integer')
	x32 = LpVariable('x32', 0, cat='Integer')
	x33 = LpVariable('x33', 0, cat='Integer')

	# Задаем кол-во километров до потребителей от складов
	a11 = 68
	a12 = 72
	a13 = 75
	a21 = 56
	a22 = 60
	a23 = 58
	a31 = 38
	a32 = 40
	a33 = 35

	# Целевая функция будет искать минимум километров (дальность поездок)
	prob = LpProblem('myProblem', LpMinimize)

	# Прописываем целевую функцию
	profit = x11 * a11 + x12 * a12 + x13 * a13 + x21 * a21 + x22 * a22 + x23 * a23 + x31 * a31 + x32 * a32 + x33 * a33

	prob += profit, "Function"

	# Указываем ограничения
	prob += x11 + x12 + x13 == 1
	prob += x21 + x22 + x23 == 1
	prob += x31 + x32 + x33 == 1
	prob += x11 + x21 + x31 == 1
	prob += x12 + x22 + x32 == 1
	prob += x13 + x23 + x33 == 1

	# Решаем
	prob.solve()

	# Форматируем вывод на экран
	output = 'Потребители: 1 | 2 | 3\n'
	output += 'г. Казань:       ' + str(math.floor(x11.value())) + ' | ' + str(math.floor(x12.value())) + ' | '  + str(math.floor(x13.value())) + '\n'
	output += 'г. Киров:         ' + str(math.floor(x21.value())) + ' | ' + str(math.floor(x22.value())) + ' | '  + str(math.floor(x23.value())) + '\n'
	output += 'г. Пермь:        ' + str(math.floor(x31.value())) + ' | ' + str(math.floor(x32.value())) + ' | '  + str(math.floor(x33.value())) + '\n'
	output += '--------------------------------\n'
	totalDistance = math.floor(x11.value() * a11 + x12.value() * a12 + x13.value() * a13 + x21.value() * a21 + x22.value() * a22 + x23.value() * a23 + x31.value() * a31 + x32.value() * a32 + x33.value() * a33)
	output += 'Суммарная дальность поездки: ' + str(totalDistance)

	# Показываем сообщение пользователю
	show_message(output)

""" Задача раскроя и упаковки """
def on_button4_clicked():
	# Задаем неизвестные
	x11 = LpVariable('x11', 0, cat='Integer')
	x12 = LpVariable('x12', 0, cat='Integer')
	x13 = LpVariable('x13', 0, cat='Integer')
	x14 = LpVariable('x14', 0, cat='Integer')

	# Задаем кол-во заготовок на каждый тип комплекта
	a11 = 0
	a12 = 1
	a13 = 2
	a14 = 3
	a21 = 5
	a22 = 3
	a23 = 2
	a24 = 0

	# Целевая функция будет искать максимум комплектов
	prob = LpProblem('myProblem', LpMaximize)

	# Прописываем целевую функцию
	profit = (x11 * a11 + x12 * a12 + x13 * a13 + x14 * a14) / 3

	prob += profit, "Function"

	# Указываем ограничения
	prob += x11 + x12 + x13 + x14 == 882
	prob += (x11 * a11 + x12 * a12 + x13 * a13 + x14 * a14) / 3 == (x11 * a21 + x12 * a22 + x13 * a23 + x14 * a24) / 5

	# Решаем
	prob.solve()

	# Форматируем вывод на экран
	output = 'Кол-во заготовок 1 вида: ' + str(math.floor(x11.value())) + '\n'
	output += 'Кол-во заготовок 2 вида: ' + str(math.floor(x12.value())) + '\n'
	output += 'Кол-во заготовок 3 вида: ' + str(math.floor(x13.value())) + '\n'
	output += 'Кол-во заготовок 4 вида: ' + str(math.floor(x14.value())) + '\n'
	output += 'Кол-во комплектов: ' + str(math.floor((x11.value() * a11 + x12.value() * a12 + x13.value() * a13 + x14.value() * a14) / 3))

	# Показываем сообщение пользователю
	show_message(output)

""" Задача теории игр """
def on_button5_clicked():
	# Задаем неизвестные
	x11 = LpVariable('x11', 0, cat='Binary')
	x12 = LpVariable('x12', 0, cat='Binary')
	x13 = LpVariable('x13', 0, cat='Binary')
	x14 = LpVariable('x14', 0, cat='Binary')
	x15 = LpVariable('x15', 0, cat='Binary')
	x16 = LpVariable('x16', 0, cat='Binary')
	x21 = LpVariable('x21', 0, cat='Binary')
	x22 = LpVariable('x22', 0, cat='Binary')
	x23 = LpVariable('x23', 0, cat='Binary')
	x24 = LpVariable('x24', 0, cat='Binary')
	x25 = LpVariable('x25', 0, cat='Binary')
	x26 = LpVariable('x26', 0, cat='Binary')
	x31 = LpVariable('x31', 0, cat='Binary')
	x32 = LpVariable('x32', 0, cat='Binary')
	x33 = LpVariable('x33', 0, cat='Binary')
	x34 = LpVariable('x34', 0, cat='Binary')
	x35 = LpVariable('x35', 0, cat='Binary')
	x36 = LpVariable('x36', 0, cat='Binary')
	x41 = LpVariable('x41', 0, cat='Binary')
	x42 = LpVariable('x42', 0, cat='Binary')
	x43 = LpVariable('x43', 0, cat='Binary')
	x44 = LpVariable('x44', 0, cat='Binary')
	x45 = LpVariable('x45', 0, cat='Binary')
	x46 = LpVariable('x46', 0, cat='Binary')
	x51 = LpVariable('x51', 0, cat='Binary')
	x52 = LpVariable('x52', 0, cat='Binary')
	x53 = LpVariable('x53', 0, cat='Binary')
	x54 = LpVariable('x54', 0, cat='Binary')
	x55 = LpVariable('x55', 0, cat='Binary')
	x56 = LpVariable('x56', 0, cat='Binary')
	x61 = LpVariable('x61', 0, cat='Binary')
	x62 = LpVariable('x62', 0, cat='Binary')
	x63 = LpVariable('x63', 0, cat='Binary')
	x64 = LpVariable('x64', 0, cat='Binary')
	x65 = LpVariable('x65', 0, cat='Binary')
	x66 = LpVariable('x66', 0, cat='Binary')

	# Задаем индекс враждебности
	a11 = 3
	a12 = 4
	a13 = 9
	a14 = 18
	a15 = 9
	a16 = 6
	a21 = 16
	a22 = 8
	a23 = 12
	a24 = 13
	a25 = 20
	a26 = 4
	a31 = 8
	a32 = 6
	a33 = 13
	a34 = 1
	a35 = 6
	a36 = 9
	a41 = 16
	a42 = 9
	a43 = 6
	a44 = 8
	a45 = 1
	a46 = 11
	a51 = 8
	a52 = 12
	a53 = 17
	a54 = 5
	a55 = 3
	a56 = 5
	a61 = 2
	a62 = 9
	a63 = 1
	a64 = 10
	a65 = 5
	a66 = 17

	# Целевая функция будет искать минимальный индекс враждебности
	prob = LpProblem('myProblem', LpMinimize)

	# Прописываем целевую функцию
	profit = x11 * a11 + x12 * a12 + x13 * a13 + x14 * a14 + x15 * a15 + x16 * a16 + \
         x21 * a21 + x22 * a22 + x23 * a23 + x24 * a24 + x25 * a25 + x26 * a26 + \
         x31 * a31 + x32 * a32 + x33 * a33 + x34 * a34 + x35 * a35 + x36 * a36 + \
         x41 * a41 + x42 * a42 + x43 * a43 + x44 * a44 + x45 * a45 + x46 * a46 + \
         x51 * a51 + x52 * a52 + x53 * a53 + x54 * a54 + x55 * a55 + x56 * a56 + \
         x61 * a61 + x62 * a62 + x63 * a63 + x64 * a64 + x65 * a65 + x66 * a66

	prob += profit, "Function"

	# Указываем ограничения
	prob += x11 + x12 + x13 + x14 + x15 + x16 == 1
	prob += x21 + x22 + x23 + x24 + x25 + x26 == 1
	prob += x31 + x32 + x33 + x34 + x35 + x36 == 1
	prob += x41 + x42 + x43 + x44 + x45 + x46 == 1
	prob += x51 + x52 + x53 + x54 + x55 + x56 == 1
	prob += x61 + x62 + x63 + x64 + x65 + x66 == 1
	prob += x11 + x21 + x31 + x41 + x51 + x61 == 1
	prob += x12 + x22 + x32 + x42 + x52 + x62 == 1
	prob += x13 + x23 + x33 + x43 + x53 + x63 == 1
	prob += x14 + x24 + x34 + x44 + x54 + x64 == 1
	prob += x15 + x25 + x35 + x45 + x55 + x65 == 1
	prob += x16 + x26 + x36 + x46 + x56 + x66 == 1

	# Решаем
	prob.solve()

	# Форматируем вывод на экран
	output = str(math.floor(x11.value())) + ' | ' + str(math.floor(x12.value())) + ' | ' + str(math.floor(x13.value())) + ' | ' + str(math.floor(x14.value())) + ' | ' + str(math.floor(x15.value())) + ' | ' + str(math.floor(x16.value())) + '\n'
	output += str(math.floor(x21.value())) + ' | ' + str(math.floor(x22.value())) + ' | ' + str(math.floor(x23.value())) + ' | ' + str(math.floor(x24.value())) + ' | ' + str(math.floor(x25.value())) + ' | ' + str(math.floor(x26.value())) + '\n'
	output += str(math.floor(x31.value())) + ' | ' + str(math.floor(x32.value())) + ' | ' + str(math.floor(x33.value())) + ' | ' + str(math.floor(x34.value())) + ' | ' + str(math.floor(x35.value())) + ' | ' + str(math.floor(x36.value())) + '\n'
	output += str(math.floor(x41.value())) + ' | ' + str(math.floor(x42.value())) + ' | ' + str(math.floor(x43.value())) + ' | ' + str(math.floor(x44.value())) + ' | ' + str(math.floor(x45.value())) + ' | ' + str(math.floor(x46.value())) + '\n'
	output += str(math.floor(x51.value())) + ' | ' + str(math.floor(x52.value())) + ' | ' + str(math.floor(x53.value())) + ' | ' + str(math.floor(x54.value())) + ' | ' + str(math.floor(x55.value())) + ' | ' + str(math.floor(x56.value())) + '\n'
	output += str(math.floor(x61.value())) + ' | ' + str(math.floor(x62.value())) + ' | ' + str(math.floor(x63.value())) + ' | ' + str(math.floor(x64.value())) + ' | ' + str(math.floor(x65.value())) + ' | ' + str(math.floor(x66.value())) + '\n'
	finalIndex = math.floor(x11.value() * a11 + x12.value() * a12 + x13.value() * a13 + x14.value() * a14 + x15.value() * a15 + x16.value() * a16 + \
         x21.value() * a21 + x22.value() * a22 + x23.value() * a23 + x24.value() * a24 + x25.value() * a25 + x26.value() * a26 + \
         x31.value() * a31 + x32.value() * a32 + x33.value() * a33 + x34.value() * a34 + x35.value() * a35 + x36.value() * a36 + \
         x41.value() * a41 + x42.value() * a42 + x43.value() * a43 + x44.value() * a44 + x45.value() * a45 + x46.value() * a46 + \
         x51.value() * a51 + x52.value() * a52 + x53.value() * a53 + x54.value() * a54 + x55.value() * a55 + x56.value() * a56 + \
         x61.value() * a61 + x62.value() * a62 + x63.value() * a63 + x64.value() * a64 + x65.value() * a65 + x66.value() * a66)
	output += 'Целевая функция: ' + str(finalIndex)

	# Показываем сообщение пользователю
	show_message(output)


if __name__ == '__main__':
	main()