def mediatotal():
       a = int (input ("Digite a primeira nota "))
       b = int (input ("Digite a segunda nota "))
       
       media = (a + b ) / 2
    
       print(media)
        
       if media <= 9:
           print("Reprovado")
       else:
           print('Aprovado')

mediatotal()