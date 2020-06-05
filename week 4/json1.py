class Student:
    def __init__(self,**kwargs):
        self.stud_rec = dict()
        Student.add_student(self,**kwargs)
        
    def __repr__(self):
        return ','.join(list(self.stud_rec.keys()))
        
    def add_student(self,**kwargs):
        self.stud_rec[kwargs['Name']] = kwargs