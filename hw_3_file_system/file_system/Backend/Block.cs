using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace file_system.Backend
{
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
        }

        public string getInfo()
        {
            string temp = new string(info);
            return temp;
        }
    }
}
