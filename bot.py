import time
from seleniumwire import webdriver
import argparse
import csv
import random
from selenium.webdriver.common.keys import Keys
import os

#########################################################################
#               GET RANDOM EMAIL & NAME FROM FILES
#########################################################################

chosen_row = []
with open("emailnamelist.csv", 'r') as f:
	reader = csv.reader(f)
	chosen_row = random.choice(list(reader))

f.close()

email = chosen_row[0]
name = chosen_row[1]
last_name = ""
with open("last-names.txt", 'r') as lread:
        last_name = random.choice(lread.readlines()).swapcase()

lread.close()
        
phone = "+1" + str(random.randint(2000000000, 9999999999))
password = name + "#FBIAgent420"

#########################################################################
#         DICT OF HTML ELEMENT IDENTIFIERS/ XPATHS/ SELECTORS
#########################################################################

xdict = {
        "email" : {
                "xpaths" : [
                        "/html/body/div[1]/div[10]/div/div/div/div/div/input",
                        "/html/body/div[1]/div/div/div/article/div/div/div/div/div[2]/form/div/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input",
                        "//*[contains(@name, 'email')]",
                        "//*[contains(@type, 'email')]",
                        "//*[contains(@id, 'email')]", 
                        "//*[contains(@placeholder, 'email')]",
                        "//*[contains(@placeholder, 'e-mail')]",
                        "//*[contains(@placeholder, 'Email')]",
                        "/html/body/div/div/form/div/div[1]/div/div[2]/div[1]/div/input",
                        "/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/form/div/div[2]/label/div[2]/input"
                        ],
                "tagnames" : [
                        "input"
                        ],
                "css-selector" : [
                        "#webform_c_kp6y6"
                        ]
                },
        "f_name" : {
                "xpaths" : [
                        "//*[@id=\"edi-gglru62\"]",
                        "//*[contains(@type, 'name')]",
                        "//*[contains(@id, 'name')]",
                        "//*[contains(@placeholder, 'name')]",
                        "//*[contains(@placeholder, 'Name')]"
                        ],
                },
        "submit" : {
                "xpaths" : [
                        "/html/body/div[1]/div[12]/div/div/div/div/div/a/span[1]",
                        "//*[contains(@type, 'submit')]",
                        "/html/body/div/div/form/div/div[2]/div/button",
                        "//*[contains(@type, 'button')]",
                        "//*[contains(@id, 'submit')]",
                        "//*[contains(@name, 'submit')]",
                        "//*[contains(@class, 'button')]",
                        "//*[contains(@slug, 'button')]",
                        "//*[@id=\"app\"]/div/div/div[2]/section/div/div/div/div/div/div/div/div[4]/button",
                        "/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/div/form/div/div[3]/a"
                        ],
                "tagnames" : [
                        "a",
                        "button"
                        ],
                "css-selector" : [
                        "#c_zrdtt > div > button"
                        ]
                }
        }

#########################################################################
#        THIS SECTION BELOW FETCHES COMMAND-LINE ARGUMENTS
#########################################################################

parser = argparse.ArgumentParser()
parser.add_argument("--proxy", help="set the proxy server in IP:PORT format")
parser.add_argument("--url", help="set the URL to be loaded")
parser.add_argument("--useragent", help="set the UserAgent")
args = parser.parse_args()

#########################################################################
#              SET CHROME AND SELENIUM WIRE OPTIONS
#########################################################################

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://%s' % args.proxy)
#options.add_argument('--headless') #enable this for headless mode
#options.add_argument('--no-sandbox')
#options.add_argument('--ignore-certificate-errors-spki-list')
#options.add_argument('--ignore-ssl-errors')
options.add_argument('--user-agent=%s' % args.useragent)

selenium_options = {
    'proxy' : {
        'http' : 'http://%s' % args.proxy,
        'https' : 'http://%s' % args.proxy
        },
    'exclude_hosts': [
        'www.partnerwithantony.com',
        'pwa.cmsecureorders.com',
        'mccdn.me',
        'www.multipleincomefunnel.com',
        'www.cashmagnets.com',
        'teamblackbelt.net',
        '*.multipleincomefunnel.com',
        'multipleincomefunnel.com',
        'fonts.gstatic.com',
        'accounts.google.com',
        '*.facebook.com',
        'facebook.com',
        'facebook.net',
        'fonts.googleapis.com',
        '*.firebaseio.com',
        '*.googleapis.com',
        'googleapis.com',
        'firebaseio.com',
        '*.bootstrapcdn.com',
        'vipbotclub.net',
        'www.clickfunnels.com',
        'warriorplus.com',
        '*.gvt1.com',
        '*.gvt2.com',
        'gvt1.com',
        'gvt2.com',
        'my.funnely.com',
        'www.clubcashfund.com',
        '*.trafficauthority.net',
        'storage.builderall.com',
        '*.verproduto.com',
        'sitebuilder-editor.omb11.com',
        'omb11.com',
        'allmarijuanastocks.com',
        '*.digitalmarky.com',
        'digitalmarky.com',
        '*.free.builderall.com',
        'builderall.com',
        '*.builderall.com',
        'rapidprofit.blessmusaonline.net',
        'assets.clickfunnels.com',
        'thebreakoutcode.com',
        'bestsolotraffic.com',
        'newmoneytraders.com',
        'olspsystem.com',
        '*.facebook.net',
        'bing.com',
        '*.partnerwithantony.com',
        'clickwealthsystem.com',
        'www.clickenginesuccess.com',
        'www.jasoncryder.com'
        ]  # Bypass Selenium Wire for these hosts to save proxy data and speed it up
}
#########################################################################
#                    INITIALIZES THE ChromeDriver
#########################################################################

driver = webdriver.Chrome(options=options, seleniumwire_options=selenium_options) #

#########################################################################
# interceptor to abort video server connections and bypass excluded hosts
#########################################################################

def interceptor(request):
    # Block video and image server requests containing these strings/hosts 
    blocked_hosts = (
        'images',
        'youtube',
        'vimeo',
        'video',
        'ytimg',
        'uploads.3ng.io',
        'www.set-forget.com',
        'player.vimeo.com',
        'f.vimeocdn.com',
        '*.youtube.com',
        'i.ytimg.com',
        'youtube.com'
        )
    for block in blocked_hosts:
        if block in str(request):
            print("<<ABORTING>> %s" % str(request))
            request.abort()
            break
    #print(request)

driver.request_interceptor = interceptor

#########################################################################
#                          navigate to URL
#########################################################################

try:
    driver.get(args.url)
except:
    print("error proxy bad")

time.sleep(20)

if ("www.bing.com" in driver.current_url or "google.com" in driver.current_url or "blocked" in driver.current_url or "qliker.io" in driver.current_url): 
        #driver.save_screenshot('screenshots/'+str(time.time_ns())+'-BADCLICK.png')
        print(driver.current_url)
        driver.close()
        print("bad click! Exiting...")
        exit()

#########################################################################
#      LOOP THROUGH webdriver WINDOWS and FIND ELEMENTS & INTERACT
#########################################################################
eng_depth = 4

found_something = False #Boolean set to true once a valid element combo is found. If false means something is broken

while (eng_depth > 0):
        for handle in driver.window_handles:
                driver.switch_to_window(handle)
                xdict["email"]["element"] = None
                xdict["f_name"]["element"] = None
                xdict["submit"]["element"] = None
                for k in xdict.keys():
                        for xpath in xdict[k]["xpaths"]:
                                try:
                                        if (xdict[k]["element"] is None):
                                                xdict[k]["element"] = driver.find_element_by_xpath(xpath)
                                                print(k,"element found! with xpath -> ",xpath)
                                                #if (xdict[k]["element"].is_displayed() is False or xdict[k]["element"].is_enabled() is False):
                                                #        xdict[k]["element"] = None
                                except:
                                        pass
                        if ("tagnames" in xdict[k].keys()):
                                for tagname in xdict[k]["tagnames"]:
                                        try:
                                                if (xdict[k]["element"] is None):
                                                        xdict[k]["element"] = driver.find_element_by_tag_name(tagname)
                                                        print(k,"element found! with tagname -> ",tagname)
                                                        #if (xdict[k]["element"].is_displayed() is False or xdict[k]["element"].is_enabled() is False):
                                                        #        xdict[k]["element"] = None
                                        except:
                                                pass
                        if ("css-selector" in xdict[k].keys()):
                                for selector in xdict[k]["css-selector"]:
                                        try:
                                                if (xdict[k]["element"] is None):
                                                        xdict[k]["element"] = driver.find_element_by_css_selector(selector)
                                                        print(k,"element found! with CSS selector -> ",selector)
                                                        #if (xdict[k]["element"].is_displayed() is False or xdict[k]["element"].is_enabled() is False):
                                                        #        xdict[k]["element"] = None
                                        except:
                                                pass
                try:
                        if (xdict["email"]["element"] is not None):
                                xdict["email"]["element"].click()
                                xdict["email"]["element"].send_keys(email,Keys.ENTER)
                        if (xdict["f_name"]["element"] is not None):
                                xdict["f_name"]["element"].click()
                                time.sleep(1)
                                xdict["f_name"]["element"].send_keys(name.capitalize())
                        if (xdict["submit"]["element"] is not None):
                                xdict["submit"]["element"].click()
                                found_something = True
                except:
                        pass
                eng_depth -= 1
                #os.system('image_rec.exe')
                time.sleep(15)
                print(driver.current_url)
                #driver.save_screenshot('screenshots/'+str(time.time_ns())+'-optin.png')
try:
        if (found_something == False):
                print('ERROR!! -->> ', driver.current_url,' <<-- NO ELEMENTS FOUND ERROR!!!!!!')
        driver.close()
except:
	print("...")


