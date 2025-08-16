# 编程机试acm模式输入输出总结(Python)

与leetcode的核心代码模式不同，acm模式下需要自己编写输入与输出函数。

**我用这个练习**  [牛客网在线编程_算法笔面试篇_输入输出练习](https://www.nowcoder.com/exam/oj?page=1&tab=算法笔面试篇&topicId=372)

> 记住：再刷这个的时候重心要在怎么把数据读取进来，不是处理数据的逻辑，要和逻辑部分解耦合
>
> **Python 的序列解包（unpacking）**: n,m = [3,4]
>
> python 字符串反转的方法：切片 `[::-1]` 的意思是步长为 -1，从后往前取。
>
> `::` 是 **切片的扩展语法**，完整形式是：s[start : stop : step]
>
> **python 切片基础与高级用法一定要会**
>
> 对字符串矩阵转置，则用zip(), zip(*matrix)会把矩阵按行展开

序列解包的两种用法：

> **# 序列解包**
>
> \- 除了显示的序列解包，如n,m = [2,3]
>
> \- 还有一种这样的序列解包 *list, 函数调用里,它会把列表的元素拆开，当作多个独立参数传给函数。

`zip()` 会把多个可迭代对象“并行”打包成元组序列,返回的是一个迭代器，懒加载，里面的元素和外面的都是元组形式

则zip(*matrix)

>**倒序打印列表**
>
>**在列表前面插入元素**
>
>这两种优先选择**倒序打印[::-1]**,这和字符反转一样

我犯了一个错误，split()默认空格分割字符，如果字符连在一起则分不开了

> 怎么去除字符串中的空格
>
> 字符串的replace() 方法 :print(s.replace(" ", "")) 

处理浮点数很简单，读取的时候像int() 改为 float(), 这个时候输入几位小数就是几位小数

- 用字符串的方法`format()` 

- print("{:.3f}".format(float(input())))  这是自动补0 和四舍五入的
- "{[字段名]:[格式说明]}".format(值)，花括号 `{}` 内部的 `:` 是 **格式说明符的分隔符**
- 格式说明好用09就是宽度为9，不够补0

我这里有两个短板要补，一个是模运算和除运算总是搞混，一个是2进制和十进制转换代码

- 模运算%
- 除运算/
- 进制转换

python 中的π

- math.pi
- np.pi
- 自己定义的

不能用str(list) 将列表中的元素都为字符，可以用列表生成式和map()

- [str(x) for x in arr]
- list(map(str, arr))



其他几个网站练习acm模式**（我还没尝试）**：

[牛客竞赛_ACM/NOI/CSP/CCPC/ICPC算法编程高难度练习赛_牛客竞赛OJ](https://ac.nowcoder.com/acm/contest/5657#question)

[华为机试_在线编程_牛客网](https://www.nowcoder.com/exam/oj/ta?tpId=37)

[AcWing - 在线题库](https://www.acwing.com/problem/)



>**学习重点**
>
>输入：
>
>- input()：读取控制台一行的输入，将接受的数据返回为一个`string`类型
>- split()：默认以空字符为分隔符，包括空格、换行(\n)、制表符(\t)等，也可以是用‘,’ 的字符，返回是是一个**list**
>- map()：`map()`函数返回的是一个迭代器不能改变值，想要改变值还要加list(),类型转换
>
>所以我们经常用list(map(int, input().split())) 得到输入行的整数
>
>输出：
>
>- print(): 常与 ‘’.join()   搭配使用，如**print("*".join(res))**

[TOC]

## 参考文献

[Python ACM 模式下的输入输出 - 文山湖的猫 - 博客园](https://www.cnblogs.com/jfchen/p/python-acm-input-and-output.html)

## 1. 输入函数模板

### 1.1 获取输入数据（最基本的用法，input()、split()、map()）

Python输入数据主要通过`input()`函数实现，`input()`会读取控制台一行的输入，如果输入有多行的话，需要多次使用`input()`。

与Python2中不同，Python3中的`input()`会将接受的数据返回为一个`string`类型，如果一行中有多个数据的话，则需要使用`split()`进行切割。`split()`切割后返回一个列表。

因为`input()`返回的是`string`，分割后也是一个字符列表，如果输入数据是数字则需要进行类型转换。可以单个转换或是用列表批量转换，或者是使用`map()`并行转换。**`map()`函数返回的是一个迭代器，不能改变值**，如果需要改变值的话还需要转换成列表。

**note:** map()返回的迭代器对象，不会立刻把所有数据转为int,  他是惰性求值，等你迭代到的时候才去计算。迭代器内部的指针就向前走一步，所以最后就“耗尽了”。

### 1.2 三种情况的输入数据(高级用法)

情况1: 多行输入，同时未指定用例的个数

- 写上一个while True,把处理逻辑放入 这个循环里面，一般考试的使用没这种情况
- 需要加上异常捕获，当做结束信号

情况2: 多行输入， 指定用例个数

- 写一个 for _ in range(n), 这个考试里面几乎都是这一种。这种一定要掌握

情况3: 多行输入，指定某个条件退出

- while True  + if判断。好奇怪，这个不用异常捕获因为这里有结束条件
- **还可以直接用except()当做结束条件, 这可以捕获EOF**

## 2. 输出函数模板

Python3的输出主要靠`print()`函数，就是把结果打印至终端。需要对`print()`函数的`sep`和`end`两个参数有一定的了解

- `sep`
- `end`

情况1: 输出单个数字

情况2: 输出多个数字，同时要求以分隔符（sep）隔开

- 这就要用到 sep,

情况3：最终结果是一个列表

- 就是把结束符从 换行符改为空字符

**情况4: 将字符列表合成一个字符串，需要用到`join()`函数**

- 这个在考试常用
- 输出在一行很方便

## 3. 链表的输入输出

acm模式中的链表也是通过输入一个数组来模拟的，所以获取输入数据和前面没有什么不同。
主要在于定义链表结构、将输入数据转化为链表以及输出链表。
[华为机试：从单向链表中删除指定值的节点](https://www.nowcoder.com/practice/f96cd47e812842269058d483a11ced4f?tpId=37&tqId=21271&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)
[华为机试：输出单向链表中倒数第k个节点](https://www.nowcoder.com/practice/54404a78aec1435a81150f15f899417d?tpId=37&tqId=21274&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=)

## 4. 二叉树

详见参考文献。

### 4.1 完全二叉树格式输入



### 4.2 其他格式输入



## 参考博客

[ACM模式笔试编程题Python3的输入和输出格式详解](https://www.bilibili.com/read/cv15996133)
[ACM模式下链表、二叉树的输入Python实现](https://blog.csdn.net/weixin_42327752/article/details/124381258)

