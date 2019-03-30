Title: 物件導向武功秘笈（3）：內功篇 — 物件導向指導原則SOLID
Date: 2018-04-14 12:00
Category: Coding
Tags: 軟體設計
Slug: introduction-object-oriented-programming_3
Author: YC Chen
Illustration: coding_front_board.jpg
Alias: /YCNote/post/49.html
related_posts: introduction-object-oriented-programming_1,introduction-object-oriented-programming_2

### 物件導向怎麼用才能成就好的程式碼？

一個好的工具，也要配合對於工具的理解，才能發揮效用。[在上一回中](http://www.ycc.idv.tw/introduction-object-oriented-programming_2.html)，我們完整介紹了Java和Python的物件導向實現方式，我們講到了「封裝」、「繼承」、「多型」等等物件導向的特色，也講了「抽象類別」、「接口」等抽象化的方法，不過我並沒有告訴大家該怎麼用這些工具？使用這些工具是不是有什麼樣的法則？

在接下來的這一篇，我將會介紹物件導向的使用方式，我會提到物件導向著名的六大法則：

1. 單一職責原理
2. 開閉原理
3. 里氏替換原則
4. 迪米特法則
5. 依賴倒置原則
6. 接口分隔原則

在這之前我們先來介紹描述類別關係的UML類別圖。


### UML類別圖

開始介紹各種原則之前，先來介紹UML類別圖，UML全名稱為Unified Modeling Language，是一種使用圖形來描繪軟體工程架構的方法，這邊準備介紹的是它的類別圖，這個工具有助於我們快速的了解物件與物件之間的關係。

* 類別(Class): -代表`private`，+代表`public`，#代表`protected`

![Class](https://www.ycc.idv.tw/media/SOLID_Introduction/Class.png)



* 抽象類別(Abstract Class)

![AbstractClass](https://www.ycc.idv.tw/media/SOLID_Introduction/AbstractClass.png)

* 接口(Interface)

![Interface](https://www.ycc.idv.tw/media/SOLID_Introduction/Interface.png)

* 繼承關係(Inheritance)和抽象類、接口實現

![Inheritance](https://www.ycc.idv.tw/media/SOLID_Introduction/Inheritance.png)

* 關聯關係(Association)：A類中使用B類當作「成員變數」，但是A和B並沒有「擁有」的關係，只能說是「有個」的關係，就稱為：A關聯到B，英文為"has-a"的關係。

![Associatione](https://www.ycc.idv.tw/media/SOLID_Introduction/Association.png)

* 聚合關係(Aggregation)：A類中使用B類當作「成員變數」，而且A和B有一個弱的「擁有」關係，A包含B，但B不是A的一部分，拔掉B，A依然能存在，就稱為：A聚合到B，英文為"owns-a"關係。

![Aggregation](https://www.ycc.idv.tw/media/SOLID_Introduction/Aggregation.png)

* 合成（組合）關係(Composition)：A類中使用B類當作「成員變數」，而且A和B有一個強的「擁有」關係，B是A的組成的一部分，拔掉B，A就不完整，就稱為：A合成到B，英文為"is-part-of"關係。

![Composition](https://www.ycc.idv.tw/media/SOLID_Introduction/Composition.png)

* 依賴關係(Dependency)：A類中使用到B類，但僅僅是弱連結，譬如：B類作為A類方法的參數、B類作為A類的局域變數、A類調用B類的靜態方法、B類作為A類方法的回傳值，就稱為：A依賴B，英文為"uses-a"的關係。

![Dependency](https://www.ycc.idv.tw/media/SOLID_Introduction/Dependency.png)

### 單一職責原則(Single Responsibility Principle, SRP)



* 定義：There should never be more than one reason for a class to change.（一個類別中不要有多於一個以上的變化理由）



* 簡單的說，就是一個類別中不要做超過一件事，要去切分直到不能再分割為止，如此一來可以提高內聚性。



* 乍看之下，這樣的原則很容易實現，但是魔鬼藏在細節裡，我們常常會沒注意到其實還可以繼續的切分。舉個例子，假設我想設計一個電話的接口，我可能是這樣設計的

![phone_1](https://www.ycc.idv.tw/media/SOLID_Introduction/phone_1.png)

乍看之下沒有問題，一個電話擁有撥號、掛號、數據傳送和接收，但是等等！連接的過程和數據的傳輸其實是兩個職責啊！它們之間沒有強烈的關聯性，完全是可以分開處理的，因此這個配置不符合「單一職責原則」，可以繼續切分下去，修改如下。

![phone_2](https://www.ycc.idv.tw/media/SOLID_Introduction/phone_2.png)



* 「單一職責原則」原文指的是類別的單一職責，但是務實上，類別如果切分到如此程度，程式碼會變得細碎不堪，這違反了程式碼的「可讀性」，所以我們一般只要求「接口必須保持單一原則」，而類別去套用接口，類別就盡量達成少的職責就好。

### 開閉原則(Open-Closed Principle, OCP)

* 定義：Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.（軟體中的實體，例如：類、模組、函數等等，都必須對延伸開放，但對修改封閉）



* 對延伸開放：實體在因應新的改變時，必須是可以靈活擴充的。



* 對修改封閉：實體一旦完成，就盡量不要再去修改它了。



* 綜合以上兩點，我們可以總結出：實體本身的內聚性要高，可以讓我們未來不需要再做修改，單一職責可以做到增強內聚性；實體間的耦合性要低，所以實體像是積木一樣可以因應各種需求去任意組合、擴充。所以「開閉原則」只是進一步的把「低耦合高內聚」再說的更清楚一點，實現「開閉原則」將有利於單元測試、提高維護和擴充能力。

### 里氏替換原則(Liskov Subsititution Principle, LSP)

* 定義：What is wanted here is something like the following substitution property: If for each object o1 of type S there is an object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2 then S is a subtype of T.（簡言之：子類對象能夠替換其父類對象，使用父類方法而不會有問題）



* 「里氏替換原則」用於規範繼承，子類繼承自父類的方法是保有彈性可以覆寫(Overriding)和多載(Overloading)的，但是應該怎麼做，程式碼才不會髒掉？「里氏替換原則」告訴我們一個簡單的法則，就是先寫一段父類的執行代碼，然後把父類替換成子類，然後再跑跑看能不能正常執行，如果正常執行代表這個繼承關係是健康的。



* 為什麼要這樣檢查？之前我們提過繼承主要是為了要避免Repeat Yourself而生，我們找出各種類別共享的屬性和方法，把它獨立出來，然後大家再一起繼承自它，所以我們要盡可能的避免父類出現不是共享的性質。也就是說在理想情況下「父類必須等於子類們的交集」，所以「父類必定是任一子類的子集合」，因此「使用子類來執行父類是不應該有問題的」，這就是「里氏替換原則」。



* 為了遵循「里氏替換原則」，則子類必須完全實現父類的方法。如果子類不能完整地實現父類的方法，或者父類的某些方法在子類中已經發生了「畸變」，則建議斷開父子繼承關係，採用依賴、聚集、組合等關係替代。



* 有了「里氏替換原則」，我們終於可以談談一個上一章沒提到的重要問題：什麼情況可以做繼承？有一些書籍會告訴你，繼承為"is-a"的關係，例如：瑪爾濟斯(B) is-a 狗(A)，所以瑪爾濟斯(B)可以繼承狗(A)，乍看之下沒問題，但這樣的說法存在缺陷，舉個例子，假設今天我先有了類別`Retangle`，也就是長方形，然後我想要弄一個新的類別`Square`，也就是正方形，我可以讓`Square`繼承自`Retangle`嗎？我們用"is-a"來檢視：正方形是一個長方形？答案是Yes，但是「里氏替換原則」持相反意見，來看一下，

![square_1](https://www.ycc.idv.tw/media/SOLID_Introduction/square_1.png)

依照「里氏替換原則」，`Square`不能繼承自`Retangle`，因為`Square`只需要`width`的成員變數，而`Retangle`則需要`width`和`height`兩個成員變數，當我們將子類`Square`放到父類`Retangle`的方法中，因為缺少`height`變數，必然會出錯，所以違反「里氏替換原則」，因此這兩類不適合作為「繼承」關係。我們可以這樣改善，讓`Square`應用`Retangle`來幫忙計算，使用「關聯」關係取代「繼承」關係。

![square_2](https://www.ycc.idv.tw/media/SOLID_Introduction/square_2.png)

* 下面這一張集合圖是我自創的，圖中清楚的指出「繼承」中的父類和子類應該是什麼樣的關係。

![Inheritance Principle.jpeg](https://www.ycc.idv.tw/media/SOLID_Introduction/inheritance_principle.jpeg)


### 迪米特法則(Law of Demeter, LoD)

* 又稱為「最少知識原則」

* 定義：
	1. Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
	2. Each unit should only talk to its friends; don't talk to strangers.
	3. Only talk to your immediate friends.


* 「朋友」的定義：對於類別C的所有方法M而言，在M的方法中僅能訪問以下物件的方法
	* `self`，類別C自身
	* M的輸入參數
	* C的成員變數
	* M的輸出物件
	* 全域變數的物件

* 白話總結：
	1. 僅能訪問那些類別出現在自身、成員變數、方法的輸入和輸出參數中的方法。
	2. 減少類別的對外方法，將沒必要對外公布的方法隱藏起來。 

**（詳解）僅能訪問那些類別出現在自身、成員變數、方法的輸入和輸出參數中的方法。**

-- 例子: 假設今天一名老師給了學生名條想叫班長幫忙點名。

錯誤示範：

```python
### Python3.4

class Student: #friends: None
    def __init__(self,name):
	    self.name = name

class Leader: #friends: Student
    def countStudents(self,student_list):
	    print("Total number of students is "+len(student_list))
		
class Teacher: #friends: Leader
    def command(self,name_list,leader):
	    student_list = []
	    for name in name_list:
		    student_list.append(Student(name)) #`Student` is not a friend
		leader.countStudents(student_list)

if __name__ == "__main__":
    teacher = Teacher()
	leader = Leader()
	name_list = ['A','B','C','D','E']
	teacher.command(name_list,leader)
```

![teacher-leader-student_1](https://www.ycc.idv.tw/media/SOLID_Introduction/teacher-leader-student_1.png)

以上程式違反「迪米特法則」，因為在類別`Teacher`的方法`command`中訪問了不是朋友的`Student`，這會使得`Teacher`和`Student`會產生不必要的耦合，我們可以將創造`student_list`的權責轉移到`Leader`上，如此一來就可以斷開`Teacher`和`Student`的耦合。

正確示範：

```python
### Python3.4

class Student: #friends: None
    def __init__(self,name):
	    self.name = name

class Leader: #friends: Student
    def giveNameList(self,name_list):
		student_list = []
	    for name in name_list:
		    student_list.append(Student(name))  
	    self.__student_list = student_list
		
    def countStudents(self):
	    print("Total number of students is "+len(self.__student_list))
		
class Teacher: #friends: Leader
    def command(self,name_list,leader):
	    leader.giveNameList(name_list)
		leader.countStudents()

if __name__ == "__main__":
    teacher = Teacher()
	leader = Leader()
	name_list = ['A','B','C','D','E']
	teacher.command(name_list,leader)
```

![teacher-leader-student_2](https://www.ycc.idv.tw/media/SOLID_Introduction/teacher-leader-student_2.png)

-- Why it works? 

先來想想「朋友」有什麼共通之處？其實它們都是類別本身無法斷開耦合的物件，既然無法斷開耦合，何不運用到底，運用這些「朋友」來完成任務，不要再去增加其他的耦合性，也同時幫助提升類別的內聚性，這就是「迪米特法則」真正想做的事。

以這樣的方式去寫程式，也可以避免寫出像是`A.getB().getC()`的程式碼（A和C不是朋友），這樣冗長的程式碼不僅增加了無益的耦合，也讓程式變得不利於可讀性。

**（詳解）減少類別的對外方法，將沒必要對外公布的方法隱藏起來。**

-- 例子: 安裝程式。

錯誤範例：

```python
### Python3.4

class Wizard: # 3 public methods
    def first(self):
		print("Install first step of wizard at mode")
	def second(self,mode):
	    print("Install second step of wizard at mode "+mode)
	def third(self):
	    print("Install third step of wizard")

class Install:
    def install(self,wizard,mode):
	    wizard.first()
		wizard.second(mode)
		wizard.third()
```

有太多沒必要對外公布的細節了，依照「迪米特法則」，我們應該將盡量減少對外公布的資訊，把不必要公布的細節私有化。

正確範例：

```python
### Python3.4

class Wizard: # only 1 public method
    def install(self,mode):
		self.__first()
		self.__second(mode)
		self.__third()
		
    def __first(self):
	    print("Install first step of wizard")
	def __second(self,mode):
	    print("Install second step of wizard at mode "+mode)
	def __third(self):
	    print("Install third step of wizard")

class Install:
    def install(self,wizard,mode):
	    wizard.install(mode)
```

### 依賴倒置原則(Dependence Inversion Principle, DIP)

* 定義：High level modules should not depend upon low level modules. Both should depend upon abstractions. Abstractions should not depend upon details. Details should depend upon abstractions.（高層次模組不應該依賴低層次模組，兩者都應該依賴抽象。而抽象不應該依賴細節，反之細節應該要依賴抽象。）

* 範例：假設我們成立一家玩具車公司，開始著手設計我們的第一款車款A，設計的架構圖如下

![toycar_1](https://www.ycc.idv.tw/media/SOLID_Introduction/toycar_1.png)

`ToyCarA`是我們的實體車子，可以使用`setRPM`來設定在幾秒之後到達什麼轉速，而控制他的是電腦模擬的虛擬車`VirtualCar`，虛擬車提供方法`setSpeeed`可以設定車速，當然！模擬的車速要和真實車速吻合，還需配合適當的調控實體車的轉速，所以`VirtualCarA`關聯到`ToyCarA`去做控制。然後我們公司會提供一個控制器`ControllerA`來控制車子，控制器上的搖桿分為五級，讓使用者可以控制速度，使用`controlBarLevel`方法根據級數去控制`VirtualCarA`的速度。

檢驗一下這個設計圖，它違反「依賴倒置原則」，`ControllerA`依賴`VirtualCarA`，`VirtualCarA`依賴`ToyCarA`，這些都是實體類別，高層次依賴了低層次。不過，公司的車子A還是賣得很好，沒有什麼大礙。

終於有一天災難降臨了，市場出現了比車子A馬力更強大的玩具車，我們公司如果不趕緊採用新的馬達推出新的車款，就會失去競爭力，我們需要採用新的玩具車`ToyCarB`，它擁有更好的馬達，我們需要為因應高速度而推出九級分級的搖桿，新的控制器`ControllerB`，結果回頭一看原本設計圖，完了！所有的A系列的程式碼都耦合在一起了，核心程式`VirtualCarA`原可以不需要大改，就建造出`VirtualCarB`的，但是現在程式碼全部耦合在一起，它已經變得不可擴張了。

如果我們一開始就依照「依賴倒置原則」，我們來看看擴張會有多容易



![toycar_2](https://www.ycc.idv.tw/media/SOLID_Introduction/toycar_2.png)



`VirtualCar`中的很多方法都可以在B車款上再重用，大大的減少重新開發的成本。

* 依賴倒置原則又稱為「面向接口原則」，這裡的接口應該想的更廣義一點，不侷限在interface上，我認為只要藉由抽象化將架構擬定出來的這些抽象單元都可以稱作接口，「廣義的接口」可以是指

1. 客戶端和業務邏輯的分離介面
2. 物件的開放方法
3. 抽象類別
4. 定義行為的interface

我們不讓作為實現的類別彼此依賴，而是使用接口將抽象架構擬定好，再讓類別去依賴接口實現目標。


### 接口分隔原則(Interface Segregation Principle, ISP)

* 定義：Clients should not be forced to depend uponn interfaces that they don't use. The dependency of one class to another one should depend on the smallest possible interface.（客戶類不應該被強迫依賴那些它不需要的接口，類別間的彼此依賴應該建立在盡可能小的接口上）

* 這裡說的接口同樣的是剛剛所說的「廣義接口」，可以是客戶端和業務邏輯的分離介面、物件的開放方法、抽象類別和Interface。

* 接口分隔原則建議我們要讓這些廣義接口盡可能的細切，但在實務上，切的過細會導致程式碼非常零碎難以閱讀，所以YC的建議是切到遵守「單一職責原理」就足夠了，與剛剛的建議一致，Interface一定要遵守「單一職責原理」，但是類別就盡力而為吧！

* 範例：剛剛玩具車公司的設計圖其實還是不夠好，如果今天公司想要開發新的車款C，添加新「方向盤」的功能，你會發現夢魘又再次的降臨，抽象類別`ToyCar`、`VirtualCar`、`Controller`都需要改變，而且就算真的把「方向盤」的相關方法添加上去，抽象類別也會開始出現多於一的職責，所以我們用Interface來重新改寫架構，如下圖所示。不難看出，控制馬達、控制速度、控制搖桿的行為是彼此依賴的，我們可以將他們的行為由Interface獨立拉出並相互依賴。

![toycar_3](https://www.ycc.idv.tw/media/SOLID_Introduction/toycar_3.png)

如此一來，當我們想要開發新的車款C，添加新「方向盤」的功能，也能輕鬆的擴充，如下所示。`ToyCarPlus`、`VirtualCarPlus`、`ControllerPlus`是我們實作C車款的抽象類別，它現在可以直接套用`IMotor`、`ISpeed`、`IControlBar`的Interface。

![toycar_4](https://www.ycc.idv.tw/media/SOLID_Introduction/toycar_4.png)


### 總結：物件導向的指導原則—SOLID

上面介紹的六大原理：

1. Single Responsibility Principl
2. Open-Closed Principle
3. Liskov Subsititution Principle
4. Law of Demeter
5. Interface Segregation Principle
6. Dependence Inversion Principle

剛剛好組成SOLID這個單字，所以又被統稱SOLID原則。

事實上，這些原則所要達到的目的，不外乎就是我們[第一篇](http://www.ycc.idv.tw/YCNote/post/47)當中所介紹的好的程式碼特性：「正常執行」、「穩健」、「不重複撰寫」、「可讀性」、「可擴展」，或者是「低耦合、高內聚」，所以寫程式時如果能時時注意，說不定你也可以自己領會這六大法則。

我來快速的總結這六大法則告訴我們的事：

1. 在開發程式的初期，先定義好抽象架構，也就是廣義的接口，徹底的使客戶端與業務邏輯分離，將「行為」定義成Interface，將「類別的泛化」定義成Abstract Class。
2. 所有的實體類別都依賴於抽象，細節依賴於抽象。
3. 每個單元盡量達到：單一權責、對延伸開放但對修改封閉、盡可能少的對外方法。
4. 牽涉「繼承」，必須要問自己：子類可以替換父類執行嗎？父類是不是為子類的交集？
5. 類別中的方法僅能訪問那些類別出現在自身、成員變數、方法的輸入和輸出參數中的。

如此一來，我們心中就有一個準則去使用物件導向。

在一般情形下，這三篇的內容應該就足夠讓你寫出好的程式碼，但是實際面上使用仍然會碰到許多問題，於是乎有人將問題整理並總結出一些套路，這就是「設計模式」，我們以後再來談談吧！今天就先到這。

### Reference

1. [大話設計模式](https://www.tenlong.com.tw/products/9789866761799)
2. [設計模式之禪](https://www.tenlong.com.tw/products/9787111437871)




