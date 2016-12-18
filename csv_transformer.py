"""
Transform the csv into a format that can be used to fill up our database
with existing values.
"""
from csv import reader, writer

outFile = open('output.csv', "w+")
csv_writer = writer(outFile)

out_header = ['pincode', 'company_name', 'money_limit', 'priority']
csv_writer.writerow(out_header)

with open("pincode.csv") as pc:
    data = reader(pc)
    header = data.next()
    for row in data:
        pincode = row[0]
        delivery_status_limited = row[1:7]
        delivery_status_nolimit = row[7:9]
        priority_list = row[9:]
        for i in xrange(0, len(delivery_status_limited), 2):
            if delivery_status_limited[i] == 'Y':
                delivery_company = header[i+1]
                delivery_limit = delivery_status_limited[i+1]
                if delivery_company in priority_list:
                    priority = priority_list.index(delivery_company) + 1
                else:
                    priority = 0
                service_status = [pincode, delivery_company, delivery_limit, priority]
                csv_writer.writerow(service_status)
        for i in xrange(0, len(delivery_status_nolimit)):
            if delivery_status_nolimit[i] == 'Y':
                delivery_company = header[i+7]
                delivery_limit = 0
                if delivery_company in priority_list:
                    priority = priority_list.index(delivery_company) + 1
                else:
                    priority = 0
                service_status = [pincode, delivery_company, delivery_limit, priority]
                csv_writer.writerow(service_status)

outFile.close() 
