from flask import Flask, url_for, render_template, request, session


app=Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/ma_page')
def ma_page():
    return render_template('main.html')

if __name__=="__main__":
    app.run(debug=True)
