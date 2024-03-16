class employee(object):
    ' this is built in attribut program'
    ecount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.ecount+=1
    def display(self):
        print("employee object count",employee.ecount)
    def displayemp(self):
        print("employee name:",self.name,"employee salary:",self.salary)
obj=employee("darshu",20000)
obj.display()
obj.displayemp()
print("employee .__doc__ :",obj.__doc__)
print("employee.__name__:",employee.__name__)
print("employee .__module__:",obj.__module__)
print("employee .__bases__:",employee.__bases__)
print("employee .__dict__ :",obj.__dict__)

