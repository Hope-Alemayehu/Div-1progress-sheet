# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        total_importance = 0
        #to map empoloyee id with each employee
        emp_dict = {emp.id: emp for emp in employees}
        qu = [id]

        while qu:
            curr_id = qu.pop(0)
            curr_emp = emp_dict[curr_id]
            total_importance += curr_emp.importance
            qu.extend(curr_emp.subordinates)

        return total_importance
