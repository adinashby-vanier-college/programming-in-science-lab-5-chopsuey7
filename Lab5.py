# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    return ""

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for n in range(1, 5):
        for j in range(1, n + 1):
            result += str(j)
        result += "\n"
    return result

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    b=0
    sum=0
    while b <n:
      b+=1
      sum+=b
    return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):

  
    return 