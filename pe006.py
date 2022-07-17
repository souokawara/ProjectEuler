"""
PE006
Find the difference between the sum of the squares
of the first one hundred natural numbers
and the square of the sum.
"""
#100までの自然数の平方の和と100までの自然数の総和の平方の差を求める。
#これは簡単そうだ。

#変数
the_sum_of_squares = 0
square_of_the_sum = 0
the_sum = 0

#平方の和
for i in range(1,101):
    the_sum_of_squares += i ** 2

#和の平方
for j in range(1,101):
    the_sum += j

square_of_the_sum= the_sum ** 2

print(the_sum_of_squares)
print(square_of_the_sum)

answer = square_of_the_sum - the_sum_of_squares
print(answer)

"""
これは実に簡単で拍子抜けだ。
""" 
