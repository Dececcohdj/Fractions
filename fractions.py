# (3/4) + (4/6)

# This is called "Brute Force"
# 
# 4, 8, 12 
# is (4 + 4 + ...) until we get to 12
#
# TO DO: Make a program that brute forces its way to 12 with 4

# 6, 12 
# is ()
#
# TO DO: Make a program that brute forces its way to 12 with 6

# 9 18 27 36 45 54 63 72 81
# is ()
# TO DO: Make a program that brute forces its way to 81 with 9



# (4 x 3) and (6 x 2) both give the least common denominator

# 4 x 3 = 12

# 6 x 2 = 12

denominator = 1

print("before loop: ", denominator)

while denominator == 12:
    denominator = 0 + 4
    print("in loop: ", denominator)
    if denominator == 12:
        print("after if: ", denominator)
        break   

print("after loop: ", denominator)

