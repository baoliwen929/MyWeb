#！/usr/bin/python
# coding = utf-8

__author__="Baoliwen"

from flask import Flask,request,render_template
app=Flask(__name__,static_url_path="")

@app.route("/")
def First_page():
    return render_template("test.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        return "login"
    else:
        return "register"
@app.route("/index.html")
def index(name=None):
    return render_template("index.html")


@app.route("/user/<username>")
def show_user_profile(username):
    return "user %s" %username

@app.route("/about")
def about():
    return "the about page"

if __name__=="__main__":
    app.run(debug=True)