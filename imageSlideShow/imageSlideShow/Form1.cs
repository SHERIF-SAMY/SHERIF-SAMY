using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace imageSlideShow
{
    public partial class Form1 : Form
    {
        
        List<string> imagePaths = new List<string> {
            "C:\\Users\\Asus\\Desktop\\cluint of sticky\\2.png",
            "C:\\Users\\Asus\\Desktop\\cluint of sticky\\WhatsApp Image 2024-10-22 at 00.30.57_402a17d1.jpg",
            "C:\\Users\\Asus\\Desktop\\cluint of sticky\\WhatsApp Image 2024-10-22 at 19.02.22_45ae6a24.jpg",
        };

        int currentImageIndex = 0;

        public Form1()
        {
            InitializeComponent();
            LoadImage();
        }

        private void LoadImage()
        {
            if (imagePaths.Count > 0)
            {
                try
                {
                    pictureBox1.Image = Image.FromFile(imagePaths[currentImageIndex]);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error loading image: " + ex.Message);
                }
            }
        }

        private void Previous_Click(object sender, EventArgs e)
        {
            if (currentImageIndex > 0)
            {
                currentImageIndex--;
                LoadImage();
            }
            else
            {
                MessageBox.Show("No previous image.");
            }
        }

        private void Next_Click(object sender, EventArgs e)
        {
            if (currentImageIndex < imagePaths.Count - 1)
            {
                currentImageIndex++;
                LoadImage();
            }
            else
            {
                MessageBox.Show("No next image.");
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            LoadImage();
        }
    }
}
