# Python script to do frequency analysis from csv files

# import modules
import pandas


print('Enter filename for analysis (Include .csv file extension):')
InputFileName = input(' ')
print('Enter name for output file (without file extension):')
OutputFileName = input(' ')

#Select Fields for frequency analysis
Fields = ['client_ip_addr', 'server_ip_addr']

ImportData = pandas.read_csv(InputFileName)

#Start loop on each field
for Field in Fields:

    ClientFrequency = pandas.crosstab(index=ImportData[Field], columns='count')
    #Adds count collum with frequency value

    OutputClient = ClientFrequency.sort_values(by=['count'], ascending=False)
    #Sorts the Client IPs by frequency

    OutputClient.to_csv(OutputFileName+'_'+Field+'.csv')
#TODO: Add join to include other fields from original data