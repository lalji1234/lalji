import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
student = [
    {'id': 100,
     'Name': 'Ram Kumar',
     'Address': 'Tambaram',
     'Total_mark': '480',
     'Passing_year': '2012'},
    {'id': 101,
     'Name': 'Shyam Sah',
     'Address': 'Crompet',
     'Total_mark': '450',
     'Passing_year': '2013'},
    {'id': 102,
     'Name': 'Balamurgan',
     'Address': 'Checpet',
     'Total_mark': '490',
     'Passing_year': '2014'},
    {'id': 103,
     'Name': 'Pavi Vas',
     'Address': 'Chennai Central',
     'Total_mark': '500',
     'Passing_year': '2015'},
     {'id': 104,
     'Name': 'Vasvi',
     'Address': 'chengalpet',
     'Total_mark': '520',
     'Passing_year': '2016'}

]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Please check your result</h1>
<p>Through this you will get more information about student.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/students', methods=['GET'])
def api_all():
    return jsonify(student)


@app.route('/api/students/id', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in student:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)




app.run()