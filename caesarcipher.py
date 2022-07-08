from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar( text, shift, direction ):
  result_text = ""
  for char in text:
    if char in alphabet:                #to acommodate spaces, special characters and numbers 
      position = alphabet.index(char)
      if direction == "encode":
          new_position = position + shift
      elif direction == "decode":
        new_position = position - shift
      result_text += alphabet[new_position]
    else:
      result_text += char               #places the whitespace/special character/number that is not in the list
    
    
  print(f"The {direction}d text is {result_text}")
  
cont = True
while cont:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26                    #to acommodate huge shift values
  
  caesar(text, shift, direction)

  check_cont = input("\nType 'yes' if you want to continue using caesar cipher or 'no' to exit: ")
  if check_cont == "no":
    cont = False
    print("\nGoodbye!")
  elif check_cont == "yes":
    cont = True