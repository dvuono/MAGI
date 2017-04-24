# MAGI
Microbial Anaerobic Growth Intervalometer (MAGI)
This repo contains software to control the opertation of MAGI, which uses software-driven automation to control an orbital shaker/incubator, data aquisition, and remote visualization.
  1) Arduino code (Runs the data aquisition and articulating arm)
  2) Crontab (raspberry pi - Synchronizes operation interval)
  3) OrbitalShakerDriver.py (Controls orbital shaker start, stop, and speed)
  4) ODServiceRoutine.py (The main control function for periodic instrumentation reads)
  5) index.html, style.css, and background image for web server
  6) ReadDataFromFile.py (Opens data text file and converts it into JSON format)
  7) deletefile.py (After experiment is done, delete data files)
  8) queryODAsEthernetClient.py (Sets up the data on the server)
  9) wsgi.py
  10) gunicornscript (Script to start the gunicorn webserver)
  11) UdpOpticalDensityWebServer.ino (arduino control)
  
  Extras:
  1) CreateChart.py
  2) queryOD.py
