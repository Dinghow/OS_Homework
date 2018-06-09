# 电梯调度

[TOC]

## 1.项目背景

某一层楼20层，有五部互联的电梯。基于线程思想，编写一个电梯调度程序。 更能描述如下：

- 每个电梯里面设置必要功能键：如数字键、关门键、开门键、上行键、下行键、报警键、当前电梯的楼层数、上升及下降状态等
- 每层楼的每部电梯门口，应该有上行和下行按钮和当前电梯状态的数码显示器
- 五部电梯门口的按钮是互联结的，即当一个电梯按钮按下去时，其他电梯的相应按钮也就同时点亮，表示也按下去了
- 所有电梯初始状态都在第一层。每个电梯如果在它的上层或者下层没有相应请求情况下，则应该在原地保持不动 
- 调度算法自行设计 

## 2.需求分析

电梯调度算法即电梯响应用户的请求来进行不同楼层间的移动，而用户的请求可以分为两类：

- 外部请求：用户在不同楼层按向上或向下键，请求电梯前来所在楼层接乘
- 内部请求：用户在电梯内部按指定楼层键，请求电梯送至相应楼层

电梯调度算法将请求分配入对应电梯的响应队列，每运行到一层楼都会检测响应队列，如果有相关响应需求，则会有开门和关门操作，没有则继续运行。

### 2.1 外部请求

对外部请求的需求如下：

1. 每一楼层可以发出两种外部请求：向上，向下，五部电梯的按钮为互联结
2. 每一次发出外部请求，根据调度算法找到最合适的电梯，将该请求加入其响应队列
3. 按下的按钮直到被响应前一直保持按下状态，得到响应后恢复初始状态

### 2.2 内部请求

对内部请求的需求如下：

1. 每一部电梯的内部请求互相独立
2. 用户在电梯内部任意时刻都可以发出请求
3. 当电梯的运行方向确定时，内部请求受外部请求限制，如用户在7楼按下向下键，进入电梯后发出的内部请求只能到7楼以下
4. 当电梯的运行方向未定时，内部请求可以为任意楼层
5. 电梯内部可以显示当前楼层，按下的按钮直到被响应前一直保持按下状态，得到响应后恢复初始状态

### 2.3 内外请求之间的关联

1. 同一部电梯可以同时接受内部请求和外部请求，且接收到的请求一定会得到响应
2. 电梯的运行方向确定时，内部请求受外部请求限制（如用户在7楼按下向下键，进入电梯后发出的内部请求只能到7楼以下）

## 3.算法设计

我们按照面向对象的思想来进行算法设计，建立电梯类`Elevator`,调度器类`Controller`，通过调度器来处理所有内、外部请求，将请求按算法分配给指定的电梯对象。

采用**多线程**的思想，每一部电梯的运行开辟一个线程，每一电梯均有内、外部请求响应队列，接受请求后加入相应队列。

### 3.1 外部请求调度算法

对于外部请求，我们根据实际生活中电梯调度算法将优先级设定如下：

1. 将要途径请求楼层，且运动方向同请求方向相同的电梯
2. 空闲状态的电梯
3. 所有电梯都处在工作状态且不满足1时，根据轮转调度法来处理请求

活动图如下：

![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/external_request_AD.png)

### 3.2 内部请求响应算法

用户发出内部请求后，首先要检测其是否满足当前电梯运行状况，若目标楼层表示的方向与当前运动方向相反，则忽略该请求，当电梯状态为空闲后，则可以响应任何内部请求（如在7楼发出向下请求，某电梯从10楼到1楼途中响应了该请求，该用户在下降途中若发出前往楼8的请求不会被响应，到达1楼后则可以发出该请求）

活动图如下：

![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/internal_request_AD.png)

### 3.3 响应队列的处理算法

电梯类设置属性`direction`,`destination`，分别用于表示当前电梯的运动方向和最终目的地，通过这两个属性来控制电梯的运动，每次有新的请求加入响应队列后都会对两属性进行更新：

#### 3.3.1 加入新的外部请求

- 电梯处于运行状态：

  - 加入的外部请求为满足顺路且同向：不改变`direction`,`destination`
  - 加入的外部请求为轮转调度安排:设置专门的属性`rotateDes`保存该请求，待电梯处于空闲状态后令`destination=rotateDes`，并计算新的`direction`

- 电梯处于空闲状态：

  ​	`destination`即为请求的楼层，根据当前楼层和目标楼层可以计算`direction`

#### 3.3.2 加入新的内部请求

- 电梯处于运行状态：

  ​	若新的内部请求楼层在同方向上更远，则更新`destination`

- 电梯处于空闲状态：

  ​	`destination`即为请求的楼层，根据当前楼层和目标楼层可以计算`direction`

电梯在`direction`方向上每次运动一个楼层，每到一个楼层后就检测内外响应队列是否有该楼层的请求：

- 有：执行开门关门操作，并将请求清除，表示得到响应
- 无：继续执行电梯运动

## 4.核心代码

### 4.1 电梯类

```python
class Elevator(object):
    def __init__(self):
        self.internal_request = [0 for _ in range(20)]
        self.external_request = [0 for _ in range(20)]
        # 1 means running,0 means vacancy
        self.status = 0
        # 1 means up,-1 means down,0 means vacancy
        self.direction = 0
        self.current_floor = 1
        self.destination = 1
        # Used for round-robin schedule
        self.isRotated = 0
        self.rotateDes = 0

    def set_internal(self, f):
        self.internal_request[int(f-1)] = 1

    def set_external(self, f, direction):
        if direction == 1:
            self.external_request[int(f-1)] = 1
        elif direction == -1:
            self.external_request[int(f-1)] = -1

    def update_direction(self):
        if self.destination == self.current_floor:
            self.direction = 0
            self.status = 0
        else:
            self.direction = (self.destination - self.current_floor)/abs(self.destination - self.current_floor)
            self.status = 1

    def update_destination(self, floor):
        # if the distance between new request and current floor is further than that now,update the destination value
        if abs(floor - self.current_floor) > abs(self.destination - self.current_floor):
            self.destination = floor

    def check_internal(self, floor):
        # if the direction of new internal request is opposite of elevator direction,the request won't be responded
        i_direction = (floor - self.current_floor)/abs(floor - self.current_floor)
        if i_direction*self.direction < 0:
            return False
        return True

    # Judge whether to open the door at each floor
    def check_open(self):
        if self.internal_request[int(self.current_floor - 1)] == 1:
            time.sleep(0.5)
            self.internal_request[int(self.current_floor - 1)] = 0
        if abs(self.external_request[int(self.current_floor - 1)]) == 1:
            time.sleep(0.5)
            self.external_request[int(self.current_floor - 1)] = 0

    def run(self):
        while True:
            self.update_direction()
            if not self.direction == 0:
                self.current_floor += self.direction
                self.check_open()
            elif not self.isRotated == 0:
                self.destination = self.rotateDes
                self.isRotated = 0
            time.sleep(0.5)
```

### 4.2 调度器类

```python
class Controller(object):
    def __init__(self):
        self.elevator1 = Elevator()
        self.elevator2 = Elevator()
        self.elevator3 = Elevator()
        self.elevator4 = Elevator()
        self.elevator5 = Elevator()

    # flag:0: internal request,1: external request,ele_num: number of elevator requesting
    # floor: request floor,direction: direction of external request
    def dispatch(self, flag, ele_num, floor, direction):
        # Internal request
        if flag == 0:
            if ele_num == 1:
                if self.elevator1.check_internal(floor):
                    self.elevator1.set_internal(floor)
                    self.elevator1.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 2:
                if self.elevator2.check_internal(floor):
                    self.elevator2.set_internal(floor)
                    self.elevator2.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 3:
                if self.elevator3.check_internal(floor):
                    self.elevator3.set_internal(floor)
                    self.elevator3.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 4:
                if self.elevator4.check_internal(floor):
                    self.elevator4.set_internal(floor)
                    self.elevator4.update_destination(floor)
                else:
                    print("Internal request error!")
            elif ele_num == 5:
                if self.elevator5.check_internal(floor):
                    self.elevator5.set_internal(floor)
                    self.elevator5.update_destination(floor)
                else:
                    print("Internal request error!")
            else:
                raise print("Ele_num error!")
        # External request order
        elif flag == 1:
            if not self.find_nearest(floor, direction):
                if not self.find_vacant(floor, direction):
                    self.find_rotate(floor, direction)
        else:
            raise print("Request type error!")
 	#Find the nearest elevator who satisfies direction requirement
    def find_nearest(self, floor, direction):
        distance = [0 for _ in range(5)]
        # Calculate the distance between each elevator and destination,100 means
        # the elevator is not running closer to destination
        if min(self.elevator1.current_floor, self.elevator1.destination) < floor \
                < max(self.elevator1.current_floor, self.elevator1.destination) and \
                self.elevator1.direction == direction:
            distance[0] = abs(self.elevator1.current_floor - floor)
        else:
            distance[0] = 100

        if min(self.elevator2.current_floor, self.elevator2.destination) < floor \
                < max(self.elevator2.current_floor, self.elevator2.destination) and \
                self.elevator2.direction == direction:
            distance[1] = abs(self.elevator2.current_floor - floor)
        else:
            distance[1] = 100

        if min(self.elevator3.current_floor, self.elevator3.destination) < floor \
                < max(self.elevator3.current_floor, self.elevator3.destination) and \
                self.elevator3.direction == direction:
            distance[2] = abs(self.elevator3.current_floor - floor)
        else:
            distance[2] = 100

        if min(self.elevator4.current_floor, self.elevator4.destination) < floor \
                < max(self.elevator4.current_floor, self.elevator4.destination) and \
                self.elevator4.direction == direction:
            distance[3] = abs(self.elevator4.current_floor - floor)
        else:
            distance[3] = 100

        if min(self.elevator5.current_floor, self.elevator5.destination) < floor \
                < max(self.elevator5.current_floor, self.elevator5.destination) and \
                self.elevator5.direction == direction:
            distance[4] = abs(self.elevator5.current_floor - floor)
        else:
            distance[4] = 100

        # Find the minimum distance
        min_dis = min(distance)
        if min_dis == 100:
            return False
        else:
            min_index = distance.index(min_dis) + 1
            if min_index == 1:
                self.elevator1.set_external(floor, direction)
            elif min_index == 2:
                self.elevator2.set_external(floor, direction)
            elif min_index == 3:
                self.elevator3.set_external(floor, direction)
            elif min_index == 4:
                self.elevator4.set_external(floor, direction)
            elif min_index == 5:
                self.elevator5.set_external(floor, direction)
            return True
        
	#Find the vacant elevator
    def find_vacant(self, floor, direction):
        # Based on numerical order,find the first vacant elevator
        if self.elevator1.status == 0:
            self.elevator1.set_external(floor, direction)
            self.elevator1.status = 1
            self.elevator1.destination = floor
            return True
        elif self.elevator2.status == 0:
            self.elevator2.set_external(floor, direction)
            self.elevator2.status = 1
            self.elevator2.destination = floor
            return True
        elif self.elevator3.status == 0:
            self.elevator3.set_external(floor, direction)
            self.elevator3.status = 1
            self.elevator3.destination = floor
            return True
        elif self.elevator4.status == 0:
            self.elevator4.set_external(floor, direction)
            self.elevator4.status = 1
            self.elevator4.destination = floor
            return True
        elif self.elevator5.status == 0:
            self.elevator5.set_external(floor, direction)
            self.elevator5.status = 1
            self.elevator5.destination = floor
            return True
        else:
            return False

    # Use round-robin schedule
    def find_rotate(self, floor, direction):
        if self.elevator1.isRotated == 0:
            self.elevator1.isRotated = 1
            self.elevator1.rotateDes = floor
            self.elevator1.external_request[int(floor - 1)] = direction
        elif self.elevator2.isRotated == 0:
            self.elevator2.isRotated = 1
            self.elevator2.rotateDes = floor
            self.elevator2.external_request[int(floor - 1)] = direction
        elif self.elevator3.isRotated == 0:
            self.elevator3.isRotated = 1
            self.elevator3.rotateDes = floor
            self.elevator3.external_request[int(floor - 1)] = direction
        elif self.elevator4.isRotated == 0:
            self.elevator4.isRotated = 1
            self.elevator4.rotateDes = floor
            self.elevator4.external_request[int(floor - 1)] = direction
        elif self.elevator5.isRotated == 0:
            self.elevator5.isRotated = 1
            self.elevator5.rotateDes = floor
            self.elevator5.external_request[int(floor - 1)] = direction
        else:
            print("Can't respond this request!")
```

### 4.3 多线程说明

```python
 	# 建立Controller类对象
    controller = Controller()
    # t0线程执行GUI的监控函数，确保GUI实时反映实际情况
    t0 = Thread(target=ui.status_monitor, args=())
    # t1-t5依次为5部电梯的线程
    t1 = Thread(target=controller.elevator1.run, args=())
    t2 = Thread(target=controller.elevator2.run, args=())
    t3 = Thread(target=controller.elevator3.run, args=())
    t4 = Thread(target=controller.elevator4.run, args=())
    t5 = Thread(target=controller.elevator5.run, args=())
    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
```



## 5.程序演示

### 5.1 界面说明

![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/gui_1.png)

左侧区域为电梯1-5内部面板，按钮分别表示发出1-20层的内部请求，数字控件显示当前楼层

右侧区域的左半部分为1-20成发出向上、向下外部请求的按钮，右半部分表示5部电梯的运行状况

### 5.2 功能演示

#### 5.2.1 外部请求响应

1. 优先响应顺路的情况（将电梯1置于15层，发出前往1楼的内部请求，同时在5楼发出向下请求，可以看到由电梯1进行响应，其余电梯保持空闲状态）：

![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/gui_4.png)

2. 无顺路电梯则调用空闲电梯（楼层15、16发出向下请求，电梯1、2分别对其响应）：

   ![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/gui_5.png)

3. 所有电梯均在运行，且不满足顺路条件，采用轮转调度法（电梯1-5均在向下运动，此时高楼层发出向上请求，则首先轮转至电梯1响应，将该请求加入等待队列，运行至目的地后再上行响应用户请求）

   ![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/gui_6.png)

   ![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/gui_7.png)

   

#### 5.2.2 内部请求响应

   运动状态下可以响应同方向的任意请求

![](https://github.com/Dinghow/OS_Homework/tree/master/hw_1/img/gui_8.png)

​	空闲状态下可以响应所有请求：

​	![](G:\coding\Python\elevator\img\gui_9.png)

## 6.附录

### 6.1 文件说明：

`eleavtor_algo.py`为调度算法的核心python代码

`elevator_gui.py`为调度算法的gui代码

`elevator_gui.exe`为生成的可执行文件

**由于python环境问题，exe文件运行并不稳定（使用pyinstaller生成），所以使用时建议执行**`elevator_gui.py`，所需环境为：`PyQt5`

### 6.2 开发环境

- 操作系统：windows10 1803 64bit
- 语言：python 3.6
- 相关python包：PyQt5,PyQt-tools,PyUIC