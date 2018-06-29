# 文件系统模拟

[TOC]

## 1.项目背景

### 1.1 相关背景

文件系统是操作系统中统一管理信息资源的一种软件，管理文件的存储、检索、更新，提供安全可靠的共享和保护手段，并且方便用户使用。对于操作系统而言，文件系统是必不可少，本次项目要求实现一个模拟的文件系统。

### 1.2 项目需求

在内存中开辟一个空间作为文件存储器，在其上实现一个简单的文件系统。

退出这个文件系统时，需要该文件系统的内容保存到磁盘上，以便下次可以将其恢复到内存中来。

### 1.3 项目目的

- 熟悉文件存储空间的管理；
- 熟悉文件的物理结构、目录结构和文件操作；
- 熟悉文件系统管理实现；
- 加深对文件系统内部功能和实现过程的理解



## 2.需求分析

#### 具体技术细节:

文件存储空间管理可采取显式链接（如FAT）或者其他方法。（即自选一种方法）

空闲空间管理可采用位图或者其他方法。如果采用了位图，可将位图和FAT表合二为一。

文件目录采用多级目录结构。采用索引节点结构。目录项目中应包含：文件名、物理地址、长度等信息。

#### 文件系统提供的操作：

- 格式化
- 创建子目录
- 删除子目录
- 显示目录
- 更改当前目录
- 创建文件
- 打开文件
- 关闭文件
- 写文件
- 读文件
- 删除文件

## 3.算法设计

### 3.1 单个文件的管理

建立`File`类用于表示文件类，建立`FCB`类用于表示文件控制块类，每一个FCB对象与File对象一一对应，`FCB`类中存储着文件的名称、类型、父目录指针、兄弟FCB指针等信息，我们同过`FCB`来管理文件。

### 3.2 文件目录的组织

建立`Catalog`类表示文件目录，使用字典结构管理所有的`FCB`和`File`对象，该类可以提供`FCB`和`Flie`对象之间的互相查找和增添删除映射关系，同时利用`FCB`类中的父目录指针和兄弟指针建立起文件目录结构。

### 3.3 文件的存储管理

按照项目需求，在内存中开辟一个空间作为文件存储器，在其上实现一个简单的文件系统。

#### 3.3.1 存储单位

在内存上存储数据，建立了`Block`类作为存储数据的基本单位，每个Block可以存储16个char的数据，并且拥有设置和获得数据的接口。

#### 3.3.2 空闲空间管理

采用位图管理空闲空间，建立`BitMap`类,包含对象`bool`数组`bitMap[]`与`blocks[]`一一对应，用`bitMap`作为0-1变量模拟二进制位表示对应的`block`使用情况，0表示空闲，1表示已经分配，空闲空间的分配按照循环遍历的原则，先找到的空位先进行分配。

#### 3.3.3 物理结构

采用多级索引表管理文件存储的物理结构，建立`IndexTable`类作为主索引表,`PrimaryIndex`类作为一级索引表，`SecondaryIndex`类作为二级索引表，每一级索引表中都包含着索引数组`index[]`，利用该数组顺序记录`bitMap`分配的空闲空间索引，每一个`File`对象都包含一个索引表，用于记录该文件存储的blocks的索引。

### 3.4 内存与磁盘间的数据交互

利用C#的序列化功能，将`BitMap`,`Catalog`,`File`,`FCB`,`IndexTable`,`Block`类均声明为**Serializable**，在关闭程序时设置回调，将该文件管理系统每个类的数据序列化后分别用不同文件流存储到硬盘，再次启动程序时可以选择读取上一次的数据，即可通过反序列化将数据从硬盘读回内存中

## 4.核心代码

### 4.1 File类

```C#
namespace file_system
{
    [Serializable]
    public class File
    {
        public string name, size, type, path;
        public DateTime createTime;
        public int filePointer;
        public IndexTable indexPointer;

        public File(string name,string size)
        {
            this.name = name;
            this.size = size;
            this.createTime = DateTime.Now;
            indexPointer = new IndexTable(); 
        }

        public File(FCB item,string fatherPath = "")
        {
            name = item.fileName;
            size = "0";
            type = item.fileType.ToString();
            path = fatherPath + '\\' + name;
            filePointer = item.filePointer;
            indexPointer = new IndexTable();
            createTime = DateTime.Now;
        }
    }
}
```

### 4.2 FCB类

```c#
namespace file_system
{
    //File Control Block
    [Serializable]
    public class FCB
    {
        public enum FileType { folder, txt };

        public string fileName;
        public int filePointer;
        public FileType fileType;
        public FCB father = null, son = null, next = null, pre = null;
        public static int file_counter = 0;

        public FCB()
        {
            this.fileType = FileType.folder;
            this.filePointer = file_counter++;
        }

        public FCB(string fileName,FileType fileType)
        {
            this.fileName = fileName;
            this.fileType = fileType;
            this.filePointer = file_counter++;
        }

        public void addSonItem(FCB newItem)
        {
            if(this.son == null)
            {
                this.son = newItem;
                newItem.father = this;
            }
            else
            {
                FCB temp = this.son;
                while(temp.next != null)
                {
                    temp = temp.next;
                }
                temp.next = newItem;
                newItem.pre = temp;
            }
        }

        public void remove()
        {
            if(father != null)
            {
                father.son = next;
            }
            else if (pre != null)
            {
                pre.next = next;
            }
        }
    }
}
```

### 4.3 Catalog类

```c#
// FCB catalog
    [Serializable]
    public class Catalog
    {
        public Dictionary<int, File> file_table = new Dictionary<int, File>();
        public Dictionary<int, FCB> fcb_table = new Dictionary<int, FCB>();

        public void map(FCB item,File file)
        {
            file_table[item.filePointer] = file;
            fcb_table[item.filePointer] = item;
        }

        public File getFile(FCB item)
        {
            if (fcb_table.ContainsKey(item.filePointer))
            {
                return file_table[item.filePointer];
            }
            else
                return null;
        }

        public File getFile(int filePointer)
        {
            if (fcb_table.ContainsKey(filePointer))
            {
                return file_table[filePointer];
            }
            else
                return null;
        }

        public FCB getFCB(File file)
        {
            if (file_table.ContainsKey(file.filePointer))
            {
                return fcb_table[file.filePointer];
            }
            else
                return null;
        }

        public void removeFile(FCB item)
        {
            file_table.Remove(item.filePointer);
        }

        public void removeFCB(File file)
        {
            fcb_table.Remove(file.filePointer);
        }
    }
```

### 4.4 Block类

```c#
namespace file_system
{
    //The most basic data storage unit
    [Serializable]
    public class Block
    {
        private char[] info;
        private int length;

        public Block()
        {
            info = new char[16];
         }

        public void setInfo(string new_info)
        {
            length = (new_info.Length > 16) ? 16 : new_info.Length;
            for(int i = 0; i < length; i++)
            {
                info[i] = new_info[i];
            }
        }

        public string getInfo()
        {
            string temp = new string(info);
            return temp;
        }
    }
}

```

### 4.5 BitMap类与IndexTable类

```c#
namespace file_system
{
    //Use bitmap to manage the blocks
    [Serializable]
    public class BitMap
    {
        public static int Capcity = 100 * 100 * 100;
        private Block[] blocks = new Block[Capcity];
        private bool[] bitMap = new bool[Capcity];
        private int bitPointer = 0;

        public BitMap()
        {
            //Initialize the bitmap,all blocks are empty 
            for (int i = 0; i < Capcity; i++)
            {
                bitMap[i] = true;
            }
        }

        //Get a block's data
        public string getBlock(int i)
        {
            return blocks[i].getInfo();
        }

        //Find the first empty block and set data on it
        public int allocateBlock(string data)
        {
            bitPointer = bitPointer % Capcity;
            int tempPointer = bitPointer;
            while (true)
            {
                if (bitMap[tempPointer])
                {
                    blocks[tempPointer] = new Block();
                    blocks[tempPointer].setInfo(data);
                    bitPointer = tempPointer + 1;
                    return tempPointer;
                }
                else
                    tempPointer = (tempPointer + 1) % Capcity;
                if (tempPointer == bitPointer)
                    break;
            }
            return -1;
        }

        //Withdraw a block,set its status to empty
        public void withdraw(int index)
        {
            bitMap[index] = true;
        }

        public void withdraw(List<int> indexs)
        {
            foreach(int i in indexs)
            {
                bitMap[i] = true;
            }
        }

        //Create a index table to save the numbers of a file's block
        public IndexTable write(string data)
        {
            IndexTable table = new IndexTable();

            while (data.Count() > 16)
            {
                table.addIndex(allocateBlock(data.Substring(0, 15)));
                data = data.Remove(0, 15);
            }
            table.addIndex(allocateBlock(data));

            return table;
        }
    }
}
```

```c#
namespace file_system
{
    //Use muti-level index table to manage the physical structure
    [Serializable]
    public class IndexTable
    {
        private int[] index;
        private int indexPointer;
        private PrimaryIndex primaryIndex;
        private SecondaryIndex secondaryIndex;

        public IndexTable()
        {
            index = new int[100];
            for (int i = 0; i < 100; i++)
            {
                index[i] = -1;
            }
            indexPointer = 0;
        }

        public bool full()
        {
            return indexPointer >= 100;
        }

        public bool addIndex(int data)
        {
            if (!full())
            {
                index[indexPointer] = data;
                indexPointer++;
                if(indexPointer == 100)
                {
                    primaryIndex = new PrimaryIndex();
                }
            }
            else if (!primaryIndex.full())
            {
                primaryIndex.addIndex(data);
                if (primaryIndex.full())
                {
                    secondaryIndex = new SecondaryIndex();
                }
            }
            else if(!secondaryIndex.full())
            {
                secondaryIndex.addIndex(data);
            }
            else
            {
                return false;
            }
            return true;
        }

        public List<int> readTable()
        {
            List<int> content = new List<int>();

            for(int i = 0; i < indexPointer; i++)
            {
                content.Add(index[i]);
            }
            if(indexPointer == 100)
            {
                for(int j = 0;j < primaryIndex.indexPointer; j++)
                {
                    content.Add(primaryIndex.index[j]);
                }
            }
            if (primaryIndex != null && primaryIndex.full())
            {
                foreach (PrimaryIndex temp in secondaryIndex.index)
                {
                    for(int k = 0; k < temp.indexPointer; k++)
                    {
                        content.Add(temp.index[k]);
                    }
                }
            }

            return content;
        }
    }

    [Serializable]
    public class PrimaryIndex
    {
        public int[] index;
        public int indexPointer;

        public PrimaryIndex()
        {
            index = new int[100];
            indexPointer = 0;
        }

        public void addIndex(int data)
        {
            index[indexPointer] = data;
            indexPointer++;
        }
        
        public bool full()
        {
            return indexPointer >= 100;
        }
    }

    [Serializable]
    public class SecondaryIndex
    {
        public List<PrimaryIndex> index;
        public int indexPointer;

        public SecondaryIndex()
        {
            index = new List<PrimaryIndex>();
            index.Add(new PrimaryIndex());
            indexPointer = 0;
        }

        public bool full()
        {
            return indexPointer >= 100;
        }

        public void addIndex(int data)
        {
            PrimaryIndex temp = index[indexPointer];
            if(temp.full())
            {
                index.Add(new PrimaryIndex());
                indexPointer++;
                temp = index[indexPointer];
            }
            temp.addIndex(data);
            indexPointer++;
        }
    }
}
```

## 5.程序演示

### 5.1 界面说明

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_3_file_system/img/1.png)

上方菜单栏：（该菜单栏功能可在当前目录区域右键实现）

- 文件：
  - 新建：文件文件夹
  - 打开
  - 删除
  - 重命名
  - 加载之前数据
- 返回：返回上一级目录
- 格式化：格式化当前文件系统

地址栏会显示当前目录所在地址

左侧为文件系统树状结构，右侧为当前目录的文件视图

### 5.2 新建文件与文件夹

该文件系统具有重名查找功能，会自动用序号避免重名

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_3_file_system/img/2.png)

### 5.3 进入子文件夹

双击文件夹或选中后选择“打开”均可进入子文件夹，此时地址栏地址会变化，当前目录文件视图也会刷新

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_3_file_system/img/3.png)

### 5.4 文本文件的操作

双击文件或选中后选择“打开”均可打开文本编辑器，可以对txt文件进行编辑，关闭时系统会提示是否保存，并更新文件大小信息

![](https://github.com/Dinghow/OS_Homework/raw/master/hw_3_file_system/img/4.png)

![](G:\coding\C#\file_system\file_system\img\5.png)

### 5.5 格式化

点击格式化可以格式化当前文件系统

### 5.6 保存/读取文件系统信息

退出文件系统时会提示是否保存系统信息，点击确定后会将当前的数据序列化后存储到硬盘中，在菜单栏中可以读取本地保存的文件系统数据

## 6.附录

### 6.1 文件说明

`file_system`文件夹：文件代码

`file_system.sln`：VS项目文件

`file_system.ext`:项目的可执行文件

`README.pdf`：项目文档

### 6.2 开发环境

- 操作系统：windows10 1803 64bit

- 语言：C#
- 开发环境：Visual Studio 2017