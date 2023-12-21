import re

strA = ""
# 如果strA有中文將中文取出
listA = re.findall(r'[\u4e00-\u9fa5]', strA)

for i in range(len(listA)):
    for j in range(i+1, len(listA)):
        if listA[i] == listA[j]:
            listA[j] = ""

strA = "".join(listA)
print(strA)