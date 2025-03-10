## Spotify Dashboard Reflection

## Implementation since Milestone 2:

## Enhancements and Fixes: 

1. Adjust footer styles to not span full width + add cards for components + remove actions button from altair char
2. Add browser tab title
3. Modularize app.py into callbacks, selectors, and UI elements
4. Fix mismatched header size
5. Redo artist ranking section to include colour coded rank and popularity scores
6. Fix logic for artists with multiple songs by averaging score + add tooltip explanation
7. Decrease maximum brightness to make it less distracting.
8. Fixed data path to get to root from src
9. Changed scatterplot dots to be green
10. Add y-axis selection, refactor file loader, and gitignore (#88)
11. Added gitignore
12. Renamed 'data' folder to 'data_loader' for improved clarity and to eliminate confusion over folder references.
13. Updated load_data to dynamically locate the project root and ensure reliable handling of file paths.
14. Make y-axis selectable through different song atrributes
15. Change wording shown in UI
16. Update last updated message

## Features not yet implemented:

- Missing Energy Bar Chart & Genre Pie Chart
Difference: The sketch included a genre popularity pie chart and an energy level bar chart, which were not implemented.
Reason: These were likely deprioritized due to dataset constraints or a focus on danceability and popularity metrics instead.

- Filters & Interactivity
Difference: The original sketch had filters for loudness and song length, which are missing. The genre filter is now a dropdown.
Reason: Loudness and song length were removed to keep the interface clean. A dropdown for genres saves space and improves usability.


## Strengths:
Clean and Modern UI – The dark theme enhances readability and makes visualizations stand out.
User Interactivity – Sliders and dropdowns allow dynamic filtering, making trend exploration easy.
Effective Data Visualization – The scatter plot provides insights into danceability vs. popularity.
Clear Key Insights – The "Most Popular Artists in 2010" section is visually prominent.
Tooltips on Data Points – Displays song title, artist, popularity, and danceability for better context.

## Limitations:
Limited Genre Filtering – Unclear if multiple genres can be selected or if a default is applied.
No Song Preview – Users lack the ability to click on a song for more details or a sample.
BPM Range Clarity – The BPM filter does not indicate which ranges are typical for genres.

## Potential Improvements:
Search or Sorting for Artists – A search bar for artists or sorting by popularity within different genres could improve usability.
More Data Insights – Including additional metrics such as energy level, loudness could provide deeper insights into music trends.

Better Navigation for Time Periods – The current year slider works well but could benefit from an animation feature or a “Play” button to observe trends over time dynamically.
Edge Cases & Bugs – If a user selects an extreme BPM range, does it still return meaningful results? Checking for empty datasets would improve robustness.

## Deviations from the Proposal:
Comparing the final dashboard with the original sketch, here are the key differences and the reasons for the changes:
- Layout and Structure
Difference: The sketch included a genre pie chart and an energy bar chart, which are missing in the final dashboard.
Reason: These were omitted due to time constraints or implementation complexity.

- Top Artists Section
Difference: The sketch listed the top artists as plain text, while the final version uses visually appealing green-highlighted boxes.
Reason: The final design is more engaging and makes comparisons easier.

## Conclusion:
The final dashboard maintains the core ideas of the original sketch while refining usability and visual engagement. While some features like loudness, energy visualization, and additional charts were omitted, the focus on interactivity and clarity makes the dashboard effective. Future iterations could reintroduce missing elements and improve genre filtering, search functionality, and time-based navigation.
