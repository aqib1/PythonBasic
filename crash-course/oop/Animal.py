class Animal:
    def __init__(self, name: str):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def to_string(self):
        print(self.name)


if __name__ == '__main__':
    animal = Animal('Dog')
    print(animal.get_name())
    animal.set_name('Cat')
    animal.to_string()