import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/melvingonsalves/Desktop/AMF_US-A74_BASE_HH_1-5.csv'

df = pd.read_csv('/Users/melvingonsalves/Desktop/AMF_US-ADR_BASE_HH_1-5.csv')

#print(df)

count = 0

le = df.LE
#print(le)

dd = le.iloc[7250:11665]
#print(dd)
ff = le.iloc[24818:29233]

lee = dd.append(ff)

print(lee)

total_data = np.zeros(48)

missing = np.zeros(48)


lee = lee.values

print(lee)
          
for i in range(len(lee)):
        j = i%48
        if lee[i] == -9999:
                missing[j] = missing[j] + 1
        elif lee[i] != -9999:
                total_data[j] = total_data[j] + lee[i]


print("Total Data: ",total_data)
print("Array of missing data: ",missing)

total_count = np.full(1,365.,dtype=np.int) ### Make an array of how many values should be in the average
print("Total count: ",total_count)
    
count_with_missing = total_count - missing
print("Count missing values: ",count_with_missing)


avg_data = total_data/count_with_missing
print("Averaged data values: ",avg_data)
print(total_data)
print(count_with_missing)
print("Avg Data Shape", np.shape(avg_data))


modely = [4.769, 2.837, 2.639, 2.188, 57.521, 104.644, 109.314, 96.822]
modelx = [0, 3, 6, 9, 12, 15, 18, 21]


time = np.arange(0,24,.5)

plt.figure(1)
plt.xticks([0,3,6,9,12,15,18,21,24])
print("Time Shape",np.shape(time))
plt.plot(time,avg_data, label = 'Station Data')
plt.plot(modelx, modely, label = 'Model Data')
plt.xlabel('Hours')
plt.ylabel('Latent Heat Flux')
plt.legend()

plt.savefig('SAVED_IMAGES/Summer_AMF_ADR.png')
#plt.show()
