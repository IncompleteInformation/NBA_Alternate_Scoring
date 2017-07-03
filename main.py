import NBAscrape as scraper
import NBAformat as formatter
import NBAcalculate as calculator

url = "http://www.basketball-reference.com/boxscores/pbp/201610260BOS.html"

def main():
    dirtyList = scraper.scrape(url)
    formatted = formatter.format(dirtyList)
    finalScore = formatted[-1]
    print "Game Stats Hosted Here: {}".format(url)
    print "game score:      {}".format(finalScore)
    bonuses = calculator.calculate(formatted)
    print "bonuses:         {}".format(bonuses)
    modifiedScore = [sum(x) for x in zip(*[finalScore, bonuses])]
    print "modified score:  {}".format(modifiedScore)

main()
