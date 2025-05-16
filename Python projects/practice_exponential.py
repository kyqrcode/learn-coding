def exp(base, power):
    ans = 1
    while (power > 0):
        ans = ans * base
        power -= 1
    return ans

print(exp(5,6))

#def raise_to_power(base, power):
#    ans = 1
#    for index in range(power):
#        ans = ans * base
#    return ans
#
#print(raise_to_power(5, 6))