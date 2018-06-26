using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Collections.ObjectModel;
using System.Runtime.Serialization.Formatters.Binary;

namespace file_system
{
    public partial class MainWindows : Form
    {
        FCB root_fcb = new FCB();
        public FCB current_catalog;
        Stack<FCB> folderStack = new Stack<FCB>();
        Catalog catalog = new Catalog();
        public static BitMap bitMap = new BitMap();
        public string dir = System.IO.Path.GetDirectoryName(System.IO.Path.GetDirectoryName(Directory.GetCurrentDirectory()));
        private Dictionary<int, ListViewItem> list_table = new Dictionary<int, ListViewItem>();
        TreeNode root_node;

        public MainWindows()
        {
            InitializeComponent();
            current_catalog = root_fcb;
            folderStack.Push(current_catalog);
            InitializeWindows();
        }
        
        public void InitializeWindows()
        {
            InitializeListView();
            InitializeTreeView();
            textBox1.Text = "root\\";
        }

        public void InitializeListView()
        {
            listView1.Items.Clear();
        }

        public void InitializeTreeView()
        {
            treeView1.Nodes.Clear();
            root_node = new TreeNode("root");
            treeView1.Nodes.Add(root_node);
        }

        public void UpdateView()
        {
            UpdateTreeView();
            UpdateListView(current_catalog);
        }

        public void UpdateTreeView()
        {
            treeView1.Nodes.Clear();
            root_node = new TreeNode("root");
            nodeDFS(root_node,root_fcb);
            treeView1.Nodes.Add(root_node);
        }

        public void UpdateListView(FCB item)
        {
            list_table = new Dictionary<int, ListViewItem>();
            listView1.Items.Clear();
            if(item.son != null)
            {
                FCB son = item.son;
                do
                {
                    File temp = catalog.getFile(son);
                    ListViewItem file = new ListViewItem(new string[]
                    {
                        temp.name,
                        temp.size,
                        temp.type,
                        temp.createTime.ToString()
                });
                    if (temp.type == "folder")
                        file.ImageIndex = 0;
                    else
                        file.ImageIndex = 1;

                    listMap(temp, file);
                    listView1.Items.Add(file);
                    son = son.next;
                } while (son != null);
            }
        }

        private void nodeDFS(TreeNode node,FCB dir)
        {
            if(dir.son != null)
            {
                FCB son = dir.son;
                do
                {
                    if (son.fileType == FCB.FileType.folder)
                    {
                        TreeNode new_node = new TreeNode(son.fileName);
                        nodeDFS(new_node, son);
                        node.Nodes.Add(new_node);
                    }
                    son = son.next;
                } while(son != null);
            }
        }

        private string nameCheck(string s,string ext = "")
        {
            FCB current_dir = current_catalog.son;
            int counter = 0;
            while(current_dir != null)
            {
                string[] sArray = current_dir.fileName.Split('(');
                if (sArray[0] != current_dir.fileName && sArray[0] == s) 
                {
                    counter++;
                }
                else if (current_dir.fileName == s + ext)
                {
                    counter++;
                }
                current_dir = current_dir.next;
            }
            if(counter > 0)
                s += "(" + counter.ToString() + ")";
            return s + ext;
        }

        private void 打开ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ListViewItem current_item = new ListViewItem();
            if (listView1.SelectedItems.Count != 0 )
            {
               current_item = listView1.SelectedItems[0];
            }
            else
            {
                MessageBox.Show("Please select a item");
                return;
            }

            File current_file = catalog.getFile(getPointer(current_item));
            FCB current_fcb = catalog.getFCB(current_file);

            openClick(current_fcb, current_file);
        }

        private void openClick(FCB fcb,File file)
        {
            switch (fcb.fileType){
                case FCB.FileType.folder:
                    current_catalog = fcb;
                    folderStack.Push(fcb);
                    textBox1.Text = catalog.getFile(current_catalog).path;
                    UpdateListView(fcb);
                    break;
                case FCB.FileType.txt:
                    FileEditor fileEditor = new FileEditor(file);
                    fileEditor.Show();
                    fileEditor.CallBack = UpdateView;
                    break;
                default:
                    break;
            }
        }

        private void 文件ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            string file_name = nameCheck("New text", ".txt");
            string fatherPath;
            //Add new FCB
            FCB new_fcb = new FCB(file_name, FCB.FileType.txt);
            current_catalog.addSonItem(new_fcb);

            //Add new File
            //Build new file path
            File father = catalog.getFile(current_catalog);
            fatherPath = (father == null) ? "root" : father.path;

            File new_file = new File(new_fcb, fatherPath);
            catalog.map(new_fcb, new_file);

            UpdateListView(current_catalog);
        }

        private void 文件夹ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            string file_name = nameCheck("New folder");
            string fatherPath;
            //Add new FCB
            FCB new_fcb = new FCB(file_name, FCB.FileType.folder);
            current_catalog.addSonItem(new_fcb);

            //Add new File
            //Build new file path
            File father = catalog.getFile(current_catalog);
            fatherPath = (father == null) ? "root" : father.path;
            File new_file = new File(new_fcb, fatherPath);
            catalog.map(new_fcb, new_file);

            UpdateView();
        }

        private void 删除ToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            ListViewItem current_item = new ListViewItem();
            if (listView1.SelectedItems.Count != 0)
            {
                current_item = listView1.SelectedItems[0];
            }
            else
            {
                MessageBox.Show("Please select a item");
                return;
            }

            File current_file = catalog.getFile(getPointer(current_item));
            FCB current_fcb = catalog.getFCB(current_file);

            List<int> indexs = current_file.indexPointer.readTable();
            bitMap.withdraw(indexs);

            current_fcb.remove();
            catalog.removeFile(current_fcb);

            UpdateView();
        }

        private void 返回ToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            if (current_catalog == root_fcb)
                return;
            current_catalog = current_catalog.father;
            if(current_catalog == root_fcb)
                textBox1.Text = "root\\";
            else
                textBox1.Text = catalog.getFile(current_catalog).path;
            UpdateListView(current_catalog);
        }

        private void 格式化ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            root_fcb = new FCB();
            catalog = new Catalog();
            folderStack = new Stack<FCB>();
            bitMap = new BitMap();
            current_catalog = root_fcb;

            UpdateView();
        }

        public void listMap(File file, ListViewItem item)
        {
            list_table[file.filePointer] = item;
        }

        public ListViewItem getItem(File file)
        {
            if (list_table.ContainsKey(file.filePointer))
            {
                return list_table[file.filePointer];
            }
            else
                return null;
        }

        public int getPointer(ListViewItem item)
        {
            if (list_table.ContainsValue(item))
            {
                foreach (KeyValuePair<int, ListViewItem> kvp in list_table)
                {
                    if (kvp.Value.Equals(item))
                        return kvp.Key;
                }
                return -1;
            }
            else
            {
                MessageBox.Show("Can't get the pointer");
                return -1;
            }
        }

        private void 文件ToolStripMenuItem2_Click(object sender, EventArgs e)
        {
            string file_name = nameCheck("New text", ".txt");
            string fatherPath;
            //Add new FCB
            FCB new_fcb = new FCB(file_name, FCB.FileType.txt);
            current_catalog.addSonItem(new_fcb);

            //Add new File
            //Build new file path
            File father = catalog.getFile(current_catalog);
            fatherPath = (father == null) ? "root" : father.path;

            File new_file = new File(new_fcb, fatherPath);
            catalog.map(new_fcb, new_file);

            UpdateListView(current_catalog);
        }

        private void 文件夹ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string file_name = nameCheck("New folder");
            string fatherPath;
            //Add new FCB
            FCB new_fcb = new FCB(file_name, FCB.FileType.folder);
            current_catalog.addSonItem(new_fcb);

            //Add new File
            //Build new file path
            File father = catalog.getFile(current_catalog);
            fatherPath = (father == null) ? "root" : father.path;
            File new_file = new File(new_fcb, fatherPath);
            catalog.map(new_fcb, new_file);

            UpdateView();
        }

        private void 返回ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            if (current_catalog == root_fcb)
                return;
            current_catalog = current_catalog.father;
            if (current_catalog == root_fcb)
                textBox1.Text = "root\\";
            else
                textBox1.Text = catalog.getFile(current_catalog).path;
            UpdateListView(current_catalog);
        }

        private void 打开ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            ListViewItem current_item = new ListViewItem();
            if (listView1.SelectedItems.Count != 0)
            {
                current_item = listView1.SelectedItems[0];
            }
            else
            {
                MessageBox.Show("Please select a item");
                return;
            }

            File current_file = catalog.getFile(getPointer(current_item));
            FCB current_fcb = catalog.getFCB(current_file);

            openClick(current_fcb, current_file);
        }

        private void 删除ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            ListViewItem current_item = new ListViewItem();
            if (listView1.SelectedItems.Count != 0)
            {
                current_item = listView1.SelectedItems[0];
            }
            else
            {
                MessageBox.Show("Please select a item");
                return;
            }

            File current_file = catalog.getFile(getPointer(current_item));
            FCB current_fcb = catalog.getFCB(current_file);

            List<int> indexs = current_file.indexPointer.readTable();
            bitMap.withdraw(indexs);

            current_fcb.remove();
            catalog.removeFile(current_fcb);

            UpdateView();
        }

        private void listView_DoubleClick(object sender, EventArgs e)
        {
            ListViewItem current_item = new ListViewItem();
            if (listView1.SelectedItems.Count != 0)
            {
                current_item = listView1.SelectedItems[0];
            }
            else
            {
                MessageBox.Show("Please select a item");
                return;
            }

            File current_file = catalog.getFile(getPointer(current_item));
            FCB current_fcb = catalog.getFCB(current_file);

            openClick(current_fcb, current_file);
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void 新建ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void splitContainer2_Panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }


        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void 重命名ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ListViewItem current_item = new ListViewItem();
            if (listView1.SelectedItems.Count != 0)
            {
                current_item = listView1.SelectedItems[0];
            }
            else
            {
                MessageBox.Show("Please select a item");
                return;
            }

            File current_file = catalog.getFile(getPointer(current_item));
            FCB current_fcb = catalog.getFCB(current_file);

            InputBox inputBox = new InputBox(current_file,current_fcb);
            inputBox.Show();
            inputBox.CallBack = UpdateView;
        }

        private void contextMenuStrip1_Opening(object sender, CancelEventArgs e)
        {

        }

        private void 重命名ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            ListViewItem current_item = new ListViewItem();
            if (listView1.SelectedItems.Count != 0)
            {
                current_item = listView1.SelectedItems[0];
            }
            else
            {
                MessageBox.Show("Please select a item");
                return;
            }

            File current_file = catalog.getFile(getPointer(current_item));
            FCB current_fcb = catalog.getFCB(current_file);

            InputBox inputBox = new InputBox(current_file, current_fcb);
            inputBox.Show();
            inputBox.CallBack = UpdateView;
        }

        public void serialize()
        {
            FileStream fileStream1, fileStream2, fileStream3;
            BinaryFormatter b = new BinaryFormatter();

            fileStream1 = new FileStream(System.IO.Path.Combine(dir, "catalogTree.dat"),FileMode.Create);
            b.Serialize(fileStream1, root_fcb);
            fileStream1.Close();

            fileStream2 = new FileStream(System.IO.Path.Combine(dir, "catalogTable.dat"), FileMode.Create);
            b.Serialize(fileStream2, catalog);
            fileStream2.Close();

            fileStream3 = new FileStream(System.IO.Path.Combine(dir, "bitMap.dat"), FileMode.Create);
            b.Serialize(fileStream3, bitMap);
            fileStream3.Close();
        }

        public void deserialize()
        {
            FileStream fileStream1, fileStream2, fileStream3;
            BinaryFormatter b = new BinaryFormatter();

            fileStream1 = new FileStream(System.IO.Path.Combine(dir, "catalogTree.dat"), FileMode.Open,FileAccess.Read,FileShare.Read);
            root_fcb = b.Deserialize(fileStream1) as FCB;
            fileStream1.Close();

            fileStream2 = new FileStream(System.IO.Path.Combine(dir, "catalogTable.dat"),FileMode.Open, FileAccess.Read, FileShare.Read);
            catalog = b.Deserialize(fileStream2) as Catalog;
            fileStream2.Close();

            fileStream3 = new FileStream(System.IO.Path.Combine(dir, "bitMap.dat"),FileMode.Open, FileAccess.Read, FileShare.Read);
            bitMap = b.Deserialize(fileStream3) as BitMap;
            fileStream3.Close();
        }

        public void MainWindows_Closing(object sender, EventArgs e)
        {
            if (MessageBox.Show("Do you want to save data?", "Tips", MessageBoxButtons.YesNo) == DialogResult.Yes)
            {
                serialize();
            }
        }

        private void 加载之前数据ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            deserialize();
            UpdateView();
        }
    }
}
