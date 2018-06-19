using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace file_system.Backend
{
    public class BitMap
    {
        public static int Capcity = 10240;
        private Block[] blocks = new Block[Capcity];
        private bool[] bitMap = new bool[Capcity];
        private int bitPointer = 0;

        public BitMap()
        {
            for (int i = 0; i < Capcity; i++)
            {
                bitMap[i] = true;
            }
        }

        public string getBlock(int i)
        {
            return blocks[i].getInfo();
        }

        public int allocate(string data)
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
                    return bitPointer;
                }
                else
                    tempPointer = (tempPointer + 1) % Capcity;
                if (tempPointer == bitPointer)
                    break;
            }
            return -1;
        }

        public void withdraw(int index)
        {
            bitMap[index] = true;
        }
    }
}
