# Patient Length of Stay Prediction (MVP)

**Author:** Mark Merkouchev

## 🚀 Live Demo

Check out the live deployment of the project here:
👉 **[app.markmerk21.com](https://app.markmerk21.com)**

### 💻 What the Website Does
The web application serves as an interactive user interface for the prediction model. It allows medical staff or hospital administrators to:
1.  **Input Patient Parameters:** Enter key admission data such as age, specialist department, and primary diagnosis via a clean Streamlit form.
2.  **Get Real-Time Predictions:** The app processes the input through the trained machine learning model.
3.  **Visualize Results:** Instantly displays the predicted length of stay (in days) to aid in bed capacity planning and discharge management.

---

## 📋 Overview

**Patienten Aufenthaltsvorhersage**

The occupation of beds and the precise estimation of their re-availability require a high degree of experience – a competence that is typically attributed to experienced nursing or medical specialists. Currently, prognoses regarding discharge times are often based on empirical values, which not infrequently leads to bottlenecks, transfers, and delays.

The challenge is to reliably predict a patient-specific length of stay based on a few characteristics available at admission – such as age, specialist department, or primary diagnosis. To this end, we provide real, anonymized routine data to make capacities visible early on, specifically automate discharge management, and predict future capacities.

## 🛠️ Tech Stack

* **Frontend:** Streamlit Python Module
* **Machine Learning:** Predictive modeling using Python (Scikit-learn/Pandas)
* **Backend/Prototyping:** Jupyter Notebook
* **Deployment & Infrastructure:** Hosted on **AWS EC2** (Ubuntu **t3.medium** instance)
* **Data Inspiration:** [Healthcare Analytics II (Kaggle)](https://www.kaggle.com/datasets/nehaprabhavalkar/av-healthcare-analytics-ii/data)

---

## ⚙️ Setup & Installation

Follow these steps to set up the project environment on your local machine. We recommend using Conda and the provided `environment.yml` file for the most reliable setup.

### Option 1: Using Conda (Recommended)

This method uses the `environment.yml` file to recreate the exact development environment.

1.  **Clone the repository:**
```bash
git clone 'https://github.com/MarkMerk/Healthcare.git'
cd AGAthon
```
2.  **Ensure you have Conda installed.** If not, we recommend installing [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).
3.  **Create the Conda environment:**
```bash
conda env create -f environment.yml
```
4.  **Activate the environment:**
```bash
conda activate agathon
```

### Option 2: Using pip (Alternative)

1.  **Clone the repository:**
```bash
git clone 'https://github.com/MarkMerk/Healthcare.git'
cd AGAthon
```
2.  **Ensure you have Python installed** (version 3.10 or higher recommended).
3.  **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the App Locally

After installing the requirements, navigate to the example directory and run the Streamlit app:

```bash
streamlit run webapp.py
```

🤝 Contribution Guidelines
Use feature branches when working on tasks.

Commit with clear messages.

Open Pull Requests for review before merging.