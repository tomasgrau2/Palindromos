def palindromo(x):
    x = x.lower()
    x = x.replace(" ","")
    x = x.replace("ú","u")
    x = x.replace("á","a")
    x = x.replace("é","e")
    x = x.replace("í","i")
    x = x.replace("ó","o")
    if x == x[::-1]:
        return(True)
    else: 
        return(False)    




