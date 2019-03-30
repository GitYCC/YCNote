Title: 物件導向武功秘笈（1）：認知篇 — 什麼是好的程式？
Date: 2018-04-05 12:00
Category: Coding
Tags: 軟體設計
Slug: introduction-object-oriented-programming_1
Author: YC Chen
Illustration: coding_front_board.jpg
Alias: /YCNote/post/47.html
related_posts: introduction-object-oriented-programming_2,introduction-object-oriented-programming_3



### 物件導向為何重要？

我相信很多朋友一定像YC我一樣，想要學某個程式語言，就去買那個程式語言的簡介書籍，然後一章一章的唸下去，這種書通常會先教變數怎麼設定？然後再教if、while、for、function等程式邏輯。

那如果你學的是「物件導向」的語言，譬如：Java、C++、Python，接下來的章節就會開始介紹「類別」、「物件」等等難懂的東西，然後就會陷入一種霧煞煞的狀態，然後心中就會出現一種聲音：為什麼寫個程式你跟我扯什麼「物件」？我原本用前面所學的方法就可以完成所有事情啦！為何要把事情弄的這麼複雜？這東西到底有什麼好處啊？

YC一開始也是充滿著疑惑，然後一知半解的就把這些定義記在心中，然後天真的認為「物件導向」只是讓程式比較整齊的方法罷了！直到後來學了資料結構與演算法，然後又學了一點設計模式，然後又有過幾個大型軟體開發的經驗，一路走過才漸漸的了解「物件導向」是怎麼一回事？

所以我打算把這些收穫用三篇文章來說明，好讓讀者們可以少走一點冤枉路，在第一篇中，也就是本篇，我會帶大家認識好的程式是長什麼樣子的，它擁有什麼樣的特點，有了正確的認知，除了可以讓我們避免寫出糟糕的程式之外，我們也才能漸漸的認識到「物件導向」為何重要。


### 程式的好壞？ 

一開始，我們必須要對程式培養出鑑賞能力，我曾經聽過電視上有一位歌唱老師說過：「好的歌手必須先練他的聽力」，我覺得相同的，一個好的Programmer要先培養出對於程式的鑑賞能力。

首先，一個好的程式當然要「能正常執行」，要能滿足客戶的需求，這是基本款，所以一般而言我們會使用很多的測試去看看程式是否可以正常運作，我們會找一些一般的條件來測試，我們也會找一些合法但是位於極端條件的例子，也就是邊界條件（Edge Case）來測試，或者找一些不合法的例子試試程式是否可以排除錯誤條件。

測試可以即早的發現Bug，即早的治療，如果真的發現有Bug的話，接下來就是去找出Bug的源頭，這可就相當的困難，這裡想像一下喔！如果你的程式總共有1000行，而當你測試時發現有Bug，那想從這麼多行當中找出Bug的來源是相當困難的，所以好的方法是這樣的，先將一個大任務分解成為幾個小任務，然後完成這幾個小任務後，逐一的進行測試，稱之為「單元測試」，最後在將這些測試完成的小任務組合成為大任務，然後再做最後的總測試，這麼一來就可以避免在大範圍中找尋Bug，又可以做到對程式從裡到外的完整測試以達到程式「能正常執行」的目的。

這裡提出一個問題讓大家思考，究竟要使用什麼方法去解析問題？讓我們可以有條理的拆解出小「單元」，來組合出最後的目標，有沒有一個系統化的思考方法？

第二點，一個好的程式必須是「穩健的」(Robust)，程式原本能用的功能，不會因為更新、不會因為添加新功能，就出現錯誤！要做到這一點，除了剛剛說的「單元」拆分以外，還要讓「單元」和「單元」之間不會有太多的彼此影響，這麼一來在原先的功能所調用的「單元」不被動到的前提下，我還可以新增新的功能，才能做到「穩健的」特質。

第三點，一個好的程式必須具備「不重複撰寫」的特性，有一句經典的法則叫做「Don't Repeat Yourself」，不要去重複寫已經寫過的程式碼，如果是重複需要用到的「單元」我們就把它獨立出來，讓其他程式去調用它，對於工程師來說，「不重複撰寫」意味著可以少寫一點程式碼，增加開發的速度，更重要的是，調用公享的程式碼可以讓程式更有邏輯，更具一致性，能夠減少出錯的可能性。

第四點，好的程式要具有「可讀性」，軟體開發常常是長時間、多人合作、龐大的程式碼，如果程式碼沒有具備清晰的邏輯、沒有在該註解的部分寫清楚、沒有一個統一的規範，這樣的開發終就會陷入泥坑，永遠解不完的Bug會不斷的出現，解了一個又產生一個，永無止盡的輪迴，而且最慘的是完全不清楚真正的源頭在哪裡，這可是軟體工程師的夢魘啊！

第五點，一個好的程式要具備「可擴展」，工程師最討厭的一句話應該就是客戶說：「我突然想到我還需要XXX功能，這只是在這邊再多一點而已，應該不難吧！」呵呵～通常「這多一點」就要大大的修改整個程式碼，弄不好還可能把原本的功能給搞壞，所以工程師應該在設計的一開始就考慮到會有什麼潛在需要更改的部分，而先採取因應措施，好讓程式易於擴展，好讓自己不會因此而加班！


### 低耦合、高內聚

再重複一次，一個好的程式要具備「正常執行」、「穩健」、「不重複撰寫」、「可讀性」、「可擴展」的特性，請將這些原則記在心裡，隨時的檢視自己的程式是不是有違反這些規則。

而剛剛我們有了一個大致的想法：將任務分成幾個小的「單元」是一個很好的策略，而為了讓程式「穩健」，這些「單元」之間不能有太多的相依性；但是站在另外一個角度看，為了讓程式「不重複撰寫」，我們需要讓一個「單元」使用另外一個「單元」，好讓工程師可以做到「Don't Repeat Yourself」，如此一來則是增加了「單元」間的相依性，這兩者是一個Trade-off。

有關「單元」的相依性有兩個重要術語—耦合性(Coupling)和聚合性(Cohesion)，耦合性指的是「單元」和「單元」之間資訊或參數依賴的程度，所以我們要追求「低耦合」。聚合性指的是「單元」內使用到自身資訊或參數的程度，所以我們要追求「高內聚」，通常「低耦合」都會伴隨著「高內聚」。



### 程式碼精練之旅

來看個例子，假設今天我想要實現一個求最大公因數的計算機，使用**Python**隨便寫一段程式碼可能是這樣的。

```python
def main():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")
    
    numA = int(str_numA)
    numB = int(str_numB)
    
    prime_factorize_A = dict()
    i = 2
    while(numA > 1):
        if numA % i == 0:
            prime_factorize_A[i] = prime_factorize_A.get(i,0) + 1
            numA /= i
        else:
            i += 1
            
    prime_factorize_B = dict()
    i = 2
    while(numB > 1):
        if numB % i == 0:
            prime_factorize_B[i] = prime_factorize_B.get(i,0) + 1
            numB /= i
        else:
            i += 1    
    
    common_prime = set(prime_factorize_A.keys()) & set(prime_factorize_B.keys())
    
    gcf = 1
    for prime in list(common_prime):
        m = min(prime_factorize_A[prime],prime_factorize_B[prime])
        gcf = gcf * (prime ** m)
    
    print("Greatest Common Factor: "+ str(gcf))
```

好！那接下來用剛剛的規則來檢視看看這個程式，第一點，有沒有「可正常執行」？上述的例子，沒有考慮到一些Edge Case，當輸入的值不是正整數，必須要報錯，所以我們將程式修改一下。

```python
def main():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")
    
    numA = int(str_numA)
    if numA <= 0: raise ValueError("invalid positive integer: "+str(numA))
    numB = int(str_numB)
    if numB <= 0: raise ValueError("invalid positive integer: "+str(numB))
    
    prime_factorize_A = dict()
    i = 2
    while(numA > 1):
        if numA % i == 0:
            prime_factorize_A[i] = prime_factorize_A.get(i,0) + 1
            numA /= i
        else:
            i += 1
            
    prime_factorize_B = dict()
    i = 2
    while(numB > 1):
        if numB % i == 0:
            prime_factorize_B[i] = prime_factorize_B.get(i,0) + 1
            numB /= i
        else:
            i += 1    
    
    common_prime = set(prime_factorize_A.keys()) & set(prime_factorize_B.keys())
    
    gcf = 1
    for prime in list(common_prime):
        m = min(prime_factorize_A[prime],prime_factorize_B[prime])
        gcf = gcf * (prime ** m)

    print("Greatest Common Factor: "+ str(gcf))

```

再來檢查一下是不是具有「不重複撰寫」的特性？也就是Don't Repeat Yourself，顯然是沒有遵守，`numA`和`numB`處理方法幾乎一模一樣，這會造成程式碼很冗長，來稍做修改。

```python
def checkPositiveInteger(num):
    if (not isinstance(num,int)) or (num<=0):
	    raise ValueError("invalid positive integer: "+str(num))
		
def primeFactorize(num):
    checkPositiveInteger(num)
	
    prime_factorize = dict()
    i = 2
    while(num > 1):
        if num % i == 0:
            prime_factorize[i] = prime_factorize.get(i,0) + 1
            num /= i
        else:
            i += 1
    return prime_factorize

def main():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")
    
    numA = int(str_numA)
    numB = int(str_numB)
        
    prime_factorize_A = primeFactorize(numA)
    prime_factorize_B = primeFactorize(numB)

    common_prime = set(prime_factorize_A.keys()) & set(prime_factorize_B.keys())
    
    gcf = 1
    for prime in list(common_prime):
        m = min(prime_factorize_A[prime],prime_factorize_B[prime])
        gcf = gcf * (prime ** m)
    
    print("Greatest Common Factor: "+ str(gcf))
```

接下來來檢查一下「穩健度」和「可擴展」，也就是程式是否符合：低耦合、高內聚，其實上面的程式碼有一個大問題，客戶端邏輯和業務邏輯混為一談，客戶端邏輯就是實現功能的部分，而業務邏輯就是實作的細節，所以上面的程式碼把所有的實作的細節全部攤在客戶端，這是相當不好的，這會造成不易更改，因此我們將程式作單元的拆分，讓業務邏輯和客戶端邏輯相分離，讓不直接實現客戶端的程式碼可以隱藏起來，減少客戶端和業務邏輯的耦合。然後順道加入求取最小公倍數的功能。

```python
import sys
def checkPositiveInteger(num):
    if (not isinstance(num,int)) or (num<=0):
	    raise ValueError("invalid positive integer: "+str(num))
		
def primeFactorize(num):
    checkPositiveInteger(num)

    prime_factorize = dict()
    i = 2
    while(num > 1):
        if num % i == 0:
            prime_factorize[i] = prime_factorize.get(i,0) + 1
            num /= i
        else:
            i += 1
    return prime_factorize

def findGCF(nums):
    prime_factorize = list()
    for num in nums:
        prime_factorize.append(primeFactorize(num))
		
    common_prime = set(prime_factorize[0].keys())
    for pf in prime_factorize[1:]:
        common_prime &= set(pf.keys())
    
    gcf = 1
    for prime in common_prime:
        m = sys.maxsize
        for pf in prime_factorize:
            m = min(m,pf[prime])
        gcf = gcf * (prime ** m)
    
    return gcf

def findLCM(nums):
    gcf = findGCF(nums)
    lcm = gcf
    for num in nums:
        lcm *= int(num/gcf)
    return lcm

def main():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")
    
    numA = int(str_numA)
    numB = int(str_numB)
        
    nums = [numA,numB]    
    gcf = findGCF(nums)
    lcm = findLCM(nums)
    
    print("Greatest Common Factor: " + str(gcf))
    print("Lowest Common Multiple: " + str(lcm))
```

如此一來程式碼就看起來乾淨很多，function和function之間的耦合性被降低了，而function本身的內聚性提高了，程式碼達到了低耦合、高內聚，但是似乎還可以更好。


### 形塑出物件導向

剛剛我們已經完成了一個看起來很乾淨的程式碼了，但是其實還可以更好，在這裡我們就必須形塑出物件導向，才有辦法再前進一步。

剛剛的程式碼當中的`checkPositiveInteger(num)`, `primeFactorize(num)`, `findGCF(nums)`, `findLCM(nums)`函數其實都是實現同一個目標—因式計算，但卻是被寫成一個一個獨立的函數，這裡的內聚性還可以再更好。

而且`checkPositiveInteger(num)`, `primeFactorize(num)`並不是用來實現主要的目的，而只是實現目的過程中，為了避免重複而產生的，這樣寫很容易讓人不清楚什麼是重要的函數，而什麼只是中繼的函數，這裡的「可讀性」應該還可以再提升。

輸入的數字`nums`對於`findGCF`和`findLCM`，應該是一模一樣的，有沒有一個方法可以讓`nums`避免重複呢？以增強「不要重複撰寫」的原則。

要擁有以上的功能，我們需要一個「物件」，這個「物件」能夠保有屬於它的變數，才可以儲存`nums`等參數，變數可以是對外公布的，也可以是私有的。另外,這個「對象」擁有屬於它的函數方法，而方法一樣可以是對外公布的，也可以是私有的，所以我們可以公布`findGCF(nums)`, `findLCM(nums)`，而私有化
`checkPositiveInteger(num)`, `primeFactorize(num)`。我們使用「藍圖」去建構「物件」的模版，再由「藍圖」配合不同的輸入參數去生成一個一個獨立的「物件」，以因應不同的狀況。

這就是物件導向！

接下來，我將上面程式碼引入物件導向改寫如下。（看不懂～沒關係！未來會詳述）

```python
import sys
class Calculation:
    def __init__(self,nums):
        self.__nums = nums
        for num in self.__nums:
            self.__checkPositiveInteger(num)

    def __checkPositiveInteger(self,num):
        if (not isinstance(num,int)) or (num<=0):
    	    raise ValueError("invalid positive integer: "+str(num))
    		
    def __primeFactorize(self,num):
        prime_factorize = dict()
        i = 2
        while(num > 1):
            if num % i == 0:
                prime_factorize[i] = prime_factorize.get(i,0) + 1
                num /= i
            else:
                i += 1
        return prime_factorize
    
    def findGCF(self):
        prime_factorize = list()
        for num in self.__nums:
            prime_factorize.append(self.__primeFactorize(num))
			
        common_prime = set(prime_factorize[0].keys())
        for pf in prime_factorize[1:]:
            common_prime &= set(pf.keys())
        
        gcf = 1
        for prime in common_prime:
            m = sys.maxsize
            for pf in prime_factorize:
                m = min(m,pf[prime])
            gcf = gcf * (prime ** m)
        
        return gcf
    
    def findLCM(self):
        gcf = self.findGCF()
        lcm = gcf
        for num in self.__nums:
            lcm *= int(num/gcf)
        return lcm

def main():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")
    
    numA = int(str_numA)
    numB = int(str_numB)
        
    nums = [numA,numB]
    calc = Calculation(nums)
    gcf = calc.findGCF()
    lcm = calc.findLCM()
    
    print("Greatest Common Factor: " + str(gcf))
    print("Lowest Common Multiple: " + str(lcm))
```

### 總結：程式碼鑑賞能力

本章YC帶大家建立一種品味，像是藝術評論家一樣，我們學會了如何鑑賞好的程式碼，我們提到了好的程式碼須要符合「正常執行」、「穩健」、「不重複撰寫」、「可讀性」、「可擴展」的特性，並且提到我們要追求低耦合、高內聚，但是「不重複撰寫」的這個原則會和低耦合相互違和，所以工程師要小心拿捏！有了鑑賞能力，我們開始精練我們的程式，而自然而然就可以引出物件導向的概念。當然，物件導向不只如此啦！我們下章就會看到物件導向還有什麼花拳繡腿。
