## Spotify Dashboard Reflection

## Implementation since Milestone 3:

UI/UX Improvements
- Repositioned App Title for a more balanced layout.
- Added a custom favicon to enhance branding and user experience.
- Reorganized the layout, aligning elements for a cleaner and more structured appearance.
- Locked colors to genres to maintain consistency across visualizations.

Functional Enhancements
- Improved Song Duration Filtering:
- Implemented a minimum duration check, ensuring that the min duration value does not exceed the max duration.
- Adjusted input boxes to be properly aligned.

Performance Improvements:
- Used a binary format for faster data loading. Used Feather format
- Preprocessing the data and saving it in data/processed/, so the app doesn’t do unnecessary filtering/mutations.
- Implemented caching for data preprocessing and loading.

Refined Scatter Plot (Danceability vs. Popularity):
- Set Danceability as the default y-axis attribute for more meaningful insights.
- Mapped genres to broader parent genres, making the data more informative.
- Added genre as a color scheme, helping users quickly distinguish song categories.
- Incorporated duration as a color scheme, allowing users to visually assess song length trends.
- Fixed y-axis and x-axis scaling to dynamically adjust based on min/max values for better readability.
- Moved the attribute dropdown into the scatter chart card for a more intuitive experience.

## Features not yet implemented:

- Missing Energy Bar Chart & Genre Pie Chart
The sketch included a genre popularity pie chart and an energy level bar chart, which were not implemented.
Reason: These were likely deprioritized due to dataset constraints or a focus on danceability and popularity metrics instead.

- Filters & Interactivity
The original sketch had filter for loudness which is missing. The genre filter is now a dropdown.
Reason: Loudness was removed to keep the interface clean. A dropdown for genres saves space and improves usability.


## Limitations/Corner Cases:
- Expanded Genre Breakdown: A genre-specific trend analysis can be more informative, but due to time constraints, this was postponed.
- Popularity Trends Over Time: While we show individual year insights, a time-series graph to visualize trends over multiple years is missing.

## Reflection and Future Improvements

## Strengths:
Engaging & Intuitive UI with effective contrast and minimal clutter.
Interactivity through sliders and dropdowns enhances user engagement.
Actionable Insights like highlighting top artists per year.

## Limitations & Next Steps:
Add Trend Visualization: Implement a line graph to show attribute trends over time.
Improve Genre Filtering: Allow multi-select for better genre comparison.
Optimize Performance: Use data aggregation for smoother interactions.

Overall, our dashboard effectively enables users to explore Spotify song data, but additional enhancements will make it even more insightful and performant.