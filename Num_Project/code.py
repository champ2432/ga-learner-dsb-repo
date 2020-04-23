# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Code starts here

data=np.genfromtxt(path,skip_header=1,delimiter=",")

census=np.concatenate((data,new_record),axis=0)

print(census)


# --------------
#Code starts here
import numpy as np

new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

data=np.genfromtxt(path,skip_header=1,delimiter=",")

census=np.concatenate((data,new_record),axis=0)

#print(census)

age=census[:,:1]

print((age),type(age))

max_age=age.max()
print(max_age)

min_age=age.min()
print(min_age)

age_mean=age.mean()
print(age_mean)

age_std=np.std(age)
print(age_std)


# --------------
#Code starts here
import numpy as np

data=np.genfromtxt(path,skip_header=1,delimiter=",")

census=np.concatenate((data,new_record),axis=0)

#print(census)


race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=race_0[:,2].size
len_1=race_1[:,2].size
len_2=race_2[:,2].size
len_3=race_3[:,2].size
len_4=race_4[:,2].size

my_len=[len_0,len_1,len_2,len_3,len_4]

print(my_len)

minimum=min(my_len)

print(minimum)

minority_race=my_len.index(minimum)

print(minority_race)


# --------------
#Code starts here
import numpy as np

new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

data=np.genfromtxt(path,skip_header=1,delimiter=",")

census=np.concatenate((data,new_record),axis=0)

senior_citizens=census[(census[:,0]>60)]

working_hours_sum=senior_citizens[:,6].sum()

print(working_hours_sum)

senior_citizens_len=len(senior_citizens[:,0])

avg_working_hours=working_hours_sum/senior_citizens_len

print(avg_working_hours)
#print(senior_citizens)


# --------------
#Code starts here
import numpy as np

new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

data=np.genfromtxt(path,skip_header=1,delimiter=",")

census=np.concatenate((data,new_record),axis=0)

high=census[census[:,1]>10]
print(high)

low=census[census[:,1]<=10]
print(low)

avg_pay_high=high[:,7].mean()
print(avg_pay_high)

avg_pay_low=low[:,7].mean()
print(avg_pay_low)

if avg_pay_high > avg_pay_low:
    print("YES")
else:
    print("NO")
    


