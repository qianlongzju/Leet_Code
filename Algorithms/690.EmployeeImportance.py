"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for employee in employees:
            d[employee.id] = employee
        q = [id]
        total_importance = 0
        while q:
            id = q.pop(0)
            employee = d[id]
            total_importance += employee.importance
            for subordinate in employee.subordinates:
                q.append(subordinate)
        return total_importance
