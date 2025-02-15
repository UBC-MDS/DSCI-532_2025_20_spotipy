## 1. Motivation and Purpose

## 2. Description of the Data

## 3. Rsearch Questions

## 4. App Sketch and Description

[Link to the App Sketch](https://github.com/UBC-MDS/DSCI-532_2025_20_spotipy/blob/main/img/sketch.png)

This app, Spotify Top Songs, is an interactive dashboard that lets users explore trends in popular music from 2010 to 2019. 

Users can refine the songs they are shown with the filters on the left sidebar, which is collapsible. They can choose the specific year the song was released (from 2010 to 2019), and the lower and upper bounds of the song length (in seconds), the beats per minutes (in bpm), and the loudness (in decibels).

The main visualizations are on the right, which are all based on the certain year and other filters chosen and are dynamically updated. The first visualization is a scatterplot of danceability versus popularity, with a tooltip that shows song details on hover. Next, we show a list of the top six artists ranked by popularity based on the year filtered, so users can see how the artists ranking changed over time. Then, we show a pie chart of the genre popularity for the year, with a legend for clarity. Finally, we have an energy cateogires bar chart, where we group songs into low (0-33), medium (34-66), and high (67-100) energy categories, to let users see the distribution of song energy levels.