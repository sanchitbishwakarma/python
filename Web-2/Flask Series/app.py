from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/formm', methods=['GET', 'POST'])
def formm():
    error = None
    
    if request.method == 'POST':
        name = request.form['name'].strip()

        if not name:
            error = "Name cannot be empty"
        else:
            return f"You're very awesome, {name}"
    return render_template('form.html', error = error)

if __name__ == '__main__':
    app.run(debug=True,port=5000)