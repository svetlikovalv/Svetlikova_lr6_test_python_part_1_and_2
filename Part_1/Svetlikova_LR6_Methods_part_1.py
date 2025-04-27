import math
# проверка ввода
def user_input(input_str):
    if not input_str.strip():  # Проверка, что строка не пустая
        return False
        print("неверный ввод, ввдедите заново")
    for c in input_str:
        if c.isalpha():  # Проверка, является ли символ буквой
            return False
            print("неверный ввод, ввдедите заново")
    try:
        number = float(input_str)  # Используем float, аналог stold в C++
        # if number < 0:
        #     return True
    except:
        return False
    return True
# ввод чисел
def enter_number():
  promt="Enter number: "
  var=input(promt)
  while not user_input(var):
    print("Invalid.Enter number: ")
    var=input(promt)
  return float(var)

#модуль комплексного числа
def modul(a:float,b:float)-> float:
  return math.pow((a*a+b*b),0.5)
#аргумент комплексного числа
def argument(a:float,b:float)-> float:
  if a>0:
        return math.atan(b/a)
  if a<0 and b>0:
      return math.atan(b/a)+math.pi
  if a<0 and b<0: 
      return math.atan(b/a)-math.pi
  if a==0 and b>0:
      return math.pi/2
  if a==0 and b<0:
      return - math.pi/2
  if a==0 and b==0:
      return 0.0