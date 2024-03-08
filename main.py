nric = input('Enter an NRIC number: ')
# Type your code below
A= nric[0] in "TSFG" and len(nric[8:]) == 1 and nric[8:].isalpha and nric[1:8].isdigit
weight = [2,7,6,5,4,3,2]
digit = 0
if A:
  for i in range(len(weight)):
    digit += int(nric[i+1]) * weight[i]
  if nric[0] in "TG" :
    digit += 4
  rem = digit % 11
  ST = ["J","Z","I","H","G","F","E","D","C","B","A"]
  FG = ["X","W","U","T","R","Q","P","N","M","L","K"]
  if nric[0] in "ST" and nric[-1] in ST[rem] :
    print("NRIC is valid.")
  elif nric[0] in "FG" and nric[-1] in FG[rem] :
    print("NRIC is valid.")
  else:
    print("NRIC is invalid.")
else:
  print("NRIC is invalid.")