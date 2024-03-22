import json
import joblib
import numpy as np
# curl -X POST https://<lambda-url> -H "Content-Type: application/json" -d '{"Num_Children": 2, "Income": 50000, "Own_Car": 1, "Own_Housing": 0}'
#  0 (deny) or 1 (approve)

# Load the DecisionTreeClassifier model. It's more efficient to load the model once when the Lambda function is initialized
# rather than loading it each time the function is invoked.
model = joblib.load("selected_model.joblib")  # Assuming the model is stored in the Lambda at the same level

def lambda_handler(event, context):
    #print('\n', event, '\n event body\n' ,event['body'], '\n end event body \n', context,'\n')
    #print(event)
    #print(event['Own_Car'])
    # Parse the incoming JSON payload
    data = event #json.loads(event['body'])
    
    # The input features must be in the correct order expected by the model.
    # ['Num_Children', 'Income', 'Own_Car', 'Own_Housing']
    features = np.array([[data['Num_Children'], data['Income'], data['Own_Car'], data['Own_Housing']]]) 
    
    # Use the model to predict the outcome
    # DecisionTreeClassifier's predict method returns an array of predictions
    prediction = model.predict(features)
    
    # Convert the prediction array to a list and respond with the first prediction
    # assuming binary classification: 0 (deny) or 1 (approve)
    prediction_response = prediction.tolist()[0]
    
    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': prediction_response})
    }
