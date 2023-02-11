import math
import multiprocessing
import nmap
import psutil

def get_computers():
    """Returns a list of computers on the same internet"""
    nm = nmap.PortScanner()
    nm.scan(hosts='127.0.0.1/24', arguments='-sn')
    return nm.all_hosts()

def get_info(computer):
    """Returns information about the given computer"""
    data = {}
    data['cpu'] = psutil.cpu_count()
    data['memory'] = psutil.virtual_memory().total
    return data

# Fibonacci Function
def fibonacci(n):
    """Returns the Fibonacci number for the given index"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Add Function
def add(x, y):
    """Returns the sum of two numbers"""
    return x + y

# Quadratic Function
def quadratic(a, b, c):
    """Returns the roots of the quadratic equation ax^2 + bx + c = 0"""
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        # Two real roots
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # One real root
        x = -b / (2*a)
       return x,
    else:
        # No real roots
        return tuple()

def run_tasks(func, args):
    """Runs a function with given arguments on a pool of worker processes"""
    # Get a list of computers on the same internet
    computers = get_computers()

    # Create a pool of worker processes
    with multiprocessing.Pool(len(computers)) as pool:
        # Run the function on the pool
        result = pool.apply_async(func, args)

        # Return the result
        return result.get()


def main():
    # Get information from the computers
    info = {}
    for computer in get_computers():
        info[computer] = get_info(computer)

    # Print the information
    for computer, data in info.items():
        print(f"Computer: {computer}")
        print(f"CPU: {data['cpu']}")
        print(f"Memory: {data['memory']}")

    # Add tasks to the pool
    print("\n***Call Fibonacci Number Function***")
    fb_nb = input("Enter a number for fibonacci: ")
    fb_nb = int(fb_nb)  
    #tasks = [(i,) for i in range(41)]  
    # Run the fibonacci function
    result = run_tasks(fibonacci, (fb_nb,))
    print(result)

    print("\n***Call add function***")
    add_1 = input("Enter a first number for addition: ")
    add_2 = input("Enter a second number for addition: ")
    add_1 = int(add_1)
    add_2 = int(add_2)
    # Run the Add function
   result = run_tasks(add, (add_1,add_2))
    print(result)
    
    # Run the Quadratic function
    print("\n***Call Quadratic function***")
    quad_1 = input("Enter a first number for Quadratic: ")
    quad_2 = input("Enter a second number for Quadratic: ")
    quad_3 = input("Enter a third number for Quadratic: ")
    quad_1 = int(quad_1)
    quad_2 = int(quad_2)
    quad_3 = int(quad_3)
    # Run the Add function
    result = run_tasks(quadratic, (quad_1,quad_2,quad_3))
    print(result) 

if __name__ == "__main__":
    main()
