x = 0.0
for i in range(10):
    x+=0.1
    print(x)
 
 # los nuemors nunca son exactos
if x == 1.0:
    print(f'x = {x}')
else :
    print(f'x != {x}')
# mejora,  siempre compara con aproximados no identicos
if x < 1.0 and x > 0.99999:
    print(f'x = {x}')
else :
    print(f'x != {x}')    