# Python script to do frequency analysis from specific netflow exports

# import modules
import csv #this module helps with csv handling
import pandas


print('Enter filename for analysis:')
InputFileName = input(' ')
print('Enter name for output file')
OutputFileName = input(' ')

ImportData = pandas.read_csv(InputFileName)

ClientFrequency = pandas.crosstab(index=ImportData['client_ip_addr'], columns='count')
#Adds count collum with frequency value

Output = ClientFrequency.sort_values(by=['count'], ascending=False)
#Sorts the Client IPs by frequency

Output.to_csv(OutputFileName)