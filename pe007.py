"""
PE007
By listing the first six prime numbers
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
#10001番目の素数を求める。これはむずかしそうである。
#まずリストに既存の素数をデータベース化していき、
#リスト内のいずれかの要素で割れた時にはその数字は飛ばし
#どの要素でも割り切れなかった時にリストに含める。
#そしてlist[10000]の要素に収まった数が求める素数だろう。

p_list = [2,3,5,7,11,13]
i = 14 #13の次からカウントするパラメーター

while (True):

    for j in p_list:
        if (i % j == 0):
            break #素数じゃないとき
        elif (i % j != 0) and (j == p_list[-1]):#最後まで当たったけど割り切れなかった時
            p_list.append(i) #素数リストに追加
        else:
            continue #まだ素数かもしれないとき

    #もし10001番目の素数を見つけたら処理終了
    if (len(p_list) == 10001):
        break
    else:
        i += 1

print(p_list[10000])

"""
意外にあっさりやれた。プログラミングに脳が馴染んできたか。
"""
