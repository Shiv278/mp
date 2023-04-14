import datetime
import winsound
def alarm(Timing):
    altime=str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))

    altime=altime[11:-3]

    oreal=altime[:2]
    oreal=int(oreal)
    Mireal=altime[3:5]
    Mireal=int(Mireal)

    print(f"Done, alarm is set for {Timing}")

    while True:
        if oreal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                # Speak("Time to wakeup")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break