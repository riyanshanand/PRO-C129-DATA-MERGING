import csv
from email import header


dataset_1=[]
dataset_2=[]

with open("final.csv","r")as f:
    data=csv.reader(f)
    for i in data:
        dataset_1.append(i)

with open('archive_dataset_sorted1.csv',"r") as p:
    data=csv.reader(p)
    for j in data:
        dataset_2.append(j)


headers_1=dataset_1[0]
planet_data_1=dataset_1[1:]

headers_2=dataset_2[0]
planet_data_2=dataset_2[1:]

#merging column name
headers=headers_1+headers_2
#merging data 
planet_data=[]



for index,row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+ planet_data_2[index])


#creating new csv file to hold new headers and planet_data

with open("mergedataset.csv","a+")as f:
    a=csv.writer(f)
    a.writerow(headers)
    a.writerows(planet_data)


#remove blank lines
with open('mergedataset.csv') as input, open('mergedataset1.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)
