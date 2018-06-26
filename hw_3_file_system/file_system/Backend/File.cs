using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
