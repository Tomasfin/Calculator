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
 try:
  if float(value1):
   result = True
 except ValueError:
    result = False
while result is True:
 operator = input('Choose an operator (*)(/)(+)(-)\n')
 if operator in [('*'),('/'),('+'),('-')]:
   result = False
 else:
  result = True

while result is False:
 value2 = input('Choose the second number\n')
 try:
  if float(value1):
   result = True
 except ValueError:
    result = False
if operator is '*':
 print('Answer: ',multiply(float(value1), float(value2)))
if operator is '/':
 print('Answer: ',division(float(value1), float(value2)))
if operator is '+':
  print('Answer: ',addition(float(value1), float(value2)))
if operator is '-':
  print('Answer: ',subtraction(float(value1), float(value2)))
              

    

   
        


