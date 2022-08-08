# = 0.10 × 45 = $4.50
# $45 – $4.50 = $40.50

def dis(price, discount):
	full_discount = round(price - ((discount / 100) * price), 2)
	print("Price is: GBP£" + str(full_discount))
	return full_discount

price = int(input("Enter price in GBP£: "))
discount = int(input("Enter discount percentage: "))

if discount < 0 or discount > 100:
    raise Exception("Invalid discount percentage!")
    
dis(price, discount)

