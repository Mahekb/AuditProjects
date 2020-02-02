def evaluate(a): 
    if (len(a) == 0 or len(a)%2==0): 
        return -1; 
    res = int(a[0]); 
    for i in range(1,len(a),2): 
        opr = a[i]; 
        opd = a[i + 1]; 
        if (opr == '+'): 
            res = res + int(opd); 
        elif (opr == '-'): 
            res = res + int(opd); 
        elif (opr == '*'): 
            res = res * int(opd); 
        elif (opr == '/'): 
            res = int(res / int(opd)); 
        else: 
            return -1; 
    return res; 
  
a = input("Enter the expression : ")
res = evaluate(a); 
if res == -1 :
  print(a,"is Invalid") 
else :
  print("Value of",a,"is",res); 
  
 
  