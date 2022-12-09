# Πρόγραμμα σε γλώσσα python το οποίο διαβάζει ένα αλφαριθμητικό που πληκτρολογεί ο χρήστης
# και βρίσκει αν είναι παλίνδρομο.


import os


def diagrafi_kenwn(s):   
    s1 = ""     
    for x in s:   
        if x != " ":  
            s1 += x 
    return s1   


def antistrofi(s):     
    s2 = ""  
    for i in s: 
        s2 = i + s2 
    return s2 


leksi = ""     
pdict = {}    
plist = []     
leksi_1 = ""   
leksi_2 = ""   

leksi = input("Δώσε ένα αλφαριθμητικό με κεφαλαία: ")  
if len(leksi) == 0 or len(leksi)==1:  
    print("Το μήκος του αλφαριθμητικού είναι πολύ μικρό!") 
else:   
    leksi_1 = diagrafi_kenwn(leksi) 
    leksi_2 = antistrofi(leksi_1)  
    if leksi_1 == leksi_2:   
        pdict[leksi_1] = len(leksi_1) 
        plist = list(leksi_1)  
        print(pdict)  
        print(plist)
    else:  
        print ("Το αλφαριθμητικό ΔΕΝ είναι παλίνδρομο") 


os.system("pause")