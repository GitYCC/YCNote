Title: 實作Tensorflow (6)：Recurrent Neural Networks (RNN) and Long Short-Term Memory (LSTM)
Date: 2017-11-25 12:00
Category: AI.ML
Tags: Tensorflow
Slug: tensorflow-tutorial_6
Author: YC Chen
Illustration: tensorflow-logo.jpg
Alias: /YCNote/post/45.html
related_posts: ml-course-techniques_6,tensorflow-tutorial_2,tensorflow-tutorial_3,tensorflow-tutorial_4,tensorflow-tutorial_5



如果我們想要處理的問題是具有時序性的，該怎麼辦呢？本章將會介紹有時序性的Neurel Network。

本單元程式碼LSTM部分可於[Github](https://github.com/GitYCC/Tensorflow_Tutorial/blob/master/code/06_LSTM.py)下載。


### 概論RNN

當我們想使得Neurel Network具有時序性，我們的Neurel Network就必須有記憶的功能，然後在我不斷的輸入新資訊時，也能同時保有歷史資訊的影響，最簡單的作法就是將Output的結果保留，等到新資訊進來時，將新的資訊和舊的Output一起考量來訓練Neurel Network。

![unrolling](https://raw.githubusercontent.com/GitYCC/Tensorflow_Tutorial/master/img/TensorflowTutorial.010.jpeg)

這種將舊有資訊保留的Neurel Network統稱為Recurrent Neural Networks (RNN)，這種不斷回饋的網路可以攤開來處理，如上圖，如果我有5筆數據，拿訓練一個RNN 5個回合並做了5次更新，其實就等效於攤開來一次處理5筆數據並做1次更新，這樣的手法叫做Unrolling，我們實作上會使用Unrolling的手法來增加計算效率。

![RNN](https://raw.githubusercontent.com/GitYCC/Tensorflow_Tutorial/master/img/TensorflowTutorial.011.jpeg)

接下來來看RNN內部怎麼實現的，上圖是最簡單的RNN形式，我們將上一回產生的Output和這一回的Input一起評估出這一回的Output，詳細式子如下：

$$
o_{new}=tanh(i \times W_i + o \times W_o + B)
$$

如此一來RNN就具有時序性了，舊的歷史資料將可以被「記憶」起來，你可以把RNN的「記憶」看成是「短期記憶」，因為它只會記得上一回的Output而已。

### 梯度消失與梯度爆炸

但這種形式的RNN在實作上會遇到很大的問題，還記得第二章當中，我們有講過像是tanh這類有飽和區的函數，會造成梯度消失的問題，而我們如果使用Unrolling的觀點來看RNN，將會發現這是一個超級深的網路，Backpapagation必須一路通到t0的RNN，想當然爾，有些梯度將會消失，部分權重就更新不到了，那有一些聰明的讀者一定會想到，那就使用Relu就好啦！不過其實還有一個重要的因素造成梯度消失，同時也造成梯度爆炸。

注意喔！雖然我們使用Unrolling的觀點，把網路看成是一個Deep網路的連接，但是和之前DNN不同之處，這些RNN彼此間是共享同一組權重的，這會造成梯度消失和梯度爆炸兩個問題，在RNN的結構裡頭，一個權重會隨著時間不斷的加強影響一個單一特徵，因為不同時間之下的RNN Cell共用同一個權重，這麼一來若是權重大於1，影響將會隨時間放大到梯度爆炸，若是權重小於1，影響將會隨時間縮小到梯度消失，就像是蝴蝶效應一般，微小的差異因為回饋的機制，而不合理的放大或是消失，因此RNN的Error Surface將會崎嶇不平，這會造成我們無法穩定的找到最佳解，難以收斂。這才是RNN難以使用的重要原因，把Activation Function換成Relu不會解決問題，文獻上反而告訴我們會變更差。

解決梯度爆炸有一個聽起來很廢但廣為人們使用的方法，叫做Gradient Clipping，也就是只要在更新過程梯度超過一個值，我就切掉讓梯度維持在這個上限，這樣就不會爆炸啦，待會會講到的LSTM只能夠解決梯度消失問題，但不能解決梯度爆炸問題，因此我們還是需要Gradient Clipping方法的幫忙。

在Tensorflow怎麼做到Gradient Clipping呢？作法是這樣的，以往我們使用`optimizer.minimize(loss)`來進行更新，事實上我們可以把這一步驟拆成兩部分，第一部分計算所有參數的梯度，第二部分使用這些梯度進行更新。因此我們可以從中作梗，把gradients偷天換日一番，一開始使用`optimizer.compute_gradients(loss)`來計算出個別的梯度，然後使用`tf.clip_by_global_norm(gradients, clip_norm)`來切梯度，最後再使用`optimizer.apply_gradients`把新的梯度餵入進行更新。

### Long Short-Term Memory (LSTM)

LSTM是現今RNN的主流，它可以解決梯度消失的問題，我們先來看看結構，先預告一下，LSTM是迄今為止這系列課程當中看過最複雜的Neurel Network。

![LSTM](https://raw.githubusercontent.com/GitYCC/Tensorflow_Tutorial/master/img/TensorflowTutorial.012.jpeg)

最一開始和RNN一樣，Input會和上一回的Output一起評估一個「短期記憶」，

$$
f_m = tanh (i \times W_{mi} + o \times W_{mo} + B_m)
$$

但接下來不同於RNN直接輸出，LSTM做了一個類似於轉換成「長期記憶」的機制，「長期記憶」在這裡稱為State，State的狀態由三道門所控制，Input Gate負責控管哪些「短期記憶」可以進到「長期記憶」，Forget Gate負責調配哪一些「長期記憶」需要被遺忘，Output Gate則負責去決定需要從「長期記憶」中輸出怎樣的內容，先不要管這些Gate怎麼來，我們可以把這樣的記憶機制寫成以下的式子，假設State為$f_{state}$、Input Gate為$G_i$、Forget Gate為$G_f$和Output Gate為$G_o$。

$$
f_{state,new} = G_i \times f_m + G_f \times f_{state}
$$

$$
o_{new} = G_o \times tanh(f_{state,new})
$$

如果我們要使得上面中Gates的部分具有開關的功能的話，我們會希望Gates可以是0到1的值，0代表全關，1代表全開，sigmoid正可以幫我們做到這件事，那哪些因素會決定Gates的關閉與否呢？不妨考慮所有可能的因素，也就是所有輸入這個Cell的資訊都考慮進去，但上一回的State必須被剔除於外，因為上一回的State來決定下一個State的操作是不合理的，因此我們就可以寫下所有Gates的表示式了。

$$
G_i = Sigmoid (i \times W_{ii} + o \times W_{io} + B_i)
$$

$$
G_f = Sigmoid (i \times W_{fi} + o \times W_{fo} + B_f)
$$

$$
G_o = Sigmoid(i \times W_{oi} + o \times W_{oo} + B_o)
$$

這就是LSTM，「長期記憶」的出現可以解決掉梯度消失的問題，RNN只有「短期記憶」，所以一旦認為一個特徵不重要，經過幾回連乘，這個特徵的梯度就會消失殆盡，但是LSTM保留State，並且使用「加」的方法更新State，所以有一些重要的State得以留下來持續影響著Output，解決了梯度消失的問題。但是，不幸的LSTM還是免不了梯度爆炸，為什麼呢？如果一個特徵真的很重要，State會記住，Input也會強調，所以幾輪下來還是有可能出現爆炸的情況，這時候我們就需要Gradient Clipping的幫忙。

### 使用LSTM實作文章產生器

接下來我們來實作LSTM，目標是做一個文章產生器，我們希望機器可以不斷的根據前文猜測下一個「字母」(Letters)應該要下什麼，如此一來我只要給個開頭字母，LSTM就可以幫我腦補成一篇文章。


```python
import os
import random
import string
import zipfile
from urllib.request import urlretrieve
import time

import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.ERROR)
```


```python
LETTER_SIZE = len(string.ascii_lowercase) + 1  # [a-z] + ' '
FIRST_LETTER_ASCII = ord(string.ascii_lowercase[0])

def maybe_download(url, filename, expected_bytes):
    """Download a file if not present, and make sure it's the right size."""
    if not os.path.exists(filename):
        filename, _ = urlretrieve(url, filename)
    statinfo = os.stat(filename)
    if statinfo.st_size == expected_bytes:
        print('Found and verified %s' % filename)
    else:
        print(statinfo.st_size)
        raise Exception('Failed to verify ' + filename + '. Can you get to it with a browser?')
    return filename


def read_data(filename):
    with zipfile.ZipFile(filename) as f:
        name = f.namelist()[0]
        data = tf.compat.as_str(f.read(name))
    return data


def char2id(char):
    if char in string.ascii_lowercase:
        return ord(char) - FIRST_LETTER_ASCII + 1
    elif char == ' ':
        return 0
    else:
        print('Unexpected character: %s' % char)
        return 0


def id2char(dictid):
    if dictid > 0:
        return chr(dictid + FIRST_LETTER_ASCII - 1)
    else:
        return ' '

    
print('Downloading text8.zip')
filename = maybe_download('http://mattmahoney.net/dc/text8.zip', './text8.zip', 31344016)

print('=====')
text = read_data(filename)
print('Data size %d letters' % len(text))

print('=====')
valid_size = 1000
valid_text = text[:valid_size]
train_text = text[valid_size:]
train_size = len(train_text)
print('Train Dataset: size:', train_size, 'letters,\n  first 64:', train_text[:64])
print('Validation Dataset: size:', valid_size, 'letters,\n  first 64:', valid_text[:64])
```

```yaml
Downloading text8.zip
Found and verified ./text8.zip
=====
Data size 100000000 letters
=====
Train Dataset: size: 99999000 letters,
  first 64: ons anarchists advocate social relations based upon voluntary as
Validation Dataset: size: 1000 letters,
  first 64:  anarchism originated as a term of abuse first used against earl
```


上面操作我們建制完成了字母庫，接下來就可以產生我們訓練所需要的Batch Data，所以我們來看看究竟要產生怎樣格式的資料。

![LSTM Implement](https://raw.githubusercontent.com/GitYCC/Tensorflow_Tutorial/master/img/TensorflowTutorial.013.jpeg)

如上圖所示，有點小複雜，假設我要設計一個LSTM Model，它的Unrolling Number為3，Batch Size為2，然後遇到的字串是"abcde fghij klmno pqrst"，接下來就開始產生每個Round要用的Data，產生的結果如上圖所示，你會發現產生的Data第0軸表示的是考慮unrolling需要取樣的資料，總共應該會有(Unrolling Number+1)筆，如上圖例，共有4筆，3筆當作輸入而3筆當作Labels，中間有2筆重疊使用，另外還有一點，我們會保留最後一筆Data當作下一個回合的第一筆，這是為了不浪費使用每一個字母前後的組合。而第1軸則是餵入單一LSTM需要的資料，我們一次可以餵多組不相干的字母進去，如上圖例，Batch Size=2所以餵2個字母進去，那這些不相干的字母在取樣的時候，我們會盡量讓它平均分配在文字庫，才能確保彼此之間不相干，以增加LSTM的訓練效率和效果。

因此，先產生Batch Data吧！


```python
def characters(probabilities):
    """Turn a 1-hot encoding or a probability distribution over the possible
    characters back into its (most likely) character representation."""
    return [id2char(c) for c in np.argmax(probabilities, 1)]


def batches2string(batches):
    """Convert a sequence of batches back into their (most likely) string
    representation."""
    s = [''] * batches[0].shape[0]
    for b in batches:
        s = [''.join(x) for x in zip(s, characters(b))]
    return s


def rnn_batch_generator(text, batch_size, num_unrollings):
    text_size = len(text)

    ### initialization
    segment = text_size // batch_size
    cursors = [offset * segment for offset in range(batch_size)]

    batches = []
    batch_initial = np.zeros(shape=(batch_size, LETTER_SIZE), dtype=np.float)
    for i in range(batch_size):
        cursor = cursors[i]
        id_ = char2id(text[cursor])
        batch_initial[i][id_] = 1.0

        # move cursor
        cursors[i] = (cursors[i] + 1) % text_size

    batches.append(batch_initial)

    ### generate loop
    while True:
        batches = [batches[-1], ]
        for _ in range(num_unrollings):
            batch = np.zeros(shape=(batch_size, LETTER_SIZE), dtype=np.float)
            for i in range(batch_size):
                cursor = cursors[i]
                id_ = char2id(text[cursor])
                batch[i][id_] = 1.0

                # move cursor
                cursors[i] = (cursors[i] + 1) % text_size
            batches.append(batch)

        yield batches  # [last batch of previous batches] + [unrollings]


# demonstrate generator
batch_size = 64
num_unrollings = 10

train_batches = rnn_batch_generator(train_text, batch_size, num_unrollings)
valid_batches = rnn_batch_generator(valid_text, 1, 1)

print('*** train_batches:')
print(batches2string(next(train_batches)))
print(batches2string(next(train_batches)))
print('*** valid_batches:')
print(batches2string(next(valid_batches)))
print(batches2string(next(valid_batches)))
```

```yaml
*** train_batches:
['ons anarchi', 'when milita', 'lleria arch', ' abbeys and', 'married urr', 'hel and ric', 'y and litur', 'ay opened f', 'tion from t', 'migration t', 'new york ot', 'he boeing s', 'e listed wi', 'eber has pr', 'o be made t', 'yer who rec', 'ore signifi', 'a fierce cr', ' two six ei', 'aristotle s', 'ity can be ', ' and intrac', 'tion of the', 'dy to pass ', 'f certain d', 'at it will ', 'e convince ', 'ent told hi', 'ampaign and', 'rver side s', 'ious texts ', 'o capitaliz', 'a duplicate', 'gh ann es d', 'ine january', 'ross zero t', 'cal theorie', 'ast instanc', ' dimensiona', 'most holy m', 't s support', 'u is still ', 'e oscillati', 'o eight sub', 'of italy la', 's the tower', 'klahoma pre', 'erprise lin', 'ws becomes ', 'et in a naz', 'the fabian ', 'etchy to re', ' sharman ne', 'ised empero', 'ting in pol', 'd neo latin', 'th risky ri', 'encyclopedi', 'fense the a', 'duating fro', 'treet grid ', 'ations more', 'appeal of d', 'si have mad']
['ists advoca', 'ary governm', 'hes nationa', 'd monasteri', 'raca prince', 'chard baer ', 'rgical lang', 'for passeng', 'the nationa', 'took place ', 'ther well k', 'seven six s', 'ith a gloss', 'robably bee', 'to recogniz', 'ceived the ', 'icant than ', 'ritic of th', 'ight in sig', 's uncaused ', ' lost as in', 'cellular ic', 'e size of t', ' him a stic', 'drugs confu', ' take to co', ' the priest', 'im to name ', 'd barred at', 'standard fo', ' such as es', 'ze on the g', 'e of the or', 'd hiver one', 'y eight mar', 'the lead ch', 'es classica', 'ce the non ', 'al analysis', 'mormons bel', 't or at lea', ' disagreed ', 'ing system ', 'btypes base', 'anguages th', 'r commissio', 'ess one nin', 'nux suse li', ' the first ', 'zi concentr', ' society ne', 'elatively s', 'etworks sha', 'or hirohito', 'litical ini', 'n most of t', 'iskerdoo ri', 'ic overview', 'air compone', 'om acnm acc', ' centerline', 'e than any ', 'devotional ', 'de such dev']
*** valid_batches:
[' a']
['an']
```


定義一下待會會用到的函數。


```python
def sample_distribution(distribution):
    """Sample one element from a distribution assumed to be an array of normalized
    probabilities.
    """
    r = random.uniform(0, 1)
    s = 0
    for i in range(len(distribution)):
        s += distribution[i]
        if s >= r:
            return i
    return len(distribution) - 1


def sample(prediction):
    """Turn a (column) prediction into 1-hot encoded samples."""
    p = np.zeros(shape=[1, LETTER_SIZE], dtype=np.float)
    p[0, sample_distribution(prediction[0])] = 1.0
    return p


def logprob(predictions, labels):
    """Log-probability of the true labels in a predicted batch."""
    predictions[predictions < 1e-10] = 1e-10
    return np.sum(np.multiply(labels, -np.log(predictions))) / labels.shape[0]
```

開始建制LSTM Model。


```python
class LSTM:

    def __init__(self, n_unrollings, n_memory, n_train_batch, learning_rate=1.0):
        self.n_unrollings = n_unrollings
        self.n_memory = n_memory

        self.weights = None
        self.biases = None
        self.saved = None

        self.graph = tf.Graph()  # initialize new grap
        self.build(learning_rate, n_train_batch)  # building graph
        self.sess = tf.Session(graph=self.graph)  # create session by the graph

    def build(self, learning_rate, n_train_batch):
        with self.graph.as_default():
            ### Input
            self.train_data = list()
            for _ in range(self.n_unrollings + 1):
                self.train_data.append(
                    tf.placeholder(tf.float32, shape=[n_train_batch, LETTER_SIZE]))
            self.train_inputs = self.train_data[:self.n_unrollings]
            self.train_labels = self.train_data[1:]  # labels are inputs shifted by one time step.


            ### Optimalization
            # build neurel network structure and get their loss
            self.y_, self.loss = self.structure(
                inputs=self.train_inputs,
                labels=self.train_labels,
                n_batch=n_train_batch,
            )

            # define training operation

            self.optimizer = tf.train.AdagradOptimizer(learning_rate=learning_rate)

            # gradient clipping

            # output gradients one by one
            gradients, v = zip(*self.optimizer.compute_gradients(self.loss))
            gradients, _ = tf.clip_by_global_norm(gradients, 1.25)  # clip gradient
            # apply clipped gradients
            self.train_op = self.optimizer.apply_gradients(zip(gradients, v))

            ### Sampling and validation eval: batch 1, no unrolling.
            self.sample_input = tf.placeholder(tf.float32, shape=[1, LETTER_SIZE])

            saved_sample_output = tf.Variable(tf.zeros([1, self.n_memory]))
            saved_sample_state = tf.Variable(tf.zeros([1, self.n_memory]))
            self.reset_sample_state = tf.group(     # reset sample state operator
                saved_sample_output.assign(tf.zeros([1, self.n_memory])),
                saved_sample_state.assign(tf.zeros([1, self.n_memory])))

            sample_output, sample_state = self.lstm_cell(
                self.sample_input, saved_sample_output, saved_sample_state)
            with tf.control_dependencies([saved_sample_output.assign(sample_output),
                                          saved_sample_state.assign(sample_state)]):
                # use tf.control_dependencies to make sure 'saving' before 'prediction'

                self.sample_prediction = tf.nn.softmax(
                    tf.nn.xw_plus_b(sample_output,
                                    self.weights['classifier'],
                                    self.biases['classifier']))

            ### Initialization
            self.init_op = tf.global_variables_initializer()

    def lstm_cell(self, i, o, state):
        """"Create a LSTM cell. See e.g.: http://arxiv.org/pdf/1402.1128v1.pdf
        Note that in this formulation, we omit the various connections between the
        previous state and the gates."""
        ## Build Input Gate
        ix = self.weights['input_gate_i']
        im = self.weights['input_gate_o']
        ib = self.biases['input_gate']
        input_gate = tf.sigmoid(tf.matmul(i, ix) + tf.matmul(o, im) + ib)
        ## Build Forget Gate
        fx = self.weights['forget_gate_i']
        fm = self.weights['forget_gate_o']
        fb = self.biases['forget_gate']
        forget_gate = tf.sigmoid(tf.matmul(i, fx) + tf.matmul(o, fm) + fb)
        ## Memory
        cx = self.weights['memory_i']
        cm = self.weights['memory_o']
        cb = self.biases['memory']
        update = tf.matmul(i, cx) + tf.matmul(o, cm) + cb
        ## Update State
        state = forget_gate * state + input_gate * tf.tanh(update)
        ## Build Output Gate
        ox = self.weights['output_gate_i']
        om = self.weights['output_gate_o']
        ob = self.biases['output_gate']
        output_gate = tf.sigmoid(tf.matmul(i, ox) + tf.matmul(o, om) + ob)
        ## Ouput
        output = output_gate * tf.tanh(state)

        return output, state

    def structure(self, inputs, labels, n_batch):
        ### Variable
        if (not self.weights) or (not self.biases) or (not self.saved):
            self.weights = {
              'input_gate_i': tf.Variable(tf.truncated_normal(
                  [LETTER_SIZE, self.n_memory], -0.1, 0.1)),
              'input_gate_o': tf.Variable(tf.truncated_normal(
                  [self.n_memory, self.n_memory], -0.1, 0.1)),
              'forget_gate_i': tf.Variable(tf.truncated_normal(
                  [LETTER_SIZE, self.n_memory], -0.1, 0.1)),
              'forget_gate_o': tf.Variable(tf.truncated_normal(
                  [self.n_memory, self.n_memory], -0.1, 0.1)),
              'output_gate_i': tf.Variable(tf.truncated_normal(
                  [LETTER_SIZE, self.n_memory], -0.1, 0.1)),
              'output_gate_o': tf.Variable(tf.truncated_normal(
                  [self.n_memory, self.n_memory], -0.1, 0.1)),
              'memory_i': tf.Variable(tf.truncated_normal(
                  [LETTER_SIZE, self.n_memory], -0.1, 0.1)),
              'memory_o': tf.Variable(tf.truncated_normal(
                  [self.n_memory, self.n_memory], -0.1, 0.1)),
              'classifier': tf.Variable(tf.truncated_normal(
                  [self.n_memory, LETTER_SIZE], -0.1, 0.1)),

            }
            self.biases = {
              'input_gate': tf.Variable(tf.zeros([1, self.n_memory])),
              'forget_gate': tf.Variable(tf.zeros([1, self.n_memory])),
              'output_gate': tf.Variable(tf.zeros([1, self.n_memory])),
              'memory': tf.Variable(tf.zeros([1, self.n_memory])),
              'classifier': tf.Variable(tf.zeros([LETTER_SIZE])),
            }

        # Variables saving state across unrollings.
        saved_output = tf.Variable(tf.zeros([n_batch, self.n_memory]), trainable=False)
        saved_state = tf.Variable(tf.zeros([n_batch, self.n_memory]), trainable=False)

        ### Structure
        # Unrolled LSTM loop.
        outputs = list()
        output = saved_output
        state = saved_state
        for input_ in inputs:
            output, state = self.lstm_cell(input_, output, state)
            outputs.append(output)

        # State saving across unrollings.
        with tf.control_dependencies([saved_output.assign(output),
                                      saved_state.assign(state)]):
            # use tf.control_dependencies to make sure 'saving' before 'calculating loss'

            # Classifier
            logits = tf.nn.xw_plus_b(tf.concat(outputs, 0),
                                     self.weights['classifier'],
                                     self.biases['classifier'])
            y_ = tf.nn.softmax(logits)
            loss = tf.reduce_mean(
                    tf.nn.softmax_cross_entropy_with_logits(
                        labels=tf.concat(labels, 0), logits=logits))

        return y_, loss

    def initialize(self):
        self.weights = None
        self.biases = None
        self.sess.run(self.init_op)

    def online_fit(self, X):
        feed_dict = dict()
        for i in range(self.n_unrollings + 1):
            feed_dict[self.train_data[i]] = X[i]

        _, loss = self.sess.run([self.train_op, self.loss], feed_dict=feed_dict)
        return loss

    def perplexity(self, X):
        sum_logprob = 0
        sample_size = len(X)-1
        batch_size = X[0].shape[0]

        for i in range(batch_size):
            self.sess.run(self.reset_sample_state)
            for j in range(sample_size):
                sample_input = np.reshape(X[j][i], newshape=(1, -1))
                sample_label = np.reshape(X[j+1][i], newshape=(1, -1))
                predictions = self.sess.run(self.sample_prediction,
                                            feed_dict={self.sample_input: sample_input})
                sum_logprob += logprob(predictions, sample_label)
        perplexity = float(np.exp(sum_logprob / batch_size / sample_size))
        return perplexity

    def generate(self, c, len_generate):
        feed = np.array([[1 if id2char(i) == c else 0 for i in range(LETTER_SIZE)]])
        sentence = characters(feed)[0]
        self.sess.run(self.reset_sample_state)
        for _ in range(len_generate):
            prediction = self.sess.run(self.sample_prediction, feed_dict={self.sample_input: feed})
            feed = sample(prediction)
            sentence += characters(feed)[0]
        return sentence
```


```python
# build training batch generator
batch_generator = rnn_batch_generator(
    text=train_text,
    batch_size=batch_size,
    num_unrollings=num_unrollings,
)

# build validation data
valid_batches = rnn_batch_generator(
    text=valid_text, 
    batch_size=1, 
    num_unrollings=1,
)

valid_data = [np.array(next(valid_batches)) for _ in range(valid_size)]

# build LSTM model
model_LSTM = LSTM(
    n_unrollings=num_unrollings,
    n_memory=128,
    n_train_batch=batch_size,
    learning_rate=0.9
)

# initial model
model_LSTM.initialize()

# online training
epochs = 30
num_batchs_in_epoch = 5000
valid_freq = 5

for epoch in range(epochs):
    start_time = time.time()
    avg_loss = 0
    for _ in range(num_batchs_in_epoch):
        batch = next(batch_generator)
        loss = model_LSTM.online_fit(X=batch)
        avg_loss += loss
        
    avg_loss = avg_loss / num_batchs_in_epoch
    
    train_perplexity = model_LSTM.perplexity(batch)
    print('Epoch %d/%d: %ds loss = %6.4f, perplexity = %6.4f'
           % ( epoch+1, epochs, time.time()-start_time, avg_loss, train_perplexity))
    
    if (epoch+1) % valid_freq == 0:
        print('')
        print('=============== Validation ===============')
        print('validation perplexity = %6.4f' % (model_LSTM.perplexity(valid_data)))
        print('Generate From \'a\':  ', model_LSTM.generate(c='a', len_generate=50))
        print('Generate From \'h\':  ', model_LSTM.generate(c='h', len_generate=50))
        print('Generate From \'m\':  ', model_LSTM.generate(c='m', len_generate=50))
        print('==========================================')
        print('')
```

```yaml
    Epoch 1/30: 66s loss = 1.8249, perplexity = 5.6840
    Epoch 2/30: 64s loss = 1.5348, perplexity = 5.7269
    Epoch 3/30: 63s loss = 1.4754, perplexity = 5.7866
    Epoch 4/30: 62s loss = 1.4412, perplexity = 5.3462
    Epoch 5/30: 62s loss = 1.4246, perplexity = 5.8845
    
    =============== Validation ===============
    validation perplexity = 3.7260
    Generate From 'a':   ah plays agrestiom scattery at an experiments the a
    Generate From 'h':   ht number om one nine six three kg aid rosta franci
    Generate From 'm':   m within v like opens and solepolity ledania as was
    ==========================================
    
    Epoch 6/30: 64s loss = 1.4094, perplexity = 6.0429
    Epoch 7/30: 64s loss = 1.3954, perplexity = 5.6133
    Epoch 8/30: 63s loss = 1.3905, perplexity = 5.4791
    Epoch 9/30: 62s loss = 1.3675, perplexity = 5.7168
    Epoch 10/30: 62s loss = 1.3861, perplexity = 5.3937
    
    =============== Validation ===============
    validation perplexity = 3.5992
    Generate From 'a':   ands their hypenman sam diversion passes to rouke t
    Generate From 'h':   hash pryess the setuluply see include the grophistr
    Generate From 'm':   merhouses tourism in vertic or influence carbon min
    ==========================================
    
    Epoch 11/30: 64s loss = 1.3782, perplexity = 5.5835
    Epoch 12/30: 62s loss = 1.3802, perplexity = 6.0567
    Epoch 13/30: 62s loss = 1.3723, perplexity = 6.0672
    Epoch 14/30: 62s loss = 1.3729, perplexity = 6.4365
    Epoch 15/30: 62s loss = 1.3682, perplexity = 6.2878
    
    =============== Validation ===============
    validation perplexity = 3.7153
    Generate From 'a':   ate at decade a july uses mobe on the john press to
    Generate From 'h':   htell yullandi is u one five it naval railandly eng
    Generate From 'm':   ment theory president and much three sinit in harde
    ==========================================
    
    Epoch 16/30: 65s loss = 1.3647, perplexity = 5.5579
    Epoch 17/30: 63s loss = 1.3691, perplexity = 5.3885
    Epoch 18/30: 64s loss = 1.3535, perplexity = 6.4797
    Epoch 19/30: 63s loss = 1.3637, perplexity = 5.8126
    Epoch 20/30: 62s loss = 1.3567, perplexity = 5.9839
    
    =============== Validation ===============
    validation perplexity = 3.6210
    Generate From 'a':   ate treaty jack a golderazogon develoged civilized 
    Generate From 'h':   hyene is ricpstowed dark preferent crurts annivaril
    Generate From 'm':   mer centine all level end of a character of tracks 
    ==========================================
    
    Epoch 21/30: 65s loss = 1.3584, perplexity = 6.0557
    Epoch 22/30: 63s loss = 1.3535, perplexity = 7.0777
    Epoch 23/30: 63s loss = 1.3700, perplexity = 5.7674
    Epoch 24/30: 63s loss = 1.3609, perplexity = 6.1226
    Epoch 25/30: 64s loss = 1.3663, perplexity = 6.2711
    
    =============== Validation ===============
    validation perplexity = 3.6048
    Generate From 'a':   an vary palest in some live halleten converting to 
    Generate From 'h':   heper could use that the l bidging the five zero th
    Generate From 'm':   mer yort can the real forexanded or rather then for
    ==========================================
    
    Epoch 26/30: 66s loss = 1.3551, perplexity = 6.1640
    Epoch 27/30: 65s loss = 1.3586, perplexity = 6.3620
    Epoch 28/30: 65s loss = 1.3744, perplexity = 5.5748
    Epoch 29/30: 64s loss = 1.3634, perplexity = 6.0498
    Epoch 30/30: 63s loss = 1.3671, perplexity = 6.2313
    
    =============== Validation ===============
    validation perplexity = 3.4751
    Generate From 'a':   an one brivistrial empir thorodox to an of one city
    Generate From 'h':   ho wing two he wonders marding where never boat lit
    Generate From 'm':   mptemeignt linerical premore logical boldving on ch
    ==========================================
```

最後來產生一篇以"t"為開頭的1000字文章吧！


```python
print(model_LSTM.generate(c='t', len_generate=1000))
```

```yaml
th the oppose asia college on all of indirect i suicide upse angence and including khazool cashle with jeremp of the case hasway was catiline tribui s law can be wounds to free from an eventually locations university colid for admirum syn semition goths display the might the official up it alder stowinity name like or day elenth names and lesk external links a loons for have the genione e elevang cress leven isbn effects on cultural leave to oldincil he hokerzon blacklomen with the known resolvement of literated by college founded to families in ak urke player jain of highling fake state a first o al reason into the son then mmpt one nine three three npunt university unexal and currently amnyanipation behavion from ber and ii variety of the gupife number topan has one three zero z capital prime genary brown one nine five nine so universities country recipient the vegetables bether form the distinct de plus out as a first a johnson quicky s remain which an death to anti in panibus series
```


看得出來LSTM想表達什麼嗎，哈哈！

### Reference
* [https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/6_lstm.ipynb](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/6_lstm.ipynb)
* [http://colah.github.io/posts/2015-08-Understanding-LSTMs/](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)


