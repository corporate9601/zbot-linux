import os
import random
from threading import Thread
import subprocess
import csv
import time
import shutil
import argparse

def startBot(proxy,url,useragent):
    subprocess.call('python3 bot.py --proxy %s --url %s --useragent \"%s%s' % (proxy,url,useragent,"\""),shell=True)

os.system('taskkill /IM chrome.exe /F')

tempdir = os.path.realpath(os.getenv('TEMP'))

print("cleaning TEMP files...")
shutil.rmtree(tempdir, ignore_errors=True)

parser = argparse.ArgumentParser()
parser.add_argument("threads", type=int, help="set the number of threads")
args = parser.parse_args()

#########################################################################
#               GET RANDOM PROXY AND USERAGENT FROM FILEs
#########################################################################

proxies = []
with open("proxies.csv", 'r') as f:
	reader = csv.reader(f)
	proxies = list(reader)

URLs = []
with open("orders.csv", 'r') as r:
	reader = csv.reader(r)
	URLs = list(reader)

UALIST = [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
        ]

threads = {}
for n in range(0,args.threads):
    threads['t'+str(n)] = {'t' : Thread(target=startBot, args=(random.choice(proxies)[0],random.choice(URLs)[0],random.choice(UALIST))),'n' : n}
    threads['t'+str(n)]['t'].start()
    print("Thread " + str(n) + " started!")

killcounter = 0
while (1):
    killcounter += 1
    if (killcounter > 600):
        print("cleaning TEMP files...")
        shutil.rmtree(tempdir, ignore_errors=True)
        print("killing chrome instances")
        os.system('pkill chrome')
        killcounter = 0
    for t in threads.keys():
        if threads[t]['t'].is_alive() == False:
            threads[t]['t'] = Thread(target=startBot, args=(random.choice(proxies)[0],random.choice(URLs)[0],random.choice(UALIST)))
            threads[t]['t'].start()
            print("Thread " + str(threads[t]['n']) + " completed. Restarting... ")
            time.sleep(1)
    time.sleep(1)

#os.system("py bot.py --proxy %s --url %s --useragent \"%s%s" % ('37.1.221.45:23621','http://check2ip.com',USERAGENT,"\""))
#os.system("py bot.py --proxy 37.1.221.45:23621 --url http://check2ip.com --useragent %s" % USERAGENT)
