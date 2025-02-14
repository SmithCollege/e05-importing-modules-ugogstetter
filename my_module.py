"""
Pablo Frank, 2024
An example module with one function to return
the "large integer half" of a number
"""
def large_half (n):
    """ Obtains an integer split into two integer halfs
    Args:
      m: the input number
    Returns:
      the large integer half of the number

    Example:
      - the large integer half of 24 is 12 (with 12 remainder)
      - the large integer half of 25 is 13 (with 12 remainder)
    """
    # You could simply return n - n//2
    val = n - n//2
    return val

# Step 2: (Uncomment the following code until "Step2-END")
# --------------------------------------------------
def main():
    print("Inside my_module.py")
    total = 25
    large = large_half( total )
    small = total - large
    print(f"The large half of {total} is {large} and the small half is {small}")

#main()
# Step2-END ----------------------------------------


# Step 3:
# --------------------------------------------------
#   1. comment out the line that has the call to main() above
#   2. uncomment the following two lines:
print(__name__)
if __name__ == "__main__":
    main()
