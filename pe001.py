"""
PE001
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

#昨日も解いたけれど、ファイルを消してしまったので復習も兼ねて書き直してみる。

i = 1 #この宣言は必要なのだろうか？
sum = 0

#文法演習としてあえて関数を使ってみる。
def module(x):
    if(x % 3 == 0) or (x % 5 == 0):
        return x
    else:
        return 0 #関数を定義する場合、戻り値にNoneが含まれると型認識が狂う。

for i in range(1,1000):
    addition = module(i)
    sum += addition

print(sum)
