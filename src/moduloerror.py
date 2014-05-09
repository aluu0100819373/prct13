#!/usr/bin/python
#!encoding: UTF-8
import moduloaproximacion
import sys
def error(n, k, umbral):
   contador=0
   for j in range (1,k+1):
     diferencia=moduloaproximacion.aproximapi(n)-moduloaproximacion.pi
     if (abs(diferencia) > umbral):
       contador += 1
       
   return contador / float(k) * 100.0

if __name__=="__main__":
  if((len(sys.argv)==1) or (leng(sys.argv)==2)):
    print ("No se han introducido los valores necesarios. Se utilizarán los valores predeterminados")
    n=10
    k=10
    u=0.1
  else:
    n= int(sys.argv[1])
    k= int(sys.argv[k])
    u= float(sys.argv[3])
  print error(n,k,u)
  
  
