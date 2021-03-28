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
using MusicalDice;

namespace application
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private static string defaultPath = Directory.GetCurrentDirectory();
        /// <summary>
        /// 
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show((3+3).ToString());
        }

        private void chartBrowse_Click(object sender, EventArgs e)
        {
            browseButton(diceChart, chartPath);
        }

        private void templateBrowse_Click(object sender, EventArgs e)
        {
            browseButton(templateComp, templatePath);
        }

        private void outputBrowse_Click(object sender, EventArgs e)
        {
            browseButton(output, outputPath);
        }

        private void browseButton(OpenFileDialog browser, TextBox box)
        {
            browser.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            if (browser.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    box.Text = browser.FileName;
                }
                catch (Exception ex)
                {
                    box.Text = @"<Default>";
                    MessageBox.Show("Error Reading disk:\n" + ex.Message);
                }
            }
            else
            {
                box.Text = @"<Default>";
            }
        }

        private void compGen_Click(object sender, EventArgs e)
        {
            string[] inputArgs = new string[3] { templatePath.Text, chartPath.Text, outputPath.Text };
            for (int tx = 0; tx < inputArgs.Length; tx++)
            {
                if (@inputArgs[tx].Equals(@"<Default>"))
                {
                    switch (tx)
                    {
                        case 0: // template
                            inputArgs[0] = @defaultPath + @"\startingNotes.txt";
                            break;
                        case 1:
                            inputArgs[1] = @defaultPath + @"\diceChart.txt";
                            break;
                        case 2:
                            inputArgs[2] = @defaultPath + @"\output.txt";
                            break;
                    }
                }
            }
            try
            {
                MusicalDiceGen.generateComposition(inputArgs);
                MessageBox.Show("Composition generated!");
            } catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }

        }

        private void playButton_Click(object sender, EventArgs e)
        {

        }
    }
}
