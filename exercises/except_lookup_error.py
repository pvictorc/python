lost_and_found = {
    'Sunglasses': 1,
    'Hat': 2,
    'Waterbottle': 3,
}

def check_lost_and_found(item):
    try:
        return lost_and_found[item]
    except LookupError as e:
        print (f"Exception: Item '{item}' not found in lost and found.")


check_lost_and_found('T-shirt')  # This will raise a LookupError and be caught by the except block