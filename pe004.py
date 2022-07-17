"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
#9009のように左右対称になる数字のうち、三桁同士の積で最大のものを求める。
#まずある数が左右対称になっているかどうか判定する関数を作る。

#print(99*99) => 9801
#print(999*999) => 998001

#以上の実験から、二桁と二桁を掛け合わせたときに、積が四桁を越えることはなく、
#また三桁と三桁を掛け合わせても、積が六桁を越えることがないことも証明された。
#これが一般にn桁掛けるn桁の積が2n桁になるのかどうかはわからない。
#しかし、例えば五桁掛ける五桁の最小の積は10000*10000だが、
#この積は100000000で、九桁である。このとき10000*9999にすると、
#99990000で八桁に桁落ちする。なので一般に、n桁掛けるn桁の積は最低でも(2n-1)桁になる。
#そして、最大でも2n桁にしかならないようである。
#ここで求めるのは左右対称の最大値なので、六桁になると想定していいだろう。
#オーソドックスなアプローチとして、まず六桁の数字を(a*100000+b*10000+c*1000+d*100+e*10+f)
#に見立ててみる。そして、(a=f) and (b=e) and (c=d)のとき、trueを返す関数を作る。
#このとき、まず六桁の数字の方を先に生成してしまい、それらが二つの三桁の因数に分解できるか
#事後的に分析すればいいのだと考えてみる。

#色々試したがこんがらがってきたので、根本的にやり方を変える。
#まずfor文をネストして、100〜999までの数の二つの組み合わせを全て生成する。
#そして、その組み合わせをcharのリストにして、左右対称かチェック。
#最後にチェックされた数が答え。

palindromes = list()

for i in range(100,1000): #100から始めると、6桁の数字だけを計算できる。
    for j in range(i,1000): #計算量削減のため、iから始める。
        number = i * j
        string = str(number)
        list = [char for char in string]
        if (len(list) == 6) and (list[0] == list[5]) and (list[1] == list[4]) and (list[2] == list[3]): #もし左右対称なら
            palindromes.append(number) #左右対称の数を全部一つのリストに格納。

print(max(palindromes)) #最大値を出力。

#ちょっと反則的だが、嘘のようにあっけなく終わった。
#答えのPDFをみると、reverse関数というのを設定している。
#桁をひっくり返して、元の数と符号するときに返り値を返すらしい。
#これはあくまでも数学の領域内で済ましている。
