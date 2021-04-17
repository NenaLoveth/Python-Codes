files = ['amount,duration,rate,down_payment\n',
 '45230,48,0.07,4300\n',
 '883000,16,0.14,\n',
 '100000,12,0.1,\n',
 '728400,120,0.12,100000\n',
 '3637400,240,0.06,\n',
 '82900,90,0.07,8900\n',
 '316000,16,0.13,\n',
 '15230,48,0.08,4300\n',
 '991360,99,0.08,\n',
 '323000,27,0.09,4720010000,36,0.08,20000\n',
 '528400,120,0.11,100000\n',
 '8633400,240,0.06,\n',
 '12900,90,0.08,8900']
def parse_header(header_line):
    return header_line.strip().split(',')
def parse_data(data_line):
    values = []
    for items in data_line.strip().split(','):
        if items == '':
            values.append(0.0)
        else:
            values.append(float(items))
    return values
print(files[0])
print(parse_header(files[0]))
print(files[2])
print(parse_data(files[2]))
def create_file_dict(values, headers):
    file_dict = {}
    for value,header in zip(values,headers):
        file_dict[header] = value
    return file_dict
print(create_file_dict(parse_data(files[2]),parse_header(files[0])))

