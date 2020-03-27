from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from waitress import serve
from resources.admin_support.list import ListAdminSupportAPI
from resources.department.list import ListDepartmentAPI
from resources.department_country_support import ListDepartmentCountrySupportAPI
from resources.department_involved import ListDepartmentInvolvedAPI
from resources.employee_in_charge import ListEmployeeInChargeAPI
from resources.problem_type import ListProblemTypeAPI
from resources.request import ListRequestAPI
from resources.request_update import ListRequestUpdateAPI
from resources.support_department import ListSupportDepartmentAPI
from resources.users import ListUsersAPI
from resources.admin_support.delete import DeleteAdminSupportAPI

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

api.add_resource(
    ListAdminSupportAPI,
    '/supply/api/v1.0/list_admin_support/',
    endpoint='list_admin_support'
)

api.add_resource(
    ListDepartmentCountrySupportAPI,
    '/supply/api/v1.0/list_department_country_support/',
    endpoint='list_department_country_support'
)

api.add_resource(
    ListDepartmentInvolvedAPI,
    '/supply/api/v1.0/list_department_involved/',
    endpoint='list_department_involved'
)

api.add_resource(
    ListEmployeeInChargeAPI,
    '/supply/api/v1.0/list_employee_in_charge/',
    endpoint='list_employee_in_charge'
)

api.add_resource(
    ListProblemTypeAPI,
    '/supply/api/v1.0/list_problem_type/',
    endpoint='list_problem_type'
)

api.add_resource(
    ListProblemTypeAPI,
    '/supply/api/v1.0/list_problem_type/',
    endpoint='list_problem_type'
)

api.add_resource(
    ListRequestAPI,
    '/supply/api/v1.0/list_request/',
    endpoint='list_request'
)

api.add_resource(
    ListRequestUpdateAPI,
    '/supply/api/v1.0/list_request_update/',
    endpoint='list_request_update'
)

api.add_resource(
    ListSupportDepartmentAPI,
    '/supply/api/v1.0/list_support_department/',
    endpoint='list_support_department'
)

api.add_resource(
    ListUsersAPI,
    '/supply/api/v1.0/list_users/',
    endpoint='list_users'
)

api.add_resource(
    DeleteAdminSupportAPI,
    '/supply/api/v1.0/delete_admin_support/<string:id>',
    endpoint='delete_admin_support'
)
>>>>>>> 23069ae3e5c11f9eb5e0cf577a50e49cdda7b125

if __name__=='__main__':
    app.run(debug=False)
    # serve(app, host='0.0.0.0', port=8080)

# curl -u root:123456  http://127.0.0.1:5000//supply/api/v1.0/list_department/
