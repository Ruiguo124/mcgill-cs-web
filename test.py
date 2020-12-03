#!/usr/bin/python3
import pymysql
import os
from flask import Flask, redirect, url_for, render_template, request, Markup
import SQL_Interface

app = Flask(__name__)

# pass usualTeaching if user doesn't have permission and editTeaching2 if he does
usualTeaching = Markup("""teaching<span style="color: red">@CS</span>""")
editTeaching2 = Markup("""<a href="/editTeaching" style="text-decoration: none; color: white"><span style="color: red">Edit Teaching</span></a>""")

@app.route("/", methods=["GET"])
def home():
    query_string = "SELECT content FROM teaching"
    data = SQL_Interface.query(query_string)
    teaching = data[0]
    #check if have permission, change usualTeaching to editTeaching
    return render_template("index.html", teaching=teaching, editTeaching=editTeaching2)

@app.route("/editTeaching", methods=["POST", "GET"])
def editTeaching():
    if request.method == "POST":
        newteaching = request.form["editArea"]
        # add to database
        teaching = Markup(newteaching)
        update_string =  """UPDATE teaching
                            SET content='{0}'
                            WHERE ID=0"""
        update_string = update_string.format(teaching)
        print("teaching content has been updated")
        return render_template("html/edit/editConfirmation.html")
    else:
        query_string = "SELECT content FROM teaching"
        data = SQL_Interface.query(query_string)
        teaching = data[0][0]
        return render_template("html/edit/editTeaching.html", teaching=teaching)

@app.route("/login", methods=["POST", "GET"])
def login():
    print("/login")
    return render_template("html/login/login.html")

@app.route("/attempt-login", methods=["POST", "GET"])
def attempt_login():
    print("/attemp-login")
    #if request.method == "POST":
        #testLog()
    return render_template("html/login/login.html")

@app.route('/prospective')
def prospective():
    return render_template("html/prospective/menu-prospective.html")

@app.route('/general_info')
def gen_info():
    query_string = "SELECT content FROM prospective WHERE ID='generalInfo'"
    data = SQL_Interface.query(query_string)
    content = data[0][0]
    return render_template("html/prospective/gen-info.html", content=content)

@app.route('/people-menu')
def people():
    return render_template("html/people/menu-people.html")

@app.route('/academic-menu')
def academic():
    return render_template("html/academic/menu-academic.html")

@app.route('/news')
def news():
    return render_template("html/news/news.html")

@app.route('/about-menu')
def about():
    return render_template("html/about/menu-about.html")

@app.route('/research')
def research():
    return render_template("html/research/research.html")

if __name__ == "__main__":
    app.run()
