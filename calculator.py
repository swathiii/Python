from calc_art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
              "+" : add, 
              "-" : subtract, 
              "*" : multiply, 
              "/" : divide,
             }

def calculator(): 
  print(logo)
  
  num1 = float(input("What's the first number? "))
  
  for element in operations:
    print(element)
  
  prompt_ = True
  while prompt_:
    
    operator = input("What operation would you like to perform?")  #+
    
    num2 = float(input("What's the next number? "))
    
    answer = operations[operator](num1, num2)   #func = add(num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")
    
    prompt = input(f"Do you want to continue performing more operations on {answer}? type 'y' or  'n': ")
    if prompt == 'y':
      num1 = answer
    else:  
      prompt_ = False
      calculator()                              #recursion - clears every result

calculator()
    
