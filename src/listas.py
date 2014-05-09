#!/usr/bin/python
#!encoding: UTF-8
import moduloerror

def lista():
  umbral=(1.e-4, 1.e-5, 1.e-6, 1.e-7, 1.e-8)
  intervalo=(10,50,100,150,500,550,1000)
  veces=100
  errores=[]

  for i in intervalo:
    l=[]
    for j in umbral:
      resultado=moduloerror.error(i,veces,j)
      l=l+[resultado]
    print l
    errores=errores+[l]
  print errores
  return errores