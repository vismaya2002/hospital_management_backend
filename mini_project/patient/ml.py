from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

def priority_ml(symptom):
    # Sample data with symptoms and priorities
    data = {
        'Symptom': ['heart pain', 'fever', 'leg pain','headache','cough'],
        'Priority': [1, 2, 3,5,8]
    }

    dataz = {'heart pain':1,'fever':2,'leg pain':5,'headache':4,'cough':3}

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Convert the symptom labels to numerical values using LabelEncoder
    le = LabelEncoder()
    df['Symptom'] = le.fit_transform(df['Symptom'])

    # Split the data into features (X) and target (y)
    X = df[['Symptom']]
    y = df['Priority']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create the Decision Tree classifier
    clf = DecisionTreeClassifier()

    # Train the classifier on the training data
    clf.fit(X_train, y_train)

    # Function to predict the priority of a new patient's symptom
    def predict_priority(new_symptom):
        new_symptom_encoded = le.transform([new_symptom])
        priority_prediction = clf.predict([new_symptom_encoded])[0]
        return priority_prediction

    new_patient_symptom = symptom
    predicted_priority = predict_priority(new_patient_symptom)

    return dataz[new_patient_symptom],predicted_priority
