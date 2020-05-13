from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import threading
import random
import time
from generation2 import generate

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
            result = get_result(
                ctrl_prompt, 
                ctrl_seed, 
                ctrl_generate_num, 
                ctrl_temperature, 
                ctrl_nucleus, 
                ctrl_topk, 
                ctrl_penalty, 
                ctrl_print_once, 
                ctrl_topn)
            flash(result)
        else:
            flash('Enter a prompt.')
    return render_template('ctrl-demo.html', form=form)

def get_result(prompt, seed, generate_num, temperature, nucleus, topk, penalty, print_once, topn):

    # 
    seed = 1137         if seed == ''           else int(seed)
    generate_num = 256  if generate_num == ''   else int(generate_num)
    temperature = 0     if temperature == ''    else int(temperature)
    nucleus = 0.        if nucleus == ''        else float(nucleus)
    topk = 0            if topk == ''           else int(topk)
    penalty = 1.2       if penalty == ''        else float(penalty)
    print_once = False  if print_once == ''     else True
    topn = 0            if topn == ''           else int(topn)

    result = generate(
        'seqlen256_v1.ckpt/model.ckpt-413000.data-00000-of-00001',
        prompt,
        random_seed = seed,
        generate_num = generate_num,
        temperature = temperature,
        nucleus = nucleus,
        topk = topk,
        penalty = penalty,
        print_once = prince_once,
        topn = topn
    )
    return result
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
