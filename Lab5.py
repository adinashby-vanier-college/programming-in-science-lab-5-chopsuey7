# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = []
    for i in range (n):
        if i ==0 or i == n-1:
            result.append( "*" * n)
        else:
            result.append( "*" + (n-2)*" " +"*")
    return "\n".join(result)

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(1, n+1):
        for j in range(1, i + 1):
            result += str(j)
        result += "\n"
    return result.rstrip()  # Removes the last unnecessary newline

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
    s = 0
    result = []
    for i in range(n):
        spaces = n - i - 1  # Spaces before stars
        if i == 0:
            s = 1
        else:
            s += 2
        result.append(" " * spaces + "*" * s)  # Remove extra spaces at the end
    return "\n".join(result)
