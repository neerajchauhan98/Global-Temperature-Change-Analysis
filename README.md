# Global Temperature Change Analytics & Forecasting using Machine Learning (1961–2050)

This project combines data processing, data analytics, and machine learning to analyze and forecast global temperature anomalies using historical climate data. It processes over 150K+ climate records across 284 countries and regions from 1961 to 2019 through data cleaning, transformation, exploratory analysis, and regression-based forecasting to estimate future warming trends up to 2050.

## Objective

To process, clean, transform, and analyze historical climate datasets, identify long-term warming patterns, and build a regression-based forecasting model for data-driven climate analysis.

## Project Workflow

```text
Historical Climate Dataset
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Exploratory Data Analysis
        ↓
Visualization
        ↓
Regression Model
        ↓
Temperature Forecast (2050)

## Dataset Summary

| Attribute | Details |
|---|---|
| Source | FAOSTAT – Global Climate Change Dataset |
| Geographic Coverage | 284 Countries/Regions |
| Time Span | 1961–2019 (59 years) |
| Variable | Annual & Monthly Temperature Change (°C) |
| Data Cleaning | Null handling, melt transformation, and filtering for temperature change |
| Dataset File | `dataset/py_dataset.csv` |

## Key Insights and Findings

### 1. Global Warming Trend

- A sharp rise in temperature anomalies was observed after the early 2000s.
- Average global temperature anomaly exceeds 1.1°C in recent years.

### 2. Top Temperature Hotspots

- Central Asian and Eastern European regions show average temperature anomalies exceeding +2°C.
- These regions show significantly higher warming compared with the global average.

### 3. Seasonal Observations

- July shows the highest temperature anomaly among the analyzed months.
- Winter months show greater fluctuations in anomaly values.

## Model Evaluation

The project uses Linear Regression for temperature forecasting.

| Metric | Score |
|---|---:|
| R² Score | 0.8806 |
| Mean Squared Error (MSE) | 0.0265 |
| Mean Absolute Error (MAE) | 0.1292 |

The model achieved an R² score of 0.8806, indicating a strong relationship between the time variable and the observed temperature anomaly trend.

## Forecasted Temperature Change (2023–2050)

| Year | Predicted Temperature Change (°C) |
|---:|---:|
| 2023 | 1.33 |
| 2030 | 1.51 |
| 2040 | 1.77 |
| 2050 | 2.03 |

The model projects an increase of approximately +0.70°C in global temperature anomaly between 2023 and 2050.

## Visual Results

The project generates and saves visualizations in the `output/` directory.

- Global Warming Trend
- India vs China Comparison
- Top Region Warming Bar Chart
- Box Plot and Monthly Temperature Pattern
- Yearly and Country-wise Heatmaps
- 2050 Temperature Forecast

## Tech Stack and Skills

| Category | Tools |
|---|---|
| Programming | Python |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn |
| Machine Learning | Linear Regression |
| Evaluation | R², MSE, MAE |
| Techniques | Data Cleaning, Data Processing, Data Transformation, Feature Engineering, Forecasting, Visualization |

How to Run
Install Dependencies
pip install -r requirements.txt

Execute the Project
python main.py


**Author
Neeraj Chauhan**
B.Tech – Computer Science Engineering
GitHub: https://github.com/neerajchauhan98
LinkedIn: https://www.linkedin.com/in/neeraj-chauhan-5bb899298/

---

If you found this project useful, consider giving the repository a ⭐.
