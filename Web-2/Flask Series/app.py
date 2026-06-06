from flask import Flask, render_template, request
from form import NameForm

app = Flask(__name__)
app.secret_key = 'Sr2Beg+JFhtvQu3y' 

@app.route('/') # @ is decorator
def root():
    return render_template('index.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

@app.route('/wt-form', methods=['GET', 'POST'])
def formFunction():
    error = None
    form = NameForm()
    if form.validate_on_submit():
        return f"<p>I got to know that your name is {form.name.data}</p>"
    return render_template('wt-form.html', form = form)

if __name__ == '__main__':
    app.run(debug=True,port=5000)