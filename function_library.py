import serial.tools.list_ports
import time
    
def read_data_from_scale(serial_port_scale, baud=9600): #reads data from ohaus scale
    ser = serial.Serial(serial_port_scale, baudrate=baud, timeout = 1)
    ser.write('P\n\r'.encode('UTF-8'))
    s = ser.read(106) #just use readline here? 
    rawData=s.decode('utf-8') 
    index=0
    values=[]
    while index < 8:
        if len(rawData) == 0:
            print('no data')
            time.sleep(0.1) 
            ser.write('P\n\r'.encode('UTF-8'))
            s = ser.read(106) 
            rawData=s.decode('utf-8')
            continue
        elif rawData[index+3] == '-': 
            values.append("-")
        elif rawData[index+3] == ' ': 
            values.append(0)
        elif rawData[index+3]== '.':
            index+=1
            continue
        else:
            values.append(int(rawData[index+3]))
        index+=1
    stelle=10000 
    data=0
    sign_of_weight=1
    for obj in values: 
        if obj == "-":
            sign_of_weight=-1 
            stelle=stelle/10 
            continue
        data+=obj*stelle  
        stelle=stelle/10 
        
    data *= sign_of_weight 
    return data

    
        
