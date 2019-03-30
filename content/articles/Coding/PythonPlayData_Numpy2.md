Title:  Python玩數據 (3)：Numpy [2/2]
Date: 2017-05-06 12:00
Category: Coding
Tags: Python玩數據
Slug: python-play-with-data_3
Author: YC Chen
Illustration: coding_front_board.jpg
Alias: /YCNote/post/22.html
related_posts: python-play-with-data_1,python-play-with-data_2


在上一章節的討論，我們已經有了Numpy的基礎概念，在這一篇當中，我們會更深入的了解Numpy還有什麼進階的功能，包括：產生ndarray的多種方法、broadcast的概念以及ndarray的進階操作手法。

## 產生ndarray的其他方法

在上一章，ndarray的產生方法是由list產生的。

```python
>>> A = np.array([[1,2],[3,4]],dtype='float64')
```

Numpy還提供產生ndarray的其他方式，幫助我們更容易的產生ndarray，譬如，產生一個數列。

```python
>>> E = np.arange(12)
>>> E
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
>>> F = np.arange(start=1,stop=13)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
>>> G = np.arange(start=3,stop=6,step=0.5)
array([ 3. ,  3.5,  4. ,  4.5,  5. ,  5.5])
```

stop指的是停止的那點，那點是不包含在產生的數列的。

1D的數列也可轉換成多維度的數列。

```python
>>> H = F.reshape((2,6))
>>> H
array([[ 1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12]])
>>> H.shape
(2, 6)
>>> K = F.reshape((3,4))
>>> K
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

另外還有一種可以產生連續數列的方法。

```python
>>> np.linspace(0, 2, 9)
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
```

這個函數是這樣的，0是起始值，2是最終值，這個最終值是包含在數列裡的，9是代表數列會有九個數字，所以它會自動從這區間找九個數字均勻分配。

另外，也可以產生一個全部都零或一的數列，或是矩陣中的「單位矩陣」。

```python
>>> np.zeros(9).reshape((3,3))
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])
>>> np.ones(6).reshape((2,3))
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])
>>> np.eye(3)     # "eye" means "I"
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
```

或者，你想要亂數產生也可以。

```python
>>> np.random.random((2,4))
array([[ 0.14405468,  0.2312139 ,  0.79134702,  0.18676625],
       [ 0.95305253,  0.44833768,  0.87919535,  0.69051727]])
```

如果你想要數列依照你給定的規則產生，就先定義好函數，然後再利用`fromfunction`製造數列。

```Python
>>> def func1 (i,j):
    	return i + j
>>> np.fromfunction(func1, (3, 3), dtype=int)
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])
```

這麼一來，每個位置的值都是由我們所定義的函數所決定。如果你覺得那個`func1`名稱很多餘，還有下面這個方法。

```Python
>>> np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])
```

上面我使用了`lambda`，這個東西稱之為『匿名函數』。

```python
lambda i, j: i + j
```

和

```python
def something(i,j):
    return i + j
```

上面這兩個函式是等價的，差異只在於，第一個函式是沒有名稱的，稱為匿名函數，第二種就是一般的函式，具有名稱。

## Broadcasting

在上一章，我有提到一般的矩陣運算，在Numpy中是採用element-wise operation，也就是每個相應元素做運算，然後產生新的ndarray，這個前題是兩組要運算的ndarray他們的shape是相同的，那如果遇到shape不一致，Numpy會怎麼處理呢？實際上，Numpy會幫你把陣列給延伸展開，就像廣播(broadcasting)一樣的傳遞出去，這遵照所謂的broadcasting rules。

```python
>>> A = np.array([[1,2],[3,4]],dtype='float64')
>>> B = np.array([[5,0],[0,0]],dtype='float64')
>>> A + B      # element-wise plus
array([[ 6.,  2.],
       [ 3.,  4.]])
>>> A.shape
(2,2)
>>> B.shape
(2,2)
```

上面就是最普遍的兩個相同shape的矩陣作運算。

那如果是這個情況呢？

```python
>>> A = np.array([[1,2],[3,4]],dtype='float64')
>>> A + 1
array([[ 2.,  3.],
       [ 4.,  5.]])
>>> A * 2
array([[ 2.,  4.],
       [ 6.,  8.]])
```

你會發現如果矩陣對一個單一元素作運算，其實就等同於這個單一元素對矩陣內的元素分別作運算，這個方式相當好理解，那如果是這樣呢？

```python
>>> C = np.array([[2],[3]],dtype='float64')
>>> C.shape
(2, 1)
>>> D = np.array([[5,7,11]],dtype='float64')
>>> D.shape
(1,3)
>>> E = C * D
>>> E
array([[ 10.,  14., 22. ],    # [[ 2*5, 2*7, 2*11 ],
       [ 15.,  21., 33. ]])   #  [ 3*5, 3*7, 3*11 ]]
>>> E.shape
(2,3)
```

讓我來分解解說一下broadcasting究竟做了什麼，broadcasting能自動填滿矩陣有一個大前提，

> 參與運算的所有矩陣必須符合以下規則才能做broadcasting，所有矩陣的shape由axis＝-1開始對齊去比較彼此間的rank，所有矩陣的在每個axis下的rank必須符合以下兩種規則其中之一：
>
> 1. 所有rank為同一個值
> 2. 只能有一個矩陣rank為非0或1，其餘矩陣的rank都要為0或1

上面這個例子，在axis= -2之下，只有C矩陣rank具有非0或1的2，而D的rank則為1；在axis= -1之下，只有D矩陣rank具有非0或1的3，而C的rank則為1，因此這兩個陣列可以使用broadcasting rule來延伸。

為什麼我們需要這樣的前提假設，原因是符合這樣的情況下，我們可以藉由重複的複製貼上來使得兩個或多個矩陣有一樣的shape，C矩陣shape為(2,1)，所以在axis= -2的方向上，重複貼3次就會產生出shape為(2,3)的矩陣；D矩陣的shape為(1,3)，所以在axis= -1的方向上，重複貼2次就會產生出(2,3)的矩陣，如此一來兩個矩陣都是(2,3)就可以作element-wise operation。

逐步示範一下，

```
C  = [[2],[3]] # shape = (2,1)
C' = [[2,2,2],[3,3,3]] # shape = (2,3)
D  = [[5,7,11]] # shape = (1,3)
D' = [[5,7,11],[5,7,11]] # shape = (2,3)
E = C' * D'
```

以下這些都是同樣道理

```
A      (2d array):  5 x 4
B      (1d array):      1
Result (2d array):  5 x 4

A      (2d array):  5 x 4
B      (1d array):      4
Result (2d array):  5 x 4

A      (3d array):  15 x 3 x 5
B      (3d array):  15 x 1 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  2 x 3 x 4
B      (2d array):      3 x 1
Result (3d array):  2 x 3 x 4
```

我們再來看一下，如果維度不一樣是怎麼運作，譬如說2D碰上3D的，

```python
>>> F = np.arange(24).reshape((2,3,4))
>>> F
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
>>> F.shape
(2, 3, 4)
>>> G = np.array([[1],[2],[3]])
>>> G.shape
(3, 1)
>>> H = F + G
>>> H
array([[[ 1,  2,  3,  4],
        [ 6,  7,  8,  9],
        [11, 12, 13, 14]],

       [[13, 14, 15, 16],
        [18, 19, 20, 21],
        [23, 24, 25, 26]]])
>>> H.shape
(2,3,4)
```

分解一下

```
F  = [[[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]],
      [[12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]]]  # shape = (2,3,4)
G = [[1],
	 [2],
	 [3]] # shape = (3,1)
G'= [[1,1,1,1],
	 [2,2,2,2],
	 [3,3,3,3]] # shape = (3,4)
G"= [[[1,1,1,1],
	  [2,2,2,2],
	  [3,3,3,3]],
	 [[1,1,1,1],
	  [2,2,2,2],
	  [3,3,3,3]]] # shape = (2,3,4)
	  
H = F + G"
   = [[[ 0+1,  1+1,  2+1,  3+1],
       [ 4+2,  5+2,  6+2,  7+2],
       [ 8+3,  9+3, 10+3, 11+3]],
      [[12+1, 13+1, 14+1, 15+1],
       [16+2, 17+2, 18+2, 19+2],
       [20+3, 21+3, 22+3, 23+3]]]
```

那這樣的性質可以怎麼運用呢？舉個例子。

```
Example:
請問平面上這些點(102.0, 203.0),(132.0, 193.0),(45.0, 155.0),(57.0, 173.0)，哪一點最接近(111.0,188.0)?
```

```python
>>> observation = np.array([111.0,188.0])
>>> codes = np.array([[102.0, 203.0],[132.0, 193.0],[45.0, 155.0],[57.0, 173.0]])
>>> diff = codes - observation  # broadcasting
>>> diff
array([[ -9.,  15.],
       [ 21.,   5.],
       [-66., -33.],
       [-54., -15.]])
>>> dist = np.sqrt(np.sum(diff**2,axis=-1)) # distance
>>> dist
array([ 17.49285568,  21.58703314,  73.79024326,  56.04462508])
>>> nearest = np.argmin(dist)
>>> nearest
0 	# ANS is (102.0, 203.0)
```

## Slice and Fancy Indexing

最後，來看一下我們可以怎麼去切ndarray。在python內建語言中，常見的slice是這個樣子

```python
>>> s = [1,2,3,4,5]
>>> s[0]
1
>>> s[1:3]
[2, 3]
```

那如果是維度再加一級呢？則是這個樣子

```python
>>> w = [[1,2,3,4,5],[2,3,4,5,6]]
>>> w[1][4]
6
>>> w[0][1:3]
[2, 3]
```

如果是ndarray，我們常常處理維度大於1的陣列，如果用這個方法來slice，就顯得非常麻煩，Numpy提供了一種比較直覺的方式來做slice。

```python
>>> M = np.array([[1,2],[3,4],[5,6]])
>>> M
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> M[1,0]
3
```

在中括號裡頭用逗點隔開來表示在各個axis上要取的位置，還可以填入一個陣列來取出一個範圍。

```python
>>> M[1,0:2]
array([3, 4])
>>> M[1,:]   # ":"代表全取，效果和 M[1,0:2]一樣
array([3, 4])
>>> M[1,[0,1]] # 寫成陣列也可以，效果和 M[1,0:2]一樣
array([3, 4])
>>> # 還可以做到在axis=0的方向上取範圍，這是list做不到的
>>> M[:,0]
array([1, 3, 5])
```

我們也可以引入一個ndarray來做篩選，常見使用的是布林陣列。

```python
>>> N = np.array([[1,2],[3,1]])
>>> b = ( N != 1 )
>>> N
array([[1, 2],
       [3, 1]])
>>> b
array([[False,  True],
       [ True, False]], dtype=bool)
>>> N[b]
array([2, 3])
```

b是由一個邏輯運算產生，這個邏輯運算會對矩陣作element-wise operation，所以會得出一個大小相同的布林陣列。而我們可以將b引入N當作篩選器，把符合的給取出來。事實上還可以更強大的去將取出來的值改值。

```python
>>> N[b] *= 2
>>> N
array([[1, 4],
       [6, 1]])
```

上面我將取出來的值加倍，這樣的手法來取值改值會直接影響到原陣列，這是一個很重要的手法。

## 子彈總結

* 產生ndarray的其他方法：np.arange, np.linspace, np.zeros, np.ones, np.eye, np.random.random 和 np.fromfunction
* Broadcasting的前題：所有矩陣的shape由axis＝-1開始對齊去比較彼此間的rank，所有矩陣的在每個axis下的rank必須符合以下兩種規則其中之一：
  1. 所有rank為同一個值
  2. 只能有一個矩陣rank為非0或1，其餘矩陣的rank都要為0或1
* Slicing Method ( Ex: M[1,0:2] )
* 布林陣列的取值賦值方法
