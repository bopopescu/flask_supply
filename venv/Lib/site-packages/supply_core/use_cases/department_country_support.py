class DepartmentCountrySupport(object):

    def _init_(self, storage_bridge):
        self.storage_adapter = storage_bridge

    def list(self):
        try:
            value = self.storage_adapter.list()
            return value
        except:
            return "There is a problem"

    def new(self, company):
        try:
            value = self.storage_adapter.new(company)
            return value
        except Exception:
            return "There is a problem"

    def delete(self, id):
        try:
            value = self.storage_adapter.delete(id)
            return value
        except Exception:
            return "There is a problem"

    def update(self, id, department):
        try:
            value = self.storage_adapter.update(id, department)
            return value
        except Exception:
            return "There is a problem"
