def addition(value1, value2):
    return value1 + value2
def subtraction(value1, value2):
    return value1 - value2
def multiply(value1, value2):
    return value1 * value2
def division(value1, value2):
    return value1 / value2

print('Welcome to the super simple terminal calculator!')
result = False
while result is False:
 value1 = input('Please enter a number\n')
 if int(value1) / 1:
    result = True
    while result is True:
       operator = input('Choose an operator (*)(/)(+)(-)\n')
       if operator in ['*','/','+','-']:
          result = False
          while result is False:
           value2 = int(input('Choose the second number\n'))
           if value2 / 1:
              if operator is '*':
                 print(multiply(value1, value2))
              if operator is '/':
                 print(division(value1,value2))
              if operator is '+':
                 print(addition(value1,value2))
              if operator is '-':
                 print(subtraction(value1,value2))
              break

   
        


