using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
