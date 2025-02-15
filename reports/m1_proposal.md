## 1. Motivation and Purpose

## 2. Description of the Data
Our project utilizes the **Top Spotify Songs from 2010-2019** dataset published on Kaggle.  
This dataset contains **603 rows and 14 columns**, representing the **top 50 songs** on Spotify for each year during this time period.

## **Key Variables**

The dataset consists of two primary types of variables:

### **1. Song Metadata**
- `title`: Title of the track *(categorical)*.
- `artist`: Name of the artist(s) *(categorical)*.
- `genre`: Genre of the track *(categorical)*.
- `year`: The year the track reached the top 50 *(quantitative)*.

### **2. Musical and Audio Features** *(all quantitative)*  
- **Beats per Minute (BPM):** Tempo of the track.  
- **energy:** Intensity and activity level (higher = more energetic).  
- **danceability:** Suitability of the track for dancing.  
- **loudness (dB):** Sound intensity in decibels.  
- **liveness:** A "live" feel—higher values show more audience presence.  
- **valence:** Positivity of the song (higher = happier).  
- **length:** Duration of the track (in seconds).  
- **acousticness:** Degree of acoustic quality.  
- **speechiness:** The presence of spoken words.  
- **popularity:** A score representing the track's popularity.

### **Relevance to the Problem**

By analyzing these variables, this dataset provides valuable insights into Spotify's most popular tracks. It enables us to address critical questions:  
1. **What factors make songs successful?**  
   Use features like BPM, danceability, and valence to determine qualities shared by top-charting songs.  
2. **Which music genres dominated Spotify, and how have they evolved?**  
   Compare genre trends over time to understand shifts in popularity.

### **Derived Variable Plan**
We plan to create a new variable: **average metric per genre** (e.g., average BPM, valence, or popularity by genre). This will allow us to:  
- Compare differences between genres more efficiently.  
- Explore changes in genre characteristics over the decade.

---
## 3. Rsearch Questions

## 4. App Sketch and Description

[Link to the App Sketch](https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy/blob/main/img/sketch.png)

This app, Spotify Top Songs, is an interactive dashboard that lets users explore trends in popular music from 2010 to 2019. 

Users can refine the songs they are shown with the filters on the left sidebar, which is collapsible. They can choose the specific year the song was released (from 2010 to 2019), and the lower and upper bounds of the song length (in seconds), the beats per minutes (in bpm), and the loudness (in decibels).

The main visualizations are on the right, which are all based on the certain year and other filters chosen and are dynamically updated. The first visualization is a scatterplot of danceability versus popularity, with a tooltip that shows song details on hover. Next, we show a list of the top six artists ranked by popularity based on the year filtered, so users can see how the artists ranking changed over time. Then, we show a pie chart of the genre popularity for the year, with a legend for clarity. Finally, we have an energy cateogires bar chart, where we group songs into low (0-33), medium (34-66), and high (67-100) energy categories, to let users see the distribution of song energy levels.