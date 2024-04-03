class Fruit:
    def __init__(self, name:str):
        self._name = name
        print("IT works")

    @property
    def fruit_name(self):
        print("Getting theh fruit name!")
        return self._name
    
    @fruit_name.setter
    def fruit_name(self, value):
        print("Setting fruit name!")
        print(f"{self._name} is now {value}")
        self._name = value

    @fruit_name.deleter
    def fruit_name(self):
        print("Now deleting", self.fruit_name)
        del self._name

if __name__ == '__main__':
    fruit = Fruit('Pineapple')
    fruit.fruit_name
    fruit.fruit_name = 'orange'
    del fruit.fruit_name

    print(fruit.fruit_name)