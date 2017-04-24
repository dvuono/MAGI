#! python3
# A script to read data from a file and dump it
# out in JSON format.

import json
import logging

datavalues = []
filename = "/home/pi/Projects/OD/OD_data.txt"

def readdata():
    logger = logging.getLogger('ODServiceRoutine.py')
    try:
        logger.info("    Opening file...")
        file_object = open(filename, 'rb+') # Must be binary mode for remote operations
        # file_object = open(filename)
        data = file_object.readlines()
        for line in data:
            try:
                dataset = line.split(';')
                dictionary = {"Timestamp":dataset[0],
                              "Data1":(dataset[1].split('='))[1].strip(),
                              "Data2":(dataset[2].split('='))[1].strip(),
                              "Data3":(dataset[3].split('='))[1].strip(),
                              "Data4":(dataset[4].split('='))[1].strip(),
                              "Data5":(dataset[5].split('='))[1].strip(),
                              "Data6":(dataset[6].split('='))[1].strip(),
                              "Data7":(dataset[7].split('='))[1].strip(),
                              "Data8":(dataset[8].split('='))[1].strip(),
                              "Data9":(dataset[9].split('='))[1].strip(),
                              "Data10":(dataset[10].split('='))[1].strip(),
                              "Data11":(dataset[11].split('='))[1].strip(),
                              "Data12":(dataset[12].split('='))[1].strip()}
                datavalues.append(dictionary)
            except Exception as ex:
                logger.error(ex) # If there is a malformed entry, just note it and continue
    finally:
        logger.info("    Closing file...")
        file_object.close()

    f = open('/home/pi/Projects/OD/data.json', 'wb+') # Must be binary mode for remote operations
    # f = open('/home/pi/Projects/OD/data.json', 'w')
    try:
        with f as outfile:
            logger.info("    Dumping to outfile..")
            json.dump(datavalues, outfile, indent=4)
    finally:
        logger.info("    Closing outfile...")
        f.close()
    # print(json.dumps(datavalues))
    return


# If this program is the primary executable, then run the main loop
if __name__ == '__main__':
    readdata()
