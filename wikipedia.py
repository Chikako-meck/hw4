# coding: UTF-8
import sys


# リンクされている数が最多のheadを探す
def getMaxLinkLength(linksList):
    answer = 0
    index = 0
    length = len(linksList)
    for i in range(length):
        listLength = linksList[i]['linkLength']
        if  listLength > answer:
            answer = listLength
            index = i
    print  (linksList[index]['head'] +  ': ' + str(answer))


# lineがリンクされている数を調べる
def searchObject(linksList, line):
    answer = 0
    length = len(linksList)
    for i in range(length):
        if titlesList[i]['head'] == line:
            answer = linksList[i]['linkLength']
            return answer
        i += 1
    return None
        

# links.txtを読み込んで、リンクされているindexを'link'に追加する
def makeLinksList(titlesList):
    linkFile = open('links.txt', 'r')
    linksList = []
    line = linkFile.readline()
    while line:
        line = line.replace('\n', '')
        (linkTo, linkedBy)= line.split("\t")
        titlesList[int(linkedBy)]['link'].append(int(linkTo))
        line = linkFile.readline()
    linkFile.close()
    return titlesList



# pages.txtを読み込んで、リストを作成する
def makeTitlesList():
    pageFile = open('pages.txt', 'r')
    titlesList = []
    line = pageFile.readline()
    while line:
        line = line.replace('\n', '')
        (index, head) = line.split('\t')
        title = {'index': int(index), 'head': head, 'link':[], 'linkLength': 0}
        titlesList.append(title)
        line = pageFile.readline()
    pageFile.close()
    return titlesList
    

# 他ページにリンクが貼られてる数をセットする
def setLinkLength(linksList):
    listLength = len(linksList)
    for i in range(listLength):
        linkLength = len(linksList[i]['link'])
        linksList[i]['linkLength'] = linkLength
    return linksList
    

# index, head, link を含む要素からなるリストを作成
titlesList = makeTitlesList()

# リストのlinkに自分がリンクされているページのindexを追加
linksList = makeLinksList(titlesList)

# linksListの要素ごとに、リンクされている数をセット
newLinksList = setLinkLength(linksList)

# 他ページに最もリンクされている要素を出力
getMaxLinkLength(newLinksList)

while True:
    print '> ',
    line = raw_input()
    answer = searchObject(linksList, line)
    if answer == None:
        print line + ' は見つかりませんでした.'
    else:
        print "answer = %d \n" % answer
    if line == "end":
        sys.exit()
