#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Employee:
	'Common base class for all employees.'
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name : ", self.name, ", Salary : ", self.salary

emp1 = Employee("Maxsu", 2000)
emp2 = Employee("Kobe", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.salary = 7000
emp1.name = "Lyndon"
# del emp1.salary  # Delete attribute.

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

print hasattr(emp1, 'salary')
print getattr(emp1, 'salary')
print setattr(emp1, 'salary', 10000)
print delattr(emp1, 'salary')

print '****default method****'
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

