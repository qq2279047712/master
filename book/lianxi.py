import re

text = """这是一个例子。
它包含多行文本。"""

# 使用re.S标志，点号可以匹配换行符
pattern = r".+"
matches = re.findall(pattern, text, re.S)
matches2 = re.match(pattern, text, re.S)
for match in matches:
    print(repr(match))
    print(matches)
print("这是matches2=",repr(matches2))

myStr = """
<a href="http://www.baidu.com">百度</a>
<A href="http://www.id97.com">电影网址</A>
<a href="http://www.taobao.com">淘宝</a>
<a href="www.taobao.com">淘宝2</a>
<a href="http://www.dj.com">京
东</a>
"""
re.findall("<a href=\"http://.*?\">.*?</a>",myStr,re.S)
dataList = re.findall("<a href=\"http://.*?\">.*?</a>",myStr,re.I)
print(dataList)
dataList = re.findall("<[aA] href=\"http://.*?\">.*?</[aA]>",myStr,re.S)
print(dataList)
dataList = re.findall("<a href=\"http://.*?\">.*?</a>",myStr,re.S)
print(dataList)

