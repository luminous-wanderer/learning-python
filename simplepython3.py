import time
import sys
import os
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
    
name = str(input(f'''{color.G}Your name: {color.E}''').lower())

def load_animation() :
  load_str = "welcome" + " " + name + "..." + "starting ur console application..."
  ls_len = len(load_str)
  animation = "|/-\\"
  anicount = 0
  counttime = 0
  i = 0
  while (counttime != 100) :
    time.sleep(0.075)
    load_str_list = list(load_str)
    x = ord(load_str_list[i])
    y = 0
    if x !=32 and x !=46 :
      if x>90 :
        y = x-32
      else :
        y = x + 32
      load_str_list[i]= chr(y)
      
    res = ''
    for j in range(ls_len) :
      res = res + load_str_list[j]
    sys.stdout.write("\r"+res + animation[anicount])
    sys.stdout.flush() 
    load_str = res
    
    anicount = (anicount + 1)% 4
    i = (i + 1)%ls_len
    counttime = counttime + 1
        
load_animation()

os.system("clear")

print("Welcome" + " " + name)

print(f"{color.UNDERLINE}{color.G}                           {color.E}")
print ("")
print(f'''{color.Y} Learning Basic's
 Made by {color.E}{color.B} Luxxt. {color.E}''')
print("")
print(f"{color.Y}              Version{color.B} 0.2{color.E}")
print(f"{color.UNDERLINE}{color.G}                           {color.E}")
print("")

def menu() :
  print(f"{color.Y}  [MENU]{color.E}")
  print(f"{color.R}[1]Hello{color.E}")
  print(f"{color.Y}[2]Calculator{color.E}")
  print(f"{color.G}[3]Factor{color.E}")
  print(f"{color.R}[4]Ascii Generator{color.E}")
  print(f"{color.Y}[5]Simple Maze Generator{color.E}")
  
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
      print(f"{color.R}Input must be Y or N.{color.E}")
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
      print(f"{color.G}Result: {color.E}")
      print_factors(num)
    except Exception as F :
      print(f"{color.R}Input MUST be number!{color.E}")
    factor_again()
  
  def factor_again() :
    again_f = input(f'''
    {color.Y}Do another factor?{color.E}
    Please type {color.G}Y {color.E}for {color.G}YES {color.E}or {color.R}N{color.E} for {color.R}NO{color.E}
    {color.Y}Input{color.E} :''')
    if again_f.upper() == 'Y':
      print ("")
      factor()
    elif again_f.upper() == 'N':
      print('See you later.')
    else :
      print(f"{color.R}Input must be Y or N.{color.E}")
      factor_again()
  factor()
  
elif opt == 4 :
  import secrets
  import string
  
  def ascii_gen() :
    alphabet = string.ascii_letters + string.digits
    letters = ''.join(secrets.choice(alphabet) for i in range(8))
  
    print(f"{color.G}Here's your generated Ascii:{color.E}")
    print(letters)
    ascii_again()
    
  def ascii_again() :
    again_ascii = input(f'''
    {color.Y}Generate Another Ascii?{color.E}
    Please type {color.G}Y {color.E}for {color.G}YES {color.E}or {color.R}N{color.E} for {color.R}NO{color.E}
    {color.Y}Input{color.E} :''')
    if again_ascii.upper() == 'Y':
      print ("")
      ascii_gen()
    elif again_ascii.upper() == 'N':
      print('See you later.')
    else :
      print(f"{color.R}Input must be Y or N.{color.E}")
      ascii_again()
  ascii_gen()
  
elif opt == 5 : 
  from random import shuffle, randrange
  def maze_gen() :
    def make_maze(w = 16, h = 8):
      vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
      ver = [["▮  "] * w + ['▮'] for _ in range(h)] + [[]]
      hor = [["■▬▬"] * w +  ['■'] for _ in range(h + 1)]
    
      def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
          if vis[yy][xx]: continue
          if xx == x: hor[max(y, yy)][x] = "■  "
          if yy == y: ver[y][max(x, xx)] = "   "
          walk(xx, yy)

      walk(randrange(w), randrange(h))
  
      s = ""
      for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
      return s

    if __name__ == '__main__':
      print(f"{color.G}Result: {color.E}")
      print("")
      print(make_maze())
      print("honestly, i dunno wat the use of this maze ಠ_ಠ.")
      redo_maze()
      
  def redo_maze() :
    maze_redo = input(f'''
    {color.Y}Generate Another Maze?{color.E}
    Please type {color.G}Y {color.E}for {color.G}YES {color.E}or {color.R}N{color.E} for {color.R}NO{color.E}
    {color.Y}Input{color.E} :''')
    if maze_redo.upper() == 'Y':
      print ("")
      maze_gen()
    elif maze_redo.upper() == 'N':
      print('See you later.')
    else :
      print(f"{color.R}Input must be Y or N.{color.E}")
      redo_maze()
  maze_gen()
  
else :
  print(f"{color.R}Invalid option, try again!{color.E}")
  