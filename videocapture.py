import cv2
import subprocess
import numpy as np
import os

class FFmpegVideoCapture:
    # TODO probe width/height
    # TODO enforce width/height
    #
    # mode=gray,yuv420p,rgb24,bgr24
    def __init__(self,source,width,height,mode="bgr24",start_seconds=0,duration=0,verbose=False):

        x = ['ffmpeg']
        if start_seconds > 0:
            #[-][HH:]MM:SS[.m...]
            #[-]S+[.m...]
            x.append("-accurate_seek")
            x.append("-ss")
            x.append("%f" % start_seconds)
        if duration > 0:
            x.append("-t")
            x.append("%f" % duration)
        x.extend(['-i', source,"-f","rawvideo", "-pix_fmt" ,mode,"-"])
        self.nulldev = open(os.devnull,"w") if not verbose else None
        self.ffmpeg = subprocess.Popen(x, stdout = subprocess.PIPE, stderr=subprocess.STDERR if verbose else self.nulldev)
        self.width = width
        self.height = height
        self.mode = mode
        if self.mode == "gray":
            self.fs = width*height
        elif self.mode == "yuv420p":
            self.fs = width*height*6/4
        elif self.mode == "rgb24" or self.mode == "bgr24":
            self.fs = width*height*3
        self.output = self.ffmpeg.stdout
    def read(self):
        if self.ffmpeg.poll():
            return False,None
        x = self.output.read(self.fs)
        if x == "":
            return False,None
        if self.mode == "gray":
            return True,np.frombuffer(x,dtype=np.uint8).reshape((self.height,self.width))
        elif self.mode == "yuv420p":
            # Y fullsize
            # U w/2 h/2
            # V w/2 h/2
            k = self.width*self.height
            return True,(np.frombuffer(x[0:k],dtype=np.uint8).reshape((self.height,self.width)),
                np.frombuffer(x[k:k+(k/4)],dtype=np.uint8).reshape((self.height/2,self.width/2)),
                np.frombuffer(x[k+(k/4):],dtype=np.uint8).reshape((self.height/2,self.width/2))
                    )
        elif self.mode == "bgr24" or self.mode == "rgb24":
            return True,(np.frombuffer(x,dtype=np.uint8).reshape((self.height,self.width,3)))

if __name__=='__main__':
    cap=FFmpegVideoCapture("data/test1.avi",1920,1080,mode='bgr24')
    _,f=cap.read()
    cv2.imshow("",f)
    cv2.waitKey()