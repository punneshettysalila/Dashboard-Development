# DASHBOARD DEVELOPMENT
**Company**: CODETECH IT SOLUTIONS

**Name**: SALILA PUNNESHETTY

**Intern ID**: CT04DH2206

**Domain**: DATA ANALYTICS

**Duration:** 4 Weeks

**Mentor**: NEELA SANTOSH KUMAR

---

### ☔Rainfall Data Dashboard ###

## 🎯 Objective

To build an interactive dashboard for visualizing India's historical rainfall data using modern data science tools. This project enables real-time filtering, graphical insights, and printable reports.

---

## 📝 Task Description

As part of the Data Analytics Virtual Internship at **CODTECH IT SOLUTIONS PVT. LTD.**, Task 3 focused on developing a professional, interactive **data visualization dashboard**. The main objective was to gain hands-on experience with dashboard creation using Python libraries like **Dash**, **Plotly**, and **Pandas**.

This task required the analysis and visualization of a real-world dataset — **Rainfall in India (1901–2017)** — to generate insights into long-term climate trends. The key learning outcomes involved:

- Understanding data cleaning and transformation techniques using `pandas`
- Designing user-friendly web interfaces using Dash components
- Implementing real-time interactivity using Dash callbacks
- Creating visual summaries like bar and line graphs
- Integrating browser-based export functionality for reporting

The final dashboard allows users to:
- Filter by year range and region
- Visualize rainfall patterns across months and years
- View average rainfall indicators
- Export the dashboard using the browser's print-to-PDF feature

This task bridges the gap between raw data and meaningful insight — showcasing both technical and analytical skills in a real-world context.

---

##  Features
- 📍 Dropdown to select any Indian subdivision
- 📆 Range slider to filter rainfall data between 1901–2017
- 📉 Visual insights:
    - *Average Monthly Rainfall (Bar Chart)*
    - *Yearly Rainfall Trend (Line Chart)*
- 📊 Dynamic Average Rainfall Indicator
- 📄 Export-ready: Print dashboard as a PDF report

---

## ⚙️ How It Works
- **Data Source:** Cleaned Kaggle dataset (`Rainfall_Data_LL.csv`)
- **Preprocessing:** Converted wide format to long format using `pandas.melt()`
- **User Controls:** Dash `Dropdown` + `RangeSlider` for filtering
- **Visuals:** Plotly bar and line charts updated dynamically
- **Export:** Print button using JavaScript triggers browser’s PDF print

---

## 🛠️ Tech Stack

| Component       | Tool/Library             |
|----------------|--------------------------|
| Web App        | Dash (Python)            |
| Charts         | Plotly Express           |
| Styling        | Dash Bootstrap Components|
| Data Handling  | Pandas                   |
| Export Feature | HTML/JS Print            |

---

## 📂 Folder Structure
rainfall-dashboard-task3/
├── app.py # Dash app code
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── data/
└── Rainfall_Data_LL.csv # Dataset from Kaggle

## How to Run the Project

```bash
git clone https://github.com/punneshettysalila/rainfall-dashboard-task3.git
cd rainfall-dashboard-task3
pip install -r requirements.txt
python app.py

## Dataset Source
Kaggle: Rainfall in India (1901–2017)

Place it inside the data/ folder as:
Rainfall_Data_LL.csv
```
## Output

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/54d8c3ed-2298-4bf6-b17c-b9f04d0112ef" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/e4b60ad7-4acd-45fd-8c00-943c55ee1ad2" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/fc6c7e98-6fe8-4e50-b226-b87f24a72cbf" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/40696f99-9378-4567-9000-84896dddf4da" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/497382e4-f901-4d1a-a8c0-1fa6be7588e6" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/a7bda96e-42a1-4c35-9b10-4252c02cbfa7" />

## Conclusion

This project enhanced my practical skills in data visualization, interactivity, and real-time analytics using Dash and Plotly. It offered a hands-on understanding of transforming raw data into insightful visual stories. 
