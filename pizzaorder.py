#Pizza order
print("""
 ____                   
/    \	WELCOME TO SWOT PIZZERIA, LET'S ORDER YOUR PIZZA	
  u  u|      _______    
    \ |  .-''#%&#&%#``-.   
   = /  ((%&#&#&%&VK&%&))  
    |    `-._#%&##&%_.-'   
 /\/\`--.   `-."".-'
 |  |    \   /`./          
 |\/|  \  `-'  /
 || |   \     /
 
 """)
size = input("What size pizza do you eant? S, M or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

if size == 'S':
    bill = 15
if size == 'M':
    bill = 20
if size == 'L':
    bill = 25
    
if pepperoni == 'Y' and size == 'S':
    bill += 2
if pepperoni == 'Y' and (size == 'M' or size == 'L'):
    bill += 3
    
if cheese == 'Y':
    bill += 1
    
print(f"Your final bill is: ${bill}") 