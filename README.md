🌍 Global Temperature Change Forecasting (1961–2050)

A climate data analytics and forecasting project using Linear Regression to study and predict global temperature anomalies. This work analyzes historical climate change patterns across 284 countries/regions (1961–2019), identifies hotspot areas, and forecasts future warming up to 2050.

🎯 Objective

To analyze global warming patterns using real-world climate records, identify the most affected regions and months, and forecast future temperature anomalies to support data-driven climate decisions and policy insights.

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
Programming	Python
Libraries	Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn
ML & Statistics	Linear Regression, Evaluation Metrics
Techniques	Feature Engineering, Data Cleaning, Forecasting, Visualization
▶ Run This Project
📌 Install Dependencies
pip install -r requirements.txt

🚀 Execute the Script
python main.py

👨‍💻 Author

👤 Neeraj Chauhan
🔎 Data Science & Machine Learning Enthusiast

📌 Star ⭐ the repository if you like this work and want to support open-source learning.