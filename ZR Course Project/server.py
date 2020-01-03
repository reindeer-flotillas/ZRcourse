from flask import Flask, render_template
app = Flask(__name__)
@app.route('/homepage.html')
def load_hp():
    return render_template("homepage.html")
@app.route('/lessons.html')
def load_ls():
    return render_template("lessons.html")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port = 8888) #0.0.0.0 is localhost, port value just specifies which port
    #many ports possible
#whatever values are returned will show on the site