# Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__
# __setattr__(self, key, value)__ – автоматически вызывается при изменении свойства key класса;
# __getattribute__(self, item) – автоматически вызывается при получении свойства класса с именем item;
# __getattr__(self, item) – автоматически вызывается при получении несуществующего свойства item класса;
# __delattr__(self, item) – автоматически вызывается при удалении свойства item (не важно: существует оно или нет).

class Point:
    MAX_COORD = 100
    MIN_COORD = 0
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)
        
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print("__getattr__: " + item)

    def __delattr__(self, item):
        object.__delattr__(self, item)

pt1 = Point(1, 2)
pt2 = Point(10, 20)