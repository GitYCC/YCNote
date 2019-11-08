Title: 機器學習技法 學習筆記 (5)：Boost Aggregation Models
Date: 2017-04-02 12:00
Category: AI.ML
Tags: 機器學習技法
Slug: ml-course-techniques_5
Author: YC Chen
Illustration: ai_front_board.jpg
Alias: /YCNote/post/34.html
related_posts: ml-course-techniques_3,ml-course-techniques_4,ml-course-techniques_6,ml-course-techniques_7
Summary: 本篇內容涵蓋AdaBoost (Adaptive Boost)、Gradient Boost、AdaBoosted Decision Tree和Gradient Boosted Decision Tree (GBDT)。



### Boost的精髓

在上一回當中，我們介紹的Aggregation Models都屬於沒有Boost的，不管是Bagging或Decision Tree都沒有要試著在Training的過程中改善Model，**而這篇將要提到的Boost方法，則是在產生每個$g_{t}$時試圖讓Model整體更完善，更能發揮Aggregation Models中截長補短中的「補短」的效果，也就是說$g_{t}$可以彼此互補不足之處**。

那實際上我們應該怎麼做才能實踐Boost呢？其實方法的道理早就透漏在上一回中的Bagging和Decision Tree裡頭了，不管是Bagging和Decision Tree都是使用變換Data來做到變異度，在這個方法下Model的架構可以本身是不變的，這帶來相當的便利性，而今天我們要講的Boost也同樣的利用「變換Data」來做到變異度，但不同的是Boost的過程中「變換Data」這件事是有目標性的。

**Boost方法在「變換Data」時會試著去凸顯原先做錯的Data，而降低原本已經做對的Data，藉由這樣的方法訓練出來的$g_{t}$可以補齊前面的不足，所以Boost的過程將會使得Model漸漸的完善，這就是Boost的主要精髓。**

<br/>

### AdaBoost (Adaptive Boost) for Classification

剛剛上一段的最後我已經揭露了Boost的真正精髓，拿這樣的概念來做分類問題，就是我們接下來要談的AdaBoost，全名稱為Adaptive Boost。

在分類問題中我們怎麼做到「凸顯原先做錯的Data」？簡單的想法是這樣的，我們可以減少原本已經是正確分類的Data的數量，然後增加原本錯誤分類的Data的數量，**增減Data的數量其實是等效於改變每筆Data的權重**，假如我們給每筆資料權重，要做的事是拉低正確分類Data的權重，而且拉高錯誤分類Data的權重。

那我們應該要提升權重或降低權重到什麼程度才是OK的呢？換個方式思考，我們為什麼要去調整權重？目的其實是要去凸顯原先做錯的部分，降低原本做對的部分，也就是想**藉由調整每筆Data的多寡或權重來做到「弭平原先的預測性」，最好可以讓原本的預測方法看起來是隨機分布**，也就是「錯誤率＝正確率」，讓它像是擲銅板一樣，沒有什麼預測能力。

![AdaBoost](http://www.ycc.idv.tw/media/MachineLearningTechniques/MachineLearningTechniques.012.jpeg)

有了概念之後，我們來看實際應該要怎麼做？見上圖說明，首先我們需要先將Data權重$u^{(1)}$先初始化，接下來就可以開始找$g_{t}$了，我們使用任意一個分類問題的Model搭配上Data的權重，求得一組$g_{t}$，接下來計算這組$g_{t}$的**「錯誤率」$ε_{t}$**，

**$ε_{t}= 𝚺_{n} u_{n}^{(t)} ⟦y_{n}≠g_{t}(x_{n})⟧ / 𝚺_{n} u_{n}^{(t)}$**

有注意到考慮「錯誤率」$ε_{t}$的時候必須要評估$u_{n}^{(t)}$，要記得會有Data權重是為了表示增加或減少原本的Data的數量，所以依照每筆Data的出現機會不同，會有不同的權重，也就會有對「錯誤率」不同的貢獻程度。

那為了待會要對權重重新分配，我們先定義了$β_{t}$，在未來我會將錯誤的Data的權重乘上$β_{t}$，即$u_{n}^{(t+1)}=u_{n}^{(t)}×β_{t}$，並且把正確的Data權重除以$β_{t}$，即$u_{n}^{(t+1)}=u_{n}^{(t)}/β_{t}$，**而期望的結果是重新分配的Dataset在$g_{t}$的預測下可以表現的像隨機的一樣，於是乎下一次使用這組Dataset訓練出來的$g_{t+1}$將會彌補$g_{t}$的不足**，根據這樣的原則我們來推一下$β_{t}$，

 $𝚺_{n} u_{n}^{(t+1)} ⟦y_{n}≠g_{t}(x_{n})⟧ / 𝚺_{n} u_{n}^{(t+1)}=1/2$ (預測能力像隨機分布)

⇒  $𝚺_{n} u_{n}^{(t+1)} ⟦y_{n}≠g_{t}(x_{n})⟧ = 𝚺_{n} u_{n}^{(t+1)} ⟦y_{n}=g_{t}(x_{n})⟧$

⇒  $𝚺_{n} (u_{n}^{(t)}×β_{t})  ⟦y_{n}≠g_{t}(x_{n})⟧ = 𝚺_{n} (u_{n}^{(t)}/β_{t}) ⟦y_{n}=g_{t}(x_{n})⟧$

⇒  $β_{t}^{2} = 𝚺_{n} u_{n}^{(t)} ⟦y_{n}=g_{t}(x_{n})⟧ / 𝚺_{n} u_{n}^{(t)}  ⟦y_{n}≠g_{t}(x_{n})⟧$

⇒  $β_{t}^{2} = [𝚺_{n} u_{n}^{(t)} ⟦y_{n}=g_{t}(x_{n})⟧ /  𝚺_{n} u_{n}^{(t)}]/ [𝚺_{n} u_{n}^{(t)}  ⟦y_{n}≠g_{t}(x_{n})⟧ / 𝚺_{n} u_{n}^{(t)} ]$

⇒  **$β_{t}^{2} = 1-ε_{t} / ε_{t}​$**

所以我們就可以利用這個$β_{t}$來更新我的Data權重，並且在多次迭代後，得到很多個$g_{t}$。而將來我們會把所有的$g_{t}$做線性組合，而我們希望**「錯誤率」越低的$g_{t}$可以有更高的貢獻度$α_{t}$**，所以使用$β_{t}$緊接著計算「$g_{t}$的權重」$α_{t}$，定義為

**$α_{t} = ln(βt)$**

所以當一個百分之一百可以完全預測的$g_{t}$出現時，它的$ε_{t}=0$，此時它的$β_{t} →∞$，同時$α_{t} →∞$，所以這樣的$g_{t}$會有完全的貢獻。

如果一個預測效果很差的$g_{t}$出現，它的$ε_{t}=1/2$，此時它的$β_{t}=1$，同時$α_{t}=0$，所以這樣的$g_{t}$並沒有任何參考價值。

那如果出現一個$g_{t}$它的$ε_{t} > 1/2$，那這樣的$g_{t}$並不能說它沒有用處，反而是一個很好的反指標，我們只需要反著看就好了，當$ε_{t} > 1/2$時，$β_{t} < 1$，所以$α_{t} < 0$，這樣的$g_{t}$具有逆向的貢獻。

最後只要把這些訓練好的$g_{t}$乘上各自的$α_{t}$再加總起來，我們就完成了AdaBoost啦！

<br/>

### Gradient Boost for Regression

剛剛我們講了AdaBoost，是個很神奇的方法，當我們做錯了，沒關係！從哪裡跌倒就從哪裡站起來，利用這種精神我們就可以做到Boost的效果，但美中不足的是上面的方法只能用在「分類問題」上，那如果我也想在「Regression問題」也做到Boost呢？這就是接下來要講的GradientBoost的方法。

在課程中林軒田教授是從AdaBoost出發經過推導後，得到一個很像是Gradient Decent的式子，接下來將式子一般化成為可以使用任意Error Measure的形式，我稍微列一下：

> GradientBoost: $min_{η}\ min_{h}\ (1/N) 𝚺_{n} err[𝚺_{τ=1~t-1} α_{τ} g_{τ}(x_{n}) + η h(x_{n}), y_{n}]$

我們這邊會考慮err為平方誤差$(s-y)^{2}$的結果，詳細的推導這邊就不多加討論，可以到影片中學習，這裡我想要從我觀察出來的觀點，概念性的來看這個GradientBoost的方法。

「從哪裡跌倒就從哪裡站起來」就是Boost的精神，所以今天你有一個Regression問題沒做好，**留下了餘數Residual，怎麼辦？那我就把這個餘數當作另外一個Regression問題來做它**，再把這個結果附到先前的那個就好啦！如果第一次Regression後的Model是$g_{1}(x)$，那剩下的沒做好的餘數就應該是$y(x)-g_{1}(x)$，我們拿這個餘數下去在做一次Regression得到另外一個Model $g_{2}(x)$，此時合併這兩個結果的餘數就變成了$y(x)-g_{1}(x)-g_{2}(x)$，就可以使用這個餘數繼續做下去，最後組合所有的$g_{t}(x)$就會得到一個更好的Model。

![Gradient Boost](http://www.ycc.idv.tw/media/MachineLearningTechniques/MachineLearningTechniques.013.jpeg)

依循這樣的概念我們來看GradientBoost作法，如上圖，一開始我們先初始化每一筆Data的預測值$s_{n}$為0，再接下來開始產生$g_{t}$，我們先把Data的 $y_{n}$ 減去每一筆Data當前的預測值$s_{n}$，就會產生餘數$(y_{n}-s_{n})$，當然，在一開始$s_{n}=0$，所以$y_{n}-s_{n}=y_{n}$，等於是對原問題求解。

接下來因為最後我們要線性組合$g_{t}(x)$，所以需要決定$g_{t}(x)$前面的係數$α_{t}$，也就是貢獻度，這個$α_{t}$的決定方式是去求解一個One-Variable-Linear-Regression (單變數線性迴歸)，目的是**去縮放$g_{t}(x)$使得它更接近剛剛的餘數$(y_{n}-s_{n})$，而找到這個縮放值就是$α_{t}$**。所以每一次$g_{t}(x)$的產生都是為了可以把G(x)描述的更好，最後$G(x)=𝚺_{t} α_{t}g_{t}(x)$。

看到這裡有人一定會認為One-Variable-Linear-Regression求$α_{t}$這一步是多餘的，因為在一開始做$\{x_{n},y_{n}-s_{n}\}$的Regression中我們已經最佳化過$g_{t}(x)$，那為什麼還要把$g_{t}(x)$乘上$α_{t}$再做同樣的事呢？$α_{t}$一定是1的啊！就像我一開始舉的例子一樣啊！其實問題就出在於你把$g_{t}(x)$理所當然的看成是線性模型，你才會覺得這一步是多餘的，如果$g_{t}(x)$不是線性的，求$α_{t}$就很重要的，因為你要使用線性組合來組出$G(x)$，但是你的$g_{t}(x)$不是線性的，所以你只好在外面再用線性模型來包裝一遍。

<br/>

### AdaBoosted Decision Tree和Gradient Boosted Decision Tree (GBDT)

![AdaBoosted and GrandientBoosted DTree](http://www.ycc.idv.tw/media/MachineLearningTechniques/MachineLearningTechniques.014.jpeg)

和Random Forest一樣，我們也可以將AdaBoost和GradientBoost套用到Decision Tree上面，**如果是處理分類問題就使用AdaBoosted Decision Tree；那如果是處理Regression問題可以使用Gradient Boosted Decision Tree**。

但要特別注意的是，這邊的Decision Tree都必須是弱的，也就是Pruning過後的樹，如果直接使用完全長成的樹，你會發現在AdaBoosted Decision Tree中，因為$ε_{t}=0$所以$α_{t}→∞$；在Gradient Boosted Decision Tree中，$y_{n}-s_{n}→0$，因為錯誤出現的太少了，所以造成我們不能真正使用到Boost的效果，也就失去做Boost的意義了，**因此在做AdaBoosted Decision Tree或Gradient Boosted Decision Tree時要使用「弱」一點的Decision Tree**。

<br/>

### 結語

這一篇當中，我們完整提了Boost的方法，Boost的精神就是從哪裡跌倒就從哪裡站起來，使用變換Data權重的手法去凸顯原先做錯的Data，而降低原本已經做對的Data，藉由這樣的方法訓練出來的$g_{t}$可以補齊前面的不足，所以Boost的過程將會使得Model漸漸的完善。

我們提了兩種Boost的方法，如果是處理分類問題就使用AdaBoost；如果是處理Regression問題可以使用GradientBoost，而且這兩種方法都可以和Decision Tree做結合。

以上兩回，我們已經完成了Aggregation Models了，接下來的下一回將要探討的就是現今很流行的類神經網路和深度學習等等。
