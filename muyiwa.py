#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install PySimpleGUI --user')


# # USER INTERFACE DESIGN

# In[1]:


class Bad_Data(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("User Data Error: ",self.msg)
    
#Uncomment This portion out if you would like to compile this into an application
import PySimpleGUI as sg

#Home Interface
form = sg.FlexForm('HYDROWAT VERSION 2.0')
qui=25
layout = [
          [sg.Text('Please enter your Data')],
          [sg.Text('Area of Land', size=(15, 1)), sg.InputText('459130')],
          [sg.Text('CN2 Value', size=(15, 1)),sg.InputText(qui),sg.Button('Calculate')],
          [sg.Text('Rainfall Data', size=(15, 1)), sg.InputText('source'),sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]
         ]
button, values = form.Layout(layout).Read()
print(button, values[0], values[1], values[2])


#Calculating the CNII Value after Pressing The Calculate button
if button == 'Calculate':
    
    #Selecting the Soil Types Present
    form = sg.FlexForm('Hydrologic Soil Group')

    layout = [
        [sg.Text('CN Estimation',size=(20,1),font=('Helvetica',15))],
        [sg.Text('Please Select Soil Type')],
        [sg.Checkbox('Hydrologic Soil Group A')],
        [sg.Checkbox('Hydrologic Soil Group B')],
        [sg.Checkbox('Hydrologic Soil Group C')],
        [sg.Checkbox('Hydrologic Soil Group D')],
        [sg.OK()]
         ]
    button, values = form.Layout(layout).Read()
    print(button, values[0], values[1], values[2], values[3])
    
    A=values[0]
    B=values[1]
    C=values[2]
    D=values[3]
    a=0
    b=0
    c=0
    d=0
    twist=[]
    
    #Information About Soil Type A
    print('Hydrologic Soil Group A')
    if(A==True):
        Type='A'
        form1 = sg.FlexForm('Soil Group Curve Number')
        layout1 = [
            [sg.Text('Hydrologic Soil Group A')],
            [sg.Text('Cultivated Land1: Without Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Cultivated Land1: With Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Poor Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Meadow: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Thin Sand, Poor Cover, No Mulch', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Good Covers', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 75% or more Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 50% to 75% Fair Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Commercial And Business Areas (85% Impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Industrial District 72% Impervious', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (65% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (38% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (30% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (25% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (20% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Paved parking lots, driveways', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (paved)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (gravel)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (dirt)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Button('Calculate')]
        ]
        button, values = form1.Layout(layout1).Read()
        values[0] = int(values[0]) * 72
        values[1] = int(values[1]) * 62
        values[2] = int(values[2]) * 68
        values[3] = int(values[3]) * 39
        values[4] = int(values[4]) * 30
        values[5] = int(values[5]) * 45
        values[6] = int(values[6]) * 25
        values[7] = int(values[7]) * 39
        values[8] = int(values[8]) * 49
        values[9] = int(values[9]) * 89
        values[10] = int(values[10]) * 81
        values[11] = int(values[11]) * 77
        values[12] = int(values[12]) * 61
        values[13] = int(values[13]) * 57
        values[14] = int(values[14]) * 54
        values[15] = int(values[15]) * 51
        values[16] = int(values[16]) * 98
        values[17] = int(values[17]) * 98
        values[18] = int(values[18]) * 76
        values[19] = int(values[19]) * 72
        
        v=0
        i=0
        for i in range(0,20):
            v+=values[i]
            i+=1

        print('Value of v is '+str(v))
        a=v/100
        print(button, values[0])
        twist.append(Type)
        
        
    #Information About Soil Type B
    print('Hydrologic Soil Group B')
    if(B==True):
        Type='B'
        form2 = sg.FlexForm('Soil Group Curve Number')
        layout2 = [
            [sg.Text('Hydrologic Soil Group B')],
            [sg.Text('Cultivated Land1: Without Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Cultivated Land1: With Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Poor Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Meadow: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Thin Sand, Poor Cover, No Mulch', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Good Covers', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 75% or more Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 50% to 75% Fair Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Commercial And Business Areas (85% Impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Industrial District 72% Impervious', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (65% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (38% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (30% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (25% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (20% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Paved parking lots, driveways', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (paved)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (gravel)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (dirt)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Button('Calculate')]
        ]
        button, values = form2.Layout(layout2).Read()
        
        values[0] = int(values[0]) * 81
        values[1] = int(values[1]) * 71
        values[2] = int(values[2]) * 79
        values[3] = int(values[3]) * 61
        values[4] = int(values[4]) * 58
        values[5] = int(values[5]) * 66
        values[6] = int(values[6]) * 55
        values[7] = int(values[7]) * 61
        values[8] = int(values[8]) * 69
        values[9] = int(values[9]) * 92
        values[10] = int(values[10]) * 88
        values[11] = int(values[11]) * 85
        values[12] = int(values[12]) * 75
        values[13] = int(values[13]) * 72
        values[14] = int(values[14]) * 70
        values[15] = int(values[15]) * 68
        values[16] = int(values[16]) * 98
        values[17] = int(values[17]) * 98
        values[18] = int(values[18]) * 85
        values[19] = int(values[19]) * 82
        
        w=0
        e=0
        for e in range(0,20):
            w+=values[e]
            e+=1

        print('Value of w is '+str(w))
        b=w/100
        print(button, values[0])
        twist.append(Type)
        
    
    #Information About Soil Type C    
    print('Hydrologic Soil Group C')
    if(C==True):
        Type='C'
        form3 = sg.FlexForm('Soil Group Curve Number')
        layout3 = [
            [sg.Text('Hydrologic Soil Group C')],
            [sg.Text('Cultivated Land1: Without Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Cultivated Land1: With Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Poor Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Meadow: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Thin Sand, Poor Cover, No Mulch', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Good Covers', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 75% or more Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 50% to 75% Fair Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Commercial And Business Areas (85% Impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Industrial District 72% Impervious', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (65% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (38% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (30% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (25% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (20% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Paved parking lots, driveways', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (paved)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (gravel)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (dirt)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Button('Calculate')]
        ]
        button, values = form3.Layout(layout3).Read()
        
        values[0] = int(values[0]) * 88
        values[1] = int(values[1]) * 78
        values[2] = int(values[2]) * 86
        values[3] = int(values[3]) * 74
        values[4] = int(values[4]) * 71
        values[5] = int(values[5]) * 77
        values[6] = int(values[6]) * 70
        values[7] = int(values[7]) * 74
        values[8] = int(values[8]) * 79
        values[9] = int(values[9]) * 94
        values[10] = int(values[10]) * 91
        values[11] = int(values[11]) * 90
        values[12] = int(values[12]) * 83
        values[13] = int(values[13]) * 81
        values[14] = int(values[14]) * 80
        values[15] = int(values[15]) * 79
        values[16] = int(values[16]) * 98
        values[17] = int(values[17]) * 98
        values[18] = int(values[18]) * 89
        values[19] = int(values[19]) * 87
        
        x=0
        o=0
        for o in range(0,20):
            x+=values[o]
            o+=1

        print('Value of x is '+str(x))
        c=x/100
        
        print(button, values[0])
        twist.append(Type)
    
    #Information About Soil Type D
    print('Hydrologic Soil Group D')
    if(D==True):
        Type='D'
        form4 = sg.FlexForm('Soil Group Curve Number')
        layout4 = [
            [sg.Text('Hydrologic Soil Group D')],
            [sg.Text('Cultivated Land1: Without Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Cultivated Land1: With Conservation treatment', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Poor Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Pasture or Range Land: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Meadow: Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Thin Sand, Poor Cover, No Mulch', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Wood or Forest Land: Good Covers', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 75% or more Good Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Open Space: Grass cover 50% to 75% Fair Condition', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Commercial And Business Areas (85% Impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Industrial District 72% Impervious', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (65% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (38% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (30% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (25% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Residential (20% impervious)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Paved parking lots, driveways', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (paved)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (gravel)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Text('Roads (dirt)', size=(40,1)), sg.InputText('0',size=(10,1))],
            [sg.Button('Calculate')]
        ]
        button, values = form4.Layout(layout4).Read()
        
        
        values[0] = int(values[0]) * 91
        values[1] = int(values[1]) * 81
        values[2] = int(values[2]) * 89
        values[3] = int(values[3]) * 80
        values[4] = int(values[4]) * 71
        values[5] = int(values[5]) * 78
        values[6] = int(values[6]) * 83
        values[7] = int(values[7]) * 77
        values[8] = int(values[8]) * 80
        values[9] = int(values[9]) * 84
        values[10] = int(values[10]) * 95
        values[11] = int(values[11]) * 93
        values[12] = int(values[12]) * 87
        values[13] = int(values[13]) * 86
        values[14] = int(values[14]) * 85
        values[15] = int(values[15]) * 84
        values[16] = int(values[16]) * 98
        values[17] = int(values[17]) * 98
        values[18] = int(values[18]) * 91
        values[19] = int(values[19]) * 89
        
        y=0
        u=0
        for u in range(0,20):
            y+=values[u]
            u+=1

        print('Value of y is '+str(y))
        d=y/100
        
        print(button, values[0])
        twist.append(Type)
        
    print(twist)
    qui=a+b+c+d
print('abcd ='+str(qui))

#Obtaining the Interface back With the Newly Calculated Value As the CNII Value
form = sg.FlexForm('HYDROWAT VERSION 2.0')
layout = [
          [sg.Text('Please enter your Data')],
          [sg.Text('Area of Land', size=(15, 1)), sg.InputText('459130')],
          [sg.Text('CN2 Value', size=(15, 1)),sg.InputText(qui)],
          [sg.Text('Rainfall Data', size=(15, 1)), sg.InputText('source'),sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]
         ]
button, values = form.Layout(layout).Read()
print(button, values[0], values[1], values[2])

runoff_month_list ={
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

runoff_week_list ={
    'Sun': 1,
    'Mon': 2,
    'Tue': 3,
    'Wed': 4,
    'Thur': 5,
    'Fri': 6,
    'Sat': 7
}

runoff_daily_list28={
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    '11':11,
    '12':12,
    '13':13,
    '14':14,
    '15':15,
    '16':16,
    '17':17,
    '18':18,
    '19':19,
    '20':20,
    '21':21,
    '22':22,
    '23':23,
    '24':24,
    '25':25,
    '26':26,
    '27':27,
    '28':28
}

runoff_daily_list30={
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    '11':11,
    '12':12,
    '13':13,
    '14':14,
    '15':15,
    '16':16,
    '17':17,
    '18':18,
    '19':19,
    '20':20,
    '21':21,
    '22':22,
    '23':23,
    '24':24,
    '25':25,
    '26':26,
    '27':27,
    '28':28,
    '29':29,
    '30':30
}

runoff_daily_list31={
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    '11':11,
    '12':12,
    '13':13,
    '14':14,
    '15':15,
    '16':16,
    '17':17,
    '18':18,
    '19':19,
    '20':20,
    '21':21,
    '22':22,
    '23':23,
    '24':24,
    '25':25,
    '26':26,
    '27':27,
    '28':28,
    '29':29,
    '30':30,
    '31':31
}

res_list=[]

def roundoff(answer):
    return float(round(answer, 4))

#Uncomment this Portion
area_of_land = int(round(float(values[0])))
cn_two = int(round(float(values[1])))
source_file = values[2]


cn_one = roundoff(float((4.2*cn_two) / (10-(0.058*cn_two))))
cn_three = roundoff(float((23*cn_two) / (10+(0.13*cn_two))))


#calculating s for each
s_cn_one = str(roundoff(float((1000/cn_one) - 10)))
s_cn_two = str(roundoff(float((1000/cn_two) - 10)))
s_cn_three = str(roundoff(float((1000/cn_three) - 10)))
pow=2

def pe_m(p,n,s,a):
    print('This is the value of n '+str(n))
    p = int(float(p))
    base = 2
    s=int(float(s))
    result_one = roundoff(float((p-(0.2*s))))
    print("These are the values of result_one,p,s respectively "+str(result_one),str(p),str(s))
    result_one = roundoff(float(result_one ** base))
    print("Here is the value of result one after use with the base "+str(result_one))
    result_two = roundoff(float(p+(0.8*s)))
    print("Here is the value of result_two "+str(result_two))
    if p == 0:
        result = 0
    else:
        result = roundoff(float((result_one/result_two)/1000))
    runoff_month(n,result,runoff_month_list)
    print("Overall operation result for the pe function "+str(result))
    run_off = roundoff(float(result*int(a)))
    return run_off


def pe_w(p,n,s,a):
    print('This is the value of n '+str(n))
    p = int(float(p))
    base = 2
    s=int(float(s))
    result_one = roundoff(float((p-(0.2*s))))
    print("These are the values of result_one,p,s respectively "+str(result_one),str(p),str(s))
    result_one = roundoff(float(result_one ** base))
    print("Here is the value of result one after use with the base "+str(result_one))
    result_two = roundoff(float(p+(0.8*s)))
    print("Here is the value of result_two "+str(result_two))
    if p == 0:
        result = 0
    else:
        result = roundoff(float((result_one/result_two)/1000))
    runoff_week(n,result,runoff_week_list)
    print("Overall operation result for the pe function "+str(result))
    run_off = roundoff(float(result*int(a)))
    return run_off

def pe_d(p,n,s,a):
    print('This is the value of n '+str(n))
    p = int(float(p))
    base = 2
    s=int(float(s))
    result_one = roundoff(float((p-(0.2*s))))
    print("These are the values of result_one,p,s respectively "+str(result_one),str(p),str(s))
    result_one = roundoff(float(result_one ** base))
    print("Here is the value of result one after use with the base "+str(result_one))
    result_two = roundoff(float(p+(0.8*s)))
    print("Here is the value of result_two "+str(result_two))
    if p == 0:
        result = 0
    else:
        result = roundoff(float((result_one/result_two)/1000))
    if Detective == 28 or orijin == 27:
        runoff_daily28(n,result,runoff_daily_list28)
    elif Detective == 30 or orijin == 29:
        runoff_daily30(n,result,runoff_daily_list30)
    elif Detective == 31 or orijin == 30:
        runoff_daily31(n,result,runoff_daily_list31)
    print("Overall operation result for the pe function "+str(result))
    run_off = roundoff(float(result*int(a)))
    return run_off

if source_file.endswith(('xlsx','xls')):    
    import pandas as pd
    excel_f = pd.read_excel(source_file,'Sheet1',index_col=None)
    excel_f.to_csv('created.csv', encoding = 'utf-8',index=None)
    source_file='created.csv'




if source_file.endswith(('.txt','.csv')):
    Detective=0
    print('Csv File Detected')
    print('')
    print('Reading CSV File')
    import time
    time.sleep(2)
    print('')
    print('Ready')
    print('')
    
    orijin=0
    fo = open(source_file, "r")
    Detectif = fo.readline()
    for line in Detectif:
        selector=line.count(',')
        if selector==1:
            orijin+=1

    if (orijin==6):
        print('Detected Weekly Data')
        print('')
        new_week_list ={
        'Sun': 1,
        'Mon': 2,
        'Tue': 3,
        'Wed': 4,
        'Thur': 5,
        'Fri': 6,
        'Sat': 7
        }

        week_list = [1,2,3,4,5,6,7]
        add_total_result = []
        fo = open(source_file, "r")
        count = fo.readlines()
        count = list([(el.strip()) for el in count])

        print('Here is the count length '+str(count))
        print('')

        count_length = len(count)
        list = []
        new_list = []
        for a in range(0, count_length):
            list.append(count[a].split(','))
        print(list)
        print('')

        count_list= len(list)
        print("This is the count list "+str(count_list))
        i = 0
        new_list=[]
        if i < count_list:
            for a in list:
                new_list.append(a)
                print(a)
                i = i+1
            print('New value for i '+str(i))
            print(new_list)

        if count_list==i:
            print("All list have been taking into consideration")
        else:
            print('Some list have been omitted')

            
            
    elif(26<orijin<31):
        print('Daily Data Detected')
        print('')
        if(orijin==27):
            print('Data for 28days detected')
            Daily=28
            new_daily_list28={
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                '11':11,
                '12':12,
                '13':13,
                '14':14,
                '15':15,
                '16':16,
                '17':17,
                '18':18,
                '19':19,
                '20':20,
                '21':21,
                '22':22,
                '23':23,
                '24':24,
                '25':25,
                '26':26,
                '27':27,
                '28':28
            }
            new_daily_list30={}
            new_daily_list31={}
        elif(orijin==29):
            print('Data For 30 Days Detected')
            Daily=30
            new_daily_list28={}
            new_daily_list30={
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                '11':11,
                '12':12,
                '13':13,
                '14':14,
                '15':15,
                '16':16,
                '17':17,
                '18':18,
                '19':19,
                '20':20,
                '21':21,
                '22':22,
                '23':23,
                '24':24,
                '25':25,
                '26':26,
                '27':27,
                '28':28,
                '29':29,
                '30':30
            }
            new_daily_list31={}
            
        elif(orijin==30):
            print('Data for 31 Days Detected')
            Daily=31
            new_daily_list28={}
            new_daily_list30={}
            new_daily_list31={
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                '11':11,
                '12':12,
                '13':13,
                '14':14,
                '15':15,
                '16':16,
                '17':17,
                '18':18,
                '19':19,
                '20':20,
                '21':21,
                '22':22,
                '23':23,
                '24':24,
                '25':25,
                '26':26,
                '27':27,
                '28':28,
                '29':29,
                '30':30,
                '31':31
            }
        if(Daily==28):
            Daily_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        elif(Daily==30):
            Daily_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        elif(Daily==31):
            Daily_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        else:
            try:
                raise Bad_Data('The Number of Days has an error')
            except Bad_Data as  e:
                e.print_exception()
                
        add_total_result = []
        fo = open(source_file, "r")
        count = fo.readlines()
        count = list([(el.strip()) for el in count])

        print('Here is the count length '+str(count))
        print('')
        
        count_length = len(count)
        list = []
        new_list = []
        for a in range(0, count_length):
            list.append(count[a].split(','))
        print(list)
        print('')
        
        count_list= len(list)
        print("This is the count list "+str(count_list))
        i = 0
        new_list=[]
        if i < count_list:
            for a in list:
                new_list.append(a)
                print(a)
                i = i+1
            print('New value for i '+str(i))
            print(new_list)

        if count_list==i:
            print("All list have been taking into consideration")
            print(orijin)
        else:
            print('Some list have been omitted')
        
        
    elif(orijin==11):
        print('Detected Monthly Data')
        print('')
        new_month_list ={
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
        }

        month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        add_total_result = []
        fo = open(source_file, "r")
        count = fo.readlines()
        count = list([(el.strip()) for el in count])

        print('Here is the count length '+str(count))
        print('')

        count_length = len(count)
        list = []
        new_list = []
        for a in range(0, count_length):
            list.append(count[a].split(','))
        print(list)
        print('')

        count_list= len(list)
        print("This is the count list "+str(count_list))
        i = 0
        new_list=[]
        if i < count_list:
            for a in list:
                new_list.append(a)
                print(a)
                i = i+1
            print('New value for i '+str(i))
            print(new_list)

        if count_list==i:
            print("All list have been taking into consideration")
        else:
            print('Some list have been omitted')
    else:
        print('Unknown Data Format Detected, Please view Templates')
        
elif source_file.endswith('.json'):
    orijin=0
    print('Json File Detected')
    print('')
    print('Reading Json File')
    import time
    time.sleep(2)
    
    
    import json
    with open(source_file) as f:
        data= json.load(f)
        #print(data)
        Detective=0
        new_list=[]
        for trick in data['tricks'][0]:
            Detective+=1
    if Detective==7:
        print('Weekly data detected')
        new_week_list ={
        'Sun': 1,
        'Tue': 2,
        'Wed': 3,
        'Thur': 4,
        'Fri': 5,
        'Sat': 6,
        'Sun': 7
        }
        week_list = [1,2,3,4,5,6,7]
        add_total_result = []

        import json
        with open(source_file) as f:
            data= json.load(f)
            #print(data)
            s=0
            new_list=[]
            for trick in data['tricks']:
                s+=1
                b=list([trick['Sun'],trick['Mon'],trick['Tue'],trick['Wed'],trick['Thur'],trick['Fri'],trick['Sat']])
                new_list.append(b)
            print(new_list)
            print('Number of weeks counted is '+str(s))
            
            
    elif(27<Detective<32):
        print('Daily Data Detected')
        print('')
        if(orijin==28):
            print('Data for 28days detected')
            new_daily_list={
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                '11':11,
                '12':12,
                '13':13,
                '14':14,
                '15':15,
                '16':16,
                '17':17,
                '18':18,
                '19':19,
                '20':20,
                '21':21,
                '22':22,
                '23':23,
                '24':24,
                '25':25,
                '26':26,
                '27':27,
                '28':28
            }
        elif(orijin==30):
            print('Data For 30 Days Detected')
            new_daily_list={
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                '11':11,
                '12':12,
                '13':13,
                '14':14,
                '15':15,
                '16':16,
                '17':17,
                '18':18,
                '19':19,
                '20':20,
                '21':21,
                '22':22,
                '23':23,
                '24':24,
                '25':25,
                '26':26,
                '27':27,
                '28':28,
                '29':29,
                '30':30
            }
        elif(orijin==31):
            print('Data for 31 Days Detected')
            new_daily_list={
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                '11':11,
                '12':12,
                '13':13,
                '14':14,
                '15':15,
                '16':16,
                '17':17,
                '18':18,
                '19':19,
                '20':20,
                '21':21,
                '22':22,
                '23':23,
                '24':24,
                '25':25,
                '26':26,
                '27':27,
                '28':28,
                '29':29,
                '30':30,
                '31':31
            }
        if(Daily==28):
            Daily_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        elif(Daily==30):
            Daily_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        elif(Daily==31):
            Daily_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        else:
            try:
                raise Bad_Data('The Number of Days has an error')
            except Bad_Data as  e:
                e.print_exception()
                
        add_total_result = []
        fo = open(source_file, "r")
        count = fo.readlines()
        count = list([(el.strip()) for el in count])

        print('Here is the count length '+str(count))
        print('')
        
        count_length = len(count)
        list = []
        new_list = []
        for a in range(0, count_length):
            list.append(count[a].split(','))
        print(list)
        print('')
        
        count_list= len(list)
        print("This is the count list "+str(count_list))
        i = 0
        new_list=[]
        if i < count_list:
            for a in list:
                new_list.append(a)
                print(a)
                i = i+1
            print('New value for i '+str(i))
            print(new_list)

        if count_list==i:
            print("All list have been taking into consideration")
        else:
            print('Some list have been omitted')
        
    elif Detective==12:
        print('Monthly data detected')
        new_month_list ={
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
        }
        month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        add_total_result = []

        import json
        with open(source_file) as f:
            data= json.load(f)
            #print(data)
            s=0
            new_list=[]
            for trick in data['tricks']:
                s+=1
                b=list([trick['Jan'],trick['Feb'],trick['Mar'],trick['Apr'],trick['May'],trick['Jun'],trick['Jul'],trick['Aug'],trick['Sep'],trick['Oct'],trick['Nov'],trick['Dec']])
                new_list.append(b)
            print(new_list)
            print('Number of years counted is '+str(s))
    else:
        print('value for Detective is '+str(Detective))
        print('Unknown Data Format Detected, Please view Templates')

# Operation for Monthly Analysis

if Detective == 12 or orijin == 11:

    def check_month(p, result, new_month_list):
        if p == 1:
            new_month_list['Jan'] = result
        elif p ==2 :
            new_month_list['Feb'] = result
        elif p == 3 :
            new_month_list['Mar'] = result
        elif p == 4 :
            new_month_list['Apr'] = result
        elif p == 5 :
            new_month_list['May'] = result
        elif p == 6 :
            new_month_list['Jun'] = result
        elif p == 7 :
            new_month_list['Jul'] = result
        elif p == 8:
            new_month_list['Aug'] = result
        elif p == 9:
            new_month_list['Sep'] = result
        elif p == 10:
            new_month_list['Oct'] = result
        elif p == 11:
            new_month_list['Nov'] = result
        elif p == 12:
            new_month_list['Dec'] = result


    #runoff month list
    def runoff_month(p, result, runoff_month_list):
        #print(p,result)
        if p == 1:
            runoff_month_list['Jan'] = result
        elif p ==2 :
            runoff_month_list['Feb'] = result
        elif p == 3 :
            runoff_month_list['Mar'] = result
        elif p == 4 :
            runoff_month_list['Apr'] = result
        elif p == 5 :
            runoff_month_list['May'] = result
        elif p == 6 :
            runoff_month_list['Jun'] = result
        elif p == 7 :
            runoff_month_list['Jul'] = result
        elif p == 8:
            runoff_month_list['Aug'] = result
        elif p == 9:
            runoff_month_list['Sep'] = result
        elif p == 10:
            runoff_month_list['Oct'] = result
        elif p == 11:
            runoff_month_list['Nov'] = result
        elif p == 12:
            runoff_month_list['Dec'] = result
    print('Monthly Specific Analysis in Operation')
    count_exec = 0
    count_item=0    
    while count_item < (len(new_list)):
        count_item+=1
        print('Value of Count item (The Years)'+str(count_item))
        for p in month_list:
            print('Value of p (The Months) '+str(p))
            a = new_list[count_item][p-1]
            print('Value of a '+str(a))
            print(month_list.index(p), new_list[count_item].index(a))
            if (p  == 8):
                result = pe_m(a,p,s_cn_two,area_of_land)
                add_total_result.append(result)
                check_month(p,result,new_month_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >2 and p < 8):
                result = pe_m(a,p,s_cn_three,area_of_land)
                add_total_result.append(result)
                check_month(p, result, new_month_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >8 and p<11):
                result = pe_m(a,p, s_cn_three, area_of_land)
                add_total_result.append(result)
                check_month(p, result, new_month_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p in range(11,13)):
                result = pe_m(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_month(p, result, new_month_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p ==1 or p==2):
                print('Value of s_cn_one '+s_cn_one)
                print('Value of land area '+str(area_of_land))
                result = pe_m(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_month(p, result, new_month_list)
                print('Value of Count item'+str(count_item))
                print('')

# Weekly Data Analysis
elif Detective == 7 or orijin == 6:

    def check_week(p, result, new_week_list):
        if p == 1:
            new_week_list['Sun'] = result
        elif p ==2 :
            new_week_list['Mon'] = result
        elif p == 3 :
            new_week_list['Tue'] = result
        elif p == 4 :
            new_week_list['Wed'] = result
        elif p == 5 :
            new_week_list['Thur'] = result
        elif p == 6 :
            new_week_list['Fri'] = result
        elif p == 7 :
            new_week_list['Sat'] = result


    #runoff month list
    def runoff_week(p, result, runoff_week_list):
        #print(p,result)
        if p == 1:
            runoff_week_list['Sun'] = result
        elif p ==2 :
            runoff_week_list['Mon'] = result
        elif p == 3 :
            runoff_week_list['Tue'] = result
        elif p == 4 :
            runoff_week_list['Wed'] = result
        elif p == 5 :
            runoff_week_list['Thur'] = result
        elif p == 6 :
            runoff_week_list['Fri'] = result
        elif p == 7 :
            runoff_week_list['Sat'] = result
    print('Weekly Specific Analysis in Operation')
    print('')
    count_exec = 0
    count_item=0
    while count_item < (len(new_list)):
        count_item+=1
        print('Value of Count item (The Weeks)'+str(count_item))
        for p in week_list:
            print('Value of p (The Days) '+str(p))
            a = new_list[count_item][p-1]
            print('Value of a '+str(a))
            print(week_list.index(p), new_list[count_item].index(a))
            if (p  == 8):
                result = pe_w(a,p,s_cn_two,area_of_land)
                add_total_result.append(result)
                check_week(p,result,new_week_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >2 and p < 8):
                result = pe_w(a,p,s_cn_three,area_of_land)
                add_total_result.append(result)
                check_week(p, result, new_week_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >8 and p<11):
                result = pe_w(a,p, s_cn_three, area_of_land)
                add_total_result.append(result)
                check_week(p, result, new_week_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p in range(11,13)):
                result = pe_w(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_week(p, result, new_week_list)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p ==1 or p==2):
                print('Value of s_cn_one '+s_cn_one)
                print('Value of land area '+area_of_land)
                result = pe_w(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_week(p, result, new_week_list)
                print('Value of Count item'+str(count_item))
                print('')


# Daily Data Analysis for 28days
elif Detective == 28 or orijin == 27:

    def check_daily28(p, result, new_daily_list28):
        if p == 1:
            new_daily_list28['1'] = result
        elif p ==2 :
            new_daily_list28['2'] = result
        elif p == 3 :
            new_daily_list28['3'] = result
        elif p == 4 :
            new_daily_list28['4'] = result
        elif p == 5 :
            new_daily_list28['5'] = result
        elif p == 6 :
            new_daily_list28['6'] = result
        elif p == 7 :
            new_daily_list28['7'] = result
        elif p == 8 :
            new_daily_list28['8'] = result
        elif p == 9 :
            new_daily_list28['9'] = result
        elif p == 10 :
            new_daily_list28['10'] = result
        elif p == 11 :
            new_daily_list28['11'] = result
        elif p == 12 :
            new_daily_list28['12'] = result
        elif p == 13 :
            new_daily_list28['13'] = result
        elif p == 14 :
            new_daily_list28['14'] = result
        elif p == 15 :
            new_daily_list28['15'] = result
        elif p == 16 :
            new_daily_list28['16'] = result
        elif p == 17 :
            new_daily_list28['17'] = result
        elif p == 18 :
            new_daily_list28['18'] = result
        elif p == 19 :
            new_daily_list28['19'] = result
        elif p == 20 :
            new_daily_list28['20'] = result
        elif p == 21 :
            new_daily_list28['21'] = result
        elif p == 22 :
            new_daily_list28['22'] = result
        elif p == 23 :
            new_daily_list28['23'] = result
        elif p == 24 :
            new_daily_list28['24'] = result
        elif p == 25 :
            new_daily_list28['25'] = result
        elif p == 26 :
            new_daily_list28['26'] = result
        elif p == 27 :
            new_daily_list28['27'] = result
        elif p == 28 :
            new_daily_list28['28'] = result
            

    #runoff month list
    def runoff_daily28(p, result, runoff_daily_list28):
        #print(p,result)
        if p == 1:
            new_daily_list28['1'] = result
        elif p ==2 :
            new_daily_list28['2'] = result
        elif p == 3 :
            new_daily_list28['3'] = result
        elif p == 4 :
            new_daily_list28['4'] = result
        elif p == 5 :
            new_daily_list28['5'] = result
        elif p == 6 :
            new_daily_list28['6'] = result
        elif p == 7 :
            new_daily_list28['7'] = result
        elif p == 8 :
            new_daily_list28['8'] = result
        elif p == 9 :
            new_daily_list28['9'] = result
        elif p == 10 :
            new_daily_list28['10'] = result
        elif p == 11 :
            new_daily_list28['11'] = result
        elif p == 12 :
            new_daily_list28['12'] = result
        elif p == 13 :
            new_daily_list28['13'] = result
        elif p == 14 :
            new_daily_list28['14'] = result
        elif p == 15 :
            new_daily_list28['15'] = result
        elif p == 16 :
            new_daily_list28['16'] = result
        elif p == 17 :
            new_daily_list28['17'] = result
        elif p == 18 :
            new_daily_list28['18'] = result
        elif p == 19 :
            new_daily_list28['19'] = result
        elif p == 20 :
            new_daily_list28['20'] = result
        elif p == 21 :
            new_daily_list28['21'] = result
        elif p == 22 :
            new_daily_list28['22'] = result
        elif p == 23 :
            new_daily_list28['23'] = result
        elif p == 24 :
            new_daily_list28['24'] = result
        elif p == 25 :
            new_daily_list28['25'] = result
        elif p == 26 :
            new_daily_list28['26'] = result
        elif p == 27 :
            new_daily_list28['27'] = result
        elif p == 28 :
            new_daily_list28['28'] = result
    print('Daily Specific Analysis in Operation')
    print('')
    count_exec = 0
    count_item=0
    while count_item < (len(new_list)):
        count_item+=1
        print('Value of Count item (The Month)'+str(count_item))
        for p in Daily_list:
            print('Value of p (The Days) '+str(p))
            a = new_list[count_item][p-1]
            print('Value of a '+str(a))
            print(Daily_list.index(p), new_list[count_item].index(a))
            if (p  == 8):
                result = pe_d(a,p,s_cn_two,area_of_land)
                add_total_result.append(result)
                check_daily28(p,result,new_daily_list28)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >2 and p < 8):
                result = pe_d(a,p,s_cn_three,area_of_land)
                add_total_result.append(result)
                check_daily28(p, result, new_daily_list28)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >8 and p<11):
                result = pe_d(a,p, s_cn_three, area_of_land)
                add_total_result.append(result)
                check_daily28(p, result, new_daily_list28)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p in range(11,32)):
                result = pe_d(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_daily28(p, result, new_daily_list28)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p ==1 or p==2):
                print('Value of s_cn_one '+s_cn_one)
                print('Value of land area '+str(area_of_land))
                result = pe_d(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_daily28(p, result, new_daily_list28)
                print('Value of Count item'+str(count_item))
                print('')
            
#Daily Data Analysis for 30Days
elif Detective == 30 or orijin == 29:
    
    def check_daily30(p, result, new_daily_list30):
        if p == 1:
            new_daily_list30['1'] = result
        elif p ==2 :
            new_daily_list30['2'] = result
        elif p == 3 :
            new_daily_list30['3'] = result
        elif p == 4 :
            new_daily_list30['4'] = result
        elif p == 5 :
            new_daily_list30['5'] = result
        elif p == 6 :
            new_daily_list30['6'] = result
        elif p == 7 :
            new_daily_list30['7'] = result
        elif p == 8 :
            new_daily_list30['8'] = result
        elif p == 9 :
            new_daily_list30['9'] = result
        elif p == 10 :
            new_daily_list30['10'] = result
        elif p == 11 :
            new_daily_list30['11'] = result
        elif p == 12 :
            new_daily_list30['12'] = result
        elif p == 13 :
            new_daily_list30['13'] = result
        elif p == 14 :
            new_daily_list30['14'] = result
        elif p == 15 :
            new_daily_list30['15'] = result
        elif p == 16 :
            new_daily_list30['16'] = result
        elif p == 17 :
            new_daily_list30['17'] = result
        elif p == 18 :
            new_daily_list30['18'] = result
        elif p == 19 :
            new_daily_list30['19'] = result
        elif p == 20 :
            new_daily_list30['20'] = result
        elif p == 21 :
            new_daily_list30['21'] = result
        elif p == 22 :
            new_daily_list30['22'] = result
        elif p == 23 :
            new_daily_list30['23'] = result
        elif p == 24 :
            new_daily_list30['24'] = result
        elif p == 25 :
            new_daily_list30['25'] = result
        elif p == 26 :
            new_daily_list30['26'] = result
        elif p == 27 :
            new_daily_list30['27'] = result
        elif p == 28 :
            new_daily_list30['28'] = result
        elif p == 29 :
            new_daily_list30['29'] = result
        elif p == 30 :
            new_daily_list30['30'] = result

    #runoff month list
    def runoff_daily30(p, result, runoff_daily_list30):
        #print(p,result)
        if p == 1:
            new_daily_list30['1'] = result
        elif p ==2 :
            new_daily_list30['2'] = result
        elif p == 3 :
            new_daily_list30['3'] = result
        elif p == 4 :
            new_daily_list30['4'] = result
        elif p == 5 :
            new_daily_list30['5'] = result
        elif p == 6 :
            new_daily_list30['6'] = result
        elif p == 7 :
            new_daily_list30['7'] = result
        elif p == 8 :
            new_daily_list30['8'] = result
        elif p == 9 :
            new_daily_list30['9'] = result
        elif p == 10 :
            new_daily_list30['10'] = result
        elif p == 11 :
            new_daily_list30['11'] = result
        elif p == 12 :
            new_daily_list30['12'] = result
        elif p == 13 :
            new_daily_list30['13'] = result
        elif p == 14 :
            new_daily_list30['14'] = result
        elif p == 15 :
            new_daily_list30['15'] = result
        elif p == 16 :
            new_daily_list30['16'] = result
        elif p == 17 :
            new_daily_list30['17'] = result
        elif p == 18 :
            new_daily_list30['18'] = result
        elif p == 19 :
            new_daily_list30['19'] = result
        elif p == 20 :
            new_daily_list30['20'] = result
        elif p == 21 :
            new_daily_list30['21'] = result
        elif p == 22 :
            new_daily_list30['22'] = result
        elif p == 23 :
            new_daily_list30['23'] = result
        elif p == 24 :
            new_daily_list30['24'] = result
        elif p == 25 :
            new_daily_list30['25'] = result
        elif p == 26 :
            new_daily_list30['26'] = result
        elif p == 27 :
            new_daily_list30['27'] = result
        elif p == 28 :
            new_daily_list30['28'] = result
        elif p == 29 :
            new_daily_list30['29'] = result
        elif p == 30 :
            new_daily_list30['30'] = result
    print('Daily Specific Analysis in Operation')
    print('')
    count_exec = 0
    count_item=0
    while count_item < (len(new_list)):
        count_item+=1
        print('Value of Count item (The Month)'+str(count_item))
        for p in Daily_list:
            print('Value of p (The Days) '+str(p))
            a = new_list[count_item][p-1]
            print('Value of a '+str(a))
            print(Daily_list.index(p), new_list[count_item].index(a))
            if (p  == 8):
                result = pe_d(a,p,s_cn_two,area_of_land)
                add_total_result.append(result)
                check_daily30(p,result,new_daily_list30)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >2 and p < 8):
                result = pe_d(a,p,s_cn_three,area_of_land)
                add_total_result.append(result)
                check_daily30(p, result, new_daily_list30)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p >8 and p<11):
                result = pe_d(a,p, s_cn_three, area_of_land)
                add_total_result.append(result)
                check_daily30(p, result, new_daily_list30)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p in range(11,32)):
                result = pe_d(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_daily30(p, result, new_daily_list30)
                print('Value of Count item'+str(count_item))
                print('')
            elif (p ==1 or p==2):
                print('Value of s_cn_one '+s_cn_one)
                print('Value of land area '+str(area_of_land))
                result = pe_d(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_daily30(p, result, new_daily_list30)
                print('Value of Count item'+str(count_item))
                print('')

#Daily Data Analysis for 31 Days
elif Detective == 31 or orijin == 30:
    def check_daily31(p, result, new_daily_list31):
        if p == 1:
            new_daily_list31['1'] = result
        elif p ==2 :
            new_daily_list31['2'] = result
        elif p == 3 :
            new_daily_list31['3'] = result
        elif p == 4 :
            new_daily_list31['4'] = result
        elif p == 5 :
            new_daily_list31['5'] = result
        elif p == 6 :
            new_daily_list31['6'] = result
        elif p == 7 :
            new_daily_list31['7'] = result
        elif p == 8 :
            new_daily_list31['8'] = result
        elif p == 9 :
            new_daily_list31['9'] = result
        elif p == 10 :
            new_daily_list31['10'] = result
        elif p == 11 :
            new_daily_list31['11'] = result
        elif p == 12 :
            new_daily_list31['12'] = result
        elif p == 13 :
            new_daily_list31['13'] = result
        elif p == 14 :
            new_daily_list31['14'] = result
        elif p == 15 :
            new_daily_list31['15'] = result
        elif p == 16 :
            new_daily_list31['16'] = result
        elif p == 17 :
            new_daily_list31['17'] = result
        elif p == 18 :
            new_daily_list31['18'] = result
        elif p == 19 :
            new_daily_list31['19'] = result
        elif p == 20 :
            new_daily_list31['20'] = result
        elif p == 21 :
            new_daily_list31['21'] = result
        elif p == 22 :
            new_daily_list31['22'] = result
        elif p == 23 :
            new_daily_list31['23'] = result
        elif p == 24 :
            new_daily_list31['24'] = result
        elif p == 25 :
            new_daily_list31['25'] = result
        elif p == 26 :
            new_daily_list31['26'] = result
        elif p == 27 :
            new_daily_list31['27'] = result
        elif p == 28 :
            new_daily_list31['28'] = result
        elif p == 29 :
            new_daily_list31['29'] = result
        elif p == 30 :
            new_daily_list31['30'] = result
        elif p == 31 :
            new_daily_list31['31'] = result

    #runoff month list
    def runoff_daily31(p, result, runoff_daily_list31):
        #print(p,result)
        if p == 1:
            new_daily_list31['1'] = result
        elif p ==2 :
            new_daily_list31['2'] = result
        elif p == 3 :
            new_daily_list31['3'] = result
        elif p == 4 :
            new_daily_list31['4'] = result
        elif p == 5 :
            new_daily_list31['5'] = result
        elif p == 6 :
            new_daily_list31['6'] = result
        elif p == 7 :
            new_daily_list31['7'] = result
        elif p == 8 :
            new_daily_list31['8'] = result
        elif p == 9 :
            new_daily_list31['9'] = result
        elif p == 10 :
            new_daily_list31['10'] = result
        elif p == 11 :
            new_daily_list31['11'] = result
        elif p == 12 :
            new_daily_list31['12'] = result
        elif p == 13 :
            new_daily_list31['13'] = result
        elif p == 14 :
            new_daily_list31['14'] = result
        elif p == 15 :
            new_daily_list31['15'] = result
        elif p == 16 :
            new_daily_list31['16'] = result
        elif p == 17 :
            new_daily_list31['17'] = result
        elif p == 18 :
            new_daily_list31['18'] = result
        elif p == 19 :
            new_daily_list31['19'] = result
        elif p == 20 :
            new_daily_list31['20'] = result
        elif p == 21 :
            new_daily_list31['21'] = result
        elif p == 22 :
            new_daily_list31['22'] = result
        elif p == 23 :
            new_daily_list31['23'] = result
        elif p == 24 :
            new_daily_list31['24'] = result
        elif p == 25 :
            new_daily_list31['25'] = result
        elif p == 26 :
            new_daily_list31['26'] = result
        elif p == 27 :
            new_daily_list31['27'] = result
        elif p == 28 :
            new_daily_list31['28'] = result
        elif p == 29 :
            new_daily_list31['29'] = result
        elif p == 30 :
            new_daily_list31['30'] = result
        elif p == 31 :
            new_daily_list31['31'] = result
    print('Daily Specific Analysis in Operation')
    print('')
    count_exec = 0
    count_item=0
    lim=0
    pe_list=[]
    nd31_collect=[]
    while count_item < (len(new_list)):
        count_item+=1
        print('Value of Count item (The Months)'+str(count_item-1))
        for p in Daily_list:
            print('Value of p (The Days) '+str(p))
            a = new_list[count_item-1][p-1]
            print('Value of a '+str(a))
            print(Daily_list.index(p), new_list[count_item-1].index(a))
            if (p  == 8):
                result = pe_d(a,p,s_cn_two,area_of_land)
                add_total_result.append(result)
                check_daily31(p,result,new_daily_list31)
                print('Value of Count item'+str(count_item-1))
                pe_list.append(result)
                res_list.append(result)
                grp=len(res_list)
                guide=grp%31
                if (guide==0):
                    bnd=grp/31
                    bnd=int(bnd)
                    up_bnd=(31*bnd)
                    lowbnd=bnd-1
                    low_bnd=(31*lowbnd)
                    mth=[]
                    for g in range(low_bnd,up_bnd):
                        val=int(res_list[g])
                        mth.append(val)
                    nd31_collect.append(mth)
                lim=lim+1
                print(lim)
                if(lim==31):
                
                    import matplotlib.pyplot as plt; plt.rcdefaults()
                    import numpy as np
                    import matplotlib.pyplot as plt
                    plt.figure()
                    plt.subplot(2,1,2)
                    #Plotting The Graph for RunOff
                    y_pos = np.arange(len(pe_list))
                    dailyP=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
                    plt.scatter(y_pos, pe_list, linestyle='-', marker='o')
                    plt.xticks(y_pos,dailyP)
                    plt.ylabel('Runoff Values')
                    plt.title('Runoff Graph')
                    plt.savefig('Runoff_Graph'+str(count_item-1)+'.pdf')
                    plt.show()
                    print('Graph of RunOff Generated')
                    print('')
                    pe_list=[]
                    lim=0
                    
                    
                print('')
            elif (p >2 and p < 8):
                result = pe_d(a,p,s_cn_three,area_of_land)
                add_total_result.append(result)
                check_daily31(p, result, new_daily_list31)
                print('Value of Count item'+str(count_item-1))
                
                
                pe_list.append(result)
                res_list.append(result)
                grp=len(res_list)
                guide=grp%31
                if (guide==0):
                    bnd=grp/31
                    bnd=int(bnd)
                    up_bnd=(31*bnd)
                    lowbnd=bnd-1
                    low_bnd=(31*lowbnd)
                    mth=[]
                    for g in range(low_bnd,up_bnd):
                        val=int(res_list[g])
                        mth.append(val)
                    nd31_collect.append(mth)
                lim=lim+1
                print(lim)
                if(lim==31):
                
                    import matplotlib.pyplot as plt; plt.rcdefaults()
                    import numpy as np
                    import matplotlib.pyplot as plt
                    plt.figure()
                    plt.subplot(2,1,2)
                    #Plotting The Graph for RunOff
                    y_pos = np.arange(len(pe_list))
                    dailyP=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
                    plt.plot(y_pos, pe_list, linestyle='-', marker='o')
                    plt.xticks(y_pos,dailyP)
                    plt.ylabel('Runoff Values')
                    plt.title('Runoff Graph')
                    plt.savefig('Runoff_Graph'+str(count_item-1)+'.pdf')
                    plt.show()
                    print('Graph of RunOff Generated')
                    print('')
                    pe_list=[]
                    lim=0
                
                
                
                print('')
            elif (p >8 and p<11):
                result = pe_d(a,p, s_cn_three, area_of_land)
                add_total_result.append(result)
                check_daily31(p, result, new_daily_list31)
                print('Value of Count item'+str(count_item-1))
                
                pe_list.append(result)
                res_list.append(result)
                grp=len(res_list)
                guide=grp%31
                if (guide==0):
                    bnd=grp/31
                    up_bnd=(31*bnd)
                    lowbnd=bnd-1
                    low_bnd=(31*lowbnd)
                    mth=[]
                    for g in range(low_bnd,up_bnd):
                        val=int(res_list[g])
                        mth.append(val)
                    nd31_collect.append(mth)
                lim=lim+1
                print(lim)
                if(lim==31):
                
                    import matplotlib.pyplot as plt; plt.rcdefaults()
                    import numpy as np
                    import matplotlib.pyplot as plt
                    plt.figure()
                    plt.subplot(2,1,2)
                    #Plotting The Graph for RunOff
                    y_pos = np.arange(len(pe_list))
                    dailyP=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
                    plt.plot(y_pos, pe_list, linestyle='-', marker='o')
                    plt.xticks(y_pos,dailyP)
                    plt.ylabel('Runoff Values')
                    plt.title('Runoff Graph')
                    plt.savefig('Runoff_Graph'+str(count_item-1)+'.pdf')
                    plt.show()
                    print('Graph of RunOff Generated')
                    print('')
                    pe_list=[]
                    lim=0
                
                
                print('')
            elif (p in range(11,32)):
                result = pe_d(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_daily31(p, result, new_daily_list31)
                print('Value of Count item'+str(count_item-1))
                
                pe_list.append(result)
                res_list.append(result)
                grp=len(res_list)
                guide=grp%31
                if (guide==0):
                    bnd=grp/31
                    bnd=int(bnd)
                    up_bnd=(31*bnd)
                    lowbnd=bnd-1
                    low_bnd=(31*lowbnd)
                    mth=[]
                    for g in range(low_bnd,up_bnd):
                        val=int(res_list[g])
                        mth.append(val)
                    nd31_collect.append(mth)
                lim=lim+1
                print(lim)
                if(lim==31):
                
                    import matplotlib.pyplot as plt; plt.rcdefaults()
                    import numpy as np
                    import matplotlib.pyplot as plt
                    plt.figure()
                    plt.subplot(2,1,2)
                    #Plotting The Graph for RunOff
                    y_pos = np.arange(len(pe_list))
                    dailyP=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
                    plt.plot(y_pos, pe_list, linestyle='-', marker='o')
                    plt.xticks(y_pos,dailyP)
                    plt.ylabel('Runoff Values')
                    plt.title('Runoff Graph')
                    plt.savefig('Runoff_Graph'+str(count_item-1)+'.pdf')
                    plt.show()
                    print('Graph of RunOff Generated')
                    print('')
                    pe_list=[]
                    lim=0
                
                
                print('')
            elif (p ==1 or p==2):
                print('Value of s_cn_one '+s_cn_one)
                print('Value of land area '+str(area_of_land))
                result = pe_d(a,p,s_cn_one,area_of_land)
                add_total_result.append(result)
                check_daily31(p, result, new_daily_list31)
                print('Value of Count item'+str(count_item-1))
                
                pe_list.append(result)
                res_list.append(result)
                grp=len(res_list)
                guide=grp%31
                if (guide==0):
                    bnd=grp/31
                    up_bnd=(31*bnd)
                    lowbnd=bnd-1
                    low_bnd=(31*lowbnd)
                    mth=[]
                    for g in range(low_bnd,up_bnd):
                        val=int(res_list[g])
                        mth.append(val)
                    nd31_collect.append(mth)
                lim=lim+1
                print(lim)
                if(lim==31):
                
                    import matplotlib.pyplot as plt; plt.rcdefaults()
                    import numpy as np
                    import matplotlib.pyplot as plt
                    plt.figure()
                    plt.subplot(2,1,2)
                    #Plotting The Graph for RunOff
                    y_pos = np.arange(len(pe_list))
                    dailyP=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
                    plt.plot(y_pos, pe_list, linestyle='-', marker='o')
                    plt.xticks(y_pos,dailyP)
                    plt.ylabel('Runoff Values')
                    plt.title('Runoff Graph')
                    plt.savefig('Runoff_Graph'+str(count_item-1)+'.pdf')
                    plt.show()
                    print('Graph of RunOff Generated')
                    print('')
                    pe_list=[]
                    lim=0
                
                
                print('')
    #Comment Interface
    form = sg.FlexForm('Comment Interface')

    layout = [
              [sg.Text('Please Check The Graphs Generated and Comment')],
              [sg.Text('Recommendation', size=(15, 1)), sg.InputText('Comment')],
              [sg.Submit(), sg.Cancel()]
             ]
    button, values = form.Layout(layout).Read()



    def generate_results(result):
        with open('results.csv', 'a') as res:
            res.write(result)    

    if button == 'Submit':
        generate_results("No of months to be calcualted is %d \n" % len(new_list))
        generate_results("CN1: %s\n" % str(cn_one))
        generate_results("CN2: %s\n" % str(cn_two))
        generate_results("CN3: %s\n" % str(cn_three))
        generate_results("S value of  CN1: %s\n" % str(s_cn_one))
        generate_results ("S value of  CN2: %s\n" % str(s_cn_two))
        generate_results("S value of  CN3: %s\n" % str(s_cn_three))
        generate_results("Runoff for each day\n")
        i=0
        for gini in range(0,int(count_item)):
            i=i+1
            generate_results(str(nd31_collect[gini])+ '\n') 
        generate_results("Total runoff of rainfall: %s\n" % str(sum(add_total_result)))
        generate_results("Comment Made on The Result: %s\n" % str(values[0]))
        count_exec = 1
        add_total_result.clear()
        count_item = count_item +1
        print('Result written to results.csv')
    else:
        generate_results("Results for %s month\n" % (count_item+1))
        generate_results("Runoff for each day\n")
        i=0
        for gini in range(0,int(count_item)):
            i=i+1
            generate_results(str(nd31_collect[gini])+ '\n') 
        generate_results("Total runoff of rainfall: %s\n" % str(sum(add_total_result)))
        generate_results("Comment Made on The Result: %s\n" % str(values[0]))
        count_exec = 1
        add_total_result.clear()
        count_item = count_item +1
        print('Result Previously written to results.csv')

if Detective == 12 or orijin == 11:
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt

    print('Generating Graph of Runoff')

    plt.figure()
    plt.subplot(2,1,2)
    #Plotting The Graph for RunOff
    January=new_month_list['Jan']
    February=new_month_list['Feb']
    March=new_month_list['Mar']
    April=new_month_list['Apr']
    May=new_month_list['May']
    June=new_month_list['Jun']
    July=new_month_list['Jul']
    August=new_month_list['Aug']
    September=new_month_list['Sep']
    October=new_month_list['Oct']
    November=new_month_list['Nov']
    December=new_month_list['Dec']
    months=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
    y_pos = np.arange(len(months))
    Values=(January,February,March,April,May,June,July,August,September,October,November,December)
    top=max(Values)
    plt.scatter(y_pos, pe_list, linestyle='-', marker='o')
    plt.xticks(y_pos,months)
    plt.ylabel('Runoff Values')
    plt.title('Bar Plot of Runoff')
    plt.savefig('Runoff_Graph.pdf')
    plt.show()
    print('Graph of RunOff Generated')
    print('')


    #Comment Interface
    form = sg.FlexForm('Comment Interface')

    layout = [
          [sg.Text('Please Check The Graphs Generated and Comment')],
          [sg.Text('Recommendation', size=(15, 1)), sg.InputText('Comment')],
          [sg.Submit(), sg.Cancel()]
         ]
    button, values = form.Layout(layout).Read()



    def generate_results(result):
        with open('results.csv', 'a') as res:
            res.write(result)    

    if button == 'Submit':
        generate_results("No of years to be calcualted is %d \n" % len(new_list))
        generate_results("CN1: %s\n" % str(cn_one))
        generate_results("CN2: %s\n" % str(cn_two))
        generate_results("CN3: %s\n" % str(cn_three))
        generate_results("S value of  CN1: %s\n" % str(s_cn_one))
        generate_results ("S value of  CN2: %s\n" % str(s_cn_two))
        generate_results("S value of  CN3: %s\n" % str(s_cn_three))
        generate_results("Pe for each month\n")
        generate_results(str(runoff_month_list)+'\n')
        generate_results("Runoff for each month\n")
        generate_results(str(new_month_list)+ '\n')    
        generate_results("Total runoff of rainfall: %s\n" % str(sum(add_total_result)))
        generate_results("Comment Made on The Result: %s\n" % str(values[0]))
        generate_results("")
        count_exec = 1
        add_total_result.clear()
        count_item = count_item +1
        print('Result written to results.csv')
    else:
        generate_results("Results for %s year\n" % (count_item+1))
        generate_results("Pe for each month\n")
        generate_results(str(runoff_month_list)+'\n')
        generate_results("Runoff for each month\n")
        generate_results(str(new_month_list)+'\n')    
        generate_results("Total runoff of rainfall: %s\n" % str(sum(add_total_result)))
        generate_results("Comment Made on The Result: %s\n" % str(Comment))
        count_exec = 1
        add_total_result.clear()
        count_item = count_item +1
        print('Result Previously written to results.csv')


# In[ ]:





# In[ ]:




