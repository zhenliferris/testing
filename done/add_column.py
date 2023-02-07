from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
df = pd.read_csv('application_record.csv')
df.dropna(axis=1, inplace=True)
df.head(19)

X = np.array(df['AMT_INCOME_TOTAL']).reshape(-1, 1)
scaler = MinMaxScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
df['min max'] = X_scaled.reshape(1, -1)[0]
df.to_csv('application_record.csv', index=False)
