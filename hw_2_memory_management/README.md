# 请求调页存储管理方式模拟

[TOC]

## 1.项目背景

### 1.1 相关背景

​	术语请求调页指的是一种动态内存分配技术，它把页面的分配推迟到不能再推迟为止，也就是说，一直推迟到进程要访问的页不在物理内存时为止，由此引起一个缺页错误。  请求调页的置换算法有FIFO（先进先出），LRU（最近最久未使用）算法等。

### 1.2 项目需求

​	编写一个程序，模拟请求调页存储管理方式，一共有320条指令，假设每个页面可以存放10条指令，分配的作业有4个内存块，模拟该作业的执行过程，采用FIFO算法或LRU算法来实现置换。

### 1.3 项目目的

- 理解页面置换的过程
- 加深对页面置换算法的理解

## 2.需求分析

### 2.1 基本需求

​	本项目的基本情况如下：

- 指令：共320条指令

- 页面：每个页面存放10条指令，即有32个页

- 内存：该作业的内存块有4块

- 指令分布：

  - 50%顺序执行
  - 25%均匀分布在前地址部分
  - 25%均匀分布在后地址部分

- 置换算法：FIFO或LRU

  

### 2.2 模拟过程

  按照需求设计程序模拟请求调页存储管理方式：

- 在模拟过程中：

  - 如果所访问指令在内存中，则显示其物理地址，并转到下一条指令
  - 如果没有在内存中，则发生缺页，此时需要记录缺页次数，并将其调入内存
  - 如果4个内存块中已装入作业，则需进行页面置换

-  所有320条指令执行完成后，计算并显示作业执行过程中发生的缺页率 

- 置换算法可以选用FIFO或者LRU算法 



### 2.3 指令访问次序

1. 在0－319条指令之间，随机选取一个起始执行指令，如序号为m
2. 顺序执行下一条指令，即序号为m+1的指令
3. 通过随机数，跳转到前地址部分0－m-1中的某个指令处，其序号为m1
4. 顺序执行下一条指令，即序号为m1+1的指令
5. 通过随机数，跳转到后地址部分m1+2~319中的某条指令处，其序号为m2
6. 顺序执行下一条指令，即m2+1处的指令。
7. 重复跳转到前地址部分、顺序执行、跳转到后地址部分、顺序执行的过程，直到执行完320条指令。

## 3.算法设计

### 3.1 页面调度

1. 当内存有空或 新访问指令所在页已在内存中，不需要页面调度算法，更新相关信息（访问顺序，访问时间等）即可
2. 当内存已满，切新访问指令所在页不在内存中，需要执行页面调度算法，可选FIFO或LRU

### 3.2 FIFO算法

FIFO算法即先进先出算法，即当发生页面置换的时候，最先进入的页最先调出，为了实现FIFO算法，我们对每一个内存块增加辅助变量`time`，用于记录访问顺序

算法思路如下：

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_2/img/1.png)

### 3.3 LRU算法

LRU算法即最近最久未使用算法，即当发生页面置换的时候，将最长时间没有使用的页调出，我们同样使用辅助变量`time`来记录访问的时间

算法思路如下：

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_2/img/2.png)



## 4.核心代码

### 4.1 内存块

使用`Block`类表示内存块

```python
# Block class
class Block:
    def __init__(self,time):
        # page of this block
        self.page  = -1
        # Accessed or not
        self.accessed = False
        # Record the access order
        self.time = time
```



### 4.2 模拟器

使用 `Simulator`内表示页面调度模拟器

```python
# Create a stimulator class
class Simulator:
    def __init__(self):
        # Create the blocks sequence
        self.blocks = [Block(4),Block(3),Block(2),Block(1)]
        # Record whether the blocks are all accessed or not
        self.accessed_all = False
        # page faults counter
        self.missing_page_counter = 0

    # Check if all the blocks are accessed
    def accessed_all_check(self):
		...

    # Access a new page
    def access_new_page(self,new_page,algorithm):
		...

```



### 4.3 调度算法

#### 4.3.1 判断内存是否已满或页面已在

```python
 replacement = True
        self.accessed_all_check()
        for i in self.blocks:
            # Check whether the blocks are not accessed
            if not self.accessed_all:
                # If already exist
                if i.page == new_page:
                    replacement = False
                    break
                elif not i.accessed:
                    i.page = new_page
                    i.accessed = True
                    replacement = False
                    break
            # Check if the new page is already in the blocks
            elif i.page == new_page:
                replacement = False
                if algorithm == 1:
                    i.time = 1
                    for j in self.blocks:
                        if not j == i:
                            j.time += 1
```

#### 4.3.2 页面置换

```python
 if replacement:
            self.missing_page_counter += 1
            # Use FIFO replacement algorithm
            if algorithm == 0:
                for i in self.blocks:
                    if i.time == 4:
                        i.page = new_page
                        i.time = 1
                        for j in self.blocks:
                            if not j == i:
                                j.time += 1
                        break

            # Use LRU replacement algorithm
            elif algorithm == 1:
                max_value = max(self.blocks[i].time for i in range(4))
                for i in self.blocks:
                    if i.time == max_value:
                        i.page = new_page
                        i.time = 1
                        for j in self.blocks:
                            if not j == i:
                                j.time += 1
                        break
            else:
                raise print("Algorithm type error!")
```

## 5.程序演示

### 5.1 界面说明

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_2/img/3.png)

- 最上方一排为四个内存块，数字内容为块内页号
- 中部为缺页次数和缺页率
- 左下侧为访问序列和对应的页号
- 右侧为控制区，可以选择页面置换算法，以及生成随机的访问序列，并选择单步前进或者是执行到最后一条在指令

### 5.2 生成访问序列

单击`Generate List`按照访问序列的生成要求随机生成，同时生成对应页号序列，每一次点击`Generate List`，块内各项信息会重置，即重新开始模拟过程

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_2/img/4.png)



### 5.3 开始模拟访问指令过程

首先选择FIFO或者LRU算法（只能二选一），点击`Single Step`单步执行，点击`Execution to End`执行到最后一条指令：

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_2/img/5.png)

## 6.附录

### 6.1 文件说明：

`page_replacement.py`为调度算法的核心python代码

`gui.py`为调度算法的gui代码

`gui.exe`为生成的可执行文件

**由于python环境问题，exe文件运行并不稳定（使用pyinstaller生成），所以使用时建议执行**`gui.py`，所需环境为：`PyQt5`

### 6.2 开发环境

- 操作系统：windows10 1803 64bit
- 语言：python 3.6
- 相关python包：PyQt5,PyQt-tools,PyUIC