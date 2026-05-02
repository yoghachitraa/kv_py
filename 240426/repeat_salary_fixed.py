def procces_payroll () :
    base_salary = float(input('Base Salary:'))
    hra_per = float(input('HRA%:'))
    da_per = float(input('DA%:'))
    ta_per = float(input('TA%:'))
    pf_per = float(input('PF%:'))

    hra = (base_salary / 100) * hra_per
    da = (base_salary / 100) * da_per
    ta = (base_salary / 100) * ta_per

    gross_salary = base_salary + hra + da + ta 
    pf = (gross_salary / 100) * pf_per

    net_salary = gross_salary - pf 

    print(f'Base Salary: {base_salary:.2f}')
    print(f'HRA {hra_per:.2f}%: {hra:.2f}')
    print(f'DA {da_per:.2f}%: {da:.2f}')
    print(f'TA {ta_per:.2f}%: {ta:.2f}')
    print(f'Gross Salary: {gross_salary:.2f}')
    print(f'PF {pf_per:.2f}%: {pf:.2f}')
    print(f'Net Salary: {net_salary:.2f}')

    if net_salary >= 100000 :
        print ( ' 6 digit salaried ')
    else : 
        print ( ' not 6 digit salaried ')




print('Start of app...')
times = int(input('Number of times:')) # 5
# for I in range(times): #0 1 2 3 4 [5 exclue]
for I in range(1, times+1): #1 2 3 4 5 [6 exclue]
    procces_payroll()
print('End of app. Thank you for using app!')
