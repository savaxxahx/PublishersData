from flask import Flask, render_template, request , Markup, flash , Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)



@app.route("/")
def render_main():
    return render_template('home.html')

def compare_data():
      with open('publishers.json') as publishers_data:
        books = json.load(publishers_data)




if __name__=="__main__":
    app.run(debug=False, port=54321)
