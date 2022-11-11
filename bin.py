#Binning#


# dataset = []
  
# # number of elements as input
# n = int(input("Enter number of elements : "))
  
# # iterating till the range
# for i in range(n):
#     # ele = int(input(f'{i+1}\t:\t'))
#     ele=int(input())
#     dataset.append(ele)

# load data set
dataset = [4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34]

n=len(dataset)

dataset.sort()
n=int(n/3)
print("Dataset = ", dataset)
# create bins
mbin1=dataset[0:4]
mbin2=dataset[4:8]
mbin3=dataset[8:12]
bbin1=dataset[0:4]
bbin2=dataset[4:8]
bbin3=dataset[8:12]
#count
c1=0
c2=0
c3=0
mean1 = 0
mean2 = 0
mean3 = 0
for i in range(n):
    c1=c1+1
    mean1=mean1+mbin1[i]
for i in range(n):
    c2=c2+1
    mean2=mean2+mbin2[i]
for i in range(n):
    c3=c3+1
    mean3=mean3+mbin3[i]
# Bin mean
mean1 = mean1/c1

for j in range(c1):
    mbin1[j]=mean1
    
mean2 = mean2/c2

for j in range(c2):
    mbin2[j]=mean2
    
mean3 = mean3/c3

for j in range(c3):
    mbin3[j]=mean3
    
print("Bin Mean:")
print("Bin 1 = ",mbin1)
print("Bin 2 = ",mbin2)
print("Bin 3 = ",mbin3)
#Bin boundaries
for i in range(n):
    if i==0 or i==n-1:
        pass
    else:
        if (bbin1[i]-bbin1[0]) < (bbin1[n-1]-bbin1[i]):
            bbin1[i]=bbin1[0]
        else:
            bbin1[i]=bbin1[n-1]
for i in range(n):
    if i==0 or i==n-1:
        pass
    else:
        if (bbin2[i]-bbin2[0]) < (bbin2[n-1]-bbin2[i]):
            bbin2[i]=bbin2[0]
        else:
            bbin2[i]=bbin2[n-1]
for i in range(n):
    if i==0 or i==n-1:
        pass
    else:
        if (bbin3[i]-bbin3[0]) < (bbin3[n-1]-bbin3[i]):
            bbin3[i]=bbin3[0]
        else:
            bbin3[i]=bbin3[n-1]
print("Bin Boundaries:")
print("Bin 1 = ",bbin1)
print("Bin 2 = ",bbin2)
print("Bin 3 = ",bbin3)



# Enter number of elements : 12
# 21
# 24
# 4
# 8
# 9
# 15
# 21
# 34
# 29
# 28
# 26
# 25
# Dataset =  [4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34]
# Bin Mean:
# Bin 1 =  [9.0, 9.0, 9.0, 9.0]
# Bin 2 =  [22.75, 22.75, 22.75, 22.75]
# Bin 3 =  [29.25, 29.25, 29.25, 29.25]
# Bin Boundaries:
# Bin 1 =  [4, 4, 4, 15]
# Bin 2 =  [21, 21, 25, 25]
# Bin 3 =  [26, 26, 26, 34]



