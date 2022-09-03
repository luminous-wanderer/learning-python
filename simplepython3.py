import os 
import time
os.system("clear")

class color :
    B = '\033[94m'
    C = '\033[96m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    E = '\033[0m'
    W = '\033[37m'
    BO = '\033[1m'
    UNDERLINE = '\033[4m'
    
myname = (f"{color.B}Luxxt.{color.E}")

print(f"{color.UNDERLINE}{color.G}                           {color.E}")
print ("")
print(f'''{color.Y} Learning Basic's
 Made by {color.E}{color.B} Luxxt. {color.E}''')
print("")
print(f"{color.Y}        Version{color.B} 0.2{color.E}")
print(f"{color.UNDERLINE}{color.G}                           {color.E}")
print("")

def menu() :
  print(f"{color.Y}  [MENU]{color.E}")
  print(f"{color.R}[1]Hello{color.E}")
  print(f"{color.Y}[2]Calculator{color.E}")
  print(f"{color.G}[3]Factor{color.E}")
  print(f"{color.R}[4]Ascii Generator{color.E}")
  
menu()
opt = int(input(f"{color.E}Enter your option :"))

if opt == 1:
  print("Hello")

elif opt == 2:
  def calculator():
    cal = input(f'''{color.Y}Please type in the math operation you would like to colormplete{color.E}:
    {color.G}+ for addition{color.E}
    {color.R}- for subtraction{color.E}
    {color.G}* for multiplication{color.E}
    {color.R}/ for division{color.E}
    {color.Y}Input{color.E} :''')
    
    try  :
      number1 = int(input(f"{color.B}Enter your first number  : {color.E}"))
      number2 = int(input(f"{color.B}Enter your second number : {color.E}"))
    except Exception as P:
      print(f"{color.W}Input {color.R}MUST be number!{color.E}")
    
    if cal == '+':
      try :
        print(' {} + {} = '.format(number1, number2))
        print(number1 + number2)
      except Exception as p :
        ("")
    elif cal == '-':
      try :
        print(' {} - {} = '.format(number1, number2))
        print(number1 - number2)
      except Exception as m :
        ("")
    elif cal == '*':
      try :
        print(' {} * {} = '.format(number1, number2))
        print(number1 * number2)
      except Exception as t :
        ("")
    elif cal == '/':
      try :
        print(' {} / {} = '.format(number1, number2))
        print(number1 / number2)
      except Exception as e :
        print(f"{color.W}Cannot divide by{color.E} {color.R}Zero.{color.B}")
    else :
       print(f"{color.R}Invalid math operation. Please try again.{color.E}")
    again()
  
  def again():
    recal = input(f'''
    {color.Y}Do you want to calulate again?{color.E}
    Please type {color.G}Y {color.E}for {color.G}YES {color.E}or {color.R}N{color.E} for {color.R}NO{color.E}
    {color.Y}Input{color.E} :''')
    if recal.upper() == 'Y':
      print ("")
      calculator()
    elif recal.upper() == 'N':
      print('See you later.')
    else :
      again()
  calculator()
  
elif opt == 3 : 
  def factor() :
    try :
      num = input(f"{color.G}Numbers{color.E} :")
      num = int(num)
      def print_factors(x):
        print ("The factors of",x,"are:")
        for i in range(1, x + 1):
          if x % i == 0:
             print(i)
      print_factors(num)
    except Exception as F :
      print(f"{color.R}Input MUST be number!{color.E}")
    factor_again()
  
  def factor_again() :
    again_f = input(f'''
    {color.Y}Again?{color.E}
    Please type {color.G}Y {color.E}for {color.G}YES {color.E}or {color.R}N{color.E} for {color.R}NO{color.E}
    {color.Y}Input{color.E} :''')
    if again_f.upper() == 'Y':
      print ("")
      factor()
    elif again_f.upper() == 'N':
      print('See you later.')
    else :
      factor_again()
  factor()
  
elif opt == 4 :
  import secrets
  import string
  
  alphabet = string.ascii_letters + string.digits
  letters = ''.join(secrets.choice(alphabet) for i in range(8))
  
  print(letters)

else :
  print(f"{color.R}Invalid option, try again!{color.E}")

menu()
opt = int(input(f"{color.E}Enter your option :"))



  





