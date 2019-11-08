Title:  Python玩數據 (1)：安裝Python, IPython, Numpy, Pandas
Date: 2017-03-20 12:00
Category: Coding
Tags: Python玩數據
Slug: python-play-with-data_1
Author: YC Chen
Illustration: coding_front_board.jpg
Alias: /YCNote/post/18.html
related_posts: python-play-with-data_2,python-play-with-data_3
Summary: 安裝Python, IPython, Numpy, Pandas

**相較於R，我比較喜歡在工作上使用python來作數據處理**，主要原因有四個，**第一點，python是一個簡潔的語言**，讓我們可以在不寫註解的情況下還可以很容易的看出每一行code在做哪些事，這可以省去了不少時間在；**第二點，python可以更容易的寫成物件導向編程**，物件導向編程可以讓code看起來更為直覺，而且更易於修改、重構或套用，如果是大型軟體開發的話，需要多人協作，此時物件導向便是絕對必要的；**第三點，python是一個通用語言**，不僅僅只可以作資料處理而已，你可以用python寫一套視窗程式，或者當作網站的後台（這個網站就是建基在python上），如果要做一些平行運算也很容易，**最後一點，也是相當重要的一點，目前常見的deep learning套件TensorFlow或Keras都是架構在python上面**，所以如果你的數據處理結束要作deep learning的話，直接用python處理是相當理想的。講了python這麼多優點，其實它是有一項缺點是不如R的，R是一個專為資料科學設計的語言，所以背後有強大的社群，也就是說能直接取得資料分析方法的套件會比python來的多，不過這方面在這幾年已經漸漸的改善了。

講了這麼多python的強大，不過在這個系列我並不會著墨太多在python上，這個部分我會在其他的文章中分享，這系列文章主要聚焦在python的資料處理這部份，我會從基礎講起，讓不懂python的人也可以聽懂。  

<br>

### 最困難的第一步：安裝

不要以為我在開玩笑，安裝往往是最困難的一步，有些時候安裝一些套件的時候，你必須要先行安裝另外幾個相依套件，如果程式在安裝的過程無法自己補足這些相依套件的話，你就得自己安裝，一般來說如果是python的套件的話，你可以先用待會要介紹的`pip install`來安裝，如果不幸在上面找不到的話，就只好上網Google了，另外有些時候安裝還會遇到bug，這個時候Google也同樣是你的好朋友，或者到[Stack Overflow](https://stackoverflow.com) 上找答案（一個好的coder要培養自己上網找答案的能力），不過大家先不用擔心，以下我會帶大家一步一步的安裝。

我們將會用到python 2.7版（你也可以選擇更新的版本，不會差距太大），以及他的套件IPython, Numpy和Pandas。

<br>

### Python2.7

* Mac

python2.7已經是內建的程式了！打開「終端機」，直接輸入

```bash
$ python2.7 -V

Python 2.7.13
```

就會顯示他的版本。

如果沒有的話，或者你想要自己安裝一份的話，可以參考[這篇](https://stringpiggy.hpd.io/mac-osx-python3-dual-install/)的說明，或者跟著我往下作。

**Step 1:** 安裝 Xcode：打開你的App Store，搜尋Xcode並安裝。

**Step 2:** 安裝 [Homebrew](https://brew.sh) 這個Mac上好用的套件管理，打開「終端機」，輸入

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew

Press RETURN to continue or any other key to abort
```

(附註：我用 `＄  ` 代表終端機的輸入起始字元，後面才是你需要輸入的指令)

按下Enter就會開始安裝了。

安裝完畢你就可以直接在「終端機」上使用它，我們試著搜尋python

```bash
$ brew search python

app-engine-python               boost-python@1.59               micropython                    
python-markdown                 wxpython
boost-python                    gst-python                      python ✔                       
python3 ✔                       zpython
homebrew/apache/mod_python            
Caskroom/cask/kk7ds-python-runtime          
Caskroom/cask/mysql-connector-python
```

因為我的電腦已經安裝了python2.7和python3.0，所以你會看到他們已經是打勾的狀態，我們的目標就是安裝「python」。

<br>

**Step 3:** 安裝python2.7：

```bash
$ brew install python
```

安裝完畢後檔案會被放在底下這個路徑，你可以打開來看一下

```Bash
$ open /usr/local/Cellar
```

應該就會看到python的資料夾了。

<br>

**Step 4:** 設定路徑 $PATH（不跟系統 Python 打架）

這是什麼呢？當你輸入`brew` , `open` , `python2.7` 這些指令到「終端機」上，為什麼「終端機」會認的了這些指令，原因就出在於這個PATH上，又稱為「環境變數」，我們把它叫出來看看

```bash
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

你可以看到有五個路徑分別被字元 `:` 隔開，由前到後分別為`/user/local/bin`、`/usr/bin`、`/bin`、`/usr/sbin`、`/sbin`，這一些都是裝有執行檔的資料夾，今天你如果輸入某個指令，他就會從第一個資料夾下面開始找起，也就是`/user/local/bin`，沒有找到再依序往下找，直到找不到為止，如果今天`/usr/bin`底下有python，而你剛剛用brew安裝的另一個python放在`/user/local/bin` 底下，在這個例子中，你會執行到的就是第一個路徑`/user/local/bin` 下的python，那這也是我們要的結果，我們想要執行我們自己安裝的，而不是系統原有的。

如果`/user/local/bin`不是在第一個的話，就必須去修改PATH的順序。

```bash
$ sudo emacs /etc/paths
```

輸入密碼後，就會進入修改模式，然後開始修改順序，利用以下指令把`/user/local/bin` 放到最上面

control + k：把一行字剪下來

control + y：把字貼上

control + x + s：存檔

control + x + c：關掉 emacs

修改完成重開「終端機」，讓環境變數重載，在輸入一次 `echo $PATH` 應該就可以看到修改後正確的環境變數了。

<br>

**Step 5:** 那就安裝完畢啦！最後檢查一下你下`python2.7`的時候是不是來自於`/user/local/bin`

```bash
$ which python2.7
/usr/local/bin/python2.7
```

看起來很正常，Great!

<br>

* Ubuntu

請參考[這篇](https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/) 。

**Step 1:** 先安裝一些相依套件

```bash
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

**Step 2:** 從網路上下載python2.7 source code

```bash
$ cd /usr/src
$ wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
```

**Step 3:** 解壓縮並進去資料夾

```bash
$ tar xzf Python-2.7.13.tgz
$ cd Python-2.7.13
```

**Step 4:** 依環境配置並安裝

```bash
$ sudo ./configure
$ sudo make altinstall
```

`make altinstall` 是為了避免你去取代掉預設的python在/usr/bin/python。

<br>

* Windows

**Step 1:** 在這個[網站](https://www.python.org/downloads/release/python-2713/)依照你的CPU架構下載安裝檔，並安裝。

![python_win_install_01](http://www.ycc.idv.tw/media/PlayDataWithPython/python_win_install_01.jpeg)

**Step 2:** 設定環境變數

打開 控制台 > 系統及安全性 > 系統 > 進階系統設定 > 環境變數

選Path，並按下 編輯，將`C:\Python27;C:\Python27＼Scripts` 加到後面，並儲存。環境變數的說明請參考上面Mac安裝的第四步，原理是一樣的，不過在windows裡的區分的符號是`;`不是`:`。

<br>

### IPython, Numpy, Pandas

* Mac ＆Ubuntu

**Step 1:** 安裝pip

```bash
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ python2.7 get-pip.py
```

**Step 2:** 安裝套件

```bash
$ pip2.7 install ipython
$ pip2.7 install numpy
$ pip2.7 install pandas
```

<br>

* Windows

雖然不建議在windows下開發程式，不過我還是提供一個方法，讓你在接下的文章可以正常作操作。有一個好用的軟體—Anaconda，這個軟體不只可以在windows上使用，在linux和mac都有辦法使用。

1. 安裝windows版的Anaconda(python 2.7)：[網址](https://www.continuum.io/downloads#windows)
2. 安裝結束，就已經安裝好「IPython」的程式，直接打開就可以使用。
3. 安裝Numpy和Pandas：打開「Anaconda Prompt 」，輸入

```bash
$ conda install numpy
$ conda install pandas
```

<br>

### 開啟IPython

IPython將會是未來我們這系列會用的一個介面，只要能夠開啟它，我們今天就大功告成了。

* Mac ＆Ubuntu:  在終端機輸入 `$ ipython2`


* Windows：直接打開「IPython」程式

試著import numpy和pandas進來，如果都正常，就代表成功了！

![ipython](http://www.ycc.idv.tw/media/PlayDataWithPython/ipython.jpeg)

Ctrl + D 就可以結束跳出啦～ 今天就到這～
