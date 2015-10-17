import csv
from pprint import pprint
import json
def csv_read(path):
    # with open(path, "rb") as csv_file:
    csv_file = open(path, "rb")
    line = csv.reader(csv_file)
    return line

def get_col_from_header(DataList):
    nameCol = DataList.index("Book")
    authorCol = DataList.index("Author")
    genreCol = DataList.index("Genre")
    givenbyCol = DataList.index("Given by")
    pagesCol = DataList.index("Pages")
    remarksCol = DataList.index("Remarks")
    availabilityCol = DataList.index("Availability")
    levelCol = DataList.index("Level")
    currentlyWithCol = DataList.index("Currently with")
    dateGivenCol = DataList.index("Date given")
    colIndex = {
        "nameCol": nameCol,
        "authorCol": authorCol,
        "genreCol": genreCol,
        "givenbyCol": givenbyCol,
        "pagesCol": pagesCol,
        "remarksCol": remarksCol,
        "availabilityCol": availabilityCol,
        "levelCol": levelCol,
        "currentlyWithCol": currentlyWithCol,
        "dateGivenCol": dateGivenCol,
    }
    return colIndex

def create_json_item(DataList, colIndex):
    name = DataList[colIndex["nameCol"]]
    author = DataList[colIndex["authorCol"]]
    genre = DataList[colIndex["genreCol"]]
    givenby = DataList[colIndex["givenbyCol"]]
    pages = DataList[colIndex["pagesCol"]]
    remarks = DataList[colIndex["remarksCol"]]
    availability = DataList[colIndex["availabilityCol"]]
    level = DataList[colIndex["levelCol"]]
    currentlyWith = DataList[colIndex["currentlyWithCol"]]
    dateGiven = DataList[colIndex["dateGivenCol"]]
        # "number": number,
    jsonItem = {
        "name": name,
        "author": author,
        "genre": genre,
        "givenby": givenby,
        "pages": pages,
        "remarks": remarks,
        "availability": availability,
        "level": level,
        "currentlyWith": currentlyWith,
        "dateGiven": dateGiven
    }
    return jsonItem

def create_json(lineInst):
    jsonList = []
    HeaderFlag = True
    count = 1
    for DataList in lineInst:
        if HeaderFlag:
            colDict = get_col_from_header(DataList)
            HeaderFlag = False
        else:
            # print colDict
            item = create_json_item(DataList, colDict)
            item["number"] = count
            count += 1
            jsonList.append(item)
    return jsonList

if __name__ == "__main__":
    path = "The_Bookworm_Theory_Record.csv"
    lineInst = csv_read(path)
    gen = create_json(lineInst)
    # for item in gen:
    #     print json.dumps(item) + ","
    print json.dumps(gen)
