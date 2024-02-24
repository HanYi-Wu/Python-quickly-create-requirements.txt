import os

pathname = 'main服务器'
MainPath = '.\\' + pathname
paths = os.walk(MainPath)
pylist = []
pyPathList = []
theContent = []
result_list = set()
for path, dir_lst, file_lst in paths:
    for file_name in file_lst:
        pathTo = os.path.join(path, file_name)
        if file_name.endswith('.py'):
            pylist.append(file_name.split(".py")[0])
            pyPathList.append(pathTo)
for i in pyPathList:
    content = open(i, encoding='utf-8').read()
    lines = content.split('\n')  # 将文本内容按行分割成列
    result_list.update([line for line in lines if line.startswith("import")])
    result_list.update([line for line in lines if line.startswith("from")])
for importThing in result_list:
    i = importThing.split(" ")[1]
    if i not in pylist:
        theContent.append(i)
with open(os.path.join(MainPath, 'requirements.txt'), 'w') as file:
    for library in theContent:
        file.write(library + '\n')
