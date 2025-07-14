# 🛒 Market Basket Analysis for Cross-Selling & Product Bundling

## 📌 Problem Statement

Retailers and e-commerce companies are always looking for ways to increase basket size and drive incremental sales. One proven strategy is to identify **which products are frequently purchased together**, and then use this insight to create **cross-sell recommendations** and **bundle offers**.

This project performs **Market Basket Analysis** on retail transaction data to uncover these product relationships. By finding frequent itemsets and association rules, we can suggest actionable product bundles that improve customer experience and increase revenue.

---

## 📊 Data Description

We use **transaction-level retail data**, where each row represents a product purchased in a single order. The key columns are:

- `order_id`: Unique identifier for each customer transaction.
- `product_name`: Name of the product purchased.

Example structure:

`` 
order_id,product_name
1,Bread
1,Milk
1,Eggs
2,Bread
2,Butter
``

**Dataset Used**

- A small example dataset (`sample_transactions.csv`) is included for testing.
- This structure is inspired by real-world datasets like the [Instacart Market Basket Analysis dataset](https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset/data).

---

## ⚙️ Technical Approach

1️⃣ **Data Preprocessing**

- Remove duplicates and handle missing values.
- Create grouped transaction lists (products per order).

2️⃣ **Basket Matrix Creation**

- Use `TransactionEncoder` from `mlxtend` to convert transactions into a one-hot encoded basket format (products as columns, transactions as rows).

3️⃣ **Frequent Itemset Mining**

- Apply the **Apriori algorithm** (via `mlxtend`) to identify frequent product combinations based on a minimum support threshold.

4️⃣ **Association Rule Mining**

- Generate rules using `mlxtend`'s `association_rules` function.
- Evaluate rules using **support**, **confidence**, and **lift** metrics.

5️⃣ **Visualization and Insights**

- Plot support vs confidence.
- Analyze lift distributions.
- Summarize the strongest cross-sell opportunities.

---

## 🗂 Project Structure

```
├── data/
│ └── sample_transactions.csv # Sample transaction dataset for testing
├── notebooks/
│ └── eda.ipynb # Full exploratory analysis notebook
├── scripts/
│ └── association_mining.py # Reusable script for mining itemsets & rules
├── app/
│ └── app.py # Streamlit app for interactive rule exploration
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore
```

---

## 🚀 How to Run

### ✅ Setup

```bash
git clone https://github.com/shivanic02/cross-selling-recommendation.git
cd cross-selling-recommendation
pip install -r requirements.txt
```

### 💻 Run analysis in notebook

Open:

```bash
notebooks/eda.ipynb
```

### 🌟 Streamlit App

```bash
streamlit run app/app.py
```

### 🧪 Testing with Sample Data

A ready-to-use example CSV file is provided:

```bash
data/sample_transactions.csv
```

---

## 💡 Business Use Cases

- Cross-selling: Recommend complementary products on product pages or at checkout.
- Bundling: Design promotions or discounts for frequently bought-together products.
- Personalization: Improve targeted marketing based on common product pairings.

---

## 🔬 Future Enhancements

- Incorporate price and margin data to optimize for profitability.
- Segment analysis by customer demographics or time periods.
- Real-time recommendation engine integration.

---

## 📄 License

This project is licensed under the MIT License.
