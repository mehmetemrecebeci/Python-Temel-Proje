def duzlestir(k):

    for x in k:
        if isinstance(x,list):
            duzlestir(x)
        else:
            kume.append(x)
            

k =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

kume=[]
duzlestir(k)
print(kume)