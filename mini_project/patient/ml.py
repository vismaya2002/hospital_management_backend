from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

def priority_ml(symptom):
    # Sample data with symptoms and priorities
    data = {
        'Symptom': ['Fever',
    'Cough',
    'Headache',
    'Fatigue',
    'Sore Throat',
    'Shortness of Breath',
    'Muscle Pain',
    'Chills',
    'Loss of Taste',
    'Loss of Smell',
    'Nausea',
    'Vomiting',
    'Diarrhea',
    'Abdominal Pain',
    'Rash',
    'Chest Pain',
    'Dizziness',
    'Confusion',
    'Swollen Lymph Nodes',
    'Joint Pain',
    'Blurred Vision',
    'Seizures',
    'Difficulty Swallowing',
    'Difficulty Breathing',
    'Irritability',
    'Memory Problems',
    'Back Pain',
    'Frequent Urination',
    'Night Sweats',
    'Unintended Weight Loss',
    'Excessive Thirst',
    'Excessive Hunger',
    'Frequent Infections',
    'Bruising Easily',
    'Unexplained Bleeding',
    'Swollen Joints',
    'Chest Tightness',
    'Pale Skin',
    'Cold Hands and Feet',
    'Hair Loss',
    'Frequent Headaches',
    'Nosebleeds',
    'Frequent Sore Throat',
    'Weakness',
    'Yellowing of the Skin and Eyes (Jaundice)',
    'Swollen Abdomen',
    'Itchy Skin',
    'Swollen Glands',
    'Frequent Fever',
    'Frequent Chills',
    'Muscle Weakness',
    'Dry Cough',
    'Wheezing',
    'Blood in Urine',
    'Difficulty Urinating',
    'Dribbling Urine',
    'Testicular Pain',
    'Erectile Dysfunction',
    'Abnormal Vaginal Discharge',
    'Painful Intercourse',
    'Irregular Menstrual Periods',
    'Unexplained Infertility',
    'Lower Back Pain',
    'Pelvic Pain',
    'Frequent Hiccups',
    'Difficulty Speaking',
    'Slurred Speech',
    'Tremors',
    'Stiffness',
    'Loss of Balance',
    'Depression',
    'Anxiety',
    'Mood Swings',
    'Sleep Problems',
    'Feeling Hopeless',
    'Loss of Interest',
    'Suicidal Thoughts',
    'Agitation',
    'Poor Concentration',
    'Panic Attacks',
    'Rapid Heartbeat',
    'Chest Discomfort',
    'Numbness or Tingling',
    'Swollen Ankles',
    'Irregular Heartbeat',
    'Coughing up Blood',
    'Blood in Stool',
    'Blood in Vomit',
    'Unexplained Weight Gain',
    'Heavy Menstrual Bleeding',
    'Breast Changes',
    'Nipple Discharge',
    'Pelvic Pressure',
    'Shortened Menstrual Periods',
    'Hot Flashes',
    'Night Sweats',
    'Insomnia',
    'Vaginal Dryness',
    'Painful Urination',
    'Painful Bowel Movements',
    'Bloating',
    'Abdominal Cramps',
    'Feeling Full Quickly',
    'Constant Hunger',
    'Change in Bowel Habits',
    'Swollen Legs',
    'Swollen Hands',
    'Frequent Bruising',
    'Difficulty Walking',
    'Balance Problems',
    'Numbness in Extremities',
    'Vision Changes',
    'Hearing Loss',
    'Ringing in Ears',
    'Chest Pressure',
    'Heartburn',
    'Indigestion',
    'Bloody Stool',
    'Bloody Urine',
    'Abnormal Bleeding',
    'Bruising Under the Skin',
    'Increased Urination at Night',],
        'Priority': [ 8,  # Fever
    8,  # Cough
    8,  # Headache
    8,  # Fatigue
    8,  # Sore Throat
    6,  # Shortness of Breath
    7,  # Muscle Pain
    6,  # Chills
    7,  # Loss of Taste
    6,  # Loss of Smell
    8,  # Nausea
    7,  # Vomiting
    7,  # Diarrhea
    7,  # Abdominal Pain
    7,  # Rash
    5,  # Chest Pain
    5,  # Dizziness
    6,  # Confusion
    6,  # Swollen Lymph Nodes
    7,  # Joint Pain
    5,  # Blurred Vision
    2,  # Seizures
    2,  # Difficulty Swallowing
    6,  # Difficulty Breathing
    6,  # Irritability
    5,  # Memory Problems
    7,  # Back Pain
    6,  # Frequent Urination
    7,  # Night Sweats
    4,  # Unintended Weight Loss
    6,  # Excessive Thirst
    6,  # Excessive Hunger
    4,  # Frequent Infections
    5,  # Bruising Easily
    3,  # Unexplained Bleeding
    5,  # Swollen Joints
    2,  # Chest Tightness
    4,  # Pale Skin
    5,  # Cold Hands and Feet
    6,  # Hair Loss
    6,  # Frequent Headaches
    4,  # Nosebleeds
    6,  # Frequent Sore Throat
    7,  # Weakness
    2,  # Yellowing of the Skin and Eyes (Jaundice)
    1,  # Swollen Abdomen
    5,  # Itchy Skin
    5,  # Swollen Glands
    5,  # Frequent Fever
    4,  # Frequent Chills
    5,  # Muscle Weakness
    8,  # Dry Cough
    2,  # Wheezing
    1,  # Blood in Urine
    2,  # Difficulty Urinating
    4,  # Dribbling Urine
    2,  # Testicular Pain
    4,  # Erectile Dysfunction
    5,  # Abnormal Vaginal Discharge
    6,  # Painful Intercourse
    6,  # Irregular Menstrual Periods
    4,  # Unexplained Infertility
    5,  # Lower Back Pain
    4,  # Pelvic Pain
    6,  # Frequent Hiccups
    3,  # Difficulty Speaking
    2,  # Slurred Speech
    4,  # Tremors
    4,  # Stiffness
    5,  # Loss of Balance
    3,  # Depression
    3,  # Anxiety
    5,  # Mood Swings
    5,  # Sleep Problems
    3,  # Feeling Hopeless
    3,  # Loss of Interest
    2,  # Suicidal Thoughts
    3,  # Agitation
    4,  # Poor Concentration
    4,  # Panic Attacks
    2,  # Rapid Heartbeat
    2,  # Chest Discomfort
    5,  # Numbness or Tingling
    4,  # Swollen Ankles
    2,  # Irregular Heartbeat
    1,  # Coughing up Blood
    1,  # Blood in Stool
    1,  # Blood in Vomit
    5,  # Unexplained Weight Gain
    5,  # Heavy Menstrual Bleeding
    2,  # Breast Changes
    2,  # Nipple Discharge
    1,  # Pelvic Pressure
    6,  # Shortened Menstrual Periods
    6,  # Hot Flashes
    4,  # Night Sweats
    7,  # Insomnia
    7,  # Vaginal Dryness
    5,  # Painful Urination
    6,  # Painful Bowel Movements
    6,  # Bloating
    7,  # Abdominal Cramps
    7,  # Feeling Full Quickly
    7,  # Constant Hunger
    6,  # Change in Bowel Habits
    5,  # Swollen Legs
    5,  # Swollen Hands
    4,  # Frequent Bruising
    5,  # Difficulty Walking
    5,  # Balance Problems
    5,  # Numbness in Extremities
    6,  # Vision Changes
    4,  # Hearing Loss
    4,  # Ringing in Ears
    2,  # Chest Pressure
    6,  # Heartburn
    7,  # Indigestion
    1,  # Bloody Stool
    1,  # Bloody Urine
    1,  # Abnormal Bleeding
    1,  # Bruising Under the Skin
    4,  # Increased Urination at Night]
    ]}

    dataz = {  'Fever': 8,
    'Cough': 8,
    'Headache': 8,
    'Fatigue': 8,
    'Sore Throat': 8,
    'Shortness of Breath': 6,
    'Muscle Pain': 7,
    'Chills': 6,
    'Loss of Taste': 7,
    'Loss of Smell': 6,
    'Nausea': 8,
    'Vomiting': 7,
    'Diarrhea': 7,
    'Abdominal Pain': 7,
    'Rash': 7,
    'Chest Pain': 5,
    'Dizziness': 5,
    'Confusion': 6,
    'Swollen Lymph Nodes': 6,
    'Joint Pain': 7,
    'Blurred Vision': 5,
    'Seizures': 2,
    'Difficulty Swallowing': 2,
    'Difficulty Breathing': 6,
    'Irritability': 6,
    'Memory Problems': 5,
    'Back Pain': 7,
    'Frequent Urination': 6,
    'Night Sweats': 7,
    'Unintended Weight Loss': 4,
    'Excessive Thirst': 6,
    'Excessive Hunger': 6,
    'Frequent Infections': 4,
    'Bruising Easily': 5,
    'Unexplained Bleeding': 3,
    'Swollen Joints': 5,
    'Chest Tightness': 2,
    'Pale Skin': 4,
    'Cold Hands and Feet': 5,
    'Hair Loss': 6,
    'Frequent Headaches': 6,
    'Nosebleeds': 4,
    'Frequent Sore Throat': 6,
    'Weakness': 7,
    'Yellowing of the Skin and Eyes (Jaundice)': 2,
    'Swollen Abdomen': 1,
    'Itchy Skin': 5,
    'Swollen Glands': 5,
    'Frequent Fever': 5,
    'Frequent Chills': 4,
    'Muscle Weakness': 5,
    'Dry Cough': 8,
    'Wheezing': 2,
    'Blood in Urine': 1,
    'Difficulty Urinating': 2,
    'Dribbling Urine': 4,
    'Testicular Pain': 2,
    'Erectile Dysfunction': 4,
    'Abnormal Vaginal Discharge': 5,
    'Painful Intercourse': 6,
    'Irregular Menstrual Periods': 6,
    'Unexplained Infertility': 4,
    'Lower Back Pain': 5,
    'Pelvic Pain': 4,
    'Frequent Hiccups': 6,
    'Difficulty Speaking': 3,
    'Slurred Speech': 2,
    'Tremors': 4,
    'Stiffness': 4,
    'Loss of Balance': 5,
    'Depression': 3,
    'Anxiety': 3,
    'Mood Swings': 5,
    'Sleep Problems': 5,
    'Feeling Hopeless': 3,
    'Loss of Interest': 3,
    'Suicidal Thoughts': 2,
    'Agitation': 3,
    'Poor Concentration': 4,
    'Panic Attacks': 4,
    'Rapid Heartbeat': 2,
    'Chest Discomfort': 2,
    'Numbness or Tingling': 5,
    'Swollen Ankles': 4,
    'Irregular Heartbeat': 2,
    'Coughing up Blood': 1,
    'Blood in Stool': 1,
    'Blood in Vomit': 1,
    'Unexplained Weight Gain': 5,
    'Heavy Menstrual Bleeding': 5,
    'Breast Changes': 2,
    'Nipple Discharge': 2,
    'Pelvic Pressure': 1,
    'Shortened Menstrual Periods': 6,
    'Hot Flashes': 6,
    'Night Sweats': 4,
    'Insomnia': 7,
    'Vaginal Dryness': 7,
    'Painful Urination': 5,
    'Painful Bowel Movements': 6,
    'Bloating': 6,
    'Abdominal Cramps': 7,
    'Feeling Full Quickly': 7,
    'Constant Hunger': 7,
    'Change in Bowel Habits': 6,
    'Swollen Legs': 5,
    'Swollen Hands': 5,
    'Frequent Bruising': 4,
    'Difficulty Walking': 5,
    'Balance Problems': 5,
    'Numbness in Extremities': 5,
    'Vision Changes': 6,
    'Hearing Loss': 4,
    'Ringing in Ears': 4,
    'Chest Pressure': 2,
    'Heartburn': 6,
    'Indigestion': 7,
    'Bloody Stool': 1,
    'Bloody Urine': 1,
    'Abnormal Bleeding': 1,
    'Bruising Under the Skin': 1,
    'Increased Urination at Night': 4}

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
