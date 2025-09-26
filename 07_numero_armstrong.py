'''
Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
'''
 
def armstrong(num):
  num_str = str(num)  # Convert the number to a string
  digits = len(num_str)  # Get the number of digits
  digit_powers = [int(digit) ** digits for digit in num_str]  # Compute each digit raised to the power of 'digits'
  armstrong_sum = sum(digit_powers)  # Sum all the computed powers

  return armstrong_sum == num  # Check if the sum equals the original number
  
  
nums = [153, 540, 370, 564, 407]

for i in nums: 
  if armstrong(i):
    print(f'El numero {i} es un numero de Armstrong') 
  else:
    print(f'El numero {i} NO es un numero de Armstrong')