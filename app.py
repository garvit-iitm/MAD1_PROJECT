from flask import Flask,render_template

app = Flask(__name__)

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/admin")
def admin_page():
    return render_template('admin.html')

@app.route("/base")
def base():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
