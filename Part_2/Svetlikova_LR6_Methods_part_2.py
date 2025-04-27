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
        number = int(input_str)  # Используем int, аналог stoi в C++
        if number < 0:
            return False
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
  return int(var)

# функция считающая сумму цифр
def sum_of_digits(num):
    sum = 0
    for i in str(abs(num)):
      sum += int(i)
    return sum
# проверка равенства сумм цифр
def is_equal(num1:int,num2:int):
  return sum_of_digits(num1) == sum_of_digits(num2)