# Hecho por Max.
# Respuesta a pregunta 1. 


res1 = [None]*(10) 
for i in range (10):
    res1[i] = [i]*10

def obtenerSubmatriz(res1, fi, ci, ff, cf):
    res = []
    for h in range((ff-fi)+1):
        res.append([res1[h+fi][ff]])
  
    for d in range((ff-fi)+1):
        for k in range((cf-ci)):
            res[d].append(res1[d+fi][ci+1+k])

    return res

print(obtenerSubmatriz(res1,0,0,9,9))