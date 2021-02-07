def funkcija():
    lista=[]
    while True:
      n =int(input())
      if n < 0 or n == 0:
         break
      lista.append(n)
      for i in lista:
       if i % 10 == 0:
          lista.remove(i)
    return lista
    
print (funkcija())
