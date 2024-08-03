name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
elif name == 'SonjGa':
    print('Hey Sonja nueva !')
elif name == 'SonjGa 1':
    print('Hey SonjGa 1') 

    #cno se ejecutara 
elif name == 'Sonja':
    print('esto no se ejecuta porque ya se valido en la primera')


else:
    print('Hey anonymous!')