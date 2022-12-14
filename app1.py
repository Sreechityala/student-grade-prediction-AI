from flask import Flask,render_template,request
import pickle

model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def homepage():
    return(render_template('stu.html'))

@app.route('/predict',methods=['POST'])
def collectData():
    S=float(request.form['S'])
    F=float(request.form['F'])
    A=float(request.form['A'])
    G1=float(request.form['G1'])
    G2=float(request.form['G2'])
    print(S,F,A,G1,G2)
    result=model.predict([[S,F,A,G1,G2]])
    return(render_template('stu.html',result=str(result[0])))

if __name__=="__main__":
    app.run(debug=True)