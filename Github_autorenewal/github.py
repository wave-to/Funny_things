import requests
import os

def github():
    url = 'https://raw.hellogithub.com/hosts'
    response = requests.get(url=url)
    f = open('C:\Windows\System32\drivers\etc\hosts','w')
    f.write(response.text)

    try:
        if f != None:
            print('Successful writing and attempting to renewal dns……')
            cmd = 'ipconfig/flushdns'
            res = os.popen(cmd)
            output_str = res.read()
            print(output_str)

    except Exception as e:
        print(e)
        pass

    f.close()

if __name__ == '__main__':
    print("Please wait a minute,it's attempting to renewal the file of hosts……")
    github()