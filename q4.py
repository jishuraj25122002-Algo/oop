class Student :
  def __init__ (self, name,marks):
    self.name=name
    self.marks=marks 
  def average(self):
    return sum(self.marks) / len(self.marks)

s1 = Student(" Alice " , [ 85 , 48 ,29 ,39 ,92])
print(f" {s1.name} 's  Average Grade : {s1.average()}")    