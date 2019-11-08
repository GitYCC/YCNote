Title: 物件導向武功秘笈（2）：招式篇 — Python與Java的物件導向編程介紹
Date: 2018-04-10 12:00
Category: Coding
Tags: 軟體設計
Slug: introduction-object-oriented-programming_2
Author: YC Chen
Illustration: coding_front_board.jpg
Alias: /YCNote/post/48.html
related_posts: introduction-object-oriented-programming_1,introduction-object-oriented-programming_3
Summary: 物件導向編程 / 類別(Class)與物件(Object) / 方法多載（Method Overloading） / 物件導向三大特性—封裝(Encapsulation) / 物件導向三大特性—繼承(Inheritance) / 抽象化：抽象類別(Abstract Class)、抽象方法(Abstract Method)和接口(Interface) / 物件導向三大特性—多型(Polymorphism) / 


### 物件導向編程

[在上一章當中](http://www.ycc.idv.tw/introduction-object-oriented-programming_1.html)，我們藉由好的程式碼的特性：「正常執行」、「穩健」、「不重複撰寫」、「可讀性」、「可擴展」，自然而然引出物件導向的概念。在這一章當中YC會接續介紹完整的物件導向要如何實現，包括物件導向三大特性：封裝、繼承和多型。

在本章我會採用兩種語言交叉作說明，一種是靜態型別的語言Java，另一種是動態型別的語言Python，這兩種語言都是可以實現物件導向的語言，而所謂型別的動態與靜態可以用一個簡單的方法來區分：型別檢查(Type Checking)發生在什麼時候？像Java這類的靜態型別語言，它的型別檢查是在編譯時期(Compile Time)完成的，而像是Python這類的動態型別語言，它的型別檢查則是在執行時期(Runtime)才去做，所以Python可以不事先宣告變數型別，這點使得Python在開發上方便許多。

雖然Python和Java都是支援物件導向的語言，但在使用上有很大的差異，首先，因為Python的動態型別，所以有些物件導向的性質對它來說就不是那麼重要，另外，因為Python追求簡潔，簡化了相當多的東西，所以很多的使用方法不同於傳統的物件導向，需要認識到這些差異才可以讓你使用Python的物件導向不會顯得很彆扭。Java是一套對物件導向支援非常完整的語言，而Python是一套易於快速開發的語言，使用兩種語言說明物件導向是為了讓讀者更能了解物件導向的本質，而非語言本身。

本篇採用『[大話設計模式](https://www.tenlong.com.tw/products/9789866761799)』書中的物件導向篇範例。

### 類別(Class)與物件(Object)

首先來看物件導向的基本組成，類別(Class)與物件(Object)。
* 類別：建立物件的藍圖，描述所建立的物件共同的屬性和方法。
* 物件：一個自我包含的實體，物件包括屬性（Properties）和方法（Methods），屬性就是需要記憶的資訊，方法就是物件能夠提供的服務。

舉個例子，我想要創造一隻有名字的貓，她有喵喵叫的能力，在Java中可以寫成

```java
/* Java */

class Cat {  //{1}
	private String name; //{2}
    
  	public Cat(String name) { //{3}
        this.name = name; //{4}
  	}
    
	public String shout() { //{5}
        return "My name is "+name+". meow~"; //{6}
    }
}

public class Test {
    public static void main(String[] args) { //{7}
        Cat cat = new Cat("May"); //{8}
		System.out.println(cat.shout()); //{9}
    }
}
// output:
// My name is May. meow~
```

{1} 建構一個`Cat`的類別，類別不是物件，類別只是物件的藍圖。

{2} 建立一個私有變數`name`，用來代表貓的名字，我們使用`private`的修飾詞讓它是私有的，也就是說外部環境沒辦法去讀取到這個變數，只有物件內部才可以讀取的到

{3} 提供建造方法(constructor)來初始化這一個物件，初始化需要`name`的參數。

{4} 在初始化的過程中，我們會將從外部讀取的`name`存入私有變數`this.name`裡，在Java裡頭，如果外部變數名稱與本地變數名稱相同，需要使用`this`來特別區分。

{5} 創造一個公開的類別方法`shout()`。

{6} 使用私有變數`name`讓貓可以自我介紹，再發出喵喵叫的聲音。

{7} Java只要遇到`main`就會去執行，方法`main`具有靜態方法的修飾詞`static`，也就是說`Test`不需要被實體化也能執行`main`這個方法。

{8} 使用`new`來創造一個物件，在創造的過程會執行初始化，所以必須放入初始化需要的參數`name`，所以上面的新的物件有了`"May"`的名字。

{9} 接下來使用`cat.shout()`去執行喵喵叫的動作，這個方法會回傳字串，再利用`System.out.println`的方法將字串顯示出來。注意！在物件導向的習慣中，會用`.`來表示在那物件中的方法或屬性，所以`cat.shout()`就是執行在物件`cat`中的方法`shout()`。

再來看Python怎麼表示，

```python
### Python3.4

class Cat: #{1}
	def __init__(self,name): #{2}
		self.__name = name #{3}
	
	def shout(self): #{4}
		return "My name is "+self.__name+". meow~" #{5}

def main():
    cat = Cat("May") #{6}
    print(cat.shout()) #{7}

if __name__=="__main__": #{8}
    main()
	
# output:
# My name is May. meow~
```

{1} 建構`Cat`的類別，這是Python3的表示方法，如果是使用Python2.7的話，要寫成`class Cat(object):`才可以。

{2} Python的初始化方法，Python在初始化之前會先自行執行`__new__`的方法，這個過程會產生一個新的物件，也就是實體化，而這個新的物件會以第一個參數的方法被帶入`__init__`的方法裡進行初始化，我們通常會命名這個變數為`self`，這裡的`self`已經是個物件而不是類別，那初始化的過程需要引入外部資訊`name`的參數來進行命名，所以第二個參數就要設`name`，記住喔！第一個參數是Python自動產生的，不是由外部帶入的，所以外部只要給`name`一個參數就足夠了。

{3} 創造一個私有本地變數`__name`來將`name`存入，在Python當中以雙底線`__`開頭的變數會被視為是「私有的」，效果和Java的`private`接近，不過Python並沒有這麼嚴格禁止外部去讀取私有變數，所以需要配合工程師的自我規範。

{4} 類別方法`shout()`，只要你不是靜態的類別方法，Python都會自動幫你帶入物件資訊當作第一個參數，通常命名為`self`，那為什麼靜態方法沒有自動帶入，因為靜態方法不用實體化，所以根本不擁有物件的資訊。

{5} 使用到本地的`self.__name`變數

{6} 創造一個物件，在創造的過程會執行初始化，所以必須放入初始化需要的參數`name`，所以上面的新的物件有了`"May"`的名字。

{7} 接下來使用`cat.shout()`去執行喵喵叫的動作，這個方法會回傳字串，再利用`print`的方法將字串顯示出來。注意！在物件導向的習慣中，會用`.`來表示在那物件中的方法或屬性，所以`cat.shout()`就是執行在物件`cat`中的方法`shout()`。

{8} 在Python程式執行時，它的`__name__`會是`"__main__"`，也就是說會去執行這個`if`判斷式下面的程式。

### 方法多載（Method Overloading）

物件導向允許「使用不同的參數形式去實現同一個方法」，這就稱之為方法多載，這個方法涵蓋一般方法和構造初始化方法。

來延伸剛剛的貓的例子，假設今天我們允許用戶不去設定貓咪的名字，而程式會預先給貓咪No-Name的預設值，所以我們需要另外一個初始化方法是不用貓咪名字的參數形式。

Java的實現程式碼如下所示，如此一來只要碰到沒有參數的形式，程式會給予`"No-Name"`的名字去當作貓咪的名字，並進行初始化。

```java
/* Java */

class Cat {  
	private String name; 
    
  	public Cat(String name) { 
        this.name = name; 
  	}
    // method overloading
    public Cat() {
        this("No-Name"); // given "No-Name" as its name
    }
	
	public String shout() { 
        return "My name is "+name+". meow~"; 
    }
}

public class Test {
    public static void main(String[] args) { 
        Cat cat = new Cat(); // no-argumant format
		System.out.println(cat.shout());
    }
}
// output:
// My name is No-Name. meow~
```

但在Python當中，不允許這種「相同方法名稱，卻又不同參數形式」，Python採用其他的方式來產生同樣的方法多載效果，如以下所示，我們可以看到Python使用default方法來實現多載，只要我們不給予`name`，它的default就是`"No-Name"`。

```python
### Python3.4

class Cat: 
	def __init__(self,name="No-Name"): # name's default is "No-Name"
		self.__name = name 
	
	def shout(self): 
		return "My name is "+self.__name+". meow~" 

def main():
    cat = Cat() # no-argument format
    print(cat.shout()) 

if __name__=="__main__": 
    main()
	
# output:
# My name is No-Name. meow~
```

### 物件導向三大特性—封裝(Encapsulation)

還記得「低耦合，高內聚」的原則嗎？為了符合這原則，每個物件都要盡可能的去包含需要用到的屬性和方法，並且使得外部不能以不合理的方法去影響物件，這就稱之為「封裝」。

我們來看看上次的成果，我們就用這個例子來說明「封裝」。

```python
### Python3.4

import sys

class Calculation:
    def __init__(self,nums):
        self.__nums = nums #{1}
        for num in self.__nums:
            self.__checkPositiveInteger(num)

    def __checkPositiveInteger(self,num): #{2}
        if (not isinstance(num,int)) or (num<=0):
    	    raise ValueError("invalid positive integer: "+str(num))
    		
    def __primeFactorize(self,num): #{3}
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
```

{1} 使用私有變數，讓外部不能任意的改變`self.__name`變數，在這個例子當中，如果`self.__name`被任意改變，它將會逃過`__checkPositiveInteger`的檢查。
{2}&{3} 不需要由外部讀取的方法，就盡量讓它是私有的。

再回到貓咪的這個例子，如果我們想要可以調控「叫聲次數」的話，可以這樣實現。

```java
/* Java */

class Cat {
	private String name = "";
	
	public Cat(String name) {
		this.name = name;
	}
	public Cat() {
		this("No-Name");
	}
	
	private int shout_num = 3; //{1}
	public int getShoutNum() { return shout_num; } //{2}
	public void setShoutNum(int num) { //{3}
	    if (num < 0) throw new java.lang.IllegalArgumentException();
	    shout_num = num; 
	}

	public String shout() {
		String result = "";
		for (int i=0; i<shout_num; i++){
			result += "meow~ ";
		}
		return "My name is "+name+". "+result;
	}
}

public class Test {
    public static void main(String[] args) {
		Cat cat = new Cat("May");
		cat.setShoutNum(5); //{4}
		System.out.println(cat.shout());
    }
}
// output:
// My name is May. meow~ meow~ meow~ meow~ meow~
```

{1} 設置私有變數`shout_num`來決定叫聲次數。

{2} 為了做到封裝，外部不能直接去讀取`shout_num`，而是經由`getShoutNum`的外部方法來得到叫聲次數，這個`getXXX`的形式在物件導向裡頭被稱為Getter。

{3} 為了做到封裝，外部不能直接去改變`shout_num`，而是經由`setShoutNum`的外部方法來以合理的方法改變叫聲次數，在這個方法中，我們會先檢查再設定，如果是直接的改變`shout_num`將會少了這一份檢查，這個`setXXX`的形式在物件導向裡頭被稱為Setter。

{4} 使用Setter方法由外部來改變叫聲次數。

在Python中，Getter和Setter被簡化了。

```python
### Python3.4

class Cat:
    def __init__(self,name="No-Name"):
        self.__name = name
        self.__shout_num = 3
    
    @property  #{1}
    def shout_num(self):
        return self.__shout_num
        
    @shout_num.setter  #{2}
    def shout_num(self,num):
	    if num < 0: raise ValueError()
        self.__shout_num = num
        
    def shout(self):
        result = ""
        for _ in range(self.__shout_num):
            result += "meow~ "
        return "My name is "+self.__name+". "+result

def main():
    cat = Cat("May")
    cat.shout_num = 5  #{3}
    print(cat.shout())

if __name__ == "__main__":
    main()
	
# output:
# My name is May. meow~ meow~ meow~ meow~ meow~
```

{1} Python使用Decorator`@property`來創造Getter，一旦加上了`@property`，當下的函數方法就會變成一種性質。

{2} 再使用`shout_num.setter`來替`shout_num`這個特性加上Setter。

{3} 然後我們就可以以像是修改一般變數的方式來修改`shout_num`，但實際上`shout_num`是有被封裝的，如此一來就可以更為簡潔，不用去寫`getXX`和`setXXX`等囉唆的寫法。

### 物件導向三大特性—繼承(Inheritance)

還記得「Don't Repeat Yourself」原則嗎？物件導向同樣提供了這個選項，「繼承」可以讓子類擁有父類的屬性和方法，避免不必要的重寫，但同時也會增加父類和子類之間的耦合，所以使用時要去評估它影響了多少耦合性。

子類可以先繼承父類的屬性和方法，再去新增屬於子類自己的屬性和方法，甚至還可以去覆寫父類的方法，這稱之為方法覆寫(Method Overriding)，有了這些方法，子類可以在不重複撰寫父類方法的情況下，去增加自己的特色和自己的功能。

依循著剛剛的例子，如果我們今天想要增加狗的類別，但是又不想重複撰寫相同的部分，所以我們可以選擇創造動物的類別，再讓貓和狗繼承自動物。

```java
/* Java */

class Animal {
    protected String name = ""; //{1}
    
    public Animal(String name) {
        this.name = name;
    }
    public Animal() {
        this("No-Name");
    }
    
    protected int shout_num = 3;
    public int getShoutNum() {
        return shout_num;
    }
    public void setShoutNum(int num) {
	    if (num < 0) throw new java.lang.IllegalArgumentException();
        shout_num = num;
    }
}

class Cat extends Animal{
    public Cat(String name) {
        super(name); //{2}
    }
    public Cat() {
        super();
    }

    public String shout() {
        String result = "";
        for (int i=0; i<shout_num; i++){
            result += "meow~ ";
        }
        return "My name is "+name+". "+result;
    }
}
class Dog extends Animal{
    public String shout() {
        String result = "";
        for (int i=0; i<shout_num; i++){
            result += "woof~ ";
        }
        return "My name is "+name+". "+result;
    }
}
```

{1} `protected`的效果和`private`一樣，讓外部無法讀取到內部的私有化，但是`private`無法被「繼承」，而`protected`可以被繼承，所以如果希望可以被繼承的私有變數或方法，就使用`protected`。

{2} `super`指的是父類，這裡我們使用父類來做初始化，事實上這邊可以不用再初始化一次，子類本身就會繼承父類的初始化方法，所以可以像`Dog`一樣省略不寫。

```python
### Python3.4

class Animal:
    def __init__(self,name="No-Name"):
        self._name = name
        self._shout_num = 3 #{1}
        
    @property
    def shout_num(self):
        return self._shout_num
    @shout_num.setter
    def shout_num(self,num):
	    if num < 0: raise ValueError()
        self._shout_num = num
        
class Cat(Animal):
    def __init__(self,name="No_Name"):
        super().__init__(name)  #{2}
        
    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += "meow~ "
        return "My name is "+self._name+". "+result
class Dog(Animal):
    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += "woof~ "
        return "My name is "+self._name+". "+result
```

{1} Python的`protected`使用單底線`_`開頭表示。

{2} `super`指的是父類，這裡我們使用父類來做初始化，事實上這邊可以不用再初始化一次，子類本身就會繼承父類的初始化方法，所以可以像`Dog`一樣省略不寫。


### 抽象化：抽象類別(Abstract Class)、抽象方法(Abstract Method)和接口(Interface)

事實上，剛剛使用`Animal`的方法並不是很正確，我們將`Animal`當作一個類別處理，所以`Animal`其實是可以被實例化的，但是`Animal`根本沒有什麼有用的方法，它必須被繼承後再添加方法才有用處，所以我們其實可以把`Animal`抽象化，將`Animal`視為抽象類別，其中擁有一些方法需要在子類實現的，稱為抽象方法，我們直接看怎麼做。

```java
/* Java */

abstract class Animal { //{1}
    protected String name = "";
    
    public Animal(String name) {
        this.name = name;
    }
    public Animal() {
        this("No-Name");
    }
    
    protected int shout_num = 3;
    public int getShoutNum() {
        return shout_num;
    }
    public void setShoutNum(int num) {
	    if (num < 0) throw new java.lang.IllegalArgumentException();
        shout_num = num;
    }
      
    public String shout() { //{2}
        String result = "";
        for (int i=0; i<shout_num; i++){
            result += getShoutSound()+" "; //{3}
        }
        return "My name is "+name+". "+result;
    }
    abstract protected String getShoutSound(); //{4}
}

class Cat extends Animal{
    protected String getShoutSound() { //{5}
        return "meow~"; 
    }
}
class Dog extends Animal{
    protected String getShoutSound() {
        return "woof~";
    }
}
```

{1} 使用`abstract class`修飾詞來創建抽象類別，只有在抽象類別中才可以擁有抽象方法，抽象類別不能直接被實例化。

{2} 抽象類別也可以有一般的具體方法。

{3} 這裡使用的`getShoutSound()`方法要等在子類才會被實現。

{4} 使用`abstract`設置抽象方法，繼承自抽象類別的子類必須要完全實現所有的抽象方法。

{5} 實現抽象方法。

在Python中沒有原生的抽象類別和方法，必須`import abc`。

```python
### Python3.4

import abc
class Animal(abc.ABC): #{1}
    def __init__(self,name="No-Name"):
        self._name = name
        self._shout_num = 3
        
    @property
    def shout_num(self):
        return self._shout_num
    @shout_num.setter
    def shout_num(self,num):
        self._shout_num = num
    
    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += self._getShoutSound()+" "
        return "My name is "+self._name+". "+result  
    @abc.abstractmethod  #{2}
    def _getShoutSound(self):
        pass

class Cat(Animal):
    def _getShoutSound(self): #{3}
        return "meow~"

class Dog(Animal):
    def _getShoutSound(self):
        return "woof~"
```

{1} 繼承`abc.ABC`來建立抽象類別。

{2} 使用`@abc.abstractmethod`來建立抽象方法。

{3} 實現抽象方法。

還有一種類型抽象化的更為徹底，稱之為「接口」，「接口」上的所有方法都是抽象未實現的，「接口」不能擁有任何具體的方法。雖然「接口」很像是完全抽象化的「抽象類別」，也確實可以利用「抽象類別」來創造「接口」，但是兩者的意義是不同的，「抽象類別」是從子類中發現共通的東西，而泛化出現的，但是「接口」可以根本不預先知道子類是什麼，而僅僅事先定義行為本身，換句話說，「抽象類別」是類別的抽象化，而「接口」則是行為的抽象化。

例如，我想要讓某些動物擁有「飛」的能力，這是一個行為，而不會事先知道它會套用到哪一個類別上面。

在Java之中只允許單一繼承，但是卻可以有多個「接口」；而Python沒有現成的「接口」可以使用，我們必須使用「抽象方法」來創造「接口」，所以開發者要謹記「接口」的限制：不能有任何的具體方法，因為Python允許多重繼承，所以就可以直接將模擬「接口」的抽象類別直接疊加上去。

```java
/* Java */

interface IFly { //{1}
    public String flyTo(String place); //{2}
}
class FlyingCat extends Cat implements IFly { //{3}
    public String flyTo(String place) { //{4}
        return shout()+" I'm going to fly to "+place+".";
    }
}

public class Test {
    public static void main(String[] args) {
        FlyingCat cat = new FlyingCat("May");
        System.out.println(cat.flyTo("Taiwan"));
    }
}
// output: 
// My name is May. meow~ meow~ meow~ I'm going to fly to Taiwan.
```

{1} 使用`interface`創建「接口」，我們習慣會使用開頭大寫I來表示Interface(接口)。

{2} 「接口」定義未實現的抽象方法`flyTo`。

{3} `FlyingCat`繼承自`Cat`並且裝上`IFly`的「接口」。

{4} 必須實現「接口」上所有的抽象方法。

```python
### Python3.4

import abc
class IFly(abc.ABC): #{1}
    @abc.abstractmethod #{2}
    def flyTo(self,place):
        pass
		
class FlyingCat(Cat,IFly): #{3}
    def flyTo(self,place):
        return self.shout()+" I'm going to fly to "+place+".";

def main():
    cat = FlyingCat("May")
    print(cat.fly("Taiwan"))
if __name__ == "__main__":
    main()
	
# output: 
# My name is May. meow~ meow~ meow~ I'm going to fly to Taiwan.
```

{1} 使用抽象類別來創造「接口」。

{2} 要注意！「接口」裡頭不能有具體方法。

{3} 直接使用多重繼承，將`IFly`安裝上去。


### 物件導向三大特性—多型(Polymorphism)

最後，來講講物件導向的最後一個特性，那就是「多型」。「多型」的涵義是指「子類可以以父類的身分出現」，而因為是以父類的角色出現，所以只能執行父類擁有的方法，也就是只能執行這些子類共同泛化分享的方法，當然不同的子類實現後的效果會不一樣，不然使用「多型」的意義就不大了，至於子類自己的特殊方法則不可以使用「多型」去執行。

直接來看範例，假設今天我要邀請三隻貓貓狗狗來參加叫聲比賽，分別請他們叫個幾聲來聽聽，此時就需要使用到「多型」的方法。

```java
/* Java */

abstract class Animal { 
    protected String name = "";
    
    public Animal(String name) {
        this.name = name;
    }
    public Animal() {
        this("No-Name");
    }
    
    protected int shout_num = 3;
    public int getShoutNum() {
        return shout_num;
    }
    public void setShoutNum(int num) {
	    if (num < 0) throw new java.lang.IllegalArgumentException();
        shout_num = num;
    }
      
    public String shout() { 
        String result = "";
        for (int i=0; i<shout_num; i++){
            result += getShoutSound()+" "; 
        }
        return "My name is "+name+". "+result;
    }
    abstract protected String getShoutSound(); 
}

class Cat extends Animal{
    protected String getShoutSound() { 
        return "meow~"; 
    }
}
class Dog extends Animal{
    protected String getShoutSound() {
        return "woof~";
    }
}

public class ShoutGame {
    public static void main(String[] args) {
        Animal[] arrayAnimal = new Animal[3]; //{1}
        // polymorphism
        arrayAnimal[0] = new Cat("May"); //{2}
        arrayAnimal[1] = new Dog("Linda");
        arrayAnimal[2] = new Cat("Joy");
        for (Animal animal: arrayAnimal) {
            System.out.println(animal.shout()); //{3}
        }
    }
}
// output: 
// My name is May. meow~ meow~ meow~
// My name is Linda. woof~ woof~ woof~
// My name is Joy. meow~ meow~ meow~
```

{1} 創建`Animal`的Array，Animal是抽象類別不能實體化，這裡預定要放的是它的繼承實現類別。

{2} 將`Cat`和`Dog`任意放到`Animal`的Array是可以的，此時就套用「多型」，不管是`Cat`和`Dog`都是以`Animal`的形式出現，只能執行`Animal`有的方法。

{3} `shout()`是父類`Animal`有的方法，可以被執行。

而在Python當中，「多型」就沒這麼重要了，因為Python具有「鴨子型別」（Duck Typing），什麼是「鴨子型別」呢？有一句話道出它的意義：「當看到一隻鳥走起來像鴨子、游泳起來像鴨子、叫起來也像鴨子，那麼這隻鳥就可以被稱為鴨子」，因為Python是動態型別的語言，變數型態不需要事先宣告，所以一個變數具有彈性可以放入任意型別，直到出現不合適的使用方法，才會報錯，所以在Python中變數可以任意放入不同的類別的物件，只要確保這些類別都具有這些變數所需要用到的方法，就可以了，這不正是接近「多型」的概念。

```python
### Python3.4

import abc
class Animal(abc.ABC): 
    def __init__(self,name="No-Name"):
        self._name = name
        self._shout_num = 3
        
    @property
    def shout_num(self):
        return self._shout_num
    @shout_num.setter
    def shout_num(self,num):
        self._shout_num = num
    
    def shout(self):
        result = ""
        for _ in range(self._shout_num):
            result += self._getShoutSound()+" "
        return "My name is "+self._name+". "+result  
    @abc.abstractmethod
    def _getShoutSound(self):
        pass

class Cat(Animal):
    def _getShoutSound(self):
        return "meow~"

class Dog(Animal):
    def _getShoutSound(self):
        return "woof~"
def main():
    # Shout Game
	arrayAnimal = [] #{1}
    arrayAnimal.append(Cat("May")) 
    arrayAnimal.append(Dog("Linda"))
    arrayAnimal.append(Cat("Joy"))
    for animal in arrayAnimal:
        if not isinstance(animal,Animal): raise TypeError #not necessary #{2}
        print(animal.shout())

if __name__ == "__main__":
    main()
	
# output: 
# My name is May. meow~ meow~ meow~
# My name is Linda. woof~ woof~ woof~
# My name is Joy. meow~ meow~ meow~
```

{1} 要存入多型的List不需要特別處理。

{2} 可以檢查是不是繼承自`Animal`，以確保多型的嚴格定義，但這個過程是非必要的。

### 總結：物件導向使用方法

好！我們花了好大的力氣，終於了解如何在Java和Python中使用物件導向。從一開始的「類別」和「物件」講起，再來談到物件導向的三大特性：「封裝」、「繼承」和「多型」，還談到方法可以「多載」也可以「覆寫」，以及一些抽象化的東西，包括「抽象類別」、「抽象方法」和「接口」。

但是等等！你知道該怎麼運用這些技巧嗎？沒錯，僅僅是了解這些招式不足以讓你寫出卓越的程式碼，你還需要了解如何使用，就像是外功招式還得配合內功才可以是一套完整的功夫，否則只是半吊子而已，我們將在下一章節中來帶大家了解如何去使用這些招式。
