def add():
    global answer
    answer=(first_numer + second_number)

def subtract():
    global answer
    answer=(first_numer - second_number)



print("Enter number:")

first_numer=float(input()) # first number

print("Enter equation:")
equation=input() # equation
print("Enter second number:")
second_number=float(input()) # second number


if equation == "+":
    add()
elif equation =="-":
    subtract()
else:
    print("I don't understand equation")


print("Your answer is:")
print(answer)