from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from waitress import serve
#Resources
#Department
from resources.department.list import ListDepartmentAPI
from resources.department.delete import DeleteDepartmentAPI
from resources.department.new import NewDepartmentAPI
from resources.department.update import UpdateDepartmentAPI


app = Flask(__name__, static_url_path="")
CORS(app)
app.debug = False

api = Api(app)

#Department

api.add_resource(
    ListDepartmentAPI,
    '/supply/api/v1.0/list_department/',
    endpoint='list_department'
)

api.add_resource(
    DeleteDepartmentAPI,
    '/supply/api/v1.0/delete_department/<string:id>',
    endpoint='delete_department'
)

api.add_resource(
    NewDepartmentAPI,
    '/supply/api/v1.0/new_department/',
    endpoint='new_department'
)

api.add_resource(
    UpdateDepartmentAPI,
    '/supply/api/v1.0/update_department/<string:id>',
    endpoint='update_department'
)

if __name__ == "__main__":
    app.run(debug=False)
    # serve(app, host='0.0.0.0', port=8080)