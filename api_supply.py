from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from waitress import serve
from resources.department.list import ListDepartmentAPI

app = Flask(__name__, static_url_path="")
CORS(app)
app.debug = False

api = Api(app)

api.add_resource(
    ListDepartmentAPI,
    '/supply/api/v1.0/list_department/',
    endpoint='list_department'
)

if __name__=='__main__':
    app.run(debug=False)
    # serve(app, host='0.0.0.0', port=8080)
