from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/java')
def java():
    return render_template('javapoem.html')


if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0")