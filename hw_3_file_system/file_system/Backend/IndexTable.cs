using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
