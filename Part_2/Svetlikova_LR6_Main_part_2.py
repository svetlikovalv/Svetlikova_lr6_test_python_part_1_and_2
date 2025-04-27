from Svetlikova_LR6_Methods_part_2 import enter_number,is_equal,sum_of_digits
print("введите первое число ")
num1=enter_number()
print("введите второе число ")
num2=enter_number()
print("сумма цифр первого числа: ",sum_of_digits(num1),\
    "\nсумма цифр вторго числа: ",sum_of_digits(num2))
print("cуммы цифр чисел равны " if is_equal(num1,num2) else "cуммы цифр чисел не равны ")