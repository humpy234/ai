#Q1
def means_end(start, goal):
    print("Current State:", start)

    if start == goal:
        print("Goal Reached!")
    else:
        print("Action: Move towards the goal")
        means_end(goal, goal)

means_end("Home", "College")

#Q2
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = {
    'Study_Hours': [2,3,4,5,6,7,1,2,5,8],
    'Attendance': [60,65,70,75,80,85,55,62,78,90],
    'Assignment_Score': [55,60,65,70,75,80,50,58,72,85],
    'Result': ['Fail','Fail','Pass','Pass','Pass',
               'Pass','Fail','Fail','Pass','Pass']
}

df = pd.DataFrame(data)
X = df.drop('Result', axis=1)
y = df['Result']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("Prediction:", model.predict([[4, 70, 65]])[0])


