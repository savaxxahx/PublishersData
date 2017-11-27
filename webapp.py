from flask import Flask, render_template, request , Markup, flash , Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)



@app.route("/")
def render_main():
    return render_template('home.html')


@app.route("/comparison")
def render_compare():
    return render_template('comparison.html', type= compare_data())
    
    
def compare_data():
    with open('publishers.json') as publishers_data:
        books = json.load(publishers_data)
    types = []
    for b in books:
        if b["publisher"]["type"] not in types:
            types.append(b["publisher"]["type"])
         
    options = ""
    for s in types:
        options+=Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options




if __name__=="__main__":
    app.run(debug=True, port=54321)
