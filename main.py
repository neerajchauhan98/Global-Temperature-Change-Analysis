import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

warnings.filterwarnings('ignore')
plt.rcParams["figure.figsize"] = (12, 6)
os.makedirs("output", exist_ok=True)

df = pd.read_csv("dataset/py_dataset.csv", encoding='ISO-8859-1')
df_temp = df[df['Element'] == 'Temperature change']
columns_to_keep = ['Area', 'Months'] + [col for col in df_temp.columns if col.startswith('Y')]
df_temp = df_temp[columns_to_keep]
df_long = df_temp.melt(id_vars=['Area', 'Months'], var_name='Year', value_name='TempChange')
df_long['Year'] = df_long['Year'].str.extract('(\d+)').astype(int)
df_long.dropna(subset=['TempChange'], inplace=True)

print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nMissing Values Summary:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

year_cols = [col for col in df.columns if col.startswith('Y')]
print("\nStatistical Summary:\n", df[year_cols].describe())

print("\nUnique Areas:", df['Area'].nunique())
print("Unique Months:", df['Months'].nunique())
print("Unique Elements:", df['Element'].nunique())

sns.histplot(df_long['TempChange'], kde=True, bins=40, color='skyblue')
plt.title("Distribution of Temperature Change")
plt.xlabel("Temperature Change (°C)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/dist_temp.png", dpi=300)
plt.show()

monthly_avg = df_long.groupby("Months")["TempChange"].mean().sort_values()
sns.barplot(x=monthly_avg.index, y=monthly_avg.values, palette='viridis')
plt.title("Average Temperature Change by Month")
plt.xticks(rotation=45)
plt.ylabel("Avg Temp Change (°C)")
plt.tight_layout()
plt.savefig("output/monthly_avg.png", dpi=300)
plt.show()

compare_df = df_long[df_long['Area'].isin(['India', 'China'])]
sns.lineplot(data=compare_df, x="Year", y="TempChange", hue="Area")
plt.title("India vs China Temperature Change Over Time")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/india_china_compare.png", dpi=300)
plt.show()

global_avg = df_long.groupby("Year")["TempChange"].mean().reset_index()
sns.lineplot(data=global_avg, x="Year", y="TempChange", marker="o", color="red")
plt.title("Global Average Temperature Change Over Years")
plt.ylabel("Avg Temperature Change (°C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/global_trend.png", dpi=300)
plt.show()

top_countries = df_long.groupby("Area")["TempChange"].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette="coolwarm")
plt.title("Top 10 Countries by Avg Temperature Change")
plt.xlabel("Avg Temp Change (°C)")
plt.tight_layout()
plt.savefig("output/top_countries.png", dpi=300)
plt.show()

selected_countries = df_long[df_long['Area'].isin(top_countries.index)]
pivot_data = selected_countries.pivot_table(index='Area', columns='Year', values='TempChange', aggfunc='mean')
sns.heatmap(pivot_data, cmap='RdBu_r', linewidths=0.5, linecolor='gray')
plt.title("Temperature Change Heatmap (Top Countries)")
plt.xlabel("Year")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("output/countries_heatmap.png", dpi=300)
plt.show()

sns.boxplot(x='Months', y='TempChange', data=df_long)
plt.title("Box Plot of Temperature Change by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/boxplot_months.png", dpi=300)
plt.show()

month_year_avg = df_long.groupby(['Months', 'Year'])['TempChange'].mean().unstack()
sns.heatmap(month_year_avg, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap of Monthly Avg Temp Change Over Years")
plt.tight_layout()
plt.savefig("output/month_year_heatmap.png", dpi=300)
plt.show()

X = global_avg[["Year"]]
y = global_avg["TempChange"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
mae = np.mean(np.abs(y - y_pred))

print("\nMODEL EVALUATION")
print("R² Score:", round(r2, 4))
print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)

future_years = pd.DataFrame({"Year": np.arange(2023, 2051)})
future_preds = model.predict(future_years)

prediction_table = pd.DataFrame({
    "Year": future_years["Year"],
    "Predicted Temp Change (°C)": np.round(future_preds, 2)
})

print("\nFuture Temperature Change Predictions (2023–2050):")
print(prediction_table.to_string(index=False))

plt.figure(figsize=(13, 6))
plt.plot(global_avg["Year"], global_avg["TempChange"], label="Actual Data (History)", color="blue", linewidth=2)
plt.plot(future_years["Year"], future_preds, label="Predicted (2023–2050)", color="crimson", linestyle="--", linewidth=2)
plt.axvline(2022, color='gray', linestyle='--')
plt.axvspan(2023, 2050, color='orange', alpha=0.1, label="Prediction Zone")
plt.title("Predicted Global Avg Temperature Change (2023–2050)")
plt.xlabel("Year")
plt.ylabel("Avg Temperature Change (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("output/future_prediction.png", dpi=300)
plt.show()

temp_now = model.predict([[2023]])[0]
temp_2050 = model.predict([[2050]])[0]
diff = temp_2050 - temp_now

print("\nInsight: Between 2023 and 2050, global average temperature is predicted to rise by approx", round(diff, 2), "°C.")



'''
# ========================= IMPORT LIBRARIES ============================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

warnings.filterwarnings('ignore')
plt.rcParams["figure.figsize"] = (12, 6)

# LOAD & CLEAN DATA
df = pd.read_csv("py_dataset.csv", encoding='ISO-8859-1')
df_temp = df[df['Element'] == 'Temperature change']
columns_to_keep = ['Area', 'Months'] + [col for col in df_temp.columns if col.startswith('Y')]
df_temp = df_temp[columns_to_keep]

df_long = df_temp.melt(id_vars=['Area', 'Months'], var_name='Year', value_name='TempChange')
df_long['Year'] = df_long['Year'].str.extract('(\d+)').astype(int)
df_long.dropna(subset=['TempChange'], inplace=True)


# EDA

print("Dataset shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nMissing Values Summary:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

year_cols = [col for col in df.columns if col.startswith('Y')]
print("\nStatistical Summary:\n", df[year_cols].describe())

print("\nUnique Areas:", df['Area'].nunique())
print("Unique Months:", df['Months'].nunique())
print("Unique Elements:", df['Element'].nunique())

sns.histplot(df_long['TempChange'], kde=True, bins=40, color='skyblue')
plt.title("Distribution of Temperature Change")
plt.xlabel("Temperature Change (°C)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

monthly_avg = df_long.groupby("Months")["TempChange"].mean().sort_values()
sns.barplot(x=monthly_avg.index, y=monthly_avg.values, palette='viridis')
plt.title("Average Temperature Change by Month")
plt.xticks(rotation=45)
plt.ylabel("Avg Temp Change (°C)")
plt.tight_layout()
plt.show()

compare_df = df_long[df_long['Area'].isin(['India', 'China'])]
sns.lineplot(data=compare_df, x="Year", y="TempChange", hue="Area")
plt.title("🇮🇳 vs 🇨🇳 Temperature Change Over Time")
plt.grid(True)
plt.tight_layout()
plt.show()

global_avg = df_long.groupby("Year")["TempChange"].mean().reset_index()
sns.lineplot(data=global_avg, x="Year", y="TempChange", marker="o", color="red")
plt.title("Global Average Temperature Change Over Years")
plt.ylabel("Avg Temperature Change (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

top_countries = df_long.groupby("Area")["TempChange"].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette="coolwarm")
plt.title("Top 10 Countries by Avg Temperature Change")
plt.xlabel("Avg Temp Change (°C)")
plt.tight_layout()
plt.show()

selected_countries = df_long[df_long['Area'].isin(top_countries.index)]
pivot_data = selected_countries.pivot_table(index='Area', columns='Year', values='TempChange', aggfunc='mean')
sns.heatmap(pivot_data, cmap='RdBu_r', linewidths=0.5, linecolor='gray')
plt.title("Temperature Change Heatmap (Top Countries)")
plt.xlabel("Year")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

sns.boxplot(x='Months', y='TempChange', data=df_long)
plt.title("Box Plot of Temperature Change by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

month_year_avg = df_long.groupby(['Months', 'Year'])['TempChange'].mean().unstack()
sns.heatmap(month_year_avg, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap of Monthly Avg Temp Change Over Years")
plt.tight_layout()
plt.show()


X = global_avg[["Year"]]
y = global_avg["TempChange"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
mae = np.mean(np.abs(y - y_pred))

print("\n MODEL EVALUATION")
print("R² Score:", round(r2, 4))
print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)

future_years = pd.DataFrame({"Year": np.arange(2023, 2051)})
future_preds = model.predict(future_years)

prediction_table = pd.DataFrame({
    "Year": future_years["Year"],
    "Predicted Temp Change (°C)": np.round(future_preds, 2)
})

print("\n🔮 Future Temperature Change Predictions (2023–2050):")
print(prediction_table.to_string(index=False))

plt.figure(figsize=(13, 6))
plt.plot(global_avg["Year"], global_avg["TempChange"], label="Actual Data (History)", color="blue", linewidth=2)
plt.plot(future_years["Year"], future_preds, label="Predicted (2023–2050)", color="crimson", linestyle="--", linewidth=2)

for year in [2025, 2030, 2040, 2050]:
    y_val = model.predict([[year]])[0]
    plt.text(year, y_val + 0.05, str(year) + "\n" + str(round(y_val, 2)) + "°C", color="black", fontsize=9)

plt.axvline(2022, color='gray', linestyle='--')
plt.axvspan(2023, 2050, color='orange', alpha=0.1, label="Prediction Zone")
plt.title("Predicted Global Avg Temperature Change (2023–2050)")
plt.xlabel("Year")
plt.ylabel("Avg Temperature Change (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Trend Prediction
temp_now = model.predict([[2023]])[0]
temp_2050 = model.predict([[2050]])[0]
diff = temp_2050 - temp_now

print("\n Insight: Between 2023 and 2050, global average temperature is predicted to rise by approx", round(diff, 2), "°C.")
'''