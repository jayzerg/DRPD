# 📊 Dynamic Retail Performance Dashboard

A comprehensive data analytics and visualization dashboard built with **Streamlit**, **Pandas**, and **Plotly**. This application allows users to upload, clean, and visualize retail sales data with automated insights and interactive charts.

---

## 🚀 Key Features

*   **Multi-format File Support:** Seamlessly load `.csv` (with automatic encoding detection and error handling) and `.xlsx` files.
*   **Auto-detect Analytics:** Automatically identifies date, numeric, and categorical columns to generate relevant charts.
*   **Interactive Visualizations:**
    *   **Distribution Analysis:** View bar charts of revenue/metrics by category.
    *   **Trend Analysis:** Track performance over time with interactive line charts.
    *   **Category Breakdown:** Pie charts for quick market share visualization.
    *   **Correlation Analysis:** Scatter plots to find relationships between numeric variables.
*   **Dynamic Filtering:** Sidebar filters are automatically generated based on your dataset's categories.
*   **Data Export:** Download your filtered datasets directly as CSV files.

---

## 🛠️ Installation & Setup

Follow these steps to get the dashboard running on your local machine:

### 1. Prerequisites
Ensure you have **Python 3.8+** and `pip` installed. You can check your version by running:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/jayzerg/KAGGLE.git
cd KAGGLE
```

### 3. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🏃 How to Run

Launch the Streamlit server with the following command:
```bash
streamlit run app.py
```
The application will automatically open in your default web browser at `http://localhost:8501`.

---

## 📂 Project Structure

*   `app.py`: The main Streamlit entry point containing the dashboard UI and logic.
*   `scripts/`: Core processing scripts for data operations:
    *   `data_cleaning.py`: Utilities for handling missing values and data formatting.
    *   `data_manipulation.py`: Functions for transformations and aggregations.
    *   `file_reader.py`: Advanced file loading logic for different formats.
*   `requirements.txt`: List of Python libraries required to run the project.

---

## 📋 Data Requirements

*   **File Types:** `.csv`, `.xlsx`.
*   **Headers:** The system expects headers at the top of your file. If your headers are at a specific row, you can adjust the "Found headers at row #" setting in the sidebar.
*   **Clean Data:** While the app has built-in cleaning, ensure your numeric columns (Sales, Profit, etc.) don't contain non-numeric text for the best results.

---

## 💡 Usage Tips

1.  **Handling Headers:** If your data appears as "Unnamed" columns, increase the **"Found headers at row #"** slider in the sidebar.
2.  **Date Detection:** For the Best Trend Analysis, ensure your date columns contain "date", "order", or "ship" in the column name.
3.  **Large Files:** For very large datasets, use CSV format for faster loading times compared to Excel.

---

*Built with ❤️ by [jayzerg](https://github.com/jayzerg)*
