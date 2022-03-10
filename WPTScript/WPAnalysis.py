import os
import re
import xlsxwriter
import shutil
from datetime import datetime

# script starts at the bottom, scroll down to @main to understand functionality.

#change this to match number of words pairs in each session
numberOfWords = 20

# will hold all participant data
participantData = []

# this grabs the current time for naming of csv file.
now = datetime.now()
dayOfMonth = str(now.month) + "_" + str(now.day)
time = str(now.hour) + "_" + str(now.minute)

# writeCSV creates an output csv file with the wanted data.
# it includes the participant ID, the pre sleep accuracy, post
# sleep accuracy, number of practice rounds, and a list of the
# different practice accuracies. Each row of the output file
# correlates with a single participant.
def writeCSV(data, source, dest):
    fileName = dayOfMonth +"_WPT_Summary_" + time +".xlsx"
    summaryStats = xlsxwriter.Workbook(fileName)
    summarySheet = summaryStats.add_worksheet()
    summarySheet.write("A1", "Participant ID")
    summarySheet.write("B1", "Pre Sleep Accuracy")
    summarySheet.write("C1", "Post Sleep Accuracy")
    summarySheet.write("D1", "# of Practice Rounds")
    summarySheet.write("E1", "Practice Accuracy")
    row = 1
    column = 0
    for participant in data:
        for stat in participant:
            summarySheet.write(row, column, stat)
            column += 1
        row += 1
        column = 0
    summaryStats.close()
    shutil.move(source + "\\" + fileName, dest + "\\" + fileName)

# practiceAccuracy creates a list of percentages. The percentages
# are the % correct on each practice trial a participant carried out
def practiceAccuracy(pracAccList):
    correctList = []
    for string in pracAccList:
        numCorrect, tab, rest = string.partition("\t")
        numPercentage = (int(numCorrect) / numberOfWords) * 100
        correctList.append(numPercentage)
    return correctList

# readFile loops through a single raw data file and grabs the
# wanted raw data. It uses @practiceAccuracy to calculate the
# percentages a participant got correct on each practice run
def readFile(ID, myFile):
    numOfPracRounds = 0
    accuracy = []
    fileAsList = []
    postSleep = ""
    preSleep = ""
    practiceCorrect = []
    for line in myFile:
        fileAsList.append(line)
    index = 0
    while index < len(fileAsList):
        if fileAsList[index].find("correct on iteration") != -1:
            accuracy.append(fileAsList[index])
        index += 1
    numOfPracRounds = len(accuracy) - 2
    practice = accuracy[:-2]
    practiceCorrect = practiceAccuracy(practice)
    preSleep = accuracy[-2]
    postSleep = accuracy[-1]
    preSleepCorrect, tab, rest = preSleep.partition("\t")
    postSleepCorrect, tab, rest = postSleep.partition("\t")
    preSleepPercentage = (int(preSleepCorrect) / numberOfWords) * 100
    postSleepPercentage = (int(postSleepCorrect) / numberOfWords) * 100
    participantData.append([ID, preSleepPercentage, postSleepPercentage, numOfPracRounds, str(practiceCorrect)])

# main loops through the reports folder and reads each file (@readFile),
# adding gathered data to participantData list. Each list inside of participantData
# represents a different participant.
# Once all report files have been parsed, create output csv file (@writeCSV).
def main():
    rootDir = os.getcwd()
    os.chdir('Reports')
    reports = os.listdir(os.getcwd())
    for file in reports:
        #removing first 4 characters (WPT_) and last 4 characters (.txt)
        participantID = file[4:-4]
        with open(file,'r') as f:
            readFile(participantID, f)
    writeCSV(participantData, rootDir + "\Reports", rootDir + "\SummaryStatistics")
main()