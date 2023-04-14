import os
import time
from playsound import playsound
from ctypes import cast, POINTER
import webbrowser




def getCount(ar):
    if ar == [0, 0, 0, 0, 0]:
        return 0
    elif ar == [0, 1, 0, 0, 0]:
        return 1
    elif ar == [0, 1, 1, 0, 0]:
        return 2
    elif ar == [0, 1, 1, 1, 0]:
        return 3
    elif ar == [0, 1, 1, 1, 1]:
        return 4
    elif ar == [1, 1, 1, 1, 1]:
        return 5
    elif ar == [1, 1, 0, 0, 0]:
        return 6
    elif ar == [1, 1, 1, 0, 0]:
        return 7
    elif ar == [1, 1, 1, 1, 0]:
        return 8
    elif ar == [0, 1, 0, 0, 1]:
        return 9
    elif ar == [1, 1, 0, 0, 1]:
        return 10

def getSound(n):
    if n == 0:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S0.mp3')
    elif n == 1:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S1.mp3')
    elif n == 2:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S2.mp3')
    elif n == 3:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S3.mp3')
    elif n == 4:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S4.mp3')
    elif n == 5:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S5.mp3')
    elif n == 6:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S6.mp3')
    elif n == 7:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S7.mp3')
    elif n == 8:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S8.mp3')
    elif n == 9:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S9.mp3')
    elif n == 10:
        return playsound('D:\Pycharm Projects\pythonProject\Sounds\S10.mp3')
    else:
        print("Not valid gesture")

def playVideo(n: int):
    try:
        if n == 0:
            pass
        elif n == 1:
            item = "Until I found You"
            return "https://music.youtube.com/watch?v=oIKuyj2GQtY&list=OLAK5uy_l9YOtSVbG-PNcH_34SJ6x6JD-us_OwWMA"
        elif n == 2:
            # Often Kygo Remix
            return "https://music.youtube.com/watch?v=qsDfFE2i0Ws&list=OLAK5uy_ly01GlEiOSaOGY96EerK02RdL2RS5vNMA"
        elif n == 3:
            # Playlist vibe
            return "https://music.youtube.com/watch?v=aSeKe_9qgqU&list=PLEZtw9WFgxhuQtHuCg38QcW89aN6pFwfQ"
        elif n == 4:
            # YT playlist 1
            return "https://music.youtube.com/watch?v=AJL_aVxqMEc&list=PLEZtw9WFgxhtTxc69kE2SGay-ixhRsrFv"
        elif n == 5:
            # YT playlist 2
            return "https://music.youtube.com/watch?v=TA1W-pHNKl8&list=PLEZtw9WFgxhvRWyo3Soz_rwJv8A9QvzNj"
    except:
        print("Error")
"""
def generate_frames():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:

            img, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
"""

