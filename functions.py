import math  

def Jaccard(first_item,second_item,size_of_array):
    
    numerator_JC=0
    denominator_JC=0
    account_for_the_same=0
    #print(first_item)
    #print(second_item)
    for i in range(size_of_array):
        if(first_item[i]==0 or second_item[i]==0):
            denominator_JC=denominator_JC+2
            account_for_the_same=account_for_the_same+1
            continue
        if(first_item[i]==second_item[i]):
            numerator_JC=numerator_JC+1
            account_for_the_same=account_for_the_same+1
        elif(max(first_item[i],second_item[i])-min(first_item[i],second_item[i]) < 0.5):
            numerator_JC=numerator_JC+1
        else:
            denominator_JC=denominator_JC+2
    #print("arithimis:",numerator_JC,"\nparanomastis:",denominator_JC)
    if account_for_the_same==len(first_item) :
        return 0

    return round(numerator_JC/(denominator_JC+numerator_JC),2)




def K_nearest(list,k):
    #list=[0.11, 0.11, 0.05, 1. ,  0. ,  0.11, 0.18, 0.05, 0.05 ,0.05]
    #k=3
    
    position=[0]*k
    biggest_numbers=[0]*k
    position_index=0
    
    while position_index<k:
        max_number=max(list)

        for i in range(len(list)):
            if(max_number==list[i]):
                biggest_numbers[position_index]=max_number
                position[position_index]=i
                position_index=position_index+1
                list[i]=-100
                break
    
    #print(biggest_numbers,position)
    return biggest_numbers,position





def Dice(first_item,second_item,size_of_array):
    
    numerator_DC=0
    denominator_DC=0
    account_for_the_same=0
    #print(first_item)
    #print(second_item)
    for i in range(size_of_array):
        if(first_item[i]==None or second_item[i]==None):
            continue
        if(first_item[i]==second_item[i]):
            numerator_DC=numerator_DC+1
            account_for_the_same=account_for_the_same+1
        elif(max(first_item[i],second_item[i])-min(first_item[i],second_item[i]) < 0.5):
            numerator_DC=numerator_DC+1
    
    if account_for_the_same==len(first_item) :
        return 0

    return round(2*numerator_DC/(len(first_item)+len(second_item)),2)




def Cosine(first_item,second_item,size_of_array):

    numerator_CS=0
    denominator_CS_first=0
    denominator_CS_second=0
    account_for_the_same=0
    #print(first_item)
    #print(second_item)
    for i in range(size_of_array):
        numerator_CS=first_item[i]*second_item[i]+numerator_CS
        denominator_CS_first=first_item[i]**2+denominator_CS_first
        denominator_CS_second=second_item[i]**2+denominator_CS_second
        if(first_item[i]==second_item[i]):
            account_for_the_same=account_for_the_same+1
    
    denominator_sum=math.sqrt(denominator_CS_first)*math.sqrt(denominator_CS_second)
    
    if account_for_the_same==len(first_item) :
        return 0

    return round(numerator_CS/denominator_sum,2)




def Cosine_adjust(first_item,second_item,size_of_array):
    
    numerator_CS=0
    denominator_CS_first=0
    denominator_CS_second=0
    account_for_the_same=0
    denominator_for_average_first=0
    denominator_for_average_second=0

    for i in range(size_of_array):
        if(first_item[i]>0):
            denominator_for_average_first=denominator_for_average_first+1
        if(second_item[i]>0):
            denominator_for_average_second=denominator_for_average_second+1

    average_first=sum(first_item)/denominator_for_average_first
    average_second=sum(second_item)/denominator_for_average_second
    #print(average_first)
    #print(average_second)
    new_first_item=[0.0]*size_of_array
    new_second_item=[0.0]*size_of_array
    
    for i in range(size_of_array):
        if(first_item[i]>0):
            new_first_item[i]=first_item[i]-average_first
        else:
            new_first_item[i]=0
        if(second_item[i]>0):
            new_second_item[i]=second_item[i]-average_second
        else:
            new_second_item[i]=0
    #print(first_item)
    #print(second_item)
    #print(new_first_item)
    #print(new_second_item)
    for i in range(size_of_array):
        numerator_CS=new_first_item[i]*new_second_item[i]+numerator_CS
        denominator_CS_first=new_first_item[i]**2+denominator_CS_first
        denominator_CS_second=new_second_item[i]**2+denominator_CS_second
        if(first_item[i]==second_item[i]):
            account_for_the_same=account_for_the_same+1
    #print(numerator_CS)
    #print("first",denominator_CS_first)
    #print("second",denominator_CS_second)
    denominator_sum=math.sqrt(denominator_CS_first)*math.sqrt(denominator_CS_second)
    #print("denominator of all",denominator_sum)
    if account_for_the_same==len(first_item) :
        return 0
    #print(numerator_CS/denominator_sum)
    return round(numerator_CS/denominator_sum,2)



#def Predict_with_weighted_average(first_item,items_cor,positions):



def Predict_with_average(decrease_benefit_matrix,benefit_matrix,position, k,N):

    average_prediction=0
    account_for_MAE=0
    MAE=0
    for i in range(N):
        for j in range(N):
            if(decrease_benefit_matrix[i][j] == 0):
                for l in range(k):
                    index=position[i][l]
                    #print(index)
                    average_prediction=decrease_benefit_matrix[index][j]+average_prediction
                    #print(decrease_benefit_matrix[index][j])
                #print(average_prediction)
                decrease_benefit_matrix[i][j]=round(average_prediction/k,2)
                if(max(benefit_matrix[i][j],decrease_benefit_matrix[i][j])-min(benefit_matrix[i][j],decrease_benefit_matrix[i][j]) < 0.5 or benefit_matrix[i][j]==decrease_benefit_matrix[i][j] ):
                    continue
                else: 
                    MAE=abs(decrease_benefit_matrix[i][j]-benefit_matrix[i][j])+MAE
                    account_for_MAE=account_for_MAE+1
                average_prediction=0
    
    MAE=MAE/account_for_MAE
    return decrease_benefit_matrix,MAE