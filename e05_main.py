import math
import my_module

def get_tip(m):
  '''returns 20% rounded up'''
  return math.ceil(m*0.20)

def split_cost(m):
  '''returns half rounded up'''
  top = my_module.large_half(m)
  bot = m - top
  return top, bot

def main():
  print("Inside main.py:")
  #read the cost of a product
  cost = int(input("What is the cost? "))
  # find out what is the tip
  tip = get_tip(cost)
  print("The tip is:",tip)
  total = cost + tip
  print("The total cost (with tip) is:",total)
  # find out how much each person A, and B, pays
  A_pays, B_pays = split_cost(total)
  print("A_pays: $",A_pays)
  print("B_pays: $",B_pays)

main()

# Last Step:
# --------------------------------------------------
#   1. comment out the line that has the call to main() above
#   2. uncomment the following two lines:
# if __name__ == "__main__":
#     main()
