import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Dynamic Retail Dashboard", layout="wide")

# Title
st.title("📊 Dynamic Retail Performance Dashboard")
st.markdown("---")

# File uploader
st.sidebar.header("Upload Data Settings")
uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
skip_rows = st.sidebar.number_input("Found headers at row #", min_value=0, value=0, help="If columns are 'Unnamed', try increasing this.")



if uploaded_file is not None:
    # Load data
    @st.cache_data
    def load_data(file, skip):
        if file.name.endswith('.csv'):
            try:
                df = pd.read_csv(file, encoding='latin1', skiprows=skip, on_bad_lines='skip')
            except TypeError:
                file.seek(0)
                df = pd.read_csv(file, encoding='latin1', skiprows=skip, error_bad_lines=False, warn_bad_lines=True)
        else:
            # Handle potential header issues in Excel
            df = pd.read_excel(file, engine='openpyxl', skiprows=skip)
            # Clean up: strip whitespace from column names
            df.columns = [str(c).strip() for c in df.columns]
        
        # Quick check for mostly empty columns/rows often found in messy Excel exports
        df = df.dropna(how='all', axis=1).dropna(how='all', axis=0)
        return df


    
    df = load_data(uploaded_file, skip_rows)

    
    # Auto-detect column types
    def detect_column_types(df):
        """Automatically detect different types of columns"""
        date_columns = []
        numeric_columns = []
        categorical_columns = []
        
        for col in df.columns:
            # Skip if empty
            if df[col].isnull().all():
                continue

            # Try to detect date columns if not already numeric
            if 'date' in col.lower() or 'ship' in col.lower() or 'order' in col.lower():
                # Avoid re-converting if already datetime
                if not pd.api.types.is_datetime64_any_dtype(df[col]):
                    try:
                        temp_date = pd.to_datetime(df[col], dayfirst=True, errors='coerce')
                        if temp_date.notna().sum() > 0:
                            df[col] = temp_date
                            date_columns.append(col)
                            continue
                    except:
                        pass
                else:
                    date_columns.append(col)
                    continue

            # Detect ID and Metadata columns explicitly based on naming heuristics 
            col_lower = col.lower().strip()
            is_metadata = ('id' == col_lower or col_lower.endswith(' id') or col_lower.endswith('_id') or 
                         'name' == col_lower or col_lower.endswith(' name') or col_lower.endswith('_name') or
                         'email' in col_lower or 'phone' in col_lower or 'address' in col_lower)
            
            if is_metadata:
                # Force converting numeric IDs to strings prevents accidental plot summations
                df[col] = df[col].astype(str)
                categorical_columns.append(col)
                continue

            # Detect numeric columns
            if pd.api.types.is_numeric_dtype(df[col]):
                # If it's effectively a boolean or has very few values and column name doesn't suggest metric, skip for cat
                if df[col].nunique() < 10 and not any(x in col_lower for x in ['sales', 'profit', 'quantity', 'amount', 'price', 'cost']):
                    categorical_columns.append(col)
                else:
                    numeric_columns.append(col)
            else:
                # Try to convert object to numeric if it looks numeric
                try:
                    # Remove currency symbols and commas
                    temp_num = df[col].astype(str).str.replace(r'[$,]', '', regex=True)
                    temp_num = pd.to_numeric(temp_num, errors='coerce')
                    if temp_num.notna().sum() / len(temp_num) > 0.5: # If > 50% is numeric
                        df[col] = temp_num
                        numeric_columns.append(col)
                        continue
                except:
                    pass

                # Detect categorical columns: Allow text categories, bounding cardinality to 300 to avoid memory exhaustion
                if df[col].nunique() < 300: 
                    categorical_columns.append(col)

        
        return date_columns, numeric_columns, categorical_columns
    
    # Detect columns
    date_cols, numeric_cols, cat_cols = detect_column_types(df)
    
    # Display dataset info
    with st.expander("📋 View Dataset Information"):
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Rows", len(df))
        col2.metric("Total Columns", len(df.columns))
        col3.metric("Date Columns Found", len(date_cols))
        
        st.write("**Detected Categories:**")
        st.write(f"- Date Columns: {date_cols}")
        st.write(f"- Numeric Columns: {numeric_cols}")
        st.write(f"- Categorical Columns: {cat_cols}")
        
        st.write("**Raw Pandas Column Types:**")
        st.code(str(df.dtypes))

        
        st.write("**Sample Data:**")
        st.dataframe(df.head())
    
    # Sidebar filters - dynamically created
    st.sidebar.header("Filters")
    
    # Create filters for categorical columns
    filter_columns = {}
    
    # We purposefully exclude high-cardinality metadata (e.g. IDs with thousands of rows) from Sidebar multiselects to protect performance
    viable_filter_cols = [c for c in cat_cols if df[c].nunique() > 0 and df[c].nunique() <= 60]
    
    for col in viable_filter_cols[:5]:  # Limit to first 5 valid categorical columns
        options = sorted([str(x) for x in df[col].dropna().unique()])
        filter_columns[col] = st.sidebar.multiselect(
            f"Select {col}",
            options=options,
            default=options
        )
    
    # Apply filters
    df_filtered = df.copy()
    
    # 1. Categorical Filters
    for col, selected_vals in filter_columns.items():
        if selected_vals:
            df_filtered = df_filtered[df_filtered[col].astype(str).isin(selected_vals)]
            
    # 2. Global Date Filter (Filters out epoch anomalies like 1970 by default)
    if date_cols:
        st.sidebar.markdown("---")
        st.sidebar.subheader("📅 Date Range")
        primary_date = date_cols[0]
        
        # Safely determine valid date bounds - ignoring epoch parsing artifacts (year <= 1970)
        valid_dates = df_filtered[primary_date].dropna()
        valid_dates = valid_dates[valid_dates.dt.year > 1970]
        
        if not valid_dates.empty:
            min_date = valid_dates.min().date()
            max_date = valid_dates.max().date()
            
            if min_date < max_date:
                start_date, end_date = st.sidebar.slider(
                    "Filter Timeframe",
                    min_value=min_date,
                    max_value=max_date,
                    value=(min_date, max_date)
                )
                
                # Apply the chronological constraint globally across the dashboard
                df_filtered = df_filtered[
                    (df_filtered[primary_date].dt.date >= start_date) & 
                    (df_filtered[primary_date].dt.date <= end_date)
                ]
    
    # Check if data is available
    if df_filtered.empty:
        st.warning("⚠️ No data available based on the current filter settings!")
        st.stop()
    
    # KPI Metrics - automatically select key metrics
    if numeric_cols:
        st.subheader("📈 Key Performance Indicators")
        
        # Find common metric columns
        sales_col = next((col for col in numeric_cols if 'sales' in col.lower()), None)
        profit_col = next((col for col in numeric_cols if 'profit' in col.lower()), None)
        quantity_col = next((col for col in numeric_cols if 'quantity' in col.lower()), None)
        
        # Display available metrics
        num_metrics = min(4, len(numeric_cols))
        if num_metrics > 0:
            metric_cols = st.columns(num_metrics)
            
            for i, col in enumerate(numeric_cols[:4]):  # Show first 4 numeric columns
                total_val = df_filtered[col].sum()
                avg_val = df_filtered[col].mean()
                metric_cols[i].metric(
                    f"Total {col}",
                    f"${total_val:,.2f}" if total_val > 100 else f"{total_val:,.2f}",
                    f"Avg: {avg_val:,.2f}"
                )
        st.markdown("---")
    else:
        st.info("💡 No numeric columns found for KPI calculations.")

    
    # Visualization Section
    st.subheader("📊 Visualizations")
    
    # Row 1: Bar chart and Line chart
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribution Analysis")
        if cat_cols and numeric_cols:
            # Let user choose or auto-select
            cat_choice = st.selectbox("Select Category Column", cat_cols, key="bar_cat")
            num_choice = st.selectbox("Select Metric Column", numeric_cols, key="bar_num")
            
            agg_data = df_filtered.groupby(cat_choice)[num_choice].sum().reset_index()
            fig_bar = px.bar(agg_data, x=cat_choice, y=num_choice, 
                           color=cat_choice, template='plotly_white')
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("💡 Requires at least one categorical and one numeric column.")

    
    with col2:
        st.subheader("Trend Analysis")
        if date_cols and numeric_cols:
            date_choice = st.selectbox("Select Date Column", date_cols, key="line_date")
            num_choice_trend = st.selectbox("Select Metric", numeric_cols, key="line_num")
            
            # Allow user to select chronological aggregation level
            agg_level = st.selectbox("Aggregation Level", ["Daily", "Weekly", "Monthly", "Yearly"], index=2, key="line_agg")
            
            # Drop invalid dates and proactively remove any remaining zero-epoch parsing artifacts
            df_trend = df_filtered.dropna(subset=[date_choice]).copy()
            df_trend = df_trend[df_trend[date_choice].dt.year > 1970]
            df_trend = df_trend.sort_values(by=date_choice)
            
            # Resample dates based on selection to reduce data points
            if agg_level == "Daily":
                df_trend[date_choice] = df_trend[date_choice].dt.floor('D')
            elif agg_level == "Weekly":
                df_trend[date_choice] = df_trend[date_choice].dt.to_period('W').dt.start_time
            elif agg_level == "Monthly":
                df_trend[date_choice] = df_trend[date_choice].dt.to_period('M').dt.start_time
            elif agg_level == "Yearly":
                df_trend[date_choice] = df_trend[date_choice].dt.to_period('Y').dt.start_time
            
            # Group by resampled date
            time_data = df_trend.groupby(date_choice)[num_choice_trend].sum().reset_index()
            
            # Turn off markers for very large datasets to prevent visually broken graphs
            use_markers = len(time_data) <= 60
            
            fig_line = px.line(time_data, x=date_choice, y=num_choice_trend,
                             markers=use_markers, template='plotly_white')
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.info("💡 Requires at least one date and one numeric column.")
    
    # Row 2: Pie chart and Scatter plot
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Category Breakdown")
        if cat_cols and numeric_cols:
            cat_pie = st.selectbox("Select Grouping Column", cat_cols, key="pie_cat")
            num_pie = st.selectbox("Select Value Column", numeric_cols, key="pie_num")
            
            pie_data = df_filtered.groupby(cat_pie)[num_pie].sum().reset_index()
            fig_pie = px.pie(pie_data, values=num_pie, names=cat_pie,
                           template='plotly_white')
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("💡 Requires at least one categorical and one numeric column.")
    
    with col2:
        st.subheader("Correlation Analysis")
        if len(numeric_cols) >= 2:
            x_col = st.selectbox("Select X Axis", numeric_cols, key="scatter_x")
            y_col = st.selectbox("Select Y Axis", numeric_cols, key="scatter_y")
            color_col = st.selectbox("Select Color By (Optional)", [None] + cat_cols, key="scatter_color")
            
            fig_scatter = px.scatter(df_filtered, x=x_col, y=y_col,
                                   color=color_col if color_col else None,
                                   template='plotly_white',
                                   hover_data=cat_cols[:2] if cat_cols else None)
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.info("💡 Requires at least two numeric columns.")
    
    # Row 3: Top items
    st.subheader("🏆 Top Items Analysis")
    if cat_cols and numeric_cols:
        top_cat = st.selectbox("Select Category for Top Analysis", cat_cols, key="top_cat")
        top_num = st.selectbox("Select Metric", numeric_cols, key="top_num")
        top_n = st.slider("Number of Top Items", 5, 20, 10)
        
        top_data = df_filtered.groupby(top_cat)[top_num].sum().nlargest(top_n).reset_index()
        fig_top = px.bar(top_data, x=top_num, y=top_cat, orientation='h',
                        color=top_num, template='plotly_white')
        st.plotly_chart(fig_top, use_container_width=True)
    
    # Data table
    st.markdown("---")
    st.subheader("📄 Data Table")
    if st.checkbox("Show Raw Data"):
        st.dataframe(df_filtered)
    
    # Download option
    csv = df_filtered.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv'
    )

else:
    st.info("👆 Please upload a CSV or Excel file to get started!")
    
    # Show example
    st.markdown("### Example CSV Structure:")
    example_df = pd.DataFrame({
        'Order Date': ['01/01/2023', '02/01/2023'],
        'Category': ['Furniture', 'Technology'],
        'Sales': [100.50, 200.75],
        'Profit': [10.50, 20.75],
        'Region': ['East', 'West']
    })
    st.dataframe(example_df)