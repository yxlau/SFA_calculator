from calculator import *

try:
  selection = get_selection()
except ValueError:
    print("Sorry, invalid selection. BYEEEEE...")
    quit()

num1 = get_num("Provide FIRST value: ")
num2 = get_num("Provide your SECOND value: ")
                 
if selection == 1:
  value = add(num1, num2)
elif selection == 2:
  value = subtract(num1, num2)
elif selection == 3:
  value = multiply(num1, num2)
elif selection == 4:
  value = divide(num1, num2)

print(f"========\nThe calculation is: {value}")