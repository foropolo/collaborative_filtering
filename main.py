from functions import *
import numpy as np
import random
import math 
#import matplotlib.pyplot as plt


N=100
M=100
#k=27
#X=20




while True:
    k=input("Choose k for the closest neighborhoods,it should be an integer and not 0:")
    try:
        k=int(k)
        if(k>0 and isinstance(k,int)):
            break
    except ValueError:
        print("")
    
    print("It wasn't integer >0 .Try again ")

while True:
    X=input("Choose X for the percentage of delete items from the matrix,it should be an integer and not 0:")
    try:
        X=int(X)
        if(X>0 and X<100 and isinstance(X,int)):
            break
    except ValueError:
        print("")
        
    print("It wasn't integer >0 .Try again ")


#με την random.uniform εχω ομοιομορφη κατανομη, εκανα καποιους ελεγχους και οντως ειναι ομοιομορφη,
# επισης στο documentation το γραφει κιολας https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html
benefit_matrix=np.full((N,M),round(random.uniform(1,10),2)) #δεδομενα τυπου float642
decrease_benefit_matrix=np.full((N,M),round(random.uniform(1,10),2))
keeper_matrix_of_decrease=np.full((N,M),round(random.uniform(1,10),2))
for i in range(N):
    for j in range(M):
        benefit_matrix[i][j]=round(random.uniform(1,10),2)
        decrease_benefit_matrix[i][j]=benefit_matrix[i][j]
        keeper_matrix_of_decrease[i][j]=benefit_matrix[i][j]

#σβήνω το ποσοστο Χ, τυχαια διαλεγω ποια σβηνω απο τον πινακα με την random.randint
percentage_of_deleted=0
account_of_deleted=0
while True:
    if(percentage_of_deleted > X):
        break
    i=random.randint(0,N-1)
    j=random.randint(0,N-1)
    decrease_benefit_matrix[i][j]=0
    keeper_matrix_of_decrease[i][j]=0
    account_of_deleted=account_of_deleted+1
    percentage_of_deleted=(account_of_deleted/(N*M))*100


#print(percentage_of_deleted)
#print(benefit_matrix)
#print(decrease_benefit_matrix)
#print(keeper_matrix_of_decrease)
#print(benefit_matrix.shape)
#print(benefit_matrix[2])#πινακας ξεκιναει απο το 0 εως 9 για Indexing, η συγκεκριμενη εντολη
#μας δειχνει την 3η γραμμη
#print(benefit_matrix[:,0])#μας δείχνει την 1η στηλη του πινακα

#use Jaccard
Jaccard_matrix=np.full((N,N),0.0)
#print(Jaccard_matrix)
#υπολογιζω το jaccard για καθε ενα στοιχείο και το αποθηκευω σε ενα πινακα Ν*Ν, οπου στην πρωτη γραμμη
#αποθηκευονται τα Jaccard του 1ου αντικειμενου με τα υπολοιπα, σε καθε στηλη είναι η συγκριση με το αντιστοιχο
#αντικειμενο στις γραμμες. π.χ. 1η γραμμη εχουμε το item_1 και στις στηλες του κάθε jaccard των αλλων 
#αντικειμενων. Οταν υπολογιζω την jaccard ενος αντικειμενου με τον ιδιο του τον εαυτο
#αποθηκευω ως 0 και οχι ως 1,οπως κανονικα ειναι. Για λογους ευκολιας γινεται αυτο
for i in range(N):
    for j in range(N):
        Jaccard_matrix[i][j]=Jaccard(decrease_benefit_matrix[i],decrease_benefit_matrix[j],N)

#print(Jaccard_matrix)
#βρισκω τα Κ μεγαλυτερα jaccard και τα αποθηκευω στον jaccard_matrix_k ,επισης αποθηκευω περι ποιου 
#αντικειμενου προκειται
Jaccard_matrix_k=[[0]*k]*N
position_Jaccard=[[0]*k]*N

for i in range(N):
    Jaccard_matrix_k[i],position_Jaccard[i]=K_nearest(Jaccard_matrix[i],k)
    #δεν θελω να αποθηκευσει τον εαυτο του στην λιστα με position_Jaccard, ειδικα σε μικρο Κ , θα επηρεασει αρκετα
    for j in range(k):
        if (Jaccard_matrix_k[i][j]==0 and position_Jaccard[i][j]==i):
            for l in range(N):
                if (Jaccard_matrix[i][l]==0 and position_Jaccard[i][j] != l): 
                    position_Jaccard[i][j]=l
                    break


#print(Jaccard_matrix_k,position_Jaccard)
#decrease_benefit_matrix,MAE=Predict_with_average(decrease_benefit_matrix,benefit_matrix,position_Jaccard,k,N)

#use Dice
Dice_matrix=np.full((N,N),0.0)

#υπολογιζω το Dice για καθε ενα στοιχείο και το αποθηκευω σε ενα πινακα Ν*Ν, οπου στην πρωτη γραμμη
#αποθηκευονται τα Dice του 1ου αντικειμενου με τα υπολοιπα, σε καθε στηλη είναι η συγκριση με το αντιστοιχο
#αντικειμενο στις γραμμες. π.χ. 1η γραμμη εχουμε το item_1 και στις στηλες του κάθε Dice των αλλων 
#αντικειμενων. Οταν υπολογιζω την Dice ενος αντικειμενου με τον ιδιο του τον εαυτο
#αποθηκευω ως 0 και οχι ως 1,οπως κανονικα ειναι. Για λογους ευκολιας γινεται αυτο
for i in range(N):
    for j in range(N):
        Dice_matrix[i][j]=Dice(benefit_matrix[i],benefit_matrix[j],N)

#print(Dice_matrix)
#βρισκω τα Κ μεγαλυτερα Dice και τα αποθηκευω στον Dice_matrix_k ,επισης αποθηκευω περι ποιου 
#αντικειμενου προκειται
Dice_matrix_k=[[0]*k]*N
position_Dice=[[0]*k]*N
for i in range(N):
    Dice_matrix_k[i],position_Dice[i]=K_nearest(Dice_matrix[i],k)

#print(Dice_matrix_k,position_Dice)


#use Cosine
Cosine_matrix=np.full((N,N),0.0)

#υπολογιζω το Cosine για καθε ενα στοιχείο και το αποθηκευω σε ενα πινακα Ν*Ν, οπου στην πρωτη γραμμη
#αποθηκευονται τα Cosine του 1ου αντικειμενου με τα υπολοιπα, σε καθε στηλη είναι η συγκριση με το αντιστοιχο
#αντικειμενο στις γραμμες. π.χ. 1η γραμμη εχουμε το item_1 και στις στηλες του κάθε Cosine των αλλων 
#αντικειμενων. Οταν υπολογιζω την Cosine ενος αντικειμενου με τον ιδιο του τον εαυτο
#αποθηκευω ως 0 και οχι ως 1,οπως κανονικα ειναι. Για λογους ευκολιας γινεται αυτο
for i in range(N):
    for j in range(N):
        Cosine_matrix[i][j]=Cosine(benefit_matrix[i],benefit_matrix[j],N)

#print(Cosine_matrix)
#βρισκω τα Κ μεγαλυτερα Cosine και τα αποθηκευω στον Cosine_matrix_k ,επισης αποθηκευω περι ποιου 
#αντικειμενου προκειται
Cosine_matrix_k=[[0]*k]*N
position_Cosine=[[0]*k]*N
for i in range(N):
    Cosine_matrix_k[i],position_Cosine[i]=K_nearest(Cosine_matrix[i],k)

#print(Cosine_matrix_k,position_Cosine)


#use Cosine
Cosine_adjust_matrix=np.full((N,N),0.0)

#υπολογιζω το Cosine για καθε ενα στοιχείο και το αποθηκευω σε ενα πινακα Ν*Ν, οπου στην πρωτη γραμμη
#αποθηκευονται τα Cosine του 1ου αντικειμενου με τα υπολοιπα, σε καθε στηλη είναι η συγκριση με το αντιστοιχο
#αντικειμενο στις γραμμες. π.χ. 1η γραμμη εχουμε το item_1 και στις στηλες του κάθε Cosine των αλλων 
#αντικειμενων. Οταν υπολογιζω την Cosine ενος αντικειμενου με τον ιδιο του τον εαυτο
#αποθηκευω ως 0 και οχι ως 1,οπως κανονικα ειναι. Για λογους ευκολιας γινεται αυτο
for i in range(N):
    for j in range(N):
        Cosine_adjust_matrix[i][j]=Cosine_adjust(benefit_matrix[i],benefit_matrix[j],N)

#print(Cosine_adjust_matrix)
#βρισκω τα Κ μεγαλυτερα Cosine και τα αποθηκευω στον Cosine_matrix_k ,επισης αποθηκευω περι ποιου 
#αντικειμενου προκειται
Cosine_adjust_matrix_k=[[0]*k]*N
position_Cosine_adjust=[[0]*k]*N
for i in range(N):
    Cosine_adjust_matrix_k[i],position_Cosine_adjust[i]=K_nearest(Cosine_adjust_matrix[i],k)

#print(Cosine_adjust_matrix_k,position_Cosine_adjust)


while True:
    while True:
        choosing=input("Choose \n1.Jaccard\n2.Dice\n3.Cosine\n4.Adjusted Cosine \n5.Exit \nit should be 1,2,3,4 or 5:")
        try:
            choosing=int(choosing)
            if(choosing>0 and choosing < 6  and isinstance(choosing,int)):
                break
        except ValueError:
            print("")
            
        print("It wasn't 1,2,3,4 or 5 .Try again ")
    
    if(choosing==1):
        decrease_benefit_matrix,MAE=Predict_with_average(decrease_benefit_matrix,benefit_matrix,position_Jaccard,k,N)
        #print(decrease_benefit_matrix)
        print("-------------------Jaccard MAE:",MAE)
        #print(keeper_matrix_of_decrease)
        decrease_benefit_matrix=keeper_matrix_of_decrease.copy()
        #print(decrease_benefit_matrix)
    elif(choosing==2):
        decrease_benefit_matrix,MAE=Predict_with_average(decrease_benefit_matrix,benefit_matrix,position_Dice,k,N)
        #print(decrease_benefit_matrix)
        print("-------------------Dice MAE:",MAE)
        #print(keeper_matrix_of_decrease)
        decrease_benefit_matrix=keeper_matrix_of_decrease.copy()
        #print(decrease_benefit_matrix)
    elif(choosing==3):
        decrease_benefit_matrix,MAE=Predict_with_average(decrease_benefit_matrix,benefit_matrix,position_Cosine,k,N)
        print("-------------------Cosine MAE:",MAE)
        decrease_benefit_matrix=keeper_matrix_of_decrease.copy()
    elif(choosing==4):
        decrease_benefit_matrix,MAE=Predict_with_average(decrease_benefit_matrix,benefit_matrix,position_Cosine_adjust,k,N)
        print("-------------------Adjusted Cosine MAE:",MAE)
        decrease_benefit_matrix=keeper_matrix_of_decrease.copy()       
    elif(choosing==5):
        break
