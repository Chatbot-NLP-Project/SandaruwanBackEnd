import joblib
import numpy as np  # linear algebra
import pandas as pd
from sklearn.preprocessing import LabelEncoder

filename = 'model.pkl'

rf = joblib.load(filename)
combined_df = pd.read_csv('combined_df.csv')
X = combined_df[['Symptom_1', 'Symptom_2', 'Symptom_3']]  # get symptom values
P = X[:]
le = LabelEncoder()


def predictDisease(lst):
    filename = 'model.pkl'

    rf = joblib.load(filename)
    combined_df = pd.read_csv('combined_df.csv')
    X = combined_df[['Symptom_1', 'Symptom_2', 'Symptom_3']]  # get symptom values
    P = X[:]
    le = LabelEncoder()

    d = {'Symptom_1': lst[0], 'Symptom_2': lst[1], 'Symptom_3': lst[2]}
    P = P.append(d, ignore_index=True)
    for lul in P.columns:
        P[lul] = le.fit_transform(P[lul].astype(str))
    z = P.tail(1)

    # print(z)

    df2 = pd.DataFrame(z)
    y_pred = rf.predict(df2)
    k = rf.predict_proba(df2)
    prob = np.max(k, axis=1)
    if (prob > 0.7):
        return y_pred[0]
    else:
        # print(prob)
        # print('disease : ' + y_pred[0])
        n = 0
        return 0


# print(lst)

A = ['itching', 'skin_rash', 'nodal_skin_eruptions']
