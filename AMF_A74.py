import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv as c


path = '/Users/melvingonsalves/Desktop/AMF_US-A74_BASE_HH_1-5.csv'

df = pd.read_csv('/Users/melvingonsalves/Desktop/AMF_US-ARM_BASE_HH_1-5.csv')

#print(df)

count = 0

le = df.LE_1_1_1
#print(le)

#le = le.iloc[1:500]

total_data = np.zeros(48)

missing = np.zeros(48)


lee = le.values

print(lee)

for i in range(len(lee)):
	j = i%48
	if lee[i] == -9999:
		missing[j] = missing[j] + 1
	elif lee[i] != -9999:	
		total_data[j] = total_data[j] + lee[i]


print("Total Data: ",total_data)
print("Array of missing data: ",missing)

total_count = np.full(48,1095.,dtype=np.int)
print("Total count: ",np.shape(total_count))

count_with_missing = total_count - missing
print("Count minus the missing values: ",count_with_missing)


avg_data = total_data/count_with_missing
print("Averaged data values: ",avg_data)
print("Avg Data Shape", np.shape(avg_data))

time = np.arange(0,24, .5) 
print("Time Shape",np.shape(time))
plt.plot(time,avg_data)
plt.xticks([0,3,6,9,12,15,18,21,24])
plt.xlabel('Hours')
plt.ylabel('Latent Heat Flux')

#plt.savefig('SAVED_IMAGES/AMF_A74.png')
#plt.show()

