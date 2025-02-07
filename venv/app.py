from flask import Flask , request,render_template

app = Flask(__name__)

@app.route("/")
def resume():
    return render_template('resume.html')

# python main
if __name__=="__main__":
    app.run(debug=True)