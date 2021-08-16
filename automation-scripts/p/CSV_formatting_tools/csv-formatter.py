import pandas as pd

male_tags = pd.read_csv(
    '~/saveit.csv',
    usecols =[0])

male_ages = pd.read_csv(
    '~/saveit.csv',
    usecols =[1])

fem_tags = pd.read_csv(
    '~/saveit.csv',
    usecols =[2])

fem_ages = pd.read_csv(
    '~/saveit.csv',
    usecols =[3])


# # Convert Target Column dataframe to array
mt = []; ma = []; ft = []; fa = []
for i in male_tags['1']:
    mt.append(i)
for i in male_ages['2']:
    ma.append(i)
for i in fem_tags['3']:
    ft.append(i)
for i in fem_ages['4']:
    fa.append(i)

fa2=[]; ma2=[]; 
for i, x in zip(fa, ma):
    fa2.append("// " + i.strip("Estimate!!Total:!!").strip(":!!"))
    ma2.append("// " + x.strip("Estimate!!Total:!!").strip(":!!"))
    
#for i, x in zip(fa2, ft):
#    print(i)
#    print('"' + x + '",')

all1=[]
for a,b,c,d in zip(ma2, mt, fa2, ft):
    all1.append(b); all1.append(a)
    all1.append(d); all1.append(c)

n = 0
while n < len(all1):
    all1[n] = all1[n].replace("// ","").replace(":!!","").replace(" ","").replace("Male","m").replace("year","yr").replace("Female","f")
    n += 1
# print(all1)

# n = 0
# while n < len(all1):
#     if n % 2 != 0:
#         print(all1[n] + "=5.55556; ", end="")
#     n += 1

new1=[]
n = 0
while n < len(all1):
    if n % 2 != 0:
        new1.append(all1[n])
    n += 1

print(new1)