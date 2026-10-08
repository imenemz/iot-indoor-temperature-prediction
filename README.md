# IoT Indoor Temperature Prediction

A university project exploring indoor temperature prediction using data collected from a local IoT simulator.

**Author:** Imene Mazouz  
**Academic context:** L3 Artificial Intelligence, Université Côte d’Azur

## Objective

Build a Python workflow connecting simulated sensor data collection, CSV storage, regression modelling, and visualisation.

The target is the indoor temperature of Room A.

## Data Collection

The collection scripts poll a local simulator at:

`http://localhost:9797/poll`

Two datasets are included:

- `first_data.csv`: 500 observations containing outdoor and indoor temperatures.
- `data_improved.csv`: 200 observations containing outdoor temperature, humidity, wind, thermostat settings, and indoor temperature.

Outdoor temperature is converted from Kelvin to Celsius during collection.

The simulator itself is not included in this repository. The supplied CSV files allow the modelling scripts to run without it.

## Models

Both experiments use Scikit-learn's LinearRegression.

- Initial model: outdoor temperature as the input.
- Expanded model: outdoor temperature and thermostat setting as inputs.

Humidity and wind are collected but are not used by the current modelling scripts.

Both models use an 80/20 random train/test split with `random_state=42`.

## Results

Results reproduced using the included datasets and scripts:

| Experiment | MAE | MSE | R² |
|---|---:|---:|---:|
| Outdoor temperature only | 1.481 | 2.682 | 0.318 |
| Outdoor temperature and thermostat | 0.686 | 0.728 | 0.049 |

The experiments use different datasets, so their scores are not a controlled comparison of feature sets.

The low R² values indicate limited explanatory performance on the held-out samples.

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the models using the included datasets:

```bash
python the_frist_data_model_script.py
python the_improved_data_model.py
```

Plot the initial dataset:

```bash
python graphe.py
```

To collect new data, start the compatible simulator first, then run either collection script:

```bash
python first_data.py
python data_improved.py
```

Collection scripts overwrite their corresponding CSV files. Back up the included datasets before collecting new observations.

## Limitations

- Data comes from a simulator rather than physical sensors.
- Observations are collected close together in time.
- Random splitting may place closely related observations in both training and test sets.
- The models estimate indoor temperature from current inputs; they do not forecast a future temperature.
- The current linear models show limited predictive performance.

## Possible Improvements

- Evaluate using a chronological train/test split.
- Compare against a simple baseline.
- Collect longer and more varied simulation runs.
- Explore humidity, wind, and previous temperature measurements as features.
- Compare models on the same dataset.
- Validate the approach using real sensor data.
