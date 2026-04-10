import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Dynamic Retail Dashboard", layout="wide", page_icon="📊")

# === CSS INJECTION & THEME SYNC ===
def inject_modern_ui_css():
    """Inject modern, accessible, theme-aware CSS via inline <style> block."""
    st.markdown("""
<style>
/* ═══════════════════════════════════════════════════════════════════
   MODERN RETAIL DASHBOARD — DESIGN TOKENS & THEME SYSTEM
   Inline CSS only. Zero external deps. WCAG-safe. Hardware-accelerated.
   ═══════════════════════════════════════════════════════════════════ */

:root {
  /* Light Mode Tokens — Darker bg for better text visibility */
  --color-primary: #3b82f6;
  --color-primary-hover: #2563eb;
  --color-primary-active: #1d4ed8;
  --color-surface: #2d3748;
  --color-surface-elevated: #4a5568;
  --color-bg: #1a202c;
  --color-text: #f7fafc;
  --color-text-muted: #cbd5e0;
  --color-border: rgba(255, 255, 255, 0.15);
  --color-focus: rgba(59, 130, 246, 0.6);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.3);
  --shadow-lg: 0 10px 24px rgba(0, 0, 0, 0.4);
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 200ms cubic-bezier(0.4, 0, 0.2, 1);
  --font-stack: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

[data-theme="dark"] {
  /* Dark Mode Tokens — Aligned with Streamlit native dark palette */
  --color-primary: #60a5fa;
  --color-primary-hover: #93c5fd;
  --color-primary-active: #bfdbfe;
  --color-surface: #1e1e1e;
  --color-surface-elevated: #262730;
  --color-bg: #0e1117;
  --color-text: #fafafa;
  --color-text-muted: #9ca3af;
  --color-border: rgba(255, 255, 255, 0.08);
  --color-focus: rgba(96, 165, 250, 0.5);
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.25);
  --shadow-lg: 0 10px 24px rgba(0, 0, 0, 0.3);
}

/* Base App Container Optimization */
.stApp {
  font-family: var(--font-stack);
  background-color: var(--color-bg);
  color: var(--color-text);
  max-width: 100%;
  padding: 0;
}

/* Smooth content fade-in on load */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.fade-in {
  animation: fadeIn var(--transition-base) ease-out forwards;
}

/* Accessible Focus States */
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

/* Reduced Motion Compliance */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  .fade-in { animation: none !important; }
}

/* Modern Button Styling */
.stButton > button {
  background-color: var(--color-primary);
  color: #ffffff;
  border: none;
  border-radius: var(--radius-md);
  padding: 0.5rem 1.25rem;
  font-weight: 500;
  font-family: var(--font-stack);
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), background-color var(--transition-fast);
}

.stButton > button:hover {
  background-color: var(--color-primary-hover);
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

.stButton > button:active {
  background-color: var(--color-primary-active);
  transform: translateY(0);
}

/* Tabs Modernization */
.stTabs [data-baseweb="tab-list"] {
  gap: 0.75rem;
  border-bottom: 2px solid var(--color-border);
  padding-bottom: 0;
}

.stTabs [data-baseweb="tab"] {
  border-radius: var(--radius-md) var(--radius-md) 0 0;
  padding: 0.65rem 1.25rem;
  font-weight: 500;
  color: var(--color-text-muted);
  transition: color var(--transition-fast), background-color var(--transition-fast);
}

.stTabs [data-baseweb="tab"]:hover {
  color: var(--color-text);
  background-color: transparent;
}

.stTabs [aria-selected="true"] {
  color: var(--color-primary);
  background-color: transparent;
}

/* DataFrame / Table Containers */
.stDataFrame {
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  background-color: var(--color-surface);
}

/* Metric Cards Enhancement */
[data-testid="stMetric"] {
  background-color: var(--color-surface);
  border-radius: var(--radius-lg);
  padding: 1.1rem 1.25rem;
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-sm);
  transition: box-shadow var(--transition-base), transform var(--transition-fast);
}

[data-testid="stMetric"]:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

[data-testid="stMetricLabel"] {
  font-size: 0.75rem !important;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--color-text-muted);
  font-weight: 600;
}

[data-testid="stMetricValue"] {
  font-weight: 700 !important;
  color: var(--color-text);
}

/* Sidebar Refinement */
[data-testid="stSidebar"] {
  border-right: 1px solid var(--color-border);
  background-color: var(--color-surface-elevated);
}

/* Sidebar Toggle Button — Always Visible */
button[data-testid="stSidebarCollapseButton"],
button[data-testid="stSidebarExpandButton"] {
  background-color: var(--color-primary) !important;
  color: #ffffff !important;
  border: 2px solid rgba(255, 255, 255, 0.3) !important;
  border-radius: 50% !important;
  width: 32px !important;
  height: 32px !important;
  min-width: 32px !important;
  min-height: 32px !important;
  padding: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: var(--shadow-md) !important;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), background-color var(--transition-fast) !important;
  z-index: 9999 !important;
}

button[data-testid="stSidebarCollapseButton"]:hover,
button[data-testid="stSidebarExpandButton"]:hover {
  background-color: var(--color-primary-hover) !important;
  box-shadow: var(--shadow-lg) !important;
  transform: scale(1.1) !important;
}

button[data-testid="stSidebarCollapseButton"]:active,
button[data-testid="stSidebarExpandButton"]:active {
  transform: scale(0.95) !important;
}

/* Ensure toggle icon is visible */
button[data-testid="stSidebarCollapseButton"] svg,
button[data-testid="stSidebarExpandButton"] svg {
  fill: #ffffff !important;
  stroke: #ffffff !important;
}

/* Expander Styling */
[data-testid="stExpander"] {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface);
  transition: box-shadow var(--transition-base);
}

[data-testid="stExpander"]:hover {
  box-shadow: var(--shadow-md);
}

/* Radio Button Styling — High Contrast for Theme Selector */
.stRadio > label {
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 0.75rem;
}

.stRadio [data-baseweb="radio"] {
  background-color: var(--color-surface) !important;
  border: 2px solid var(--color-border) !important;
  border-radius: var(--radius-md) !important;
  padding: 0.5rem 0.75rem !important;
  margin: 0.25rem 0 !important;
  transition: all var(--transition-fast) ease;
}

.stRadio [data-baseweb="radio"]:hover {
  border-color: var(--color-primary) !important;
  background-color: var(--color-surface-elevated) !important;
}

.stRadio [data-baseweb="radio"][aria-checked="true"] {
  border-color: var(--color-primary) !important;
  background-color: var(--color-primary) !important;
}

.stRadio [data-baseweb="radio"][aria-checked="true"] label {
  color: #ffffff !important;
  font-weight: 600;
}

.stRadio [data-baseweb="radio"] label {
  color: var(--color-text) !important;
  font-weight: 500;
}

/* Multiselect Tags */
span[data-baseweb="tag"] {
  background-color: var(--color-primary) !important;
  color: #ffffff !important;
  border-radius: var(--radius-sm) !important;
  border: none !important;
  font-weight: 500;
}

span[data-baseweb="tag"]:hover {
  background-color: var(--color-primary-hover) !important;
}

span[data-baseweb="tag"] span[role="presentation"] {
  color: rgba(255, 255, 255, 0.8) !important;
}

span[data-baseweb="tag"] span[role="presentation"]:hover {
  color: #ffffff !important;
}

/* Download Button */
.stDownloadButton > button {
  background-color: var(--color-primary);
  color: #ffffff !important;
  border-radius: var(--radius-md);
  font-weight: 500;
  border: none !important;
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), background-color var(--transition-fast);
}

.stDownloadButton > button:hover {
  background-color: var(--color-primary-hover);
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

/* Alerts */
[data-testid="stAlert"] {
  border-radius: var(--radius-md);
  border-left-width: 4px;
  border-left-color: var(--color-primary);
}

/* Dividers */
hr {
  border: none;
  height: 1px;
  background: linear-gradient(to right, transparent, var(--color-border), transparent);
  margin: 1.5rem 0;
}

/* Utility Card Class for KPI/Section Wrappers */
.ui-card {
  background-color: var(--color-surface);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-sm);
  transition: box-shadow var(--transition-base), transform var(--transition-fast);
}

.ui-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

/* Cleanup: Hide Streamlit default elements */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

def sync_ui_theme(mode: str = "Light"):
    """
    Sync UI theme between Streamlit session state and DOM data-theme attribute.
    Idempotent: prevents duplicate script injection on rerenders.
    """
    if "theme" not in st.session_state:
        st.session_state.theme = mode
    
    is_dark = "Dark" in st.session_state.theme
    
    # Inject theme sync script only once per session
    if "_theme_synced" not in st.session_state:
        st.session_state._theme_synced = True
        theme_script = """
<script>
(function() {
  var appContainer = document.querySelector('.stApp');
  if (appContainer) {
    if (""" + ("true" if is_dark else "false") + """) {
      appContainer.setAttribute('data-theme', 'dark');
    } else {
      appContainer.removeAttribute('data-theme');
    }
  }
})();
</script>
"""
        st.markdown(theme_script, unsafe_allow_html=True)

def get_modern_plotly_config(theme_mode: str) -> dict:
    """
    Return optimized Plotly config dict matching the CSS design tokens.
    Theme-aware template selection with transparent backgrounds.
    """
    is_dark = "Dark" in theme_mode
    return {
        "plot_bgcolor": "rgba(0,0,0,0)",
        "paper_bgcolor": "rgba(0,0,0,0)",
        "font": {
            "family": "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
            "size": 12,
            "color": "#fafafa" if is_dark else "#111827"
        },
        "hovermode": "x unified",
        "margin": {"t": 30, "b": 40, "l": 50, "r": 20},
        "template": "plotly_dark" if is_dark else "plotly_white",
        "colorway": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4", "#ec4899", "#84cc16"],
        "xaxis": {"showgrid": True, "gridcolor": "rgba(128,128,128,0.1)"},
        "yaxis": {"showgrid": True, "gridcolor": "rgba(128,128,128,0.1)"}
    }

# Initialize CSS and theme on first load
inject_modern_ui_css()

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
            df = pd.read_excel(file, engine='openpyxl', skiprows=skip)
            df.columns = [str(c).strip() for c in df.columns]
        
        df = df.dropna(how='all', axis=1).dropna(how='all', axis=0)
        return df

    df = load_data(uploaded_file, skip_rows)
    
    # Enterprise Dashboard Customization — Theme Sync with UI Layer
    with st.sidebar.expander("⚙️ Dashboard Preferences", expanded=False):
        st.markdown("### 🎨 Appearance")
        theme_choice = st.radio(
            "Color Theme", 
            ["☀️ Light Mode", "🌙 Dark Mode"], 
            index=0, 
            key="theme_selector",
            label_visibility="collapsed"
        )
        # Sync session state for theme switching
        if "theme" not in st.session_state:
            st.session_state.theme = theme_choice
        else:
            st.session_state.theme = theme_choice
        sync_ui_theme(st.session_state.theme)
        global_theme = "plotly_white" if "Light" in theme_choice else "plotly_dark"
        # EXEC_COLORS now defined in get_modern_plotly_config for consistency

    # Auto-detect column types
    def detect_column_types(df):
        """Automatically detect different types of columns"""
        date_columns = []
        numeric_columns = []
        categorical_columns = []
        
        for col in df.columns:
            if df[col].isnull().all():
                continue

            if 'date' in col.lower() or 'ship' in col.lower() or 'order' in col.lower():
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

            col_lower = col.lower().strip()
            is_metadata = ('id' == col_lower or col_lower.endswith(' id') or col_lower.endswith('_id') or 
                         'name' == col_lower or col_lower.endswith(' name') or col_lower.endswith('_name') or
                         'email' in col_lower or 'phone' in col_lower or 'address' in col_lower)
            
            if is_metadata:
                df[col] = df[col].astype(str)
                categorical_columns.append(col)
                continue

            if pd.api.types.is_numeric_dtype(df[col]):
                if df[col].nunique() < 10 and not any(x in col_lower for x in ['sales', 'profit', 'quantity', 'amount', 'price', 'cost']):
                    categorical_columns.append(col)
                else:
                    numeric_columns.append(col)
            else:
                try:
                    temp_num = df[col].astype(str).str.replace(r'[$,]', '', regex=True)
                    temp_num = pd.to_numeric(temp_num, errors='coerce')
                    if temp_num.notna().sum() / len(temp_num) > 0.5:
                        df[col] = temp_num
                        numeric_columns.append(col)
                        continue
                except:
                    pass

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
    
    # ── Sidebar Filters ────────────────────────────────────────────────
    st.sidebar.header("Filters")
    
    df_filtered = df.copy()
    
    # 1. Categorical Filters (Hierarchical Drill-down)
    with st.sidebar.expander("🗂️ Categorical Filters", expanded=True):
        viable_filter_cols = [c for c in cat_cols if df[c].nunique() > 0 and df[c].nunique() <= 60]
        
        for col in viable_filter_cols[:5]:
            options = sorted([str(x) for x in df_filtered[col].dropna().unique()])
            if not options: continue
            selected_vals = st.multiselect(
                f"Select {col}",
                options=options,
                default=options,
                key=f"filter_{col}"
            )
            if selected_vals:
                df_filtered = df_filtered[df_filtered[col].astype(str).isin(selected_vals)]
            
    # 2. Metric Filters (Quantitative Thresholds)
    if numeric_cols:
        with st.sidebar.expander("🔢 Metric Thresholds", expanded=False):
            primary_metric = numeric_cols[0]
            min_val = float(df_filtered[primary_metric].min())
            max_val = float(df_filtered[primary_metric].max())
            
            if min_val < max_val:
                metric_range = st.slider(
                    f"Filter by {primary_metric}",
                    min_value=min_val,
                    max_value=max_val,
                    value=(min_val, max_val)
                )
                df_filtered = df_filtered[
                    (df_filtered[primary_metric] >= metric_range[0]) & 
                    (df_filtered[primary_metric] <= metric_range[1])
                ]

    # Save state before date filtering for PoP delta calculations
    df_pre_date = df_filtered.copy()
    prev_start, prev_end = None, None
            
    # 3. Global Date Filter
    if date_cols:
        with st.sidebar.expander("📅 Date Range", expanded=True):
            primary_date = date_cols[0]
            
            valid_dates = df_filtered[primary_date].dropna()
            valid_dates = valid_dates[valid_dates.dt.year > 1970]
            
            if not valid_dates.empty:
                min_date = valid_dates.min().date()
                max_date = valid_dates.max().date()
                
                if min_date < max_date:
                    start_date, end_date = st.slider(
                        "Filter Timeframe",
                        min_value=min_date,
                        max_value=max_date,
                        value=(min_date, max_date)
                    )
                    
                    df_filtered = df_filtered[
                        (df_filtered[primary_date].dt.date >= start_date) & 
                        (df_filtered[primary_date].dt.date <= end_date)
                    ]
                    
                    period_length = end_date - start_date
                    prev_start = start_date - period_length - pd.Timedelta(days=1)
                    prev_end = start_date - pd.Timedelta(days=1)
    
    # Check if data is available
    if df_filtered.empty:
        st.warning("⚠️ No data available based on the current filter settings!")
        st.stop()
    
    # ══════════════════════════════════════════════════════════════════
    # TABBED DASHBOARD NAVIGATION
    # ══════════════════════════════════════════════════════════════════
    tab_overview, tab_analytics, tab_intelligence, tab_data = st.tabs([
        "📈 Overview", "📊 Analytics", "🧠 Intelligence", "📄 Data"
    ])
    
    # ──────────────────────────────────────────────────────────────────
    # TAB 1: OVERVIEW — KPIs + AI Insights
    # ──────────────────────────────────────────────────────────────────
    with tab_overview:
        if numeric_cols:
            st.subheader("📈 Key Performance Indicators")
            
            num_metrics = min(4, len(numeric_cols))
            if num_metrics > 0:
                metric_cols = st.columns(num_metrics)
                
                for i, col in enumerate(numeric_cols[:4]):
                    total_val = df_filtered[col].sum()
                    
                    delta_str = None
                    if prev_start and prev_end and date_cols:
                        df_prev = df_pre_date[
                            (df_pre_date[primary_date].dt.date >= prev_start) & 
                            (df_pre_date[primary_date].dt.date <= prev_end)
                        ]
                        prev_total = df_prev[col].sum()
                        if prev_total > 0:
                            pct_change = ((total_val - prev_total) / prev_total) * 100
                            delta_str = f"{pct_change:+.1f}% vs Prev Period"
                    else:
                        avg_val = df_filtered[col].mean()
                        delta_str = f"Avg: {avg_val:,.2f}"
                        
                    metric_cols[i].metric(
                        f"Total {col}",
                        f"${total_val:,.2f}" if total_val > 100 else f"{total_val:,.2f}",
                        delta=delta_str,
                        delta_color="normal" if "Prev Period" in str(delta_str) else "off"
                    )
            st.markdown("---")
        else:
            st.info("💡 No numeric columns found for KPI calculations.")

        # 🤖 AI Insights (Data Storytelling)
        if numeric_cols and len(df_filtered) > 0:
            st.info("🤖 **AI Insights**")
            insights = []
            
            if cat_cols:
                primary_cat = cat_cols[0]
                primary_num = numeric_cols[0]
                top_cat_val = df_filtered.groupby(primary_cat)[primary_num].sum().idxmax()
                top_cat_sum = df_filtered.groupby(primary_cat)[primary_num].sum().max()
                total_sum = df_filtered[primary_num].sum()
                if total_sum > 0:
                    pct_contribution = (top_cat_sum / total_sum) * 100
                    insights.append(f"• The top performing **{primary_cat}** is **{top_cat_val}**, driving **{pct_contribution:.1f}%** of total {primary_num}.")
            
            profit_col = next((c for c in numeric_cols if 'profit' in c.lower()), None)
            if profit_col and cat_cols:
                profit_by_cat = df_filtered.groupby(cat_cols[0])[profit_col].sum()
                negative_cats = profit_by_cat[profit_by_cat < 0]
                if not negative_cats.empty:
                    worst_cat = negative_cats.idxmin()
                    insights.append(f"• ⚠️ **Warning**: The {cat_cols[0]} *{worst_cat}* is operating at a net loss (Total {profit_col}: ${negative_cats.min():,.2f}).")
                else:
                    insights.append(f"• ✅ Good health: All segments within {cat_cols[0]} are operating with positive net {profit_col}.")
            
            if len(numeric_cols) >= 2:
                x_col, y_col = numeric_cols[0], numeric_cols[1]
                corr = df_filtered[x_col].corr(df_filtered[y_col])
                if abs(corr) > 0.6:
                    direction = "strong positive" if corr > 0 else "strong negative"
                    insights.append(f"• There is a **{direction} correlation ({corr:.2f})** between {x_col} and {y_col}.")
                    
            if not insights:
                insights.append("• Data is evenly distributed with no stark anomalies detected in this view.")
                
            st.markdown("\n".join(insights))

    # ──────────────────────────────────────────────────────────────────
    # TAB 2: ANALYTICS — Charts & Visualizations
    # ──────────────────────────────────────────────────────────────────
    with tab_analytics:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribution Analysis")
            if cat_cols and numeric_cols:
                c1, c2 = st.columns(2)
                cat_choice = c1.selectbox("Category", cat_cols, key="bar_cat")
                num_choice = c2.selectbox("Metric", numeric_cols, key="bar_num")
                
                agg_data = df_filtered.groupby(cat_choice)[num_choice].sum().reset_index()
                plotly_config = get_modern_plotly_config(theme_choice)
                fig_bar = px.bar(agg_data, x=cat_choice, y=num_choice, 
                               color=cat_choice, template=global_theme,
                               color_discrete_sequence=plotly_config["colorway"])
                fig_bar.update_layout(showlegend=False)
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.info("💡 Requires at least one categorical and one numeric column.")

        with col2:
            st.subheader("Trend Analysis")
            if date_cols and numeric_cols:
                t1, t2, t3 = st.columns(3)
                date_choice = t1.selectbox("Date Column", date_cols, key="line_date")
                num_choice_trend = t2.selectbox("Metric", numeric_cols, key="line_num")
                agg_level = t3.selectbox("Aggregation", ["Daily", "Weekly", "Monthly", "Yearly"], index=2, key="line_agg")
                
                df_trend = df_filtered.dropna(subset=[date_choice]).copy()
                df_trend = df_trend[df_trend[date_choice].dt.year > 1970]
                df_trend = df_trend.sort_values(by=date_choice)
                
                if agg_level == "Daily":
                    df_trend[date_choice] = df_trend[date_choice].dt.floor('D')
                elif agg_level == "Weekly":
                    df_trend[date_choice] = df_trend[date_choice].dt.to_period('W').dt.start_time
                elif agg_level == "Monthly":
                    df_trend[date_choice] = df_trend[date_choice].dt.to_period('M').dt.start_time
                elif agg_level == "Yearly":
                    df_trend[date_choice] = df_trend[date_choice].dt.to_period('Y').dt.start_time
                
                time_data = df_trend.groupby(date_choice)[num_choice_trend].sum().reset_index()
                time_data['Type'] = 'Historical'
                
                show_forecast = st.checkbox("📈 Display 3-Period Forecast", value=False)
                
                @st.cache_data
                def compute_forecast(data, date_col, metric_col, periods=3):
                    y = data[metric_col].values
                    x = np.arange(len(y))
                    if len(y) < 3: return None
                    
                    coeffs = np.polyfit(x, y, 1)
                    poly_eqn = np.poly1d(coeffs)
                    
                    future_x = np.arange(len(y), len(y) + periods)
                    forecast_y = poly_eqn(future_x)
                    
                    last_date = data[date_col].iloc[-1]
                    date_diffs = data[date_col].diff().dropna()
                    if len(date_diffs) == 0: return None
                    avg_diff = date_diffs.mean()
                    future_dates = [last_date + avg_diff * i for i in range(1, periods + 1)]
                    
                    forecast_df = pd.DataFrame({
                        date_col: [last_date] + future_dates,
                        metric_col: [y[-1]] + list(forecast_y),
                        'Type': 'Forecast'
                    })
                    return forecast_df

                if show_forecast:
                    forecast_df = compute_forecast(time_data[[date_choice, num_choice_trend]], date_choice, num_choice_trend, periods=3)
                    if forecast_df is not None:
                        time_data = pd.concat([time_data, forecast_df], ignore_index=True)
                
                # Anomaly Detection
                time_data['Is_Anomaly'] = False
                if len(time_data[time_data['Type'] == 'Historical']) > 4:
                    hist_mask = time_data['Type'] == 'Historical'
                    mean_val = time_data.loc[hist_mask, num_choice_trend].mean()
                    std_val = time_data.loc[hist_mask, num_choice_trend].std()
                    anomaly_mask = hist_mask & (np.abs(time_data[num_choice_trend] - mean_val) > 2 * std_val)
                    time_data.loc[anomaly_mask, 'Is_Anomaly'] = True
                
                use_markers = len(time_data) <= 60
                
                color_map = {'Historical': '#3b82f6', 'Forecast': '#f59e0b'}
                fig_line = px.line(time_data, x=date_choice, y=num_choice_trend, color='Type',
                                 color_discrete_map=color_map, markers=use_markers, template=global_theme)
                                 
                anomalies = time_data[time_data['Is_Anomaly']]
                if not anomalies.empty:
                    fig_line.add_trace(go.Scatter(
                        x=anomalies[date_choice],
                        y=anomalies[num_choice_trend],
                        mode='markers',
                        marker=dict(color='#ef4444', size=12, symbol='x', line=dict(width=2, color='#b91c1c')),
                        name='Anomaly (>2 SD)'
                    ))
                                 
                fig_line.for_each_trace(lambda trace: trace.update(line=dict(dash='dash')) if trace.name == 'Forecast' else ())
                
                st.plotly_chart(fig_line, use_container_width=True)
            else:
                st.info("💡 Requires at least one date and one numeric column.")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Category Breakdown")
            if cat_cols and numeric_cols:
                p1, p2 = st.columns(2)
                cat_pie = p1.selectbox("Grouping Column", cat_cols, key="pie_cat")
                num_pie = p2.selectbox("Value Column", numeric_cols, key="pie_num")
                
                pie_data = df_filtered.groupby(cat_pie)[num_pie].sum().reset_index()
                plotly_config = get_modern_plotly_config(theme_choice)
                fig_pie = px.pie(pie_data, values=num_pie, names=cat_pie,
                               template=global_theme, color_discrete_sequence=plotly_config["colorway"])
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("💡 Requires at least one categorical and one numeric column.")
        
        with col2:
            st.subheader("Correlation Matrix")
            if len(numeric_cols) >= 2:
                try:
                    corr_matrix = df_filtered[numeric_cols].corr()
                    fig_corr = px.imshow(
                        corr_matrix, 
                        text_auto=".2f", 
                        aspect="auto",
                        color_continuous_scale="RdBu",
                        template=global_theme
                    )
                    st.plotly_chart(fig_corr, use_container_width=True)
                except Exception as e:
                    st.error(f"Could not generate correlation matrix: {e}")
            else:
                st.info("💡 Requires at least two numeric columns.")
    
    # ──────────────────────────────────────────────────────────────────
    # TAB 3: INTELLIGENCE — ML, Geo, What-If, Top Items
    # ──────────────────────────────────────────────────────────────────
    with tab_intelligence:
        st.subheader("🏆 Top Items Analysis")
        if cat_cols and numeric_cols:
            t1, t2, t3 = st.columns([2, 2, 1])
            top_cat = t1.selectbox("Category for Ranking", cat_cols, key="top_cat")
            top_num = t2.selectbox("Metric", numeric_cols, key="top_num")
            top_n = t3.slider("Top N", 5, 20, 10)
            
            top_data = df_filtered.groupby(top_cat)[top_num].sum().nlargest(top_n).reset_index()
            fig_top = px.bar(top_data, x=top_num, y=top_cat, orientation='h',
                            color=top_num, template=global_theme,
                            color_continuous_scale=['#93c5fd', '#1d4ed8'])
            st.plotly_chart(fig_top, use_container_width=True)
            
        st.markdown("---")
        
        ml_col, geo_col = st.columns(2)
        
        with ml_col:
            st.subheader("🧠 ML Predictive Driver Analysis")
            if numeric_cols and len(df_filtered) > 50:
                ml_target = next((c for c in numeric_cols if 'profit' in c.lower()), numeric_cols[0])
                ml_target = st.selectbox("Target Metric to Predict", numeric_cols, index=numeric_cols.index(ml_target), key="ml_target")
                
                @st.cache_data
                def run_driver_analysis(data, target_col, cats, nums):
                    try:
                        from sklearn.ensemble import RandomForestRegressor
                        from sklearn.model_selection import train_test_split
                        
                        ml_data = data.copy()
                        features = [c for c in nums if c != target_col]
                        
                        cat_features = []
                        for c in cats[:3]:
                            if ml_data[c].nunique() < 15:
                                cat_features.append(c)
                                
                        if cat_features:
                            ml_data = pd.get_dummies(ml_data, columns=cat_features, drop_first=True)
                            features.extend([c for c in ml_data.columns if any(c.startswith(f"{orig_c}_") for orig_c in cat_features)])
                                
                        X = ml_data[features].fillna(0)
                        y = ml_data[target_col].fillna(0)
                        
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                        
                        model = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1)
                        model.fit(X_train, y_train)
                        
                        r2 = model.score(X_test, y_test)
                        importances = model.feature_importances_
                        
                        imp_df = pd.DataFrame({'Feature': features, 'Importance': importances})
                        imp_df = imp_df.sort_values(by='Importance', ascending=False).head(5)
                        
                        return imp_df, r2
                    except ImportError:
                        return "missing_sklearn", None
                    except Exception as e:
                        return str(e), None

                with st.spinner("Training Driver Model..."):
                    imp_result, r_squared = run_driver_analysis(df_filtered, ml_target, cat_cols, numeric_cols)
                    
                    if isinstance(imp_result, str):
                        if imp_result == "missing_sklearn":
                            st.warning("⚠️ Scikit-Learn is not installed. Run `pip install scikit-learn`.")
                        else:
                            st.error(f"Error computing model: {imp_result}")
                    else:
                        st.success(f"**Model Accuracy (R²):** {r_squared:.2f}")
                        fig_ml = px.bar(imp_result, x='Importance', y='Feature', orientation='h', 
                                       template=global_theme, color_discrete_sequence=['#3b82f6'])
                        fig_ml.update_layout(yaxis={'categoryorder':'total ascending'})
                        st.plotly_chart(fig_ml, use_container_width=True)
            else:
                st.info("💡 Requires at least 50 rows of data and numeric columns.")
                
        with geo_col:
            st.subheader("🌍 Geospatial Analytics")
            geo_col_candidates = [c for c in cat_cols if any(heuristic in c.lower() for heuristic in ['state', 'city', 'country', 'region'])]
            if geo_col_candidates and numeric_cols:
                geo_choice = st.selectbox("Geographical Column", geo_col_candidates, key="geo_cat")
                geo_metric = st.selectbox("Map Metric", numeric_cols, key="geo_num")
                
                geo_data = df_filtered.groupby(geo_choice)[geo_metric].sum().reset_index()
                
                geo_type = st.radio("Map Style", ["Scatter (Bubbles)", "Choropleth (Filled Regions)"], horizontal=True)
                
                try:
                    if "Scatter" in geo_type:
                        fig_geo = px.scatter_geo(geo_data, locations=geo_choice, locationmode='USA-states',
                                               size=geo_metric, color=geo_metric, template=global_theme, scope="usa")
                    else:
                        fig_geo = px.choropleth(geo_data, locations=geo_choice, locationmode='USA-states',
                                              color=geo_metric, template=global_theme, scope="usa")
                    
                    fig_geo.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    st.plotly_chart(fig_geo, use_container_width=True)
                except Exception as e:
                    st.warning(f"Could not map '{geo_choice}' to standard locations. {e}")
            else:
                st.info("💡 No definitive geographic columns detected (e.g. State, City).")
        
        st.markdown("---")
        
        # Strategic What-If Simulator
        with st.expander("🔮 Strategic What-If Simulator", expanded=False):
            if numeric_cols:
                profit_col = next((c for c in numeric_cols if 'profit' in c.lower()), None)
                revenue_col = next((c for c in numeric_cols if 'sales' in c.lower()), numeric_cols[0])
                
                st.markdown("Adjust parameters below to mathematically simulate future operational scenarios based on the current aggregated trajectory.")
                w1, w2 = st.columns(2)
                cost_reduction = w1.slider("Projected Cost Reduction (%)", min_value=0.0, max_value=30.0, value=5.0, step=0.5)
                sales_growth = w2.slider("Target Sales Growth (%)", min_value=-50.0, max_value=100.0, value=10.0, step=1.0)
                
                current_revenue = df_filtered[revenue_col].sum()
                current_profit = df_filtered[profit_col].sum() if profit_col in df_filtered else (current_revenue * 0.15)
                metric_label = profit_col if profit_col else 'Inferred Profit'
                
                simulated_revenue = current_revenue * (1 + sales_growth/100)
                current_cost = current_revenue - current_profit
                simulated_cost = current_cost * (1 + sales_growth/100) * (1 - cost_reduction/100)
                simulated_profit = simulated_revenue - simulated_cost
                
                sim_df = pd.DataFrame({
                    'Metric': [revenue_col.capitalize(), revenue_col.capitalize(), metric_label.capitalize(), metric_label.capitalize()],
                    'Scenario': ['Current Trajectory', 'Simulated Scenario', 'Current Trajectory', 'Simulated Scenario'],
                    'Value': [current_revenue, simulated_revenue, current_profit, simulated_profit]
                })
                
                fig_sim = px.bar(sim_df, x='Metric', y='Value', color='Scenario', barmode='group',
                                text_auto='.2s', template=global_theme,
                                color_discrete_sequence=['#3b82f6', '#10b981'])
                fig_sim.update_traces(textposition='outside')
                
                st.plotly_chart(fig_sim, use_container_width=True)
            else:
                st.info("💡 Requires numeric columns for simulation.")

    # ──────────────────────────────────────────────────────────────────
    # TAB 4: DATA — Raw Table + Export
    # ──────────────────────────────────────────────────────────────────
    with tab_data:
        st.subheader("📄 Filtered Dataset")
        st.caption(f"Showing **{len(df_filtered):,}** rows × **{len(df_filtered.columns)}** columns after all active filters.")
        st.dataframe(df_filtered, use_container_width=True)
        
        st.markdown("---")
        csv = df_filtered.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name='filtered_data.csv',
            mime='text/csv'
        )

else:
    st.info("👆 Please upload a CSV or Excel file to get started!")
    
    st.markdown("### Example CSV Structure:")
    example_df = pd.DataFrame({
        'Order Date': ['01/01/2023', '02/01/2023'],
        'Category': ['Furniture', 'Technology'],
        'Sales': [100.50, 200.75],
        'Profit': [10.50, 20.75],
        'Region': ['East', 'West']
    })
    st.dataframe(example_df)