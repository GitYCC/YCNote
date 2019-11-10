Title: 機器學習技法 學習筆記 (1)：我們將會學到什麼? 先見林再來見樹
Date: 2017-01-12 12:00
Category: AI.ML
Tags: 機器學習技法
Slug: ml-course-techniques_1
Author: YC Chen
Illustration: ml-course-techniques.jpeg
Alias: /YCNote/post/29.html
related_posts: ml-course-foundations_3,ml-course-foundations_4,ml-course-techniques_2,ml-course-techniques_3
Summary: 有什麼特徵可以使用？ / Embedding Numerous Features ：Kernel Models / Combining Predictive Features：Aggregation Models / Distilling Implicit Features：Extraction Models

在之前四篇文章中，我總結了台大教授林軒田在Coursera上的《機器學習基石》16堂課程，我覺得這是機器學習初學很重要的基礎課程，接下來我要接續更進階的課程。

林軒田教授的機器學習是兩學期的課，第一學期是《機器學習基石》，第二學期就是接下來這個系列要講的《機器學習技法》，這兩堂課程是有相當大的銜接關係的，所以如果想看這系列的文章，請先看[這四篇《機器學習基石》的介紹](http://www.ycc.idv.tw/tag/ji-qi-xue-xi-ji-shi.html)或者[直接到Coursera上學習](https://www.coursera.org/learn/ntumlone-mathematicalfoundations)。

《機器學習技法》課程影片可以到老師的Youtube [ [https://www.youtube.com/playlist?list=PLXVfgk9fNX2IQOYPmqjqWsNUFl2kpk1U2](https://www.youtube.com/playlist?list=PLXVfgk9fNX2IQOYPmqjqWsNUFl2kpk1U2) ]上收看，投影片可以到老師的個人網站上下載 [ [https://www.csie.ntu.edu.tw/~htlin/course/mltech17spring/](https://www.csie.ntu.edu.tw/~htlin/course/mltech17spring/) ]。

以前，我曾經和實驗室的英國學長聊英國的教育方法，然後我驚人的發現，他的學校在大一就已經學過量子場論（物理上很難的學科XDD）了，我就很好奇量子場論不是需要很深厚的數學基礎嗎？大一是要怎麼教啊？他告訴我，他們大一就會完整走過物理的各大領域，不過是用非常概念的方式來學習，不牽涉到太困難的數學，但這概念的一系列課程卻是四年大學中相當重要的基礎，讓他在開始學細節前就可以知道這些東西未來會用在哪裡？產生了連結讓學習更有效率。

所以，《機器學習技法》中會介紹很多厲害的機器學習的方法，但這一篇我不直接進去看每個方法的細節，我想帶大家坐著直升機來先看看這遊樂園中有哪些遊樂設施，先來見林再來見樹，會更容易了解。

<br/>

### 有什麼特徵可以使用？

在之前《機器學習基石》中，我們講到了Features（特徵）的選擇，**Features（特徵）就是我的Model描述Data的方法，也可以說是影響Data的變數**，那在之前我們講過Features（特徵）的選擇可以是線性的，那也可以使用「特徵轉換」來產生非線性。

在這系列文章，我們會看到更多種類的Features，可以分為三類：

1. Embedding Numerous Features（嵌入大量特徵）
2. Combining Predictive Features（綜合預測結果的特徵）
3. Distilling Implicit Features（抽取隱含特性的特徵）

我已經盡力用我的理解翻譯上面的英文，哈！

這些不同種類的Features就會造成不同的Models，這些Models分別是

1. Embedding Numerous Features ：Kernel Models（Kernel模型）
2. Combining Predictive Features：Aggregation Models（集合模型）
3. Distilling Implicit Features：Extraction Models（萃取模型）

讓我們依序來看。

<br/>

### Embedding Numerous Features ：Kernel Models

還記得《機器學習基石》中，我們講了哪些Model嗎？我們一開始講了二元分類問題，然後提出了Perceptron Learning Algorithm (PLA)來解決這個問題（[詳見《機器學習基石》第一篇](http://www.ycc.idv.tw/ml-course-foundations_1.html)），如果數據是線性可分的話，我們就可以使用PLA劃分出一條邊界來區分兩種種類。

接下來提到我們可以使用Regression的方法來做二元分類問題，其中Logistic Regression考慮了雜訊造成每個Label的出現呈機率分布，給予一個較為寬鬆的區分方法，我們會稱PLA為Hard Classification，而Logistic Regression為Soft Classification。（[詳見《機器學習基石》第三篇](http://www.ycc.idv.tw/ml-course-foundations_3.html)）

最後，我們引入「特徵轉換」將我們原本的線性區分推到非線性區分，讓我的Model有更大的複雜度，也因為如此，我們需要使用Regularization和Validation來避免 Overfitting。（[詳見《機器學習基石》第四篇](http://www.ycc.idv.tw/ml-course-foundations_4.html)）

**那如果我想要使用無窮個高次方的非線性Features來當作我的Model，可以做到嗎？**

來看一下之前我們做特徵轉換怎麼做的？其實我們沒有多做什麼功夫，我們只是把高次項先產生出來，然後在把這每一項當作線性模型的Features去處理，我們就用線性模型的方法產生了非線性的效果。

那如果非線性項目的個數無窮多個，顯然這種方法就做不了了啊！

不過，數學總是會拯救我們，**我們可以使用Dual Transformation加上Kernel Function的技巧，帶我們走捷徑，直接用解析解讓我們得出答案，繞過要考慮無窮多個Features後再處理的窘境。**

第一堂課「Linear Support Vector Machine」中，提出Hard-Margin Support Vector Machine (SVM)的架構，他和PLA非常相近，屬於Hard Classification，不同的是Hard-Margin SVM還會讓這個切分的邊界落在最佳的位置上。

第二堂課 「Dual Support Vector Machine」中，我們開始使用Dual Transformation，把大部分與Data中Features有關的計算，取代成計算與Data中Labels有關的計算，讓我們朝不需要計算Features邁進一步，但是因為有另外一部分還是需要計算Features，所以一樣的我們還是無法讓Features有無窮多個。

第三堂課「Kernel Support Vector Machine」中，我們引入Kernel Function來幫助我們，現在真的可以不需去列出所有Features也能算出答案，所以我們就可以讓Features有無窮多項，但也因為Model太過複雜，我們不得不去面對Overfitting的問題。

第四堂課「Soft-Margin Support Vector Machine」中，提出Soft-Margin SVM，它是一種Soft Classification，讓我們可以允許部分錯誤發生，並且同樣的使用Dual Transformation加上Kernel Function的技巧，來讓我可以使用無窮多項的Features，而且因為Soft-Margin SVM可以允許錯誤，也就是對雜訊有容忍度，因此可以幫助我們抑制Overfitting的發生。

第五堂課「Kernel Logistic Regression」中，我們將Kernel的方法引入Logistic Regression當中來用不同於Soft-Margin SVM的方式做二元分類。

第六堂課「Support Vector Regression」中，會介紹如何使用Kernel Model來做各類Regression的問題。

**這6堂課，主要做的事是把《機器學習基石》裡面學到的東西，全部引入數學工具讓Model的Features可以擴展到無窮多項，產生更強大的Kernel Model。**

<br/>

### Combining Predictive Features：Aggregation Models

那如果今天我有很多支的Model，我有辦法融合他們得到更好的效果嗎？

**這就是Aggregation Models的精髓，Aggregation Models藉由類似於投票的方法綜合各個子Models的結果得到效果更好的Model。換個角度看，你可以把整個體系看成一個新的Model，而原本這些子Models當作轉換過後的新Features，所以Aggregation Model裡頭做了「特徵轉換」，這個轉換產生出許多有預測答案能力的Features，稱為Predictive Features，然後再綜合它們。**

Aggregation Models可以分成兩大類，第一種的作法比較簡單，先Train出一個一個獨立的Predictive Features，然後在綜合它們，**「集合」的動作是發生在得到Train好的Predictive Feature之後，這叫做「Blending Models」**；第二種作法則是，**「集合」的動作和Training同步進行，這叫做「Aggregation-Learning Models」**。

從「集合」的方法上也可以進一步細分三種類型，有票票等值的**「Uniform Aggregation Type」**，有給予Predictive Features不同權重的**「Linear Aggregation Type」**，甚至還可以用條件或任意Model來分配Predictive Features，這叫做**「Non-linear Aggregation Type」**。

所以兩種類型、三種Aggregation Type，交互產生六種Aggregation Models。

第七堂課「Bootstrip Aggregation」中，一開始介紹Blending Models的三種Aggregation Type，第一種是直接平均所有的Predictive Features，第二種則是藉由每個Predictive Feature的預測能力，使用線性模型去調配它們的權重，第三種則是使用任意模型分配權重。接著又介紹了Aggregation-Learning Models的Uniform Aggregation Type，稱之為Bagging，它的特點在於它可以利用變換Dataset來造出很多個Predictive Features，並接著做Aggregation。

第八堂課「Adaptive Boosting」中，介紹Aggregation-Learning Models的Linear Aggregation Type，稱之為AdaBoost，它的特點在於它可以使得每個Predictive Features彼此間可以截長補短。

第九堂課「Decision Tree」中，介紹Aggregation-Learning Models的Non-linear Aggregation Type，稱之為Decision Tree。

第十堂課「Random Forest」中，使用Bagging來做Decision Tree，這叫做Random Forest。

第十一堂課「Gradient Boosted Decision Tree」中，會介紹AdaBoost的Regression版本稱為GradientBoost，並且運用AdaBoost和GradientBoost在Decision Tree上面。

**這5堂課，我們將會介紹Aggregation Models，引入綜合、集合Predictive Feature的概念來使我們造出更好的Model。**

<br/>

### Distilling Implicit Features：Extraction Models

那最後這個部分則是介紹現今很流行的「類神經網路」(Neural Network) 和「深度學習」(Deep Learning)，在這裡我們通稱Extraction Models。

**Extraction Models的特色在於它「特徵轉換」的方法，使用一層一層神經元來做非線性的特徵轉換，如果具有多層神經元，那就是做了多次的非線性特徵轉換，這就是「深度學習」，藉由Data機器會自行學習出這每一層的特徵轉換，找出隱含的Features。**

第十二堂課「Neural Network」中，介紹Neural Network，並介紹Neural Network的演算法—Back-Propagation（反向傳遞法），在概念上Gradient Descent就是Back-Propagation的源頭，另外介紹避免Overfitting的方法—Early Stopping。

第十三堂課「Deep Learning」中，開始介紹「深度學習」，考慮多層神經元的Neural Network就叫做Deep Learning，我們會探討如何在Deep Learning中加入Regularization，並介紹一種叫做Auto-encoder的特殊Deep Learning方法。

第十四堂課「Radial Basis Function Network」中，介紹Radial Basis Function (RBF) Network，並且介紹K-means等非監督分類法。

第十五堂課「Matrix Factorization」中，我們會探討類別的匹配問題，例如：我想要知道用戶喜歡看什麼電影，而我的Data只有用戶的ID和電影的編號。

**這4堂課，我們將會介紹Extraction Model，使用神經元的概念來萃取出Data中的Features。**

<br/>

### 後話

最後總結一下《機器學習技法》會講哪些東西？我們會講具有三種不同「特徵轉換」方式的Models。**Kernel Model的「特徵轉換」是將非線性Features擴張到無窮多個；Aggregation Model的「特徵轉換」是產生出有預測能力的Features；Extraction Model的「特徵轉換」是利用神經元的方式來做到萃取出隱含的資訊。**

**跟《機器學習基石》不一樣的地方，《機器學習技法》中介紹更厲害的「特徵轉換」來產生更厲害的Model，不過因為會有Overfitting的狀況，所以我們還需要介紹相應的配套措施。**

在未來一系列的文章，我會帶大家一一的來看這些內容，不過和之前一樣，我不會以課堂當作單位來講，而是以單元式的方式，而且我主要的目的是去點出概念，並盡可能的不去牽涉太多的數學計算，但是數學計算的部分是很重要的，這會影響到你真正的實作，數學的部份可以去看林軒田老師的影片或投影片，裡頭都有很詳細的介紹。
