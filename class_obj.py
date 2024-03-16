class emp(object):
    collage="info tech"
    def __init__(self,sid,name):
        self.sid=sid
        self.name=name
    def disp(self):
        print("student id:",self.sid,"student name:",self.name,"collage:",emp.collage)
obj=emp(57,"darshu")
obj.name="divu"
emp.collage="nirma"
obj.disp()
