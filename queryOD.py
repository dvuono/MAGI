#!/usr/bin/python

import serial
import time
import datetime

# request and receives a data string of OD readings from the arduino.
# the "poke and listen" methodology is used rather than the apparently
# more simply configuration of having the arduino stream at regular 
# intervals and the Pi just listen when needed because that seems to 
# lead to buffering induced data mangling.
# slight delays are added at points to prevent buffering issues


### --------------------
# configure the data logging interval in seconds
sample_interval = 2
# data file name
data_file = 'test_data.txt'

# configure the serial port
serial_port = "/dev/ttyACM0"
baud_rate = 9600
time_out = 0.1
serial_cnx = serial.Serial(serial_port, baud_rate, timeout = time_out)
serial_cnx.flush()

### --------------------

def request_receive_data():
    # doesn't matter what is sent, just poke the arduino
    serial_cnx.write('1')
    while True:
        try:
            time.sleep(0.01)
            # throw away two lines to get the buffer straightened out
            data_line = serial_cnx.readline()
            return data_line
        except:
            pass
    time.sleep(0.1)

# throw out a couple lines to clear the buffer
request_receive_data()
request_receive_data()

# open the data file and start writing data
data_file_fh =  open(data_file, 'a')
while True:
    time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')
    this_data = request_receive_data()
    data_string = time_stamp + ';' + this_data
    print data_string
    data_file_fh.write(data_string + '\n')
    time.sleep(2)
data_file_fh.close()

