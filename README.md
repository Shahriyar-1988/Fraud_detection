
# 🕵️ Fraud Detection Pipeline

This project implements a machine learning pipeline for detecting fraudulent transactions using ensemble and distance-based classifiers. The pipeline includes preprocessing, model training, hyperparameter tuning, evaluation, and experiment tracking via MLflow.

---

## 📊 Models Compared

Two models were trained and evaluated:

- **ExtraTreesClassifier**
- **KNeighborsClassifier**

### ✅ Performance Summary

After cross-validation and evaluation on the test set:

- **ExtraTreesClassifier** consistently outperformed KNN in terms of:
  - **F1-score**
  - **Recall**
  - **ROC AUC**
- It also demonstrated better generalization and robustness across imbalanced class distributions.

> 📌 _Conclusion: ExtraTreesClassifier is the recommended model for this fraud detection task._

---

## 📁 Project Structure

```
Fraud_detection/
├── src/                 # Source code modules
├── notebooks/           # Jupyter notebooks for exploration and prototyping
├── configs/
│   ├── config.yaml      # Data and path configurations
│   └── params.yaml      # Model parameters
├── .env                 # Environment variables (see below)
├── main.py              # Entry point for running the pipeline
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to set up the environment and run the pipeline.

### 1. Clone the Repository

```bash
git clone https://github.com/Shahriyar-1988/Fraud_detection.git
cd Fraud_detection
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with the following content:

```dotenv
MLFLOW_TRACKING_URI=http://localhost:5000
```

> ⚠️ This URI points to the MLflow server used for experiment tracking. Make sure the server is running before executing the pipeline.

You can start a local MLflow UI using:

```bash
mlflow ui
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

### 5. Run the Pipeline

```bash
python main.py
```

---

## 🧪 Experiment Tracking with MLflow

This project uses [MLflow](https://mlflow.org) for:

- Logging models and metrics
- Comparing model performance
- Storing artifacts like confusion matrices and classification reports

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests. Contributions for improving model performance, optimizing preprocessing, or enhancing logging are welcome!

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.
