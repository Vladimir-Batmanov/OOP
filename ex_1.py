class Point:
    'Класс для представления координат точек на плоскости'
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление экземпляра: ' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point(1, 2)
print(pt.__dict__)

# Итог 1 занятия:
# Класс может сожержать:
# свойста (данные) 
# методы (действия) - функции
#
# функции:
# getattr(obj, name [, default]) - возвращает значение атрибута объекта.
# hasattr(obj, name) - проверяет на наличие атрибута name в obj.
# setattr(obj, name, value) - задает значение атрибута (если атрибут не существует, то он создается).
# delattr(obj, name) - удаляет атрибут с именем name.
#
# переменные:
# __doc__ - содержит строку с описанием класса.
# __dict__ - содержит набор атриботов экземпляра класса.

#//////////////////////////

# Итог 2 занятия:
# Понял, что self - это ссылка на экземпляр класса.

#//////////////////////////

# Итог 3 занятия:
# Инициализатор и финализатор 
# __имя магического метода__
# __init__(self) - Инициализатор объекта класса.
# __del__(self) - Финализатор класса.