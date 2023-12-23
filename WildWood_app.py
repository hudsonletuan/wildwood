import WildWood_database as db
from datetime import datetime

def see_all_people():
    print('-----------All People-----------')
    people = db.get_all_people()
    for person in people:
        print(person)
    print('--------------------------------')
    
def see_all_complex():
    print('-----------All Complexes-----------')
    all_complex = db.get_all_complex()
    for a_complex in all_complex:
        print(a_complex)
    print('--------------------------------')
    
def see_all_apartment():
    print('-----------All Apartments-----------')
    all_apartment = db.get_all_apartment()
    for apartment in all_apartment:
        print(apartment)
    print('--------------------------------')

def see_all_person_apartment():
    print('-----------All People in Apartments-----------')
    all_p_a = db.get_all_person_apartment()
    for p_a in all_p_a:
        print(p_a)
    print('--------------------------------')
    
def see_all_lease():
    print('-----------All Lease Information-----------')
    all_lease = db.get_all_lease()
    for lease in all_lease:
        print(lease)
    print('--------------------------------')
    
def see_all_maintenance_request():
    print('-----------All Maintenance Requests-----------')
    all_m_r = db.get_all_maintenance_request()
    for m_r in all_m_r:
        print(m_r)
    print('--------------------------------')
    
def see_all_maintenance_expense():
    print('-----------All Maintenance Expenses-----------')
    all_m_e = db.get_all_maintenance_expense()
    for m_e in all_m_e:
        print(m_e)
    print('--------------------------------')
    
def add_person():
    print('------Add a person into data------')
    person_id = input('New ID: ')
    f_name = input('First Name: ')
    l_name = input('Last Name: ')
    residence = input('Residence: ')
    ethnicity = input('Ethnicity: ')
    gender = input('Gender (Male/Female): ')
    birthdate = input('Birthdate (yyyy-mm-dd): ')
    role = input('Role (Headquarter Manager/Complex Manager/Tenant:): ')
    db.add_person(person_id, f_name, l_name, residence, ethnicity, gender, birthdate, role)
    print(f'---{role} {f_name} {l_name} with ID Number {person_id} added!---')
    
def del_person():
    print('------Remove a person from data------')
    person_id = input('Person ID: ')
    db.del_person(person_id)
    print(f'-----Person with ID Number {person_id} removed!-----')
    
def add_complex():
    print('------Add a complex into data------')
    num = int(input('Complex Number: '))
    name = input('Complex Name: ')
    location = input('Location: ')
    manager = input('Manager ID: ')
    db.add_complex(num, name, location, manager)
    print(f'---Complex {name} {num} under the management of manager {manager} added!---')
    
def del_complex():
    print('------Remove a complex from data------')
    num = int(input('Complex Number: '))
    db.del_complex(num)
    print(f'-----Complex {num} removed!-----')
    
def add_apartment():
    print('------Add an apartment into data------')
    num = int(input('Apartment Number: '))
    name = input('Apartment Name: ')
    address = input('Apartment Address: ')
    complex_num = input('Complex Number: ')
    db.add_apartment(num, name, address, complex_num)
    print(f'---Apartment {name} {num} at {address} in complex {complex_num} added!---')
    
def del_apartment():
    print('------Remove an apartment from data------')
    num = int(input('Apartment Number: '))
    db.del_apartment(num)
    print(f'-----Apartment {num} removed!-----')
    
def add_lease():
    print('------Add a lease into data------')
    num = int(input('Lease Number: '))
    date = input('Rent Date (yyyy-mm-dd): ')
    end = input('End Date (yyyy-mm-dd): ')
    rent = input('Rent Amount: ')
    deposit = input('Deposit Amount: ')
    due = input('Rent Due: ')
    tenant = input('Tenant ID: ')
    late_time = input('Late Time: ')
    late_amount = input('Amount charged for late time: ')
    db.add_lease(num, date, end, rent, deposit, due, tenant, late_time, late_amount)
    print(f'---Lease {num} of tenant {tenant} added!---')
    
def del_lease():
    print('------Remove a lease from data------')
    num = int(input('Lease Number: '))
    db.del_lease(num)
    print(f'-----Lease {num} removed!-----')
    
def add_maintenance_request():
    print('------Add a request into data------')
    request_id = input('Request ID: ')
    date = input('Request Date (yyyy-mm-dd): ')
    category = input('Request Category: ')
    description = input('Brief description: ')
    requester = input('Requester ID: ')
    a_num = int(input('Apartment Number: '))
    db.add_maintenance_request(request_id, date, category, description, requester, a_num)
    print(f'---Maintenance request {request_id} for apartment {a_num} by {requester} submitted!---')
    
def del_maintenance_request():
    print('------Remove a request from data------')
    request_id = input('Request ID: ')
    db.del_maintenance_request(request_id)
    print(f'---Maintenance request {request_id} removed!---')
    
def add_maintenance_expense():
    print('------Add an expense into data------')
    request_id = input('Request ID: ')
    date = input('Resolution Date (yyyy-mm-dd): ')
    cost = float(input('Cost: '))
    description = input('Description: ')
    insurance = float(input('Insurance Coverage: '))
    db.add_maintenance_expense(request_id, date, cost, description, insurance)
    print(f'---An expense for request {request_id} recorded!---')

def del_maintenance_expense():
    print('------Remove an expense from data------')
    request_id = input('Request ID: ')
    db.del_maintenance_expense(request_id)
    print(f'-----An expense for request {request_id} removed!-----')
    
def add_per_apart():
    print('------Add a person with apartment into data------')
    person_id = input('Person ID: ')
    apart_num = int(input('Apartment Number: '))
    db.add_per_apart(person_id, apart_num)
    print(f'---Person {person_id} lives in apartment {apart_num} recorded!---')

def del_per_apart():
    print('------Remove a person with apartment from data------')
    person_id = input('Person ID: ')
    apart_num = int(input('Apartment Number: '))
    db.del_per_apart(person_id, apart_num)
    print(f'-----Person {person_id} lives in apartment {apart_num} removed!-----')
    
def get_lease():
    lease_num = int(input("Enter lease number: "))
    lease_data = db.get_lease_information(lease_num)
    if len(lease_data) == 0:
        print(f'Cannot find this lease number!')
    else:
        lease_list = []
        for i in lease_data:
            lease_list += i
        rent_date = lease_list[1]
        rent_end = lease_list[2]
        rent_amount = lease_list[3]
        deposit_amount = lease_list[4]
        rent_due = lease_list[5]
        tenant_id = lease_list[6]
        late_time = lease_list[7]
        late_amount = lease_list[8]
        print('**********Lease Information**********')
        print(f'***Lease Number: {lease_num}')
        print(f'***Rent Date: {rent_date}')
        print(f'***End Date: {rent_end}')
        print(f'***Rent Amount: {rent_amount}')
        print(f'***Deposit Amount: {deposit_amount}')
        print(f'***Rent Due: {rent_due}')
        print(f'***Tenant ID: {tenant_id}')
        print(f'***Late Time: {late_time}') 
        print(f'***Late Amount: {late_amount}')
        print('**********Thank You**********')

def get_quarterly_report():
    year = input('Enter the year: ')
    quarter_num = int(input('Select the quarter (Enter 1 to 4 for Spring to Winter): '))
    period = ['Spring', 'Summer', 'Autumn', 'Winter']
    if quarter_num < 1 or quarter_num > 4:
        print('Invalid quarter, please try again...')
        return get_quarterly_report()
    else:
        if quarter_num == 1:
            time1 = year + '-01-01'
            time2 = year + '-03-31'
        elif quarter_num == 2:
            time1 = year + '-04-01'
            time2 = year + '-06-30'
        elif quarter_num == 3:
            time1 = year + '-07-01'
            time2 = year + '-09-30'
        elif quarter_num == 4:
            time1 = year + '-10-01'
            time2 = year + '-12-31'
        timec1 = datetime.strptime(time1, '%Y-%m-%d')
        timef1 = timec1.strftime('%m/%d/%Y')
        timec2 = datetime.strptime(time2, '%Y-%m-%d')
        timef2 = timec2.strftime('%m/%d/%Y')
        complex_num = int(input('Select the complex number (1 to 20): '))
        if complex_num < 1 or complex_num > 20:
            print('Invalid complex number, please try again...')
        else:
            complex_nums = db.get_complex_num()
            nums_list = []
            for i in complex_nums:
                nums_list += i
            if not complex_num in nums_list:
                print('This complex number is not in the system...')
            else:
                complex_address = db.get_complex_address(complex_num)
                apartment_total = db.get_apartment_count(complex_num)
                tenant_total = db.get_tenant_count(time2, time2, complex_num)
                if apartment_total[0][0] == 0:
                    percent_occupied = 0
                else:
                    percent_occupied = round((tenant_total[0][0]/apartment_total[0][0])*100, 2)
                complex_q_revenue = db.get_revenue(time1, time2, complex_num)
                quarter_expense = db.get_expense(time1, time2, complex_num)
                changing_tenant = db.get_changing_tenant(time1, time2, complex_num)
                total_expense = 0
                for i in quarter_expense:
                    total_expense += (i[1]-i[2])
                if complex_q_revenue[0][0] == None:
                    pro_loss = 0 - total_expense
                else:
                    pro_loss = complex_q_revenue[0][0] - total_expense

                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                print('**********Wild Wood Apartment**********')
                print('************Quarterly Report***********')
                print(f'### Building#: #{complex_num}')
                print(f'### Address: {complex_address[0][0]}')
                print(f'### Quarter: {period[quarter_num - 1]} {year} ({timef2} - {timef2})')
                print(f'### Total Apartments: {apartment_total[0][0]}')
                print(f'### End of Quarter Occupied: {tenant_total[0][0]}')
                print(f'### Percent Occupied: {percent_occupied}%')
                print(f'### No. Changing Tenants: {changing_tenant[0][0]}')
                print('***************Revenues****************')
                print(f'### Total Rent Revenue: {complex_q_revenue[0][0]}')
                print(f'### Expenses:')
                for i in quarter_expense:
                    if i[1]-i[2] > 0:
                        print('###### '+i[0]+':', i[1]-i[2])
                print('--------------------')
                print(f'### Total Expenses: {total_expense}')
                print('>>>>>>>>>>>>>>>>>>>>')
                print(f'### Total Profit/Loss: {pro_loss}')
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

def get_yearly_report():
    year = input('Enter the year: ')
    complex_num = int(input('Select the complex number (1 to 20): '))
    if complex_num < 1 or complex_num > 20:
        print('Invalid complex number, please try again...')
    else:
        complex_nums = db.get_complex_num()
        nums_list = []
        for i in complex_nums:
            nums_list += i
        if not complex_num in nums_list:
            print('This complex number is not in the system...')
        else:
            time1 = year + '-01-01'
            time2 = year + '-12-31'
            complex_address = db.get_complex_address(complex_num)
            apartment_total = db.get_apartment_count(complex_num)
            tenant_total = db.get_tenant_count(time2, time2, complex_num)
            if apartment_total[0][0] == 0:
                percent_occupied = 0
            else:
                percent_occupied = round((tenant_total[0][0]/apartment_total[0][0])*100, 2)
            changing_tenant = db.get_changing_tenant(time1, time2, complex_num)
            year_revenue = db.get_revenue(time1, time2, complex_num)
            year_expense = db.get_expense(time1, time2, complex_num)
            total_expense = 0
            for i in year_expense:
                total_expense += (i[1]-i[2])
            if year_revenue[0][0] == None:
                pro_loss = 0 - total_expense
            else:
                pro_loss = year_revenue[0][0] - total_expense
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            print('**********Wild Wood Apartment**********')
            print('*************Yearly Report*************')
            print(f'### Building#: #{complex_num}')
            print(f'### Address: {complex_address[0][0]}')
            print(f'### Year: {year}')
            print(f'### Total Apartments: {apartment_total[0][0]}')
            print(f'### End of Year Occupied: {tenant_total[0][0]}')
            print(f'### Percent Occupied: {percent_occupied}%')
            print(f'### No. Changing Tenants: {changing_tenant[0][0]}')
            print('***************Revenues****************')
            print(f'### Total Rent Revenue: {year_revenue[0][0]}')
            print(f'### Expenses:')
            for i in year_expense:
                if i[1]-i[2] > 0:
                    print('###### '+i[0]+':', i[1]-i[2])
            print('--------------------')
            print(f'### Total Expenses: {total_expense}')
            print('>>>>>>>>>>>>>>>>>>>>')
            print(f'### Total Profit/Loss: {pro_loss}')
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    
def get_complex_overall_report():
    complex_num = int(input('Select the complex number (1 to 20): '))
    if complex_num < 1 or complex_num > 20:
        print('Invalid complex number, please try again...')
    else:
        complex_nums = db.get_complex_num()
        nums_list = []
        for i in complex_nums:
            nums_list += i
        if not complex_num in nums_list:
            print('This complex number is not in the system...')
        else:
            complex_address = db.get_complex_address(complex_num)
            apartment_total = db.get_apartment_count(complex_num)
            revenue = db.get_complex_total_revenue(complex_num)
            expense = db.get_complex_total_expense(complex_num)
            total_expense = 0
            for i in expense:
                total_expense += (i[1]-i[2])
            if revenue[0][0] == None:
                pro_loss = 0 - total_expense
            else:
                pro_loss = revenue[0][0] - total_expense
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            print('**********Wild Wood Apartment**********')
            print('*************Complex Report*************')
            print(f'### Building#: #{complex_num}')
            print(f'### Address: {complex_address[0][0]}')
            print(f'### Total Apartments: {apartment_total[0][0]}')
            print('***************Revenues****************')
            print(f'### Total Rent Revenue: {revenue[0][0]}')
            print(f'### Expenses:')
            for i in expense:
                if i[1]-i[2] > 0:
                    print('###### '+i[0]+':', i[1]-i[2])
            print('--------------------')
            print(f'### Total Expenses: {total_expense}')
            print('>>>>>>>>>>>>>>>>>>>>')
            print(f'### Total Profit/Loss: {pro_loss}')
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        
def get_total_complex_report():
    complex_total = db.get_complex_count()
    revenue = db.get_total_revenue()
    expense = db.get_total_expense()
    total_expense = 0
    for i in expense:
        total_expense += (i[1]-i[2])
    if revenue[0][0] == None:
        pro_loss = 0 - total_expense
    else:
        pro_loss = revenue[0][0] - total_expense
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('**********Wild Wood Apartment**********')
    print('*************Total Report*************')
    print(f'### Total Complexes: {complex_total[0][0]}')
    print('***************Revenues****************')
    print(f'### Total Rent Revenue: {revenue[0][0]}')
    print(f'### Expenses:')
    for i in expense:
        if i[1]-i[2] > 0:
            print('###### '+i[0]+':', i[1]-i[2])
    print('--------------------')
    print(f'### Total Expenses: {total_expense}')
    print('>>>>>>>>>>>>>>>>>>>>')
    print(f'### Total Profit/Loss: {pro_loss}')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        
def get_tenant_infor(tenant_id):
    tenant_infor = db.get_tenant_infor(tenant_id)
    print('########## Personal Information ##########')
    print('### ID:', tenant_id)
    print('### Full Name:', tenant_infor[0][1], tenant_infor[0][2])
    print('### Residence:', tenant_infor[0][3])
    print('### Ethnicity:', tenant_infor[0][4])
    print('### Gender:', tenant_infor[0][5])
    print('### Birthdate:', tenant_infor[0][6])
    print('##########################################')
    
def get_lease_tenant(lease_num):
    lease_infor = db.get_lease_t(lease_num)
    print('########## Lease Information ##########')
    print('### Lease Number:', lease_infor[0][0])
    print('### Tenant ID:', lease_infor[0][6])
    print('### Rent Start Date:', lease_infor[0][1])
    print('### Rend End Date:', lease_infor[0][2])
    print('### Rent Amount Charged:', lease_infor[0][3])
    print('### Deposit Amount:', lease_infor[0][4])
    print('### Payment Due:', lease_infor[0][5])
    print('### Overdue:', lease_infor[0][7])
    print('### Overdue Charged:', lease_infor[0][8])
    print('#######################################')
    
    
def menu():
    roles = ['Headquarter Manager', 'Complex Manager', 'Tenant', 'Exit']
    options = ['Add Data', 'See data', 'See reports', 'Remove Data', 'Exit']
    options_add_data = ['Add Person', 'Add Complex', 'Add Apartment', 'Add Person With Apartment', 'Add Lease', 'Add Maintenance Request', 'Add Maintenance Expense', 'Exit']
    options_del_data = ['Remove Person', 'Remove Complex', 'Remove Apartment', 'Remove Person With Apartment', 'Remove Lease', 'Remove Maintenance Request', 'Remove Maintenance Expense', 'Exit']
    options_see_data = ['People', 'Complex', 'Apartment', 'Person in Apartment', 'Lease Information', 'Maintenance Request', 'Maintenance Expense', 'Exit']
    options_see_reports = ['Quarterly Reports', 'Yearly Reports', 'Overall Reports', 'Tenant Reports', 'Exit']
    options_overall_reports = ['Complex Overall Reports', 'Total Complexes Report', 'Exit']
    options_tenant = ['Personal Information', 'Lease Reports', 'Exit']
    options_manager = ['See data', 'See reports', 'Exit']
    
    while True:
        print('----------Roles Options----------')
        for i, role in enumerate(roles):
            print(i+1, '-', role)
        choice = int(input('Select your role: '))
        if choice == len(roles):
            break
        elif choice == 1:
            print('----------Menu Options----------')
            for i, option in enumerate(options):
                print(i+1, '-', option)
            choice = int(input('Select an option: '))
            if choice == len(options):
                break
            elif choice == 1:
                print('----------Menu Options----------')
                for i, option in enumerate(options_add_data):
                    print(i+1, '-', option)
                choice = int(input('Select an option: '))
                if choice == len(options):
                    break
                elif choice == 1:
                    add_person()
                elif choice == 2:
                    add_complex()
                elif choice == 3:
                    add_apartment()
                elif choice == 4:
                    add_per_apart()
                elif choice == 5:
                    add_lease()
                elif choice == 6:
                    add_maintenance_request()
                elif choice == 7:
                    add_maintenance_expense()
                else:
                    print('############################################')
                    print('---------The selection is not valid---------')
                    print('-----Get back to options in a second...-----')
                    print('############################################')
            elif choice == 2:
                while True:
                    print('----------Data Options----------')
                    for i, option in enumerate(options_see_data):
                        print(i+1, '-', option)
                    choice = int(input('Select a data: '))
                    if choice == len(options_see_data):
                        break
                    elif choice == 1:
                        see_all_people()
                    elif choice == 2:
                        see_all_complex()
                    elif choice == 3:
                        see_all_apartment()
                    elif choice == 4:
                        see_all_person_apartment()
                    elif choice == 5:
                        see_all_lease()
                    elif choice == 6:
                        see_all_maintenance_request()
                    elif choice == 7:
                        see_all_maintenance_expense()
                    else:
                        print('############################################')
                        print('-----The selected data is not ready yet-----')
                        print('-----Get back to options in a second...-----')
                        print('############################################')
            elif choice == 3:
                while True:
                    print('----------Reports Options----------')
                    for i, option in enumerate(options_see_reports):
                        print(i+1, '-', option)
                    choice = int(input('Select a report: '))
                    if choice == len(options_see_reports):
                        break
                    elif choice == 1:
                        get_quarterly_report()
                    elif choice == 2:
                        get_yearly_report()
                    elif choice == 3:
                        for i, option in enumerate(options_overall_reports):
                            print(i+1, '-', option)
                        choice = int(input('Select a report: '))
                        if choice == len(options_overall_reports):
                            break
                        elif choice == 1:
                            get_complex_overall_report()
                        elif choice == 2:
                            get_total_complex_report()
                        else:
                            print('############################################')
                            print('---------The selection is not valid---------')
                            print('-----Get back to options in a second...-----')
                            print('############################################')
                    elif choice == 4:
                        tenant_id = input('Enter your ID: ')
                        tenant_get_id = db.get_tenant_id()
                        id_list = []
                        for i in tenant_get_id:
                            id_list += i
                        if not tenant_id in id_list:
                            print('This ID is not in the system...')
                        else:
                            print('----------Menu Options----------')
                            for i, option in enumerate(options_tenant):
                                print(i+1, '-', option)
                            choice = int(input('Select an option: '))
                            if choice == len(options_tenant):
                                break
                            elif choice == 1:
                                get_tenant_infor(tenant_id)
                            elif choice == 2:
                                num_lease = db.get_num_lease(tenant_id)
                                for i, lease in enumerate(num_lease):
                                    print(i+1, '-', lease[0])
                                lease_o = int(input('Select the lease: '))
                                if lease_o > len(num_lease) or lease_o < 1:
                                    print('Invalid selection...')
                                else:
                                    lease_num = num_lease[lease_o - 1][0]
                                    get_lease_tenant(lease_num)
                    else:
                        print('############################################')
                        print('---------The selection is not valid---------')
                        print('-----Get back to options in a second...-----')
                        print('############################################')
            elif choice == 4:
                print('----------Menu Options----------')
                for i, option in enumerate(options_del_data):
                    print(i+1, '-', option)
                choice = int(input('Select an option: '))
                if choice == len(options):
                    break
                elif choice == 1:
                    del_person()
                elif choice == 2:
                    del_complex()
                elif choice == 3:
                    del_apartment()
                elif choice == 4:
                    del_per_apart()
                elif choice == 5:
                    del_lease()
                elif choice == 6:
                    del_maintenance_request()
                elif choice == 7:
                    del_maintenance_expense()
                else:
                    print('############################################')
                    print('---------The selection is not valid---------')
                    print('-----Get back to options in a second...-----')
                    print('############################################')
            else:
                print('############################################')
                print('---------The selection is not valid---------')
                print('-----Get back to options in a second...-----')
                print('############################################')
        elif choice == 2:
            print('----------Menu Options----------')
            for i, option in enumerate(options_manager):
                print(i+1, '-', option)
            choice = int(input('Select an option: '))
            if choice == len(options_manager):
                break
            else:
                print('########################################################################')
                print('### The access of complex managers is similar to headquarters managers.')
                print('### The difference is when filtering data or reports,')
                print('### we need a condition about complex number where the manager lives in.')
                print('''### It will be taken from manager's apartment number.''')
                print('''### As for this app, 'till now, we focus mostly about''')
                print('''### headquarter managers and tenants.''')
                print('########################################################################')
        elif choice == 3:
            tenant_id = input('Enter your ID: ')
            tenant_get_id = db.get_tenant_id()
            id_list = []
            for i in tenant_get_id:
                id_list += i
            if not tenant_id in id_list:
                print('This ID is not in the system...')
            else:
                print('----------Menu Options----------')
                for i, option in enumerate(options_tenant):
                    print(i+1, '-', option)
                choice = int(input('Select an option: '))
                if choice == len(options_tenant):
                    break
                elif choice == 1:
                    get_tenant_infor(tenant_id)
                elif choice == 2:
                    num_lease = db.get_num_lease(tenant_id)
                    for i, lease in enumerate(num_lease):
                        print(i+1, '-', lease[0])
                    lease_o = int(input('Select the lease: '))
                    if lease_o > len(num_lease) or lease_o < 1:
                        print('Invalid selection...')
                    else:
                        lease_num = num_lease[lease_o - 1][0]
                        get_lease_tenant(lease_num)
                else:
                    print('############################################')
                    print('---------The selection is not valid---------')
                    print('-----Get back to options in a second...-----')
                    print('############################################')
        else:
            print('############################################')
            print('---------The selection is not valid---------')
            print('-----Get back to options in a second...-----')
            print('############################################')
    print('-----Thank you-----')

def test():
    complex_total = db.get_complex_count()
    revenue = db.get_total_revenue()
    expense = db.get_total_expense()
    total_expense = 0
    for i in expense:
        total_expense += (i[1]-i[2])
    if revenue[0][0] == None:
        pro_loss = 0 - total_expense
    else:
        pro_loss = revenue[0][0] - total_expense
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('**********Wild Wood Apartment**********')
    print('*************Total Report*************')
    print(f'### Total Complexes: {complex_total[0][0]}')
    print('***************Revenues****************')
    print(f'### Total Rent Revenue: {revenue[0][0]}')
    print(f'### Expenses:')
    for i in expense:
        if i[1]-i[2] > 0:
            print('###### '+i[0]+':', i[1]-i[2])
    print('--------------------')
    print(f'### Total Expenses: {total_expense}')
    print('>>>>>>>>>>>>>>>>>>>>')
    print(f'### Total Profit/Loss: {pro_loss}')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#test()
menu()