#coding: UTF-8
import sys

# pages.txtを読み込んで、リストを作成する
def makeTitlesList():
    pageFile = open('pages.txt', 'r')
    titlesList = []
    line = pageFile.readline()
    while line:
        line = line.replace('\n', '')
        (index, head) = line.split('\t')
        title = {'index': int(index), 'head': head, 'link':[], 'linkLength': 0, 'pageRank': 0}
        titlesList.append(title)
        line = pageFile.readline()
    pageFile.close()
    return titlesList


# links.txtを読み込んで、リンクしているindexを'link'に追加する
def makeLinksList(titlesList):
    linkFile = open('links.txt', 'r')
    linksList = []
    line = linkFile.readline()
    while line:
        line = line.replace('\n', '')
        (linkTo, linkedBy)= line.split("\t")
        titlesList[int(linkTo)]['link'].append(int(linkedBy))
        line = linkFile.readline()
    linkFile.close()
    return titlesList


# 他ページのリンク数をセットする
def setLinkLength(linksList):
    listLength = len(linksList)
    for i in range(listLength):
        linkLength = len(linksList[i]['link'])
        linksList[i]['linkLength'] = linkLength
    return linksList


# ページランクを実行する
def pageLank(linksList, pointList):
    listLength = len(linksList)
    newPointList = [0.0] * listLength
    for i in range(listLength):
        linkLength = linksList[i]['linkLength']
        if linkLength != 0:
            point = pointList[i] / linkLength
            for j in range(linkLength):
                link = linksList[i]['link']
                index = link[j]
                newPointList[index] += point
        else:
            point = pointList[i] / listLength
            for j in range(listLength):
                newPointList[j] += point 
    return newPointList


# 点数が最大の要素を求める
def getMaxPoint(linksList):
    length = len(linksList)
    pointList = [100.0] * length
    #    for i in range(5):
    pointList = pageLank(linksList, pointList)
    for j in range(length):
        linksList[j]['pageRank'] = pointList[j]
    return linksList


# ページランクを求めたリストを大きい順にソートして、トップ20を'pageRank.txt'に出力する
def printTop20(linksList):
    sortedList = sorted(linksList, key=lambda x:x['pageRank'], reverse = True)
    file = open('pageRank2.txt', 'w')
    file.write('  PageRank \t PageNo. \t PageName\n')
    for i in range(20):
        pageRank = sortedList[i]['pageRank']
        index = sortedList[i]['index']
        head = sortedList[i]['head']
        file.write(str(pageRank) + '\t' + str(index) + '\t' + head + '\n')
    file.close()



    
# 実行部分
# index, head, link を含む要素からなるリストを作成
titlesList = makeTitlesList()

# 'link'に、リンクしているページのindexを追加
linksList = makeLinksList(titlesList)

# linksListの要素ごとに、リンクされている数をセット
newLinksList = setLinkLength(linksList)

# ページランクアルゴリズムを実行
pageRankList = getMaxPoint(newLinksList)

# ページランク、トップ20を'pageRank.txt'に出力
printTop20(pageRankList)




