# Создать класс TrafficLight (светофор).
# 1. Определить у него один атрибут color (цвет) и метод running (запуск);
# 2. Атрибут реализовать как приватный;
# 3. В рамках метода реализовать переключение светофора в режимы: красный,
# жёлтый, зелёный;
# 4. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# 5. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, жёлтый, зелёный);
# 6. Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его
# нарушении выводить соответствующее сообщение и завершать скрипт.
import time

class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            if self.__color == "red":
                print("Красный. Подождите 7 секунд")
                time.sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                print("Желтый. Подождите 2 секунды")
                time.sleep(2)
                self.__color = "green"
            elif self.__color == "green":
                print("Зеленый. Подождите 1 секунду")
                time.sleep(1)
                self.__color = "red"

light = TrafficLight()
light.running()