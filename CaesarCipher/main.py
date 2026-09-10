import alphabets

direction = input("Type encode to encode and decode to decode \n").lower()
text = input("Type your message \n").lower().strip()
shift = int(input("Enter the shift number \n"))

def encrypt(org_text,num):
    final_value = ""
    for n in org_text:
        if n not in alphabets.alpha:
             final_value += n
        else:
           x= alphabets.alpha.index(n)
           y = alphabets.alpha[(x+num)%26]
           final_value += y
    print(final_value)
    

def decrypt(org_text,num):
    final_value = ""
    for n in org_text:
       x= alphabets.alpha.index(n)
       y = alphabets.alpha[(x-num)%26]
       final_value+= y
    print(final_value)
    
 
if direction == "encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)
     
        
        
    
  
