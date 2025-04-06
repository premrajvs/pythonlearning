# Scenario: Demonstrating local and global variables.
global_var = 10

def my_function():
    local_var = 5
    print(f"Inside the function: global_var = {global_var}, local_var = {local_var}")

my_function()
print(f"Outside the function: global_var = {global_var}")
# Trying to access local_var here would cause an error.