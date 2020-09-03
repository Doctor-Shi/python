import re
import urllib.request

pattern = re.compile("ar")
print(pattern.match("army"))     # "ar"在开头，匹配成功
print(pattern.match("mary"))     # "ar"不在开头，匹配失败
print(pattern.match("mary", 1))  # "ar"不在开头，但在子串的开头
print(re.match("ar", "army", 1))
f = urllib.request.urlopen('http://172.20.8.129:8080/nmp')
line = f.readline()
print(line)


def findall(string):
    lst = re.findall(r"\d+", string)
    print(lst)

findall("jafjaa2jdhjfjh45lklk")
