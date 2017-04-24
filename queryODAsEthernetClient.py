from socket import *
import time
import datetime
import logging

# Globals
# ============================
address= ('10.16.2.177', 80) # Define server IP and port
client_socket =socket(AF_INET, SOCK_DGRAM) # Set up the Socket
client_socket.settimeout(20) # Wait time for a response
datarequest = "ReadData" # Command string recognized by the Arduino web server


# Functions
# ============================
def getdata():
    """ Sends data request to the Arduino """
    datastring = ""
    client_socket.sendto(datarequest.encode('utf-8'), address)  # Send the data request
    time.sleep(1)  # Just to allow time for data collection
    try:
        rec_data, addr = client_socket.recvfrom(2048)  # Read response from Arduino
        time.sleep(1)
        datastring = rec_data.decode("utf-8")
        # logging.info(datastring)

    except Exception as ex:
        logging.error(ex)
        return ""

    return datastring





