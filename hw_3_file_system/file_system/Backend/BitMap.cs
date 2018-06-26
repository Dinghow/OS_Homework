using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
