#Simple Calculator
def add(x,y):
  return x+y

def sub(x,y):
  return x-y

def mul(x,y):
  return x*y

def div(x,y):
  return x/y

def floatdiv(x,y):
  return x//y

print("Enter the operations you want to perform" )
print("1.Addition")
print("1.Subtract")
print("1.Multiplication")
print("1.Division")
print("1.Float division")

choice=input("choose 1/2/3/4/5")
if choice in('1','2','3','4','5'):
  n1=float(input("enter the first number"))
  n2=float(input("enter the second number"))

if choice=='1':
  print(add(n1,n2))
elif choice =='2':
  print(sub(n1,n2))
elif choice =='3':
  print(mul(n1,n2))
elif choice == '4':
  print(div(n1,n2))
elif choice =='5':
  print(floatdiv(n1,n2))
else:
  print("select the correct options")