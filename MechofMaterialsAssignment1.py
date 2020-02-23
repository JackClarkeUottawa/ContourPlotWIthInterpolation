a = 2.8
b =6.1
P = 54
Q = 36
w=37
ws= w*(a+b)

Mc = 147
Dy = -(P*a-ws*(a+b)/2-Mc-Q*(2*a+b))/(a+b)
print("dy:"+str(Dy))
By = -Dy+Q+P+w*(a+b)
print("by: "+str(By))
v1 = -P
v2 = By-P
v3 = v2-ws
v4 = v3+Dy
v5 = v4-Q
print("v1 ="+str(v1)+"\n"+
      "v2 ="+str(v2)+"\n"+
      "v3 ="+str(v3)+"\n"+
      "v4 ="+str(v4)+"\n"+
      "v5 ="+str(v5)+"\n")
vleftB = v1
vrightb = v2
M1 = 0
M2 = v1*a
      
print("v1 ="+str(v1)+"\n"+
      "v2 ="+str(v2)+"\n"+
      "v3 ="+str(v3)+"\n"+
      "v4 ="+str(v4)+"\n"+
      "v5 ="+str(v5)+"\n")
