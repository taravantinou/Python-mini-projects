# Πρόγραμμα που ζητάει από τον χρήστη αριθμούς μέχρι να πληκτρολογήσει το 'q' και υπολογίζει:
# Τον μέσο όρο των στοιχείων και το άθροισμα των τετραγώνων της διαφοράς κάθε αριθμού από το μέσο όρο τους.


import os

def listAverage(L):  
    average = 0  
    average = sum(L)/len(L)   
    return average   


def listDiffSquare(L):    
    i = 0  
    difSqr = 0   
    n = len(L)  
    for i in range(n):   
        difSqr += (L[i] - listAverage(L))**2    
    return difSqr    


A = []    
x = ""    
y = 0
while True:   
    x = str(input("Δώσε έναν αριθμό ή 'q' για τερματισμό: ")) 
    if x != 'q':  
        y = int(x)   
        A.append(y)   
    else:   
        print("Πατήθηκε το πλήκτρο 'q' και το πρόγραμμα τερματίστηκε")   
        break     
if len(A) == 0:   
    print("Δεν δώθηκε κανένας αριθμός και έχουμε κενή λίστα! ")  
else:     
    print("Η λίστα είναι: ")    
    print(A)
    print("Ο μέσος όρος των στοιχείων της λίστας είναι: ")    
    print(listAverage(A))
    print("Το άθροισμα των τετραγώνων διαφοράς είναι: ")     
    print(listDiffSquare(A))

os.system("pause")