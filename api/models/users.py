class StoreEmployee(object):
    def __init__(self, employee_id, employee_name, gender, email):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.gender = gender
        self.email = email
        

class Store_Attendant(StoreEmployee):
    def __init__(self, employee_id, employee_name,  gender, email, attendantUser_name, attendant_password):
        super().__init__(employee_id, employee_name, gender, email )
        self.store_attendantUser_name = attendantUser_name
        self.store_attendant_password = attendant_password


class Admin(StoreEmployee):
    def __init__(self, employee_id, employee_name, gender, email, adminUser_name, admin_password):
        super().__init__(employee_id, employee_name, gender, email)
        self.adminUser_name = adminUser_name
        self.admin_password = admin_password


