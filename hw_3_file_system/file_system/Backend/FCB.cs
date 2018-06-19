using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace file_system.Backend
{
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

        public FCB copy()
        {

        }
    }
}
