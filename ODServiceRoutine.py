#!/usr/bin/python3
# ODServiceRoutine.py
# The main control function for periodic instrumentation reads.
#
# 2016 Bruce Lipp (AKA The General) <bruce.lipp@dri.edu>
#
import logging
import time
import datetime
import OrbitalShakerDriver
import queryODAsEthernetClient
import os.path
import ReadDataFromFile
import os
import sys


# Globals
# ============================
data_file = "/home/pi/Projects/OD/OD_data.txt"

def main():
    pid = str(os.getpid())
    pidfile = "/home/pi/Projects/OD/ODscript.pid"
    if os.path.isfile(pidfile):
        sys.exit()
    file(pidfile, 'wb+').write(pid)

    try:
        """The main executable loop for collecting measurements"""
        logger = logging.getLogger('ODServiceRoutine.py')
        hdlr = logging.FileHandler('/home/pi/Projects/OD/odservice.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr) 
        logger.setLevel(logging.DEBUG)

        # logging.basicConfig(filename='/home/pi/Projects/OD/odservice.log')
        logger.info('========================================')
        logger.info('         New Service Log Started        ')
        now = str(datetime.datetime.now())
        # logging.info(now)
        logger.info('========================================')
        # the main execution loop

        datastring = ""
        timestampdatastring = ""
        # Stop oscillator
        logger.info("Stopping orbital shaker.")
        OrbitalShakerDriver.stoposcillating()
        time.sleep(1)  # Allow the shaker to completely stop
    
        logger.info("Collecting a measurement.")
        for x in range(0, 3): # Since we are using UDP, try to collect up to 3 times
            # Read sensors
            datastring = queryODAsEthernetClient.getdata()
            time.sleep(1) #Allow time for arm to raise and lower
            logger.info(datastring)
            if datastring:
                break
            else:
                logger.info("datastring is empty")
        
        # Write out data to log file and web page
        timestampdatastring = logdata(datastring, logger)
        time.sleep(1)
        # print(timestampdatastring)
        logger.info("Reading data from file.")
        time.sleep(1)
        ReadDataFromFile.readdata()

        # If no data, send alert
        # if datastring == "":
        # TODO: implement error notification

        # Start oscillator
        logger.info("Starting orbital shaker.")
        OrbitalShakerDriver.startoscillating()
        
    except Exception as e:
        logger.error('Caught exception: ' +str(e))
    
    finally:
        os.unlink(pidfile)
    
    return timestampdatastring.encode('utf-8')


def logdata(data, logger):
    """Function for adding the instrument readings to the data log"""
    if not os.path.isfile(data_file):
        os.mknod(data_file,0777)
    # open the data file and start writing data
    data_file_fh =  open(data_file, 'ab')
    logger.info("Data file is open.")
    time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')
    data_string = time_stamp + '; ' + data
    # print (data_string)
    data_file_fh.write(data_string + '\n')
    logger.info("Data file was written.")
    time.sleep(3)
    data_file_fh.close()
    logger.info("Data file is closed.")
    return data_string


# If this program is the primary executable, then run the main loop
if __name__ == '__main__':
    main()
