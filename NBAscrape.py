from bs4 import BeautifulSoup
import requests
import re

def scrapeList(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    return soup

def getScoresAsStrings(soup):
    dirtyScoresList = []
    for table in soup.find_all('table'):
        for row in table.findAll("tr"):
            cells = row.findAll("td", {"class" : "center"})
            for cell in cells:
                dirtyScoresList.append(cell.get_text())

    return dirtyScoresList

def removeTextFromList(scoreList):
    cleanScoresList = []
    valid = re.compile(r"[0-9]+\-[0-9]+")
    for e in scoreList:
        if valid.match(e):
            cleanScoresList.append(e)

    return cleanScoresList


def scrape(url):
    soup = scrapeList(url)
    dirtyList = getScoresAsStrings(soup)
    cleanList = removeTextFromList(dirtyList)

    return cleanList
