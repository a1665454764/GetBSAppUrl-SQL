# 瑞友 应用虚拟化系统 GetBSAppUrl SQL注入漏洞

## 漏洞描述

瑞友 应用虚拟化系统 GetBSAppUrl方法存在SQL注入漏洞，由于参数传入没有进行过滤导致存在SQL注入，攻击者通过漏洞可以获取数据库敏感信息

## 漏洞影响

瑞友应用虚拟化系统 7.0.2.1

## 网络测绘

"CASMain.XGI?cmd=GetDirApp" && title=="瑞友应用虚拟化系统"

## 漏洞复现、
![(TWY)P)CH~(0{W@9KGSV0{C](https://github.com/a1665454764/GetBSAppUrl-SQL/assets/143511005/22f4c6d7-d621-45b9-bf3f-5ef0b69db683)

![BPKDS@4QZCR_CGX9$1I_P9C](https://github.com/a1665454764/GetBSAppUrl-SQL/assets/143511005/eef3bda4-f3c5-411c-be7a-d2c67b31e6e8)
![R2Y@$}ES61OPZ((DE@NP}0N](https://github.com/a1665454764/GetBSAppUrl-SQL/assets/143511005/17754436-6db4-4f92-9548-912225fef8d0)
