acceptable_equations = ["+", "-", "*", "/"]

def is_number(number):
    try:
        number = int(number)
    except:
        try:
            number = float(number)
        except:
            print("It's not a number, try again")
            print("")
            number =input()
            is_number(number)

def is_equation():
    if equation is not acceptable_equations:
        print("Wrong equation")
        equation=input()
        is_equation()

print("Enter number:")
first_numer=input() # first number
is_number(first_numer)

print("Enter equation:")
equation=input() # equation
is_equation()

print("Enter second number:")
second_number=input() # second number
is_number(second_number)

if equation == "+":
    answer=(first_numer + second_number)
elif equation == "-":
    answer=(first_numer - second_number)
elif equation == "*":
    answer=(first_numer * second_number)
elif equation == "/":
    answer=(first_numer / second_number)
else:
    print("I don't understand equation")

function(equation)

print("Your answer is:")
print(answer)