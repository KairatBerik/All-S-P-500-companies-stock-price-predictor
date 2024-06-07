# Stock Price Predictor using Prophet
This Stock Price Predictor App predicts all S&P500 companies's stock price for how far you want using a history stock prices as a base.

P.S. Don't take it as a real financial advice. 



Created and designed by [Kairat Berik](https://www.linkedin.com/in/kairat-berik/).

## 1. Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/KairatBerik/Prohpet-Stock-Price-Predictor
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

   **or**

Install these packages yourself: 
 ```sh
  pip install pandas
  pip install yfinance
  pip install prophet
  pip install streamlit
  pip install plotly
   ```
   
## 2. Usage

1. On the sidebar you can see the **Stock Selector**, where you can:
   
      - Choose the S&P 500 company you want to work with.
      - Choose the range of years to be shown in the charts and to be used as a base for predictions.
      - Choose number of years (in days) of how far you want to predict the stock price changes.
        
3. On the main side of the page you will see a **Main graph** with the predictions that can be chosen to show data for the last week, last month, last 6 months, last year and every single data.Also there is a **Component graphs** that gives you the overall trend and yearly and weekly seasonalities .

 P.S. The sidebar is foldable and all graphs can be zoomed in/out. 
 
## 3. Features

- **Data Display**: You will be able to see the all data in history of the selected S&P 500 company. 

- **Price Prediction**: Predict price changes based on the chosen range of years to be shown for as far as you would like to (10 years max). 

## 4. Technologies used

- Python
- pandas
- yfinance
- Prophet
- Streamlit
- plotly

## Author 

Industrial Engineering student at UIC | 4th year | [Kairat Berik](https://www.linkedin.com/in/kairat-berik/).

## License

This project is licensed under the [MIT License](LICENSE).

