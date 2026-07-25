# 🛍️ Retail Analytics Dashboard

An end-to-end **Retail Analytics Dashboard** developed using **Python, Google Colab, Machine Learning, Power BI, and Streamlit**. The project transforms raw retail transaction data into meaningful business insights through data processing, customer analytics, forecasting, inventory optimization, and interactive business dashboards.

---

# 🌐 Live Project

## 🚀 Streamlit Application

https://shanmukpanchireddi-retail-analytics-dashboard-app-rdihog.streamlit.app

## 💻 GitHub Repository

https://github.com/shanmukpanchireddi/Retail-Analytics-Dashboard

---

# 📖 Project Description

This project focuses on analyzing retail sales data to help businesses understand customer behavior, predict future demand, and optimize inventory management.

The complete workflow was developed in **Google Colab**, where the data was cleaned, processed, analyzed, and used to build multiple machine learning models. The processed outputs were then visualized using **Power BI dashboards**, which were embedded into a **Streamlit web application** for interactive access.

---

# 🎯 Project Objectives

- Clean and preprocess retail transaction data
- Perform Exploratory Data Analysis (EDA)
- Analyze customer purchasing behavior
- Segment customers using RFM Analysis
- Apply Machine Learning models
- Forecast future sales demand
- Optimize inventory management
- Create interactive Power BI dashboards
- Deploy dashboards using Streamlit

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Google Colab | Development Environment |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| Prophet | Demand Forecasting |
| TensorFlow / Keras | LSTM Model |
| XGBoost | Classification Model |
| Optuna | Hyperparameter Tuning |
| MLflow | Experiment Tracking |
| Power BI | Dashboard Development |
| Streamlit | Web Application |
| GitHub | Version Control |

---

# 📊 Dashboard Screenshots

## 📌 Executive Dashboard

![Executive Dashboard](executive%20dashboard.png)

The Executive Dashboard provides a high-level summary of retail business performance through key performance indicators, enabling users to quickly evaluate sales trends and overall business insights.

---

## 📈 Sales Analysis Dashboard

![Sales Analysis](sales%20analysis%20dashboard.png)

This dashboard provides detailed sales analysis including monthly sales trends, top-selling products, country-wise sales, weekday sales patterns, and hourly sales distribution to better understand customer purchasing behavior.

---

## 👥 Customer Segmentation Dashboard

![Customer Segmentation](customer%20segmentation%20dashboard.png)

The Customer Segmentation Dashboard visualizes customer groups generated through **RFM (Recency, Frequency, Monetary) Analysis**, helping identify valuable customers and supporting targeted marketing strategies.

---

## 📉 Demand Forecasting Dashboard

![Demand Forecasting](demandforecasting%20dashboard.png)

The Demand Forecasting Dashboard presents future sales predictions generated using forecasting models. These insights help businesses estimate future demand and improve planning decisions.

---

## 📦 Inventory Optimization Dashboard

![Inventory Optimization](Inventory%20dashboard.png)

This dashboard provides inventory insights including inventory status, reorder point, safety stock, and reorder quantity, helping businesses maintain optimal inventory levels.

---

# 🔄 Project Workflow

## Step 1 – Data Processing

The retail transaction dataset was loaded into Google Colab and processed through several preprocessing steps.

Completed Tasks:

- ✅ Data Loading
- ✅ Data Cleaning
- ✅ Feature Engineering (TotalPrice)
- ✅ Exploratory Data Analysis (EDA)

---

## Step 2 – Customer Analytics

Customer purchasing behavior was analyzed using RFM Analysis.

Completed Tasks:

- ✅ Recency Calculation
- ✅ Frequency Calculation
- ✅ Monetary Value Calculation
- ✅ RFM Score Calculation
- ✅ Customer Segmentation
- ✅ Customer Segment Visualization

Generated Output:

- customer_rfm.csv

---

## Step 3 – Machine Learning

Multiple machine learning models were developed and evaluated.

Implemented Models:

- ✅ K-Means Clustering
- ✅ DBSCAN Clustering
- ✅ Prophet Demand Forecasting
- ✅ LSTM Sales Forecasting
- ✅ Random Forest Classifier
- ✅ XGBoost Classifier
- ✅ Optuna Hyperparameter Tuning

Generated Output:

- forecast_results.csv

---

## Step 4 – Inventory Analytics

Inventory metrics were calculated to improve stock management.

Completed Tasks:

- ✅ Inventory Optimization
- ✅ Safety Stock Calculation
- ✅ Reorder Point Calculation
- ✅ Reorder Quantity Calculation
- ✅ Inventory Status Classification

Generated Output:

- inventory_optimization.csv

---

## Step 5 – Model Tracking

Machine learning experiments were tracked using MLflow.

Completed Tasks:

- ✅ MLflow Experiment Logging

---

## Step 6 – Power BI Dashboard

The processed datasets were imported into Power BI to build interactive dashboards for business analysis and decision-making.

---

## Step 7 – Streamlit Deployment

The Power BI dashboards were embedded into a Streamlit application to provide an interactive web interface for users.

---

# 📁 Output Files

The project generates the following output datasets:

- ✅ cleaned_retail_data.csv
- ✅ customer_rfm.csv
- ✅ forecast_results.csv
- ✅ inventory_optimization.csv

---

# 📂 Project Structure

```text
Retail-Analytics-Dashboard
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── RetailPulses project1.pbix
├── ShanmukProject_Zidio_updated.ipynb
├── cleaned_retail_data (1).zip
├── customer_rfm (1).csv
├── forecast_results (1).csv
├── inventory_optimization (1).csv
│
└── screenshots
    ├── executive_dashboard.png
    ├── sales_analysis.png
    ├── customer_segmentation.png
    ├── demand_forecasting.png
    └── inventory_optimization.png
```

---

# ▶️ Running the Project

## 1. Clone the Repository

```bash
git clone https://github.com/shanmukpanchireddi/Retail-Analytics-Dashboard.git
```

## 2. Navigate to the Project Folder

```bash
cd Retail-Analytics-Dashboard
```

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

# 👨‍💻 Author

**Shanmuk Panchireddi**

GitHub Profile:

https://github.com/shanmukpanchireddi


## ⭐ Acknowledgement

This project was developed as part of a Data Science internship to demonstrate practical skills in data analytics, machine learning, business intelligence, and web deployment using real-world retail sales data.
