import os
import requests
from time import sleep

class LifeSimulator():
    def __init__(self):
        pass
    
    def refresh(self):
        os.system("cls")
        
    def mainScreen(self):
        self.checkUpdate()
    
    def checkUpdate(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
                   "Cookie": r"__test=d8f62c0d5c28aec55842741c276b9969; Imvf_2132_saltkey=nYY6T544; Imvf_2132_lastvisit=1677537703; Imvf_2132_auth=0cd0RMbrjsqNITLzeIrGs0nT6I3VPKPnEG56Zvdb%2BYvPqIbDhpQXkNCQWDSMpdwRQdXXFDMfq9n0bh91c12%2F; Imvf_2132_nofavfid=1; Imvf_2132_study_nge_extstyle=auto; Imvf_2132_study_nge_extstyle_default=auto; Imvf_2132_sid=m5hE5S; Imvf_2132_lip=218.13.189.218%2C1677647624; Imvf_2132_creditnotice=0D100D15D0D2D0D0D0D0D1; Imvf_2132_creditbase=0D1090D6967D160D50D0D0D0D0; Imvf_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; Imvf_2132_onlineusernum=2; Imvf_2132_ulastactivity=9dfduUKulb3Q4rRqicE2oNViHdP5uiFV2i1gp5GmLAfezMvNxAaz; PHPSESSID=980f0337ff58f75c1977381116343ff0; Imvf_2132_sendmail=1; Imvf_2132_lastact=1678341207%09home.php%09spacecp; Imvf_2132_lastcheckfeed=1%7C1678341207"}
        requrl = requests.get("http://tbdriver.byethost24.com/Version/MathBeats/version.txt", headers=headers)
        version = requrl.text
        print(version)
        pass
    
    def start(self):
        self.mainScreen()

LSMain = LifeSimulator()
LSMain.start()