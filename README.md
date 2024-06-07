# Stock Price Predictor using Prophet
This Stock Price Predictor App predicts all S&P500 companies's stock price for how far you want using a history stock price change as a base.

Created and designed by [Kairat Berik](https://www.linkedin.com/in/kairat-berik/).

## 1. Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/vikasharma005/Stock-Price-Prediction.git
   ```

2. Navigate to the project directory:
   ```sh
   cd stock-price-prediction-app
   ```

3. Install the required Python packages using pip:
   ```sh
   pip install -r requirements.txt
   ```

## Features

- **Visualize Technical Indicators**: Explore various technical indicators such as Bollinger Bands, MACD, RSI, SMA, and EMA to gain insights into stock price trends.

- **Recent Data Display**: View the most recent data of the selected stock, including the last 10 data points.

- **Price Prediction**: Predict future stock prices using machine learning models including Linear Regression, Random Forest Regressor, Extra Trees Regressor, KNeighbors Regressor, and XGBoost Regressor.

## Usage

1. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

2. The app will open in your default web browser. Use the sidebar to choose options for visualization, recent data display, or making price predictions.

3. Follow the on-screen instructions to input the stock symbol, select a date range, and choose technical indicators or prediction models.

## Technologies used

- Python
- Streamlit
- pandas
- yfinance
- Prophet
