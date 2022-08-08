dr = input("Calculate the digital root of an integer: ")

# try 
# if not type(dr) is int:
  # raise TypeError("Only integers are allowed")

def digital_root(dr):
    dr = int(dr) % 9 # As simple as a modulo 9
    
    if dr == 0:
        dr = 9 # The digital root is 9 for multiples of 9
        
    print(dr)
    return dr

digital_root(dr)
