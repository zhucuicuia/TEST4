/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stu_count=0
   stu_count_male = 0
   stu_count_female= 0
   def __init__(self,stu_no,name,stu_class,male,female,stu_count):
      self.name = name
      self.stu_no = stu_no
      self.stu_class=stu_class
      self.male=male
      self.female=female
      Student.stu_count += 1
      if self.stu_male== 'male':
         Student.stu_count_male +=1
      elif self.stu_female =='female':
            Student.stu_count_female +=1
         
   
   
   def displayStudent(self):
      print "Name : ", self.name,  ", stu_no ", self.stu_no,"stu_class:",self.stu_class,"male:",self.male
 
   def displayCount(self):
      print"Count: ",Student,stu_count
