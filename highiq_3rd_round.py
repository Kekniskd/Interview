import re

# Key: Zip Code
# Value: Income Tax %
INCOME_TAX_DICT = {
    '46410': .25,
    '07042': .3,
    '29483': .4,
    '34639': .2,
    '99654': .27,
    '21043': .16
}

s1 = '''
Employee Group: In office
EmployeeID        Gross_Salary             Net_Pay        Income_Tax      Office_Zip_Code      Occupation  \n
84061099          136020                   102015          34005          46410                Data Scientist\n
27318141          148245                   103771.5       44673.50       07042               Software Engineer\n
33947938          102731                   61638.6          41092.4        29483                Recruiter\n

Employee Group: Remote
EmployeeID        Gross_Salary             Net_Pay        Income_Tax      Office_Zip_Code      Occupation  \n
10447324          58303                    46642.4        11660.6         34639            Admin Assistant\n
21360858          64829                    47325.17        17503.83       99654               Accountant\n
'''

s2 = '''
Employee Group: In office
EmployeeID        Gross_Salary             Net_Pay        Income_Tax      Office_Zip_Code      Occupation  \n
00000001          104723                   102015.00      39,091          46410                Data Scientist\n
00000002          148245                   124,525.8      23719.2         21043-VA             Software Engineer\n

Employee Group: Remote
EmployeeID        Gross_Salary             Net_Pay        Income_Tax      Office_Zip_Code      Occupation  \n
00000003          102731                   $74993.63      27737.77        99654                Recruiter\n
00000004          58303                    40812.1        17490.9          07042-CA            Admin Assistant\n
00000005          64829                    $3,8897.4      25931.6         MD-29483             Accountant\n
'''

s3 = '''
Employee Group: In office
EmployeeID        Gross_Salary             Net_Pay        Income_Tax      Office_Zip_Code      Occupation  \n
00000011          104723                   102015.0o         $39,991           4GE1o               Data Scientist\n
00000022          148245                   12E,525.8         23,719.2          21o43-VA             Software Engineer\n

Employee Group: Remote
EmployeeID        Gross_Salary             Net_Pay        Income_Tax      Office_Zip_Code      Occupation  \n
00000033          102731                   $74993.G3         27,737.77         99g54                Recruiter\n
00000044          58303                    4O812.1          17e90.9           O7O42-CA             Admin Assistant\n
00000055          64829                    $3,8897.4          $25931.G         MD-29E83             Accountant\n
'''


# Create script to parse out table.
# Example output: [{'EmployeeID': '00000002', 'Gross_Salary': 148245.0, 'Net_Pay': 124525.8, 'Income_Tax': 23719.2, 'Office_Zip_Code': '21043', 'Occupation': 'Software Engineer'}]


# Initial script (with bugs)
def parse_table(table_string):
    # Split the text into separate lines
    lines = table_string.split('\n')
    #   print(lines)
    new_lines = []
    for val in lines:
        if not val.startswith('Employee Group') and val != '' and val != ' ':
            new_lines.append(val)
    #   print(new_lines)
    #   for i in new_lines:
    #     print(i)
    # Get column headers
    column_header_list = []
    for column_header in new_lines[0].split(' '):
        if len(column_header) > 0:
            column_header_list.append(column_header)
    #   print(column_header_list)

    # Create a dictionary for each Employee row
    line_dict_list = []
    for line in new_lines:
        # print(line)
        column_values_list = [c for c in line.split(' ') if len(c) > 0]
        # print(column_values_list)
        line_dict = {}
        for i, c_header in enumerate(column_header_list):
            column_value = column_values_list[i]
            column_value = column_value.replace(',', '')
            column_value = column_value.replace('$', '')
            #   if column_value in ['EmployeeID', 'Gross_Salary', 'Net_Pay', 'Income_Tax', 'Office_Zip_Code']:
            #     continue
            line_dict[c_header] = column_value
        if line_dict['EmployeeID'] != 'EmployeeID':
            line_dict_list.append(line_dict)
    #   for i in line_dict_list:
    #     print(i)

    return line_dict_list


redordsList = parse_table(s2)


# print(redordsList)

# Create two functions to validate the net_pay (net_pay should be gross_pay minus income_tax) and income_tax (income_tax should be gross_pay multiplied by the state tax rate) fields
def validate_net_pay(record_dict):
    """
    Validates that a record 's net pay is equal to the gross_pay - income_tax

    return: (bool)
    """
    for record in record_dict:

        if float(record['Net_Pay']) == float(record['Gross_Salary']) - float(record['Income_Tax']):
            print(True)
        else:
            print(False)


#   pass

validate_net_pay(redordsList)


def validate_income_tax(record_dict):
    """
    Validates that a record's income_tax is equal to the gross_pay * tax_rate
    return: (bool)
    """
    pass


############################################# USED FOR TESTING *********************************************************
# Testing flow
def main_flow(s1):
    employee_records = parse_table(s1)

    print(f"Employee Records are: ")
    print(f"{employee_records}")
    print("------" * 30)
    print("------" * 30)

    valid_records = []
    invalid_records = []

    for record in employee_records:
        if validate_net_pay(record) and validate_income_tax(record, INCOME_TAX_DICT):
            print(f"Valid Record ---")
            print(f"{record}")
            print("------" * 30)
            print("------" * 30)
            valid_records.append(record)
        else:
            print(f"Invaalid Record ---")
            print(f"{record}")
            print("------" * 30)
            print("------" * 30)
            invalid_records.append(record)

    return valid_records, invalid_records
############################################# USED FOR TESTING *********************************************************

# main_flow(s1)