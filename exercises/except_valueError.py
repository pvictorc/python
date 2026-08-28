
# Step 1: Define the function
def serve_popcorn(snack):
    try:
        if(snack!="popcorn"):
            raise ValueError("We only serve popcorn!")
        else:
            return(f"Serving popcorn...")
    except ValueError as e:
        return(f"Error: {e}")
        

# Step 2: Call the function with a value and store the result
result = serve_popcorn("pineapple")

# Step 3: Print the result
print(result)


# Part 2: Define the test_popcorn function and call it


# Step 1: Define the test_popcorn function
#   - Initialize a list: snacks = popcorn,candy,pretzels
#   - Loop through each snack
#   - Call serve_popcorn for each snack
#   - Print: Input: <snack>, Output: <result>
def test_popcorn():
    snacks = ["popcorn", "candy","pretzels"]
    for i in snacks:
        print(f"Input: {i}, Output: {serve_popcorn(i)}")
        
# Step 2: Call test_popcorn to run the tests
test_popcorn()


# Part 3: Define the serve_snack function and test it
def serve_snack(snack, quantity):
    try:
        if(quantity<0):
            raise ValueError("Invalid quantity")
        elif(snack!="popcorn"):
            raise TypeError("Invalid snack type")
        else:
            return(f"Serving {quantity} portions of {snack}")
    except ValueError as e_quant:
        return("Quantity can't be negative!")
    except TypeError as e_type:
        return("Unknown snack type!")

print(serve_snack("popcorn", 5) )
print(serve_snack("candy", 2) )
print(serve_snack("popcorn", -1) )


# Part 4: Define the check_quantity and purchase_snack functions and test them
def check_quantity(quantity):
    if(quantity<0):
        raise ValueError("Invalid quantity")
        
def purchase_snack(snack,quantity):
    try:
        check_quantity(quantity)
        return("Purchase successful for <quantity> portions of <snack>.")
    except ValueError as e:
        return(f"Purchase failed: {e}")

print(purchase_snack("popcorn", 5))
print(purchase_snack("candy", -3))
print(purchase_snack("pretzels", -1))