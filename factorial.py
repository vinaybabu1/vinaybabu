num=int(raw_input())
factorial=1
if num < 0:
  print("sorry, factorial does npot exists for negative number")
elif num == 0:
  print("the facorial of 0 is 1")
else:
  for i in range(1,num+1):
    factorial=factorial*i
  print("the factorial of",num,"is",factorial)  
