# Energy Consumption Forecasting

This project focuses on forecasting energy consumption using various machine learning models. It includes data preprocessing, feature engineering, model training, and evaluation steps.

## Project Structure

- `data/`: Contains raw and processed data.
  - `raw/`: Original dataset files.
  - `processed/`: Feature-engineered datasets.
- `models/`: Stores trained models in pickle format.
- `notebooks/`: Jupyter notebooks for data exploration, feature engineering, modeling, cross-validation, and evaluation.
- `outputs/`: Contains output files such as predictions and evaluation metrics.
  - `reports/`: Summary reports of model results and evaluations.
- `scripts/`: Python scripts for data preprocessing, feature engineering, and model training.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preprocessing**:
   - Run the `data_preprocessing.py` script to clean and prepare the raw data.

2. **Feature Engineering**:
   - Use the `feature_engineering.py` script or the `feature_engineering.ipynb` notebook to generate additional features.

3. **Model Training**:
   - Train models using the `model_training.py` script or the `modeling.ipynb` notebook.

4. **Cross-Validation**:
   - Evaluate models using cross-validation in the `cross_validation.ipynb` notebook.

5. **Evaluation**:
   - Assess model performance and visualize results in the `evaluation.ipynb` notebook.

## Results

- The `outputs/reports/` directory contains:
  - `model_results.csv`: Metrics for trained models.
  - `model_evaluation_summary.csv`: Summary of evaluation results.

## Dependencies

The project requires the following Python libraries:
- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn
- xgboost
- jupyter

Install them using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.