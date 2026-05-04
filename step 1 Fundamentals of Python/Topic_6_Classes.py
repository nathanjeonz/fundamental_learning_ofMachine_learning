class Cat():
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def meow(self):

        print('Meow')

C1 = Cat('Toby','orange')
C2 = Cat('Sam','white')
C3 = Cat('Freya','black and white')

C1.meow()