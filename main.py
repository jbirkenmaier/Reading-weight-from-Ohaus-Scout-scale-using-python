'''
BASIC EXAMPLE

This is a very simple example for the use of the function 'read_data_from_scale(...)',
just make sure to set the correct serial port that the scale is connected to, in my case that is 'COM3'
'''

serial_port_of_scale = 'COM3'
weight = read_data_from_scale(serial_port_of_scale)

print(weight)

        
