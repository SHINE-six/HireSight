from preprocess import preprocess_text, postprocess_text
from features import feature_extraction
import joblib
import nltk
import json

nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('words')

def predict_text(df):
    model = joblib.load('ai_text_detector/app/model/gb_model_v1.pkl')
    pca = joblib.load('ai_text_detector/app/model/pca_v5.pkl')
    

    X = df.drop(['normal_text', 'cleaned_text'], axis=1)
    X_pca = pca.transform(X)

    prediction_proba = model.predict_proba(X_pca)
    prediction = model.predict(X_pca)

    return prediction, prediction_proba


def main():
    text = """
ETL, which stands for Extract, Transform, Load, is a fundamental process in data management and analytics used to consolidate 
and organize data from various sources into a unified format for analysis, reporting, and decision-making purposes. The process begins with extraction, 
where data is gathered from disparate sources such as databases, applications, files, or even streaming platforms. This extraction phase involves 
identifying relevant data and retrieving it in its raw form. Once extracted, the data undergoes transformation, which encompasses several operations 
including cleaning, filtering, aggregating, and structuring the data to conform to a predefined schema or data model. Transformation may also involve 
enriching the data by integrating it with supplementary sources, performing calculations, or applying business rules to ensure consistency and accuracy.
 Finally, the transformed data is loaded into a target database, data warehouse, or analytical platform where it can be accessed, queried, and analyzed 
 by users or applications. ETL processes are essential for maintaining data integrity, improving data quality, and enabling organizations to derive 
 valuable insights from their data assets. Additionally, ETL pipelines can be automated and scheduled to ensure the timely and efficient processing 
 of data, facilitating real-time analytics and decision-making.
#     """ # This is the data i need put text here

    process_data = preprocess_text(text)

    feature_df = feature_extraction(process_data)

    result_df = postprocess_text(feature_df)

    prediction, prediction_proba = predict_text(result_df)

    probability_human = round(prediction_proba[0][0] * 100, 2)
    probability_ai = round(prediction_proba[0][1] * 100, 2)
    
    if prediction == 0:
        result = "human"
    else:
        result = "ai"
    data = {
    "final_result": result,
    "probability_human": str(probability_human),
    "probability_ai": str(probability_ai)
    }
    json_data = json.dumps(data)
    return json_data
    # return jsonify({'result': result, 'probability1': str(probability_human), 'probability2': str(probability_ai)})

print(main())

