from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import threading
import random
import time
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    prompt = TextField('Prompt:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def send_prompt():
    form = ReusableForm(request.form)
    #print(form.errors)
    if request.method == 'POST':
        ctrl_prompt         =request.form['prompt']
        ctrl_seed           =request.form['seed']
        ctrl_generate_num   =request.form['generate_num']
        ctrl_temperature    =request.form['temperature']
        ctrl_nucleus        =request.form['nucleus']
        ctrl_topk           =request.form['topk']
        ctrl_penalty        =request.form['penalty']
        ctrl_print_once     =request.form['print_once']
        ctrl_topn           =request.form['topn']
        if form.validate():
            flash('{}{}{}{}{}{}{}{}{}'.format(
                ctrl_prompt,
                ctrl_seed,
                ctrl_generate_num,
                ctrl_temperature,
                ctrl_nucleus,
                ctrl_topk,
                ctrl_penalty,
                ctrl_print_once,
                ctrl_topn
                ))
        else:
            flash('Enter a prompt.')
    return render_template('test_ctrl.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
