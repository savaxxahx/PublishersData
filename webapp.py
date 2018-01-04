from flask import Flask, render_template, request , Markup, flash , Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)



@app.route("/")
def render_main():
    return render_template('home.html')
	
@app.route("/publishers")
def render_publishers():
    if "publishertype" in request.args:
        return render_template('publishers.html', type2 = compare_data(), publishers = publisher_list(request.args["publishertype"]))
    else:
	    return render_template('publishers.html', type2 = compare_data())

@app.route("/comparison")
def render_compare():
    if "publishertype" in request.args:
       return render_template('comparison.html', type1= compare_data(), info = get_info(request.args["publishertype"]))
    else:
       return render_template('comparison.html', type1 = compare_data())
	   
@app.route("/genre")
def render_genre():
    return render_template('genre.html', genredata = genre_list())
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

def get_info(publishertype):
    with open('publishers.json') as publishers_data:
        books = json.load(publishers_data)
    first = books[0]["statistics"]["average rating"]
    x = books[0]["daily"]["units sold"]
    y = books[0]["daily"]["gross sales"]
    for b in books:
        if b["publisher"]["type"] == publishertype:
            if b["statistics"]["average rating"]> first:
                first = b["statistics"]["average rating"]
            if b["daily"]["units sold"]> x:
                x = b["daily"]["units sold"]
            if b["daily"]["gross sales"] > y:
                y = b["daily"]["gross sales"]
    return str(" For") + " " + publishertype + str(" the highest units sold is") + " " + str(x) + str(",") + str(" the higest average rating is") +" " +  str(first)+ str(",") +" " + str("and the highest gross sales is") + " " + str(y) + str(".")
	
def publisher_list(publishertype):
    with open('publishers.json') as publishers_data:
        books = json.load(publishers_data)
    names = []
    for b in books:
        if b["publisher"]["type"] == publishertype:
            if b["publisher"]["name"] not in names:
                names.append(b["publisher"]["name"])

				
    return names
            
def genre_list():
    with open('publishers.json') as publishers_data:
        books = json.load(publishers_data)
    genre ={}
    for b in books:
        if b["genre"] not in genre:
            genre[b["genre"]] = 1
        if b["genre"] in genre:
            genre[b["genre"]] = genre[b["genre"]] +1
    g = "{"
    for s in genre:
	    g += Markup("x:" + "'" + s + "'"+ ", y:"+ str(genre[s]) + "},{")

    return g[0:-2]

if __name__=="__main__":
    app.run(debug=True, port=54321)
