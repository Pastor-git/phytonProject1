# Definicja funkcji silnia_i
def silnia_i(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s
# 4! = 1*2*3*4


print(silnia_i(2000))

# def silnia_r(n):
#     # if n in (0,1):
#     # if n <=1 :
#     # if n == 0 or n == 1:
#     if n <= 1:
#         return 1
#     elif n > 1:
#         return n * silnia_r(n-1)
#
# print(silnia_r(998))