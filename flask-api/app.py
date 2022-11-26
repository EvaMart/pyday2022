from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
from flask_cors import CORS, cross_origin


# https://flask.palletsprojects.com/en/2.2.x/quickstart/
app = Flask(__name__)


# connect to the database
def connect_to_db():
    '''
    Connect to the database and returns the snippets collection
    NOTE: Hardcoded for dev purposes, but should be changed to use 
    environment variables or a config file for production    
    '''
    connection = MongoClient('localhost', 27019)
    snippets = connection["PyDayBCN"]["snippets"]
    return snippets


def get_snippets():
    '''
    Get snippets from the database
    '''
    try:
        # connect to the collection in the DB
        snippets = connect_to_db()

        # get all the snippets as a list
        snippets_list = list(snippets.find())

        # remove the _id field from the response, 
        # as it is not needed and it is not JSON serializable
        [entry.pop('_id') for entry in snippets_list]

    # return a response + status code
    except Exception as err:
        # if there is an error, return a 500 response
        error_msg = f"Error getting snippets: {err}"
        resp = make_response(jsonify(error_msg), 503)
    
    else:
        # if everything went well, return a 200 response 
        # and the requested list of snippets
        resp = make_response(jsonify(snippets_list), 201)
    
    finally:    
        return resp

def get_snippet_by_type(snippet_type):
    '''
    Get snippets by type from the database
    '''
    try:
        snippets = connect_to_db()
        snippets_list = list(snippets.find({"type": snippet_type}))
        [entry.pop('_id') for entry in snippets_list]
    except Exception as err:
        error_msg = f"Error getting snippets: {err}"
        resp = make_response(jsonify(error_msg), 503)
    else:
        resp = make_response(jsonify(snippets_list), 201)

    finally:    
        return resp

def add_snippet(snippet_content):
    '''
    Add a  single snippet to the database
    `snippet_content`: content of the snippet
    '''
    try:
        snippets = connect_to_db()
        snippets.insert_one(snippet_content)
    
    except Exception as err:
        error_msg = f"Error adding snippet: {err}"
        resp = make_response(jsonify(error_msg), 400)
    
    else:
        # if everything went well, return a 201 response and a success message
        resp = make_response(jsonify("Snippet added successfully"), 201)
    
    finally:    
        return resp



@app.route('/snippet', methods=['GET', 'POST'])
@cross_origin(origin='*')
def snippet(): 
    '''
    get all snippets in the database
    '''
    if request.method == 'GET':
        if request.args.get('type'):
            data = get_snippet_by_type(request.args.get('type'))
        else:
            data = get_snippets()

    elif request.method == 'POST':
        data = add_snippet(request.json)
    
    return data



if __name__ == '__main__':
    # run the app in debug mode when script is executed directly
    app.run(debug=True, port=3500)
