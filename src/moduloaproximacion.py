#!/usr/bin/python
#!encoding: UTF-8
pi=3.1415926535897931159979634685441852
def aproximapi(n):
  sumatorio=0.0
  if(n!=0):
   for i in range(1,n+1):
     x=(i-0.5)/float(n)
     #!b=i/float(n)
     #!a=(i-1)/float(n)
     fx=4.0/(1+x**2)
     #!print'Subintervalos[%.3f %.3f] x_i:%.3f fx_i:%.3f' % (a, b, x,fx)
     sumatorio=sumatorio+fx
     p=(sumatorio/n)
   return p
   
if __name__=="__main__":
  import sys
  if((len(sys.argv)==1) or (leng(sys.argv)==2)):
    print ("No se han introducido los valores necesarios. Se utilizarán los valores predeterminados")
    k=10
    n=10
  else:
    n= int(sys.argv[2])
    k= int(sys.argv[1])
  s=[]
  for t in range(1,k+1):
    #!print 'El valor aproximado de pi con 35 decimales es: %.35f' %pi
    aproximacion=aproximapi(n*t)
    s=s+[aproximacion]
  print s