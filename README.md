# Spotipy Dashboard  

Spotipy is an interactive dashboard tailored for music labels and professionals, such as A&R (Artists & Repertoire) executives, to help them make informed decisions about artists to sign and the musical elements driving commercial success. By analyzing Spotify's top-charting songs from 2010 to 2019, Spotipy provides powerful visualizations and insights on emerging trends, hit song characteristics, and more.

---

## For Dashboard Users

### **Project Motivation**
Spotify has reshaped the music industry, but professionals often struggle to make sense of the massive data available, such as artist popularity, audio features, and genre trends. The Spotipy Dashboard solves this problem by providing an intuitive platform to explore Spotify's top-charting songs and gain insights essential for data-driven decision-making.

### **Key Features**  
- **Top Artist Exploration**: Identify the most popular artists for each year between 2010–2019 and analyze patterns in artist dominance.  
- **Musical Trends Analysis**: Explore important characteristics such as danceability, energy, BPM, and valence to reveal what makes tracks successful.  
- **Genre Trends and Evolution**: Visualize how music genres have evolved over the years, highlighting stand-out genres and emerging sub-genres.  
- **Interactive Visualizations**: User-friendly, dynamic elements like dropdown filters for years, genres, and audio attributes to personalize the experience.  
- **Professional Decision-Support**: Gain actionable insights into rising stars and music trends to support business strategies.  

---

### **Deployed App**
Try out the Spotipy Dashboard here: [Spotipy Dashboard](https://dsci-532-2025-20-spotipy.onrender.com)

---

### **Demo**
<a href="https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy/blob/main/img/demo.gif">
    <img src="img/play.png" alt="Spotipy Demo" width="40">
</a>
<div>Click the play button above to view the demo.</div>


---

### **Need Help?**
If you have questions or encounter issues:  
- **Open an Issue:** [GitHub Issues](https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy/issues)  
- **Contact Us:** Reach out via the repository issues page above.

---

## For Developers and Contributors  

We welcome contributions to enhance and expand Spotipy! Here’s how you can set up the project locally and get started.

### **Get Started**  

#### 1. Clone the Repository:  
```bash
git clone https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy.git
cd DSCI-532_2025_20_spotipy  
```

#### 2. Set Up the Environment:  
Use the `environment.yml` file to set up a Conda environment:  
```bash
conda env create -f environment.yml
conda activate 532_project
```

#### 3. Run the Dashboard  
Execute the `app.py` file to launch the Spotipy dashboard:  
```bash
python src/app.py  
```  

#### 4. View the Dashboard:  
Once the app is running, open your browser and visit [http://127.0.0.1:8050/](http://127.0.0.1:8050/).  

---

### **Contributing**

We welcome all contributions, whether they’re minor fixes or new features! Follow these steps to contribute:

1. **Fork This Repository**:  
   Create your own copy of the repository by clicking on the "Fork" button.  
  
2. **Create a New Branch**:  
   Use a descriptive branch name for your feature or fix:  
   ```bash
   git checkout -b feature_branch_name  
   ```

3. **Make Your Changes**:  
   Commit your updates with a helpful commit message:  
   ```bash
   git commit -m "Explain your fixes or feature"  
   ```

4. **Push Your Changes**:  
   Push your branch to your fork:  
   ```bash
   git push origin feature_branch_name  
   ```

5. **Open a Pull Request**:  
   Submit a Pull Request (PR) from your forked branch to the main repository for review.

For more details, refer to our [Contributing Guide](https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy/blob/main/CONTRIBUTING.md).  

---

## Why Contribute?
- Help professionals in the music industry make better sense of Spotify data.
- Collaborate with others passionate about data visualization and music.
- Expand the dashboard’s features and promote innovation.  

---

## License  
This project is licensed under the MIT License - see the [LICENSE](https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy/blob/main/LICENSE) file for details.

---