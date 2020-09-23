#import zone
from . import app, db
from flask import render_template, request, redirect, url_for, session, flash
from .forms import Input, Update
from .functions import dota2_dictionary, update_baseinfo, create_numerical_hist, export_csv_num_history
from .backend_update import update_history_backend
from .logistic_regression_model import logistic_regression, decode_result
import pickle
############


@app.route('/backend_update')
def backend_update():
    update_history_backend()
    return redirect(url_for('retrain_model'))

############

@app.route('/')
@app.route('/index', methods=['POST','GET'])
def predict():
    form_i = Input()
    if request.method == 'POST': 
        X_input = dota2_dictionary(form_i.tm_r.data, form_i.pos1_r.data, form_i.pos2_r.data, form_i.pos3_r.data,
                                   form_i.pos4_r.data, form_i.pos5_r.data, form_i.tm_d.data, form_i.pos1_d.data,
                                   form_i.pos2_d.data, form_i.pos3_d.data, form_i.pos4_d.data, form_i.pos5_d.data)
        session["input"] = X_input
        return redirect(url_for('show_predict'))
    return render_template('index.html', form=form_i)




@app.route('/predict', methods=['POST','GET'])
def show_predict():

    form_i = Input()

    X_input = session.get("input", None)

    logistic_regression_model = pickle.load(open('app/ML_model/logistic_regression_model.pkl','rb'))

    logistic_regression_pred = logistic_regression_model.predict(X_input)

    prob_pred = logistic_regression_model.predict_proba(X_input)

    result, prob = decode_result(logistic_regression_pred, prob_pred)
    
    return render_template('index.html', form=form_i, results=result, prob=prob)


@app.route('/name_encyclopedia')
def name_encyclopedia():
    return render_template('name_encyclopedia.html')


@app.route('/update', methods=['POST','GET'])
def update():
    form_u = Update()
    if request.method == 'POST':
        update_baseinfo(form_u.tm_r.data, form_u.pos1_r.data, form_u.pos2_r.data, form_u.pos3_r.data, form_u.pos4_r.data,
                        form_u.pos5_r.data, form_u.tm_d.data, form_u.pos1_d.data, form_u.pos2_d.data, form_u.pos3_d.data,
                        form_u.pos4_d.data, form_u.pos5_d.data, form_u.a_result.data, form_u.time_stamp.data)
        
    return render_template('update.html', form=form_u, title='Update')

@app.route('/retrain_model', methods=['POST','GET'])
def retrain_model():
    if request.method == 'POST':
        if request.form.get('prepare_data'):
            # return render_template('debugging.html')
            create_numerical_hist()
            export_csv_num_history()
        elif request.form.get('logistic_regression_model'):
            logistic_regression()
        
    return render_template('retrain_model.html')



