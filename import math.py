import math

#Creating a safe dictionary of allowed functions and constants from the math module
safe_dictionary = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "pi": math.pi,
    "e": math.e
}

while True:
    #Waiting for user input
    user_input = input()

    #Evaluating the user input in a safe environment
    try:
        result = eval(user_input, safe_dictionary)
        print(result)
    #If the user tries to divide by zero, print an error message
    except ZeroDivisionError:
        print("Error")
    #If the user does a math domain error, print an error message
    except ValueError as e:
        print(f"Error: {e}")
    #If the user inputs invalid syntax, print an error message
    except SyntaxError:
        print("Error")
    #If there is any other unknown error, print an error message
    except Exception as e:
        print(f"Error: {e}")