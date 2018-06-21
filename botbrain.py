def gpsfollowing():
    moveNS = [0,0]
    moveEW = [0,0]
    direction = [0,0]
    import android
    import time
    import ftplib
    import json
    
    droid = android.Android()
    BT_DEVICE_ID = '20:15:03:20:13:68'
    droid.bluetoothConnect('00001101-0000-1000-8000-00805F9B34FB', BT_DEVICE_ID)
    session = ftplib.FTP('ftp.tennesseeyankeenovel.com','tennesseeyankeenovel','Stlfdr139!67')
    file = open('/storage/emulated/0/qpython/scripts3/latret.txt','w')
    session.retrlines('RETR /siteyeah/lat.txt', file.write)
    file.close()
    file = open('/storage/emulated/0/qpython/scripts3/latret.txt','r')
    dla = int(file.read())
    file.close()
    file = open('/storage/emulated/0/qpython/scripts3/lonret.txt','w')
    session.retrlines('RETR /siteyeah/lon.txt', file.write)
    file.close()
    file = open('/storage/emulated/0/qpython/scripts3/lonret.txt','r')
    dlo = int(file.read())
    file.close()
    session.close()
    droid.startLocating()
    time.sleep(3)
    print ("\n"*100)
    loc = droid.readLocation().result
    try:
        n = loc['gps']
        la = int(float (n['latitude'])*100000)
        lo = int(float (n['longitude'])*100000)
        print(dla)
        print(dlo)
        print (la)
        print (lo)
        if la<dla and lo <=dlo:
            direction [1] = 2
        if la>=dla and lo <dlo:
            direction [1] = 4
        if la>dla and lo>=dlo:
            direction [1] = 6
        if la<=dla and lo>dlo:
            direction [1] = 8
        #find which direction the bot is moving
        if la>moveNS[0] and lo>=moveEW[0]:
            direction[0] = 2
        if la<=moveNS[0] and lo>moveEW[0]:
            direction[0] = 4
        if la<moveNS[0] and lo<=moveEW[0]:
            direction[0] = 6
        if la>=moveNS[0] and lo<moveEW[0]:
            direction[0] = 8
        #figure out how to move
        if direction[0] == 2:
            if direction[1] == 2:
    
                print ("forward")
                droid.bluetoothWrite('w')
                time.sleep(2)
            if direction[1] == 8:
                print("turn left")
                droid.bluetoothWrite('a')
        
                time.sleep(2)
            if direction[1] == 4:
                print("turn right")
                droid.bluetoothWrite('d')
                time.sleep(2)
            if direction[1] == 6:
                print("go backwards")
                droid.bluetoothWrite('d')
                time.sleep (2)
        if direction[0] == 4:
            if direction[1] == 4:
                print ("forward")
                droid.bluetoothWrite('w')
                time.sleep (2)
            if direction[1] == 2:
                print("turn left")
                droid.bluetoothWrite('a')
                time.sleep (2)
            if direction[1] == 6:
                print("turn right")
                droid.bluetoothWrite('d')
                time.sleep (2)
            if direction[1] == 8:
                print("go backwards")
                droid.bluetoothWrite('d')
                time.sleep (2)
        if direction[0] == 6:
            if direction[1] == 6:
                print ("forward")
                droid.bluetoothWrite('w')
                time.sleep (2)
            if direction[1] == 4:
                print("turn left")
                droid.bluetoothWrite('a')
                time.sleep (2)
            if direction[1] == 8:
                print("turn right")
                droid.bluetoothWrite('d')
                time.sleep (2)
            if direction[1] == 2:
                print("go backwards")
                droid.bluetoothWrite('d')
                time.sleep (2)
        if direction[0] == 8:
            if direction[1] == 8:
                print ("forward")
                droid.bluetoothWrite('w')
                time.sleep (2)
            if direction[1] == 6:
                print("turn left")
                droid.bluetoothWrite('a')
                time.sleep (2)
            if direction[1] == 2:
                print("turn right")
                droid.bluetoothWrite('d')
                time.sleep (2)
            if direction[1] == 4:
                print("go backwards")
                droid.bluetoothWrite('d')
                time.sleep (2)
        moveNS[0] = la
        moveEW[0] = lo
        droid.stopLocating()
        
    except KeyError:
        time.sleep(1)
        droid.stopLocating()
        print ('acquisition of signal in process. chill out dude')
        
def main():
    import ftplib
    
    updateTime = [0,0,0,0,0]
    session = ftplib.FTP('ftp.tennesseeyankeenovel.com','tennesseeyankeenovel','Stlfdr139!67')
    file = open('/storage/emulated/0/qpython/scripts3/updatetime.txt','w')
    session.retrlines('RETR /siteyeah/updatetime.txt', file.write)
    file.close()
    session.close()
    file = open('/storage/emulated/0/qpython/scripts3/updatetime.txt','r')
    updateTime.append(round(float(file.read())))
    del updateTime[0]
    if updateTime[4]==updateTime[0]:
        #cbotwebhook()
        tempPlaceholderVariable='butts and whatnot'
    else:
        gpsfollowing()
    file.close()
    
while True:
    main()
