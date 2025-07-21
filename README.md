# 🛍️ Customer Segmentation Dashboard

An interactive dashboard built using Streamlit and K-Means clustering to uncover key customer personas. This project blends data analytics with UI-driven storytelling to visualize behavioral segments in a retail dataset.

## 🚀 Overview

This dashboard analyzes customer behavior based on Age, Annual Income, and Spending Score, and presents five distinct user clusters with persona mappings. Each segment is styled with its own identity to help uncover product targeting or UX customization opportunities — especially useful for fintech interfaces like Bluestock’s.

## 📁 Project Structure

| File                             | Purpose                                                        |
|----------------------------------|----------------------------------------------------------------|
| `app.py`                         | Streamlit app with cluster filtering, visual plots, and UX personas |
| `Mall_Customers_with_Cluster.csv` | Final dataset with cluster labels                             |
| `customer_segmentation_analysis.ipynb` | Jupyter notebook with preprocessing, EDA, and clustering logic |
| `black_land_rover_defender_8k.jpg` | Banner image used in app header                               |
| `README.md`                      | Project summary and walkthrough                               |

## 📊 Key Features

- ✔️ Clustering using K-Means (`scikit-learn`)
- 📉 Data scaling via `StandardScaler`
- 🧠 Cluster-based persona mapping
- 🎨 Interactive UI with dropdown filters and plot styling
- 📦 Streamlit dashboard integration with clean layout flow

## 🔧 How to Run

```bash
streamlit run app.py