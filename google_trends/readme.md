# Google Trends Dashboard 

## Overview

This Google Trends Dashboard provides a comprehensive analysis of search interest for key data-related job roles, including **Data Analyst**, **Data Scientist**, **Business Analyst**, **AI Engineer**, and **BI Developer**. This project leverages Google Trends data to visualize search trends over time, across regions, and by related keywords, providing insights into the popularity and demand for these roles.

This dashboard is a reflection of my learning and growth in data analytics, showcasing my ability to collect, process, and visualize data to uncover meaningful trends. It’s designed for anyone interested in understanding job market trends, including aspiring data professionals, recruiters, and analysts.

## Purpose

As a part of my data analytics journey, I wanted to understand the demand for various data-related roles and how public interest in these roles has evolved over time. By building this dashboard, I aimed to:
- Practice extracting and analyzing real-time data using APIs.
- Develop skills in data visualization and interpretation using Power BI.
- Gain insights into the job market to guide my career path in data analytics.

## Features

1. **Search Interest Over Time**:
   - Visualize the search interest for each role over a specified time period.
   - Compare trends for multiple roles on a single graph.
   - Example: The dashboard shows a peak in search interest for Data Analyst around Q1 2025, with 1922 searches on March 19, 2025.

2. **Regional Interest**:
   - Analyze search interest by country.
   - Example: The dashboard highlights countries like Hungary, India, Indonesia, Iran, Ireland, Israel, Italy, and Japan, showing Data Analyst as the most searched term at 42.3%.

3. **Keyword Comparison**:
   - Compare the total search volume for each role.
   - Example: Data Analyst has 6158 searches, while Business Analyst has 7349 searches over a longer period.

4. **Rising and Top Keywords**:
   - Identify rising keywords (e.g., "Cognizant," "data analyst," "Employment") and top keywords (e.g., "Analyst," "Course," "Job") associated with each role.
   - Example: "data analyst" has 1,900 searches, and "Cognizant" is a rising keyword with 100 searches.

5. **Real-Time Data with SerpApi**:
   - Fetch real-time search data from Google Trends using SerpApi.
   - Example: The dashboard shows 27K total searches over the last 7 days, with a breakdown by day (e.g., March 18 to March 25).

6. **Customizable Parameters**:
   - Edit parameters to filter by specific keywords, regions, and timeframes.
   - Example: The dashboard allows filtering for "Data Analyst" as the main keyword, with related keywords like "Data Scientist" and "Business Analyst."

## Live Dashboard

You can interact with the live dashboard on Power BI by clicking the link below:

[Google Trends Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNzdlNTAyOWYtNjJhZi00YTkyLWI5ZGUtZmE3M2Y4ZmM2ZDQyIiwidCI6ImQ5MGEwYWU5LWJiMzUtNDVjMi1iOWQzLWM5MmIzM2YyZDI0MiJ9)


## How to Use the Dashboard

1. **Navigate Tabs**:
   - Use the tabs at the bottom (e.g., `overview`, `keyword_by_date`, `real_time_data`, `rising_top_keyword`) to switch between different views.
   - Example: The `keyword_by_date` tab shows historical trends, while `real_time_data` focuses on the last 7 days.

2. **Edit Parameters**:
   - Click on the "Edit Parameters" button to customize the keywords, regions, and timeframes for analysis.
   - Example: You can filter for "Data Analyst" and related keywords like "Data Scientist" and "Business Analyst."

3. **Track Keyword Performance**:
   - Use the "Track keyword performance by Date" button to monitor how specific keywords perform over time.
   - Example: Track the performance of "Data Analyst" over the last 7 days.

4. **Interpret the Data**:
   - **Search Interest Over Time**: Higher peaks indicate greater interest in a role at a specific time.
   - **Regional Interest**: Identify which countries are most interested in specific roles.
   - **Rising Keywords**: Spot emerging trends or companies (e.g., "Cognizant" as a rising keyword).
   - **Top Keywords**: Understand the most common search terms associated with each role.

## Data Interpretation

- **Search Volume**:
  - The dashboard shows a total of 27K searches for all roles over the last 7 days, with Data Analyst leading in regional interest at 42.3%.
  - Over a longer period, Business Analyst has the highest search volume at 7349, followed by Data Analyst at 6158.

- **Trends**:
  - Data Analyst and Business Analyst show consistent interest over time, with peaks around Q1 2025.
  - AI Engineer and BI Developer have lower search volumes (360 and 216, respectively), indicating less public interest compared to other roles.

- **Rising Keywords**:
  - Keywords like "Cognizant," "data analyst," and "Employment" are gaining traction, suggesting growing interest in specific companies or job opportunities.

- **Top Keywords**:
  - Common search terms include "Analyst," "Course," and "Job," indicating that users are often looking for educational resources or job opportunities in these fields.

## Technical Details

- **Data Source**: The dashboard fetches data from Google Trends using SerpApi, a powerful API for scraping real-time search data.
- **SerpApi Integration**:
  - I connected the dashboard to SerpApi to retrieve real-time Google Trends data, enabling up-to-date insights into search trends.
  - Example: The `real_time_data` tab uses SerpApi to display search volumes for the last 7 days, such as 27K total searches from March 18 to March 25, 2025.
- **Visualization Tool**: The dashboard is developed using **Power BI**, a business intelligence platform that allows for interactive data visualization and analysis.

## Requirements

- **SerpApi Account**: An active SerpApi account and API key are required to fetch real-time Google Trends data.
- **Power BI**: The dashboard is built using Power BI, so you’ll need access to Power BI Desktop or Power BI Service to view or edit the dashboard.
- **Internet Connection**: Required to fetch real-time data via SerpApi and refresh the dashboard in Power BI.

## Limitations

- **Data Accuracy**: Google Trends data, even when fetched via SerpApi, is based on a sample of searches and may not reflect the entire population's behavior.
- **Time Lag**: Real-time data may have a slight delay depending on when the dashboard was last refreshed (e.g., last refreshed on March 25, 2025, at 07:25 PM).
- **Regional Bias**: Search interest may be skewed by internet access and user demographics in different regions.

## What I Learned

- **API Integration**: Learned how to use SerpApi to fetch real-time data from Google Trends.
- **Power BI Development**: Improved my ability to create interactive dashboards using Power BI, including data modeling, visualization, and report design.
- **Trend Analysis**: Developed a deeper understanding of how to interpret search trends and apply them to real-world scenarios, such as career planning.

## Future Improvements

- Add more granular filters for specific industries or job sectors.
- Include sentiment analysis to understand the context of searches (e.g., positive vs. negative sentiment).
- Integrate predictive analytics to forecast future trends in job role popularity.

## Credits

This project was inspired from **[The Developer](https://www.youtube.com/@The-Developer-BI)** YouTube channel, which provides valuable insights into Power BI storytelling and visualization.  
