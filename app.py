from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/admin")
def admin_page():
    return render_template('admin.html')

@app.route("/user")
def user_page():
    return render_template('user.html')

if __name__ == "__main__":
    app.run(debug=True)
