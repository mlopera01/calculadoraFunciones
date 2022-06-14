#Program calculator
#Autor Nora Orozco 
#Version 1.0
#Date 9 June 2022
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def get_plus(self):
        plus = self.a + self.b
        print("-->The add is " + str(plus))

    def get_subtract(self):
        subtract = self.a  - self.b
        print("-->The subtract is " + str(subtract))

    def get_divide(self):
        divide = self.a  / self.b
        print("-->The divide is " + str(divide))

    def get_multiply(self):
        multiply = self.a  * self.b
        print("-->The multiply is " + str(multiply))

    def get_square(self):
        result = self.a **self.b
        print("-->The square is " + str(result))

    def area_of_circule(self):
        P = 3.141592
        result = P * (self.b **2)
        print("-->The Area is " + str(result))



def main():
    operation = int(input("""
List Operations:
        1) add
        2) subtract
        3) divide
        4) multiply
        5) Elevar un número a otro
        6) Area del circulo

Enter operation: """))
    if (operation >= 1 and operation <= 5):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        num = calculator(num1, num2)
        if operation == 1:
            num.get_plus()
        elif operation == 2:
            num.get_subtract()
        elif operation == 3:
            num.get_divide()
        elif operation == 4:
            num.get_multiply()
        elif operation == 5:
            num.get_square()
    else:
        if operation == 6:
           num1 = int(input("Enter radio : "))
           num = calculator(num1, num1)
           num.area_of_circule()
        else:
           print("wrong operation")
            
if __name__ == "__main__":
    main()


    
