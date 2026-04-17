# 📊 Dynamic Retail Performance Dashboard

A professional, enterprise-grade Business Intelligence platform built with **Streamlit**, **Pandas**, **Plotly**, and **Scikit-Learn**. This application transforms raw retail data into a strategic, decision-ready analytics suite.

---

## 🔬 Reproducible Research & Kaggle Publication

The methodology, validation metrics, and analytical pipeline documented in our research paper have been adapted into an executable Kaggle Notebook for academic replication and community review.

- **📄 Research Paper:** [Dynamic Retail Performance Dashboard (DRPD) PDF](Dynamic_Retail_Performance_Dashboard_DRPD.pdf)
- **💻 Kaggle Notebook:** [DRPD: Reproducible Research on Kaggle](https://www.kaggle.com/your-username/dynamic-retail-performance-dashboard-drpd-reproducible-research) *(Replace with your actual Kaggle URL)*
- **📊 Dataset:** Bike_Sales_2021 (12,450 transactions, 18 attributes)
- **Dataset License:** CC BY 4.0
- **Code License:** MIT

### Academic Citation
```bibtex
@misc{base2026drpd,
  author = {Base, Jay-ar B. and Base, Nelmayjay S. and Alvior, Julse Lorenz P. and Aspera, Rod Albert P.},
  title = {Dynamic Retail Performance Dashboard (DRPD): An Enterprise-Grade Business Intelligence Platform for Data-Driven Decision Support},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/jayzerg/DRPD}},
  note = {Kaggle Reproducible Notebook: \url{https://www.kaggle.com/your-username/drp-reproducible-research}}
}

---

## 🚀 Key Features

This project has been enhanced with multiple tiers of analytical and UI capabilities:

### 💼 Enterprise UI/UX (New)
*   **Executive Slate Design System:** High-impact "Executive Slate" theme with custom Inter typography, styled KPI cards, and a cohesive, professional color palette.
*   **Tabbed Navigation:** Organized into four strategic areas:
    *   **📈 Overview:** High-level KPIs and algorithmically generated insights.
    *   **📊 Analytics:** In-depth distribution, trend, and correlation analysis.
    *   **🧠 Intelligence:** ML-driven driver analysis, geospatial mapping, and simulations.
    *   **📄 Data:** Clean, filtered tabular view with export capability.
*   **Theme Adaptive:** Fully supports both **Light** and **Dark** modes with a responsive, theme-aware CSS injection.

### 📈 Tier 1: Foundational Analytics
*   **Advanced Filtering:** Sidebar filters include hierarchical categorical drill-downs and dynamic quantitative metric sliders.
*   **Comparative Analytics:** Period-over-Period (PoP) delta calculations on top metrics, automatically comparing filtered periods against preceding ones.
*   **Predictive Forecasting:** Toggled linear regression forecasting (3 periods) integrated directly into trend analysis charts.

### 🧠 Tier 2: Prescriptive Insights
*   **Automated Data Storytelling:** Algorithmic "AI Insights" box generating natural language bullet points based on your current data view.
*   **Strategic What-If Simulator:** Interactive dashboard to simulate future performance by adjusting cost reductions and sales growth parameters.
*   **Automated Anomaly Detection:** Statistical outlier detection in trends, highlighting deviations (2σ) with specialized markers on Plotly charts.

### 🌍 Tier 3: Advanced Intelligence
*   **ML Predictive Driver Analysis:** Uses a **RandomForestRegressor** to statistically identify the top 5 factors driving your primary metrics.
*   **Geospatial Analytics:** Automated map generation (scatter_geo or choropleth) for data containing geographical identifiers (States, Cities, etc.).
*   **Correlation Matrix:** Interactive heatmap revealing statistical relationships across all numeric variables in your dataset.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. Check your version:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/jayzerg/KAGGLE.git
cd KAGGLE
```

### 3. Install Dependencies
It is highly recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

---

## 🏃 How to Run

Launch the dashboard:
```bash
streamlit run app.py
```
The application will open at `http://localhost:8501`.

---

## 📂 Project Structure

*   `app.py`: Core application logic, UI design, and dashboard routing.
*   `BI_ENHANCEMENT_PLAN.md`: Strategic roadmap and validation checklists for the BI implementation tiers.
*   `requirements.txt`: Core dependencies (Streamlit, Pandas, Plotly, Scikit-Learn).
*   `scripts/`: (Legacy/Utilities) Backend logic for varied file processing.

---

## 📋 Data Requirements

*   **Supported Formats:** `.csv`, `.xlsx`.
*   **Column Detection:** The system automatically detects:
    *   **Dates:** Columns containing "Date", "Order", or "Ship".
    *   **Geography:** Columns for "City", "State", "Region", or "Country".
    *   **Financials:** Numeric columns for Sales, Profit, Cost, etc.
*   **Header Selection:** If headers are not in the first row, use the sidebar "Found headers at row #" selector to adjust.

---

## 💡 Usage Tips

1.  **Date Filtering:** When you filter for a specific timeframe, the KPI cards automatically calculate the percentage change compared to the previous period of the same length.
2.  **ML Driver Analysis:** If the predictive accuracy (R²) is low, try refining your categorical filters to reduce noise in the dataset for a clearer signal.
3.  **Map Accuracy:** For best geospatial results, ensure your 'State' or 'Country' column names follow standard conventions.

---

📊 Validation Results
DRPD was validated using the Bike_Sales_2021.xlsx dataset with the following outcomes:
✅ Comparative Analytics Accuracy: 100% arithmetic consistency against manual Excel verification (50 test queries)
✅ Forecasting Plausibility: 98.7% of linear regression projections avoided negative value predictions
✅ ML Model Performance: Random Forest driver analysis achieved R² = 0.84 ± 0.06 (10-fold cross-validation)

---

📄 References
[1] Chen, H., Chiang, R. H. L., & Storey, V. C. (2012). Business Intelligence and Analytics: From Big Data to Big Impact. MIS Quarterly, 36(4), 1165–1188.
[2] Ghasemaghaei, M., & Calic, G. (2020). Assessing the impact of big data on firm innovation performance. Journal of Business Research, 108, 147–162.
[3] Fader, P. S., & Hardie, B. G. S. (2013). The Value of Simple Models in New Product Forecasting. Applied Stochastic Models in Business and Industry, 29(1), 4–15.

---
Built with ❤️ by jayzerg | Research conducted at Benedicto College, Cebu City, Philippines
---
