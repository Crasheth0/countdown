#!/usr/bin/env python
def countdown():
    from time import sleep
    from sys import stdout
    ch = raw_input ("Timer in second (s),minute (m)?,Exit (e)")
    if ch == 's' :
        t = input ("Seconds?:")
        for i in range (t,-1,-1):
            stdout.write ("\r%d" % i )
            stdout.flush ()
            sleep(1)
            stdout.write("\n")
        beep()
        countdown ()
    elif ch == 'm' :
        t = input ("Minute?:\n")
        for i in range (t,-1,-1):
            stdout.write ("\r%d" % i )
            stdout.flush ()
            sleep(60)
            stdout.write("\n")
        beep()
        countdown()
    elif ch == 'e' :
        quit ("Goodbye!\a")
    else :
        countdown()

def beep():
#For Linux OS
    import os
    for i in range (1):
        os.system ('play --no-show-progress --null --channels 1 synth %s sine %f' % (1, 1000))

#Start program
countdown ()
                                                    #Crasheth0
