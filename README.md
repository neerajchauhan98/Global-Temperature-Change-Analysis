# 🌍 Global Temperature Change Analytics & Forecasting using Machine Learning (1961–2050)

This project combines **Data Processing**, **Data Analytics**, and **Machine Learning** to analyze and forecast global temperature anomalies using historical climate data. It processes over **150K+ climate records** collected across **284 countries/regions (1961–2019)** through data cleaning, transformation, exploratory analysis, and regression-based forecasting to predict future warming trends up to **2050**.

🎯 Objective

To process, clean, transform, and analyze large-scale historical climate datasets, identify long-term warming patterns, and build a regression-based forecasting model that supports data-driven climate analysis and policy insights.


## 📊 Project Workflow

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

📂 Dataset Summary
Attribute	Details
📁 Source	FAOSTAT – Global Climate Change Dataset
🌍 Geographic Coverage	284 Countries/Regions
📅 Time Span	1961–2019 (59 years)
🌡 Variable	Annual & Monthly Temperature Change (°C)
🔧 Cleaning	Null handling + Melt transformation + Filtering for Temperature Change
📌 Format	Local file dataset/py_dataset.csv
📊 Key Insights & Findings
🌡 1. Global Warming Trend

Sharp anomaly rise after early 2000s, indicating accelerated warming.

Average global anomaly now exceeds 1.1°C.

📍 2. Top Temperature Hotspots

Based on average anomaly values, Central Asia & Eastern European regions are warming almost twice as fast as the global rate, with average anomalies exceeding +2°C.

⚠ These regions are major climate risk hotspots due to landlocked geography & dry climate sensitivity.

📆 3. Seasonal Observations

July shows the highest anomaly among all months (peak temperature deviation).

Winter months display highly fluctuating anomaly values, indicating unstable seasonal shifts.

🤖 Model Evaluation (Linear Regression)
Metric	Score
📌 R² Score	0.8806
📉 Mean Squared Error (MSE)	0.0265
📏 Mean Absolute Error (MAE)	0.1292

✔ A strong R² value shows temperature rise has a consistent linear pattern over time.

🔮 Forecasted Temperature Change (2023–2050)
Year	Predicted Δ Temp (°C)
2023	1.33
2030	1.51
2040	1.77
2050	2.03

📌 Insight: Global anomaly is expected to increase by ≈ +0.70°C between 2023 and 2050, exceeding multiple international climate threshold targets.

🖼 Visual Results

All plots are automatically saved in: output/

✔ Global Warming Trend
✔ India vs China Comparison
✔ Top Region Warming Bar Chart
✔ Box Plot & Monthly Bar Pattern
✔ Heatmaps (Yearly & Country-wise)
✔ 2050 Forecast Visualization

Saved as .png using plt.savefig().

🛠 Tech Stack & Skills
Domain	Tools
Programming -	Python
Libraries - 	Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn
ML & Statistics - 	Linear Regression, Evaluation Metrics
Techniques - Data Cleaning, Data Processing, Data Transformation, Feature Engineering, Forecasting, Visualization

▶ Run This Project
📌 Install Dependencies
pip install -r requirements.txt

🚀 Execute the Script
python main.py

👨‍💻 Author

👤 Neeraj Chauhan
🔎 Data Science & Machine Learning Enthusiast

📌 Star ⭐ the repository if you like this work and want to support open-source learning.
