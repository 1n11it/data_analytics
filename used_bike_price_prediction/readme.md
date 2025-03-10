# Used Bike Price Prediction

## Project Overview
This project develops a machine learning-based framework for predicting used bike prices in the Indian market. By analyzing key factors such as brand, power, kilometers driven, and age, the model provides satisfactory price predictions to help buyers and sellers make informed decisions in a market characterized by price inconsistencies and lack of transparency.

## Problem Statement
The used bike market in India is expanding rapidly due to increasing demand for affordable two-wheelers. However, the lack of structured pricing models leads to price inconsistencies, making it difficult for buyers and sellers to make informed decisions. Various factors influence the price, yet there is no standardized approach to determine the fair market value of a used bike.

## Objectives
- Analyze key factors influencing the price of used bikes in India
- Visualize market trends and insights using Tableau
- Develop and compare machine learning models for accurate price prediction
- Provide a data-driven price estimation framework for buyers and sellers

## Dataset
The project utilizes a dataset from Kaggle containing information about used bikes in India:  
[Used Bikes Prices in India Dataset](https://www.kaggle.com/datasets/saisaathvik/used-bikes-prices-in-india)
- Brand and BIke Name
- Age of Bike
- No. of Owner(s)
- Power (CC)
- Kilometers driven
- Location (City)
- Price

## Technologies Used
- **Programming Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **Visualization Tool**: Tableau
- **Development Environment**: Jupyter Notebook (VS Code)
- **Machine Learning Models**: Decision Tree Regressor, Linear Regression, Random Forest, XGBoost

## Methodology
### 1. Data Preprocessing
- Handling missing values using imputation techniques
- Encoding categorical variables
- Outlier detection and removal
- Feature scaling

### 2. Exploratory Data Analysis (EDA)
- Correlation analysis
- Distribution analysis using histograms and box plots
- Scatter plots to visualize relationships between features and price
- Trend analysis based on manufacturing year

### 3. Feature Engineering
- Creating new features like "Age of Bike" and "Price per KM"
- Feature selection using importance scores and correlation analysis

### 4. Model Development
- Implementing various regression models
- Hyperparameter tuning using GridSearchCV
- Model evaluation using R² score, MSE, and MAE

### 5. Visualization
- Creating interactive dashboards in Tableau
- Visualizing price distributions, brand comparisons, and market trends

## Key Findings
- Brand, power, and kilometers driven significantly influence price variations
- Decision Tree Regressor achieved the highest accuracy (R² = 0.986)
- Linear Regression performed with R² = 0.828
- Polynomial Regression achieved R² = 0.974
- KNN Regressor model reached R² = 0.982

## Project Structure
```
used_bike_price_prediction/
│
├── bike_price_model.pkl     # Serialized machine learning model
├── data.xlsx                # Dataset
├── predict.py               # Notebook for price predictions
├── scaler.pkl               # Saved feature scaler for preprocessing new data
├── train_model.ipynb        # Main Jupyter Notebook with analysis and model training
├── visuals.twbx             # Tableau workbook with visualizations
└── readme.md                # Project documentation
```

## Visualizations
The project includes several Tableau visualizations:
1. **Market Structure and Brand Analysis**
   - Price distribution across brands
   - Brand-wise price analysis
   - Power distribution by brand

2. **Performance and Value Analysis**
   - Comprehensive bike performance matrix
   - Power vs. age relationship

3. **Geographic Market Analysis**
   - Regional price variations across Indian states

## How to Use
1. Clone the repository
2. Install required dependencies:
   ```
   pip install pandas numpy scikit-learn matplotlib seaborn joblib
   ```
3. Run the Jupyter notebooks to explore the analysis and models
4. Use `bike_price_predictions.ipynb` to make new predictions
5. Open Tableau visualizations in Tableau Desktop or Tableau Public

## Limitations
- Limited dataset scope, restricting generalization beyond Indian markets
- Lack of real-time demand data
- Potential overfitting in the Decision Tree model despite high accuracy

## Future Enhancements
- Incorporate additional factors like demand trends and seller credibility
- Enhance model robustness through ensemble learning techniques
- Deploy as a web application for easy accessibility
