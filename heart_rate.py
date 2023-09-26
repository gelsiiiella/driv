import cv2
import numpy as np
from scipy.signal import find_peaks
import scipy.signal


def bandpass_filter(signal,lowcut,highcut,fs,order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut/ nyquist
    b,a = scipy.signal.butter(order, [low,high],btype = 'band')
    filtered_signal = scipy.signal.lfilter(b,a,signal)
    return filtered_signal


cap = cv2.VideoCapture(0)
frame_rate = 30
heart_rate_history = []

while True:
    ret,frame = cap.read()
    x,y,w,h = 100,50,150,150
    roi = frame [y:y+h, x:x+w]

    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    filtered_signal = bandpass_filter(gray.flatten(), lowcut=0.5,highcut=2.5,fs=frame_rate)

    peaks, _ = scipy.signal.find_peaks(filtered_signal, height=10)

    heart_rate = len(peaks) * (60.0 / len(filtered_signal)*frame_rate)

    heart_rate_history.append(heart_rate)

    cv2.putText(frame,f"Heart Rate:{heart_rate:.1f} BPM",(x,y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    cv2.imshow("Video",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()