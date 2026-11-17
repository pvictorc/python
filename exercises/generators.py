
# Step 1: Define the generator function
def bake_cookies(batch_size, max_batches):
    total_cookies=0
    batch_count=0
    while(batch_count<max_batches):
        total_cookies+=batch_size
        batch_count+=1
        yield(total_cookies)
# Step 2: Create a generator object
cookie_batches = bake_cookies(5,3)

# Step 3: Use a for loop to iterate through the generator and generate batches of cookies
for cookies in cookie_batches:
    print(f"Total cookies baked: {cookies}")

# Your code here

# Step 1: Copy the previous generator function, rename, and modify
def bake_cookies_updated(batch_size, max_batches=None):
    total_cookies=0
    batch_count=0
    while(max_batches is None or batch_count<max_batches):
        total_cookies+=batch_size
        batch_count+=1
        yield(total_cookies)

# Step 2: Create a generator object with no limit
unlimited_cookie_batches_updated = bake_cookies_updated(5,None)

# Step 3: Use next() to retrieve batches of cookies (no limit imposed)
print("Unlimited Batches:")
for i in range(1,5):
    print(f"Batch {i}: {next(unlimited_cookie_batches_updated)} cookies")

