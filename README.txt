Flight Price Prediction - data-driven dropdowns

Place flight_price_model.pkl next to app.py. It must be the full fitted
scikit-learn pipeline saved by Flight_Price_Prediction_Student_Fixed.ipynb.

Project structure:
    app.py
    train.csv
    flight_price_model.pkl     <- copy your trained model here
    templates/home.html
    static/css/styles.css

Run:
    pip install flask pandas scikit-learn lightgbm xgboost catboost
    python app.py

Dropdowns come directly from the Airline, Source, Destination and
Total_Stops columns in train.csv. Destination options depend on source;
airline options depend on route; stops depend on route and airline.

The saved model pipeline, not app.py, performs one-hot encoding.
If the model file is absent, the form still displays but predictions
will explain that the model file is missing.
