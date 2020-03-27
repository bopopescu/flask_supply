from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from waitress import serve
#LIST
from resources.department.list import ListDepartmentAPI
from resources.admin_support.list import ListAdminSupportAPI



#DELETE
from resources.admin_support.delete import DeleteAdminSupportAPI
from resources.department.delete import DeleteDepartmentAPI
from resources.department_country_support.delete import DeleteDepartmentCountrySupportAPI
from resources.department_involved.delete import DeleteDepartmentsInvolvedAPI
from resources.employee_in_charge.delete import DeleteEmployeeInChargeAPI
from resources.problem_type.delete import DeleteProblemTypesAPI
#from resources.request.delete import


app = Flask(__name__, static_url_path="")
CORS(app)
app.debug = False

api = Api(app)
#LIST
api.add_resource(
    ListDepartmentAPI,
    '/supply/api/v1.0/list_department/',
    endpoint='list_department'
)

#DELETE
api.add_resource(
    DeleteAdminSupportAPI,
    '/supply/api/v1.0/delete_admin_support/<string:id>',
    endpoint='delete_admin_support'
)

api.add_resource(
    DeleteDepartmentAPI,
    '/supply/api/v1.0/delete_department/<string:id>',
    endpoint='delete_department'
)

api.add_resource(
    DeleteDepartmentCountrySupportAPI,
    '/supply/api/v1.0/delete_department_country_support/<string:id>',
    endpoint='delete_department_country_support'
)

api.add_resource(
    DeleteDepartmentsInvolvedAPI,
    '/supply/api/v1.0/delete_department_involved/<string:id>',
    endpoint='delete_department_involved'
)

api.add_resource(
    DeleteProblemTypesAPI,
    '/supply/api/v1.0/delete_problem_types/<string:id>',
    endpoint='delete_problem_types'
)


if __name__=='__main__':
    app.run(debug=False)
    # serve(app, host='0.0.0.0', port=8080)
