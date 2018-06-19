using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace file_system.Backend
{
    public class Catalog
    {
        private Dictionary<int, File> file_table = new Dictionary<int, File>();
        private Dictionary<int, FCB> fcb_table = new Dictionary<int, FCB>();

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
}
