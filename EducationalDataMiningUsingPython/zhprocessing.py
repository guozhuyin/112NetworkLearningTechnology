import re

strA = "我是一個中文句子，我有一些中文標點符號，例如，。；：、（）「」。"
# 如果strA有中文及中文標點符號，則取出
strA = re.sub(r'[^\u4e00-\u9fa5，。；：、（）「」]', "", strA)
# 將strA轉成list
listA = list(strA)

for i in range(len(listA)):
    for j in range(i+1, len(listA)):
        if listA[i] == listA[j]:
            listA[j] = ""

strA = "".join(listA)
print(strA)