import requests
import brotli
import os
import time
from bs4 import BeautifulSoup


fileList = os.listdir("..\\tiddlers")
for x in range(len(fileList)):
    dot = fileList[x].find('.')
    fileList[x] = fileList[x][:dot]
    

sourceList = []
checks = dict()

for group in range(1,2):
    print("Loading group",group,"source index..")
    sourcePage = requests.get("https://2e.aonprd.com/Sources.aspx?Group="
                              + str(group))
    sourceSoup = BeautifulSoup(sourcePage.content,"lxml")
    sourceListSoup = sourceSoup.find(id="main").table.find_all("td")
    for s in sourceListSoup:
        if s.a is not None:
            sourceList.append((s.a.text, s.a["href"]))



for (sourceName, sourceUrl) in sourceList:
    print("Loading",sourceName,"..")
    checks[sourceName] = []
    indexPage = requests.get("https://2e.aonprd.com/"+sourceUrl)
    indexSoup = BeautifulSoup(indexPage.content, "lxml")
    sections = indexSoup.find(id="main").find_all("h2")
    for section in sections:
        cursor = section
        cursor = cursor.next_sibling
        while cursor is not None and cursor.name == "u":
            checks[sourceName].append(cursor.a.text)
            cursor = cursor.next_sibling
            if cursor is not None and cursor.text[0] == ",":
                cursor = cursor.next_sibling
    time.sleep(3)

for book in checks:
    items = checks[book]
    print("Checking",len(items),"items from",book,"...")
    someExist = False
    missing = []
    for item in items:
        found = item in fileList
        if not found:
            if '(' in item:
                br = item.find("(")
                shortitem = item[:br-1]
            else:
                shortitem = item
            shortitem = shortitem.strip().lower()
            for match in fileList:
                if '(' in match:
                    br = match.find("(")
                    shortmatch = match[:br-1]
                else:
                    shortmatch = match
                shortmatch = shortmatch.strip().lower()
                if shortmatch == shortitem:
                    found = True
                    print("Shortmatched",item,"and",match)
                    break
        if found:
            someExist = True
        else:
            missing.append(item)
    if not someExist:
        print("Book not started.")
    else:
        if len(missing) == 0:
            print("Done!!")
        else:
            for x in missing:
                print("(" + x + ")")
                
            
    
    
