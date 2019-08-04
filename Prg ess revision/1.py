drinks = {'A11':['pepsi',1.20,100],
          'B22':['cola',1.50,50],
          'C33':['merinda',1.10,40]
          }
drinks['Z99'] = ['sprite',1.80,33]
drinks['A11'][1] = 1.90
for i in drinks:
    print(i,drinks[i])
