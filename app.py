from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process')
def process():
    return True

if __name__ == "__main__":
    app.run(debug=True)
