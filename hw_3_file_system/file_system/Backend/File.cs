using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace file_system.Backend
{
    public class File
    {
        public string name, size, type, path;
        public DateTime createTime;
        public int filePointer;
        public IndexTable indexPointer;

        public string CreateTime
        {
            get
            {
                return createTime.ToString(System.Globalization.CultureInfo.InvariantCulture);
            }
            set
            {
                createTime = DateTime.Parse(value);
            }
        } 

        public File(string name,string size)
        {
            this.name = name;
            this.size = size;
            this.createTime = DateTime.Now;
        }

        public File(FCB item,string fatherPath = "")
        {
            name = item.fileName;
            size = "0";
            type = item.fileType.ToString();
            path = fatherPath + '/' + name;
            filePointer = item.filePointer;
            indexPointer = new IndexTable();
        }

        public File copy(FCB item)
        {
            File temp = new File(item);

        }
    }
}
