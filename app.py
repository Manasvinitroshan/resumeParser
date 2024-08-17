from flask import Flask, request, render_template
import pickle
from PyPDF2 import PdfReader
import re


#helper functions
def pdf_to_text(file):
    reader = PdfReader(file)
    text = ''
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text


#cleaning the resume from the redundant fillers:
def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)  
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText) 
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText


#predict and categorize
def predict_categorize(resume_text):

    resume_text = cleanResume(resume_text)
    resume_tfdif = tfidf_vectorizer.transform([resume_text])
    predicted_category = rf_classifier_1


#import the models

rf_classifier_categorization = pickle.load(open('models/rf_classifier_categorization.pkl', 'rb'))
tfidf_vectorizer_categorization = pickle.load(open('models/tfidf_vectorizer_categorization.pkl', 'rb'))
rf_classifier_job_recommendation = pickle.load(open('models/rf_classifier_job_recommendation.pkl', 'rb'))
tfidf_vectorizer_job_recommendation = pickle.load(open('models/tfidf_vectorizer_job_recommendation.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def resume():
    return render_template('resume.html')

@app.route("/pred",methods=["POST"])

def pred():
    if 'resume' in request.files:
        file = request.files['resume']
        filename = file.filename

        if filename.endwith('.pdf'):
            text = pdf_to_text(file) #this is from Py2PDf and this is what converts the pdf to text

        else:
            
            return render_template('resume.html', message="Invalid file format please input a PDF")
        

        




if __name__ == '__main__':
    app.run(debug=True)