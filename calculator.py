# user input
def user_input():
  return (input("enter the problem: "))

def calculation(values_given):
    split=values_given.split()
    num1=int(split[0])
    operator=(split[1])
    num2=int(split[2])
    split=num1,operator,num2
    if operator=="+":
      return addition(num1,num2)
    elif operator=="-":
      return subtraction(num1,num2)
    elif operator=="*":
      return multiplication(num1,num2)
    elif operator=="/":
      return division(num1,num2)
  
    
    
#function for add
def addition(num1,num2):
  return num1+num2

#function for subtraction
def subtraction(num1,num2):
  return num1-num2

#function for division
def division(num1,num2):
  return num1/num2

def multiplication(num1,num2):
  return num1*num2


#function for display
def display(result):
  print(result)

#main function
def main():
  values_given=user_input()
  result=calculation(values_given)
  display(result)

main()
