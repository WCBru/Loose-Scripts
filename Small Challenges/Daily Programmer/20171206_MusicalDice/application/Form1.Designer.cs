namespace application
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.templateBrowse = new System.Windows.Forms.Button();
            this.title = new System.Windows.Forms.Label();
            this.templateLabel = new System.Windows.Forms.Label();
            this.templatePath = new System.Windows.Forms.TextBox();
            this.templateComp = new System.Windows.Forms.OpenFileDialog();
            this.diceLabel = new System.Windows.Forms.Label();
            this.chartPath = new System.Windows.Forms.TextBox();
            this.chartBrowse = new System.Windows.Forms.Button();
            this.diceChart = new System.Windows.Forms.OpenFileDialog();
            this.outputBrowse = new System.Windows.Forms.Button();
            this.outputPath = new System.Windows.Forms.TextBox();
            this.outputLabel = new System.Windows.Forms.Label();
            this.output = new System.Windows.Forms.OpenFileDialog();
            this.compGen = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // templateBrowse
            // 
            this.templateBrowse.Location = new System.Drawing.Point(380, 43);
            this.templateBrowse.Name = "templateBrowse";
            this.templateBrowse.Size = new System.Drawing.Size(75, 26);
            this.templateBrowse.TabIndex = 0;
            this.templateBrowse.Text = "Browse";
            this.templateBrowse.UseVisualStyleBackColor = true;
            this.templateBrowse.Click += new System.EventHandler(this.templateBrowse_Click);
            // 
            // title
            // 
            this.title.AutoSize = true;
            this.title.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F);
            this.title.Location = new System.Drawing.Point(148, 9);
            this.title.Name = "title";
            this.title.Size = new System.Drawing.Size(215, 25);
            this.title.TabIndex = 1;
            this.title.Text = "Musical Dice Generator";
            // 
            // templateLabel
            // 
            this.templateLabel.AutoSize = true;
            this.templateLabel.Location = new System.Drawing.Point(12, 50);
            this.templateLabel.Name = "templateLabel";
            this.templateLabel.Size = new System.Drawing.Size(111, 13);
            this.templateLabel.TabIndex = 2;
            this.templateLabel.Text = "Template Composition";
            // 
            // templatePath
            // 
            this.templatePath.Location = new System.Drawing.Point(129, 46);
            this.templatePath.Name = "templatePath";
            this.templatePath.Size = new System.Drawing.Size(244, 20);
            this.templatePath.TabIndex = 3;
            this.templatePath.Text = "<Default>";
            // 
            // diceLabel
            // 
            this.diceLabel.AutoSize = true;
            this.diceLabel.Location = new System.Drawing.Point(12, 81);
            this.diceLabel.Name = "diceLabel";
            this.diceLabel.Size = new System.Drawing.Size(57, 13);
            this.diceLabel.TabIndex = 4;
            this.diceLabel.Text = "Dice Chart";
            // 
            // chartPath
            // 
            this.chartPath.Location = new System.Drawing.Point(129, 77);
            this.chartPath.Name = "chartPath";
            this.chartPath.Size = new System.Drawing.Size(244, 20);
            this.chartPath.TabIndex = 5;
            this.chartPath.Text = "<Default>";
            // 
            // chartBrowse
            // 
            this.chartBrowse.Location = new System.Drawing.Point(380, 76);
            this.chartBrowse.Name = "chartBrowse";
            this.chartBrowse.Size = new System.Drawing.Size(75, 23);
            this.chartBrowse.TabIndex = 6;
            this.chartBrowse.Text = "Browse";
            this.chartBrowse.UseVisualStyleBackColor = true;
            this.chartBrowse.Click += new System.EventHandler(this.chartBrowse_Click);
            // 
            // outputBrowse
            // 
            this.outputBrowse.Location = new System.Drawing.Point(380, 107);
            this.outputBrowse.Name = "outputBrowse";
            this.outputBrowse.Size = new System.Drawing.Size(75, 23);
            this.outputBrowse.TabIndex = 9;
            this.outputBrowse.Text = "Browse";
            this.outputBrowse.UseVisualStyleBackColor = true;
            this.outputBrowse.Click += new System.EventHandler(this.outputBrowse_Click);
            // 
            // outputPath
            // 
            this.outputPath.Location = new System.Drawing.Point(129, 108);
            this.outputPath.Name = "outputPath";
            this.outputPath.Size = new System.Drawing.Size(244, 20);
            this.outputPath.TabIndex = 8;
            this.outputPath.Text = "<Default>";
            // 
            // outputLabel
            // 
            this.outputLabel.AutoSize = true;
            this.outputLabel.Location = new System.Drawing.Point(12, 112);
            this.outputLabel.Name = "outputLabel";
            this.outputLabel.Size = new System.Drawing.Size(58, 13);
            this.outputLabel.TabIndex = 7;
            this.outputLabel.Text = "Output File";
            // 
            // compGen
            // 
            this.compGen.Cursor = System.Windows.Forms.Cursors.Default;
            this.compGen.Location = new System.Drawing.Point(199, 137);
            this.compGen.Name = "compGen";
            this.compGen.Size = new System.Drawing.Size(120, 23);
            this.compGen.TabIndex = 10;
            this.compGen.Text = "Generate Composition";
            this.compGen.UseVisualStyleBackColor = true;
            this.compGen.Click += new System.EventHandler(this.compGen_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(467, 172);
            this.Controls.Add(this.compGen);
            this.Controls.Add(this.outputBrowse);
            this.Controls.Add(this.outputPath);
            this.Controls.Add(this.outputLabel);
            this.Controls.Add(this.chartBrowse);
            this.Controls.Add(this.chartPath);
            this.Controls.Add(this.diceLabel);
            this.Controls.Add(this.templatePath);
            this.Controls.Add(this.templateLabel);
            this.Controls.Add(this.title);
            this.Controls.Add(this.templateBrowse);
            this.Name = "Form1";
            this.Text = "Musical Dice Generator";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button templateBrowse;
        private System.Windows.Forms.Label title;
        private System.Windows.Forms.Label templateLabel;
        private System.Windows.Forms.TextBox templatePath;
        private System.Windows.Forms.OpenFileDialog templateComp;
        private System.Windows.Forms.Label diceLabel;
        private System.Windows.Forms.TextBox chartPath;
        private System.Windows.Forms.Button chartBrowse;
        private System.Windows.Forms.OpenFileDialog diceChart;
        private System.Windows.Forms.Button outputBrowse;
        private System.Windows.Forms.TextBox outputPath;
        private System.Windows.Forms.Label outputLabel;
        private System.Windows.Forms.OpenFileDialog output;
        private System.Windows.Forms.Button compGen;
    }
}

