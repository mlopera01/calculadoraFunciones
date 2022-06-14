RESULT_MESSAGE = "The result of "

RESULT_LINES = "______________________________________"

P = 3.141592

def addition_of_two_numbers(a,b):

    print("Processing a addition")

    print("Arguments " + str(a) + " and " + str(b))

    type_calculator = "addition"

    result = a + b

    print(RESULT_MESSAGE  + "addition is: " + str(result))

    print(RESULT_LINES)
          

def substraction_of_two_numbers(a,b):

    print("Processing a substraction")

    print("Arguments " + str(a) + " and " + str(b))
    
    type = "addition"

    result = a - b

    print(RESULT_MESSAGE  + "substraction is: " + str(result))

    print(RESULT_LINES)

def multiply_of_two_numbers(a,b):

    print("Processing a multiply")

    print("Arguments " + str(a) + " and " + str(b))

    result = a * b

    print(RESULT_MESSAGE  + "multiply is: " + str(result))
    
    print(RESULT_LINES)

def divition_of_two_numbers(a,b):

    print("Processing a divition")

    print("Arguments " + str(a) + " and " + str(b))

    result = a / b

    print(RESULT_MESSAGE  + "divition is: " + str(result))

    print(RESULT_LINES)

def square_of_two_numbers(a,b):

    print("processing a square")

    print("Arguments " + str(a) + " and " + str(b))

    result = a ** b

    print(RESULT_MESSAGE  + "square is: " + str(result))

    print(RESULT_LINES)

def area_of_circule(b):

    print("Processing a area of circule")

    print("Arguments " + str(b))

    result = P * (b **2)

    print(RESULT_MESSAGE  + "area of circule is: " + str(result))

    print(RESULT_LINES)

def even_or_odd(b):

    print("Processing a even or odd")

    print("Arguments " + str(b))

    result =  b % 2 

    if  result == 0:

        print(RESULT_MESSAGE  + "it's odd number: " + str(result))
          
    else:
        
         print(RESULT_MESSAGE  + "it's even number: " + str(result))

    print(RESULT_LINES)
    

def main():

    addition_of_two_numbers(3,4)
    substraction_of_two_numbers(3,4)
    multiply_of_two_numbers(3,4)
    divition_of_two_numbers(3,4)
    square_of_two_numbers(3,4)
    area_of_circule(4)
    even_or_odd(4)
    
   
if __name__ == "__main__":

    main()
 	