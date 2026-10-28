def apply_operation(function, number):
 return function(number) 
def double(number):
 return number * 2
def square(number):
 return number ** 2
print(apply_operation(double, 7))
print(apply_operation(square, 3))