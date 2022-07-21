import requests
import linecache
import os

def gitAllUrl():
    url = "https://raw.hellogithub.com/hosts"
    response = requests.get(url)
    f = open('hosts.txt','w+')
    f.write(response.text)
    f.close()

def gitRightUrl():
    fHosts = open('C:\Windows\System32\drivers\etc\hosts','w')
    content = linecache.getline('hosts.txt',13)
    # print("content:"+content)
    fHosts.write(content)

def flashDns():
    cmd = 'ipconfig/flushdns'
    os.popen(cmd)
    # output_str = res.read()
    # print(output_str)

if __name__ == '__main__':
    print("Please wait a minute,it's attempting to renewal the file of hosts……")
    gitAllUrl()
    gitRightUrl()
    flashDns()
