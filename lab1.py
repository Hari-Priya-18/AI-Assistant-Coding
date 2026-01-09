# ===== ITERATIVE METHOD =====
# Function to generate Fibonacci series iteratively up to n terms
def fibonacci_iterative(n):
    """
    Generate and print the Fibonacci series using iterative approach.
    
    Args:
        n (int): The number of terms in the Fibonacci series to generate
    """
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    print("Fibonacci series (Iterative):")
    
    # Iterate n times to generate n terms of the Fibonacci series
    for i in range(n):
        # Print the current Fibonacci number
        print(a, end=" ")
        # Update a and b to the next two consecutive Fibonacci numbers
        a, b = b, a + b
    
    # Print a newline at the end for better formatting
    print()


# ===== RECURSIVE METHOD =====
# Function to generate Fibonacci series recursively
def fibonacci_recursive(n):
    """
    Generate and print the Fibonacci series using recursive approach.
    
    Args:
        n (int): The number of terms in the Fibonacci series to generate
    """
    # Base case: if n is 0 or negative, return empty list
    if n <= 0:
        return []
    
    # Helper function to calculate the nth Fibonacci number
    def fib_helper(num):
        # Base cases for recursion
        if num == 0:
            return 0
        elif num == 1:
            return 1
        # Recursive case: sum of previous two Fibonacci numbers
        else:
            return fib_helper(num - 1) + fib_helper(num - 2)
    
    print("Fibonacci series (Recursive):")
    
    # Generate and print n Fibonacci numbers using recursion
    for i in range(n):
        # Call the helper function to get the ith Fibonacci number and print it
        print(fib_helper(i), end=" ")
    
    # Print a newline at the end for better formatting
    print()


# Main program
if __name__ == "__main__":
    # Take the number of terms from the user
    n = int(input("Enter the number of terms: "))
    
    # Display both iterative and recursive approaches
    print()
    
    # Call the iterative Fibonacci function
    fibonacci_iterative(n)
    
    print()
    
    # Call the recursive Fibonacci function
    fibonacci_recursive(n)

