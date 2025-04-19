import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load model
best_model = joblib.load('model_xgb.joblib')

# Load data untuk prediksi
data_predict = pd.read_csv('Data Prediction Employee.csv')


# Preprocessing data
data_ =data_predict.copy()
numerical = data_.select_dtypes(exclude='object').columns.tolist()
categorical = data_.select_dtypes(include='object').columns.tolist()

data_[categorical] = data_[categorical].apply(LabelEncoder().fit_transform)
data_[numerical] = MinMaxScaler().fit_transform(data_[numerical])

# Melakukan prediksi
predictions = best_model.predict(data_)

# Menambahkan kolom 'Attrition' ke dalam data_predict
data_predict['Attrition'] = predictions

# Simpan ke file baru
data_predict.to_csv('prediction_result.csv', index=False)

print("Hasil prediksi telah ditambahkan ke dalam file 'prediction_result.csv'")