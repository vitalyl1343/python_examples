class MyClass:
    __hiddenVariable = 0# Скрытый член класса

# Метод, который изменяет__hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print (self.__hiddenVariable)

obj = MyClass()
obj.add(2)
obj.add(2)
obj.add(2)
print(obj.__hiddenVariable)