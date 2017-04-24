#!/usr/bin/python3
#
# A simple serial application to control the orbital shaker.
#
# 2016 Bruce Lipp <bruce.lipp@dri.edu>
#
import serial
import time
import logging

# comport = "/dev/tty.usbserial-AL01Z6CH"
comport = "/dev/ttyUSB0"
ser = serial.Serial()
ser.port = comport
ser.baudrate = 1200
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1          # non-block read
ser.xonxoff = False      # disable software flow control
ser.rtscts = False       # disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       # disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     # timeout for write


def _openserialport():
    logger = logging.getLogger('ODServiceRoutine.py')
    logger.info('Opening serial port...')
    if not ser.isOpen():
        ser.open()
        time.sleep(1)
    logger.info('Serial port open = %s', ser.isOpen())
    return


def _closeserialport():
    logger = logging.getLogger('ODServiceRoutine.py')
    logger.info('Closing serial port...')
    if ser.isOpen():
        ser.close()
        time.sleep(1)
    logger.info('Serial port open = %s', ser.isOpen())
    return


def _sendcommand(command):
    logger = logging.getLogger('ODServiceRoutine.py')
    logger.info('Sending command %s', command)
    ser.write(command.encode('utf-8'))
    response = ser.read(100)
    if command.encode('utf-8').strip() in response:
        return True
    else:
        logger.error('Incorrect response: %s', response)
        return False


def startoscillating():
    _openserialport()
    _sendcommand('I=*\r')    # Take out of index mode
    _sendcommand('S0225\r')  # Oscillate at 225 rpm
    _closeserialport()


def stoposcillating():
    _openserialport()
    _sendcommand('I=*\r')    # Take out of index mode
    _sendcommand('O\r')  # Oscillate at 0 rpm
    _closeserialport()


# stoposcillating()
# time.sleep(10)
# startoscillating()
