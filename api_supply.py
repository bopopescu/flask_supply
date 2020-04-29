from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from waitress import serve
# Resources

# Admin Support
from resources.admin_support.list import ListAdminSupportAPI
from resources.admin_support.delete import DeleteAdminSupportAPI
from resources.admin_support.new import NewAdminSupportAPI
from resources.admin_support.update import UpdateAdminSupportAPI

# Department
from resources.department.list import ListDepartmentAPI
from resources.department.delete import DeleteDepartmentAPI
from resources.department.new import NewDepartmentAPI
from resources.department.update import UpdateDepartmentAPI

# Department Country Support
from resources.department_country_support.list import ListDepartmentCountrySupportAPI
from resources.department_country_support.delete import DeleteDepartmentCountrySupportAPI
from resources.department_country_support.new import NewDepartmentCountrySupportAPI
from resources.department_country_support.update import UpdateDepartmentCountrySupportAPI

# Department Involved
from resources.department_involved.list import ListDepartmentInvolvedAPI
from resources.department_involved.delete import DeleteDepartmentsInvolvedAPI
from resources.department_involved.new import NewDepartmentInvolvedAPI
from resources.department_involved.update import UpdateDepartmentInvolvedAPI

# Employee In Charge
from resources.employee_in_charge.list import ListEmployeeInChargeAPI
from resources.employee_in_charge.delete import DeleteEmployeeInChargeAPI
from resources.employee_in_charge.new import NewEmployeeInChargeAPI
from resources.employee_in_charge.update import UpdateEmployeeInChargeAPI

# Problem Type
from resources.problem_type.list import ListProblemTypeAPI
from resources.problem_type.delete import DeleteProblemTypesAPI
from resources.problem_type.new import NewProblemTypesAPI
from resources.problem_type.update import UpdateProblemTypesAPI

# Request
from resources.request.list import ListRequestAPI
from resources.request.delete import DeleteRequestAPI
from resources.request.new import NewRequestAPI
from resources.request.update import UpdateRequestAPI
from resources.request.count import CountRequestAPI

# Request Update
from resources.request_update.list import ListRequestUpdateAPI
from resources.request_update.delete import DeleteRequestUpdateAPI
from resources.request_update.new import NewRequestUpdateAPI
from resources.request_update.update import UpdateRequestUpdateAPI

# Support Department
from resources.support_department.list import ListSupportDepartmentAPI
from resources.support_department.delete import DeleteSupportDepartmentAPI
from resources.support_department.new import NewSupportDepartmentAPI
from resources.support_department.update import UpdateSupportDepartmentAPI

# Users
from resources.users.list import ListUsersAPI
from resources.users.delete import DeleteUserAPI
from resources.users.new import NewUserAPI
from resources.users.update import UpdateUserAPI

app = Flask(__name__, static_url_path="")
CORS(app)
app.debug = False

api = Api(app)

#Admin Support
api.add_resource(
    ListAdminSupportAPI,
    '/supply/api/v1.0/list_admin_support/',
    endpoint='list_admin_support'
)

api.add_resource(
    DeleteAdminSupportAPI,
    '/supply/api/v1.0/delete_admin_support/<string:id>',
    endpoint='delete_admin_support'
)

api.add_resource(
    NewAdminSupportAPI,
    '/supply/api/v1.0/new_admin_support/',
    endpoint='new_admin_support'
)

api.add_resource(
    UpdateAdminSupportAPI,
    '/supply/api/v1.0/update_admin_support/<string:id>',
    endpoint='update_admin_support'
)

#################    Department   ##########################

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

#################    Department Country Support  ##########################

api.add_resource(
    ListDepartmentCountrySupportAPI,
    '/supply/api/v1.0/list_department_country_support/',
    endpoint='list_department_country_support'
)

api.add_resource(
    DeleteDepartmentCountrySupportAPI,
    '/supply/api/v1.0/delete_department_country_support/<string:id>',
    endpoint='delete_department_country_support'
)

api.add_resource(
    NewDepartmentCountrySupportAPI,
    '/supply/api/v1.0/new_department_country_support/',
    endpoint='new_department_country_support'
)

api.add_resource(
    UpdateDepartmentCountrySupportAPI,
    '/supply/api/v1.0/update_department_country_support/<string:id>',
    endpoint='update_department_country_support'
)

#################    Department Involved  ##########################

api.add_resource(
    ListDepartmentInvolvedAPI,
    '/supply/api/v1.0/list_department_involved/',
    endpoint='list_department_involved'
)

api.add_resource(
    DeleteDepartmentsInvolvedAPI,
    '/supply/api/v1.0/delete_department_involved/<string:id>',
    endpoint='delete_department_involved'
)

api.add_resource(
    NewDepartmentInvolvedAPI,
    '/supply/api/v1.0/new_department_involved/',
    endpoint='new_department_involved'
)

api.add_resource(
    UpdateDepartmentInvolvedAPI,
    '/supply/api/v1.0/update_department_involved/<string:id>',
    endpoint='update_department_involved'
)

##################   Employee In Charge #########################
api.add_resource(
    ListEmployeeInChargeAPI,
    '/supply/api/v1.0/list_employee_in_charge/',
    endpoint='list_employee_in_charge'
)

api.add_resource(
    DeleteEmployeeInChargeAPI,
    '/supply/api/v1.0/delete_employee_in_charge/<string:id>',
    endpoint='delete_employee_in_charge'
)

api.add_resource(
    NewEmployeeInChargeAPI,
    '/supply/api/v1.0/new_employee_in_charge/',
    endpoint='new_employee_in_charge'
)

api.add_resource(
    UpdateEmployeeInChargeAPI,
    '/supply/api/v1.0/update_employee_in_charge/<string:id>',
    endpoint='update_employee_in_charge'
)
#######################   Problem Type #########################
api.add_resource(
    ListProblemTypeAPI,
    '/supply/api/v1.0/list_problem_type/',
    endpoint='list_problem_type'
)

api.add_resource(
    DeleteProblemTypesAPI,
    '/supply/api/v1.0/delete_problem_type/<string:id>',
    endpoint='delete_problem_type'
)

api.add_resource(
    NewProblemTypesAPI,
    '/supply/api/v1.0/new_problem_type/',
    endpoint='new_problem_type'
)

api.add_resource(
    UpdateProblemTypesAPI,
    '/supply/api/v1.0/update_problem_type/<string:id>',
    endpoint='update_problem_type'
)

####################   Request   #########################
api.add_resource(
    ListRequestAPI,
    '/supply/api/v1.0/list_request/',
    endpoint='list_request'
)

api.add_resource(
    DeleteRequestAPI,
    '/supply/api/v1.0/delete_request/<string:id>',
    endpoint='delete_request'
)

api.add_resource(
    NewRequestAPI,
    '/supply/api/v1.0/new_request/',
    endpoint='new_request'
)

api.add_resource(
    UpdateRequestAPI,
    '/supply/api/v1.0/update_request/<string:id>',
    endpoint='update_request'
)

api.add_resource(
    TicketsCountAPI,
    '/supply/api/v1.0/tickets_count/',
    endpoint='tickets_count'
)

############   Request Update   ##########################
api.add_resource(
    ListRequestUpdateAPI,
    '/supply/api/v1.0/list_request_update/',
    endpoint='list_request_update'
)

api.add_resource(
    DeleteRequestUpdateAPI,
    '/supply/api/v1.0/delete_request_update/<string:id>',
    endpoint='delete_request_update'
)

api.add_resource(
    NewRequestUpdateAPI,
    '/supply/api/v1.0/new_request_update/',
    endpoint='new_request_update'
)

api.add_resource(
    UpdateRequestUpdateAPI,
    '/supply/api/v1.0/update_request_update/<string:id>',
    endpoint='update_request_update'
)

#############   Support Department  ###################
api.add_resource(
    ListSupportDepartmentAPI,
    '/supply/api/v1.0/list_support_department/',
    endpoint='list_support_department'
)

api.add_resource(
    DeleteSupportDepartmentAPI,
    '/supply/api/v1.0/delete_support_department/<string:id>',
    endpoint='delete_support_department'
)

api.add_resource(
    NewSupportDepartmentAPI,
    '/supply/api/v1.0/new_support_department/',
    endpoint='new_support_department'
)

api.add_resource(
    UpdateSupportDepartmentAPI,
    '/supply/api/v1.0/update_support_department/<string:id>',
    endpoint='update_support_department'
)

#################    Users  ##########################

api.add_resource(
    ListUsersAPI,
    '/supply/api/v1.0/list_user/',
    endpoint='list_user'
)

api.add_resource(
    DeleteUserAPI,
    '/supply/api/v1.0/delete_user/<string:id>',
    endpoint='delete_user'
)

api.add_resource(
    NewUserAPI,
    '/supply/api/v1.0/new_user/',
    endpoint='new_user'
)

api.add_resource(
    UpdateUserAPI,
    '/supply/api/v1.0/update_user/<string:id>',
    endpoint='update_user'
)

if __name__ == "__main__":
    app.run(debug=False)
    # serve(app, host='0.0.0.0', port=8080)
