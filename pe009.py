"""
PE009
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
#a<b<cかつa+b+c=1000かつa^2+b^2=c^2を満たすabcの積を求める。

#ピタゴリアントリプレットかをチェックする関数。
def checker(a,b,c):
    if(a < b) and (b < c) and (a ** 2 + b ** 2 == c ** 2):
        sum = a + b + c
        return sum
    else:
        return None

#checker()に投げ込む引数を生成するループ処理。

for i in range(998,1):
    for j in range(i,1):
        for k in range(j,1):
            sum_of_triplet = checker(i,j,k)
            print(sum_of_triplet,i,j,k)
            #if (sum_of_triplet == 1000):
            #    print(i * j * k)
            #else:
            #    continue
