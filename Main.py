import csv
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier

#yardline dir = 1 or 0   OWN = 1     OPP = 0
class FeatureSet:
    def __init__(self, quarter, secondsleft, down, togo, yardline, scorediff, yarddirection, formation):
        self.quarter = quarter
        self.secondsleft = secondsleft
        self.down = down
        self.togo = togo
        self.yardline = yardline
        self.scorediff = scorediff
        #Formation
        if(formation=='SHOTGUN'):
            self.formation = 1
        elif(formation=='UNDER CENTER'):
            self.formation = 2
        elif(formation=='NO HUDDLE'):
            self.formation = 3
        elif(formation=='FIELD GOAL'):
            self.formation = 4
        elif(formation=='PUNT'):
            self.formation = 5
        elif(formation=='NO HUDDLE SHOTGUN'):
            self.formation = 6
        else:
            self.formation = -1

        #YardDir
        if(yarddirection=='OWN'):
            self.yarddir = 1
        if(yarddirection=='OPP'):
            self.yarddir = 0
        else:
            self.yarddir= -1

    def createArray(self):
        return [self.quarter, self.secondsleft, self.down, self.togo, self.yardline, self.scorediff, self.yarddir, self.formation]

##Utility method to filter to a specific team's offensive plays.
def filterDataSet(fileName):
    with open(fileName+'.csv', 'rb') as inp, open(fileName+'-editted.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[5] == "NE":
                writer.writerow(row)

#filterDataSet("datasets/pbp-2015")
#filterDataSet("datasets/pbp-2016")

### Algorithm starts here ###

def createFeatureLabelSets():
    features = []
    labels = []
    with open('datasets/pbp-combined_ALL.csv', 'rb') as inp:
        for row in csv.reader(inp):
            #Marking of important features:
            #Quarter = [2], Seconds_Left = [3]*60 + [4], Down = [7], togo = [8], yardline = [9], scorediff = [10]
            quarter = int(row[2])
            seconds_left = (int(row[3])*60) + int(row[4])
            down = int(row[7])
            togo = int(row[8])
            yard_line = int(row[9])
            yard_dir = row[39]
            #scorediff = int(row[10])
            formation = row[20]

            playtype = row[21] #Label
            if(playtype=='PASS'):
                playtype+=' ' + str(row[26])
            if(playtype=='RUSH'):
                if(str(row[37])!='0'):
                    playtype+=' ' + str(row[37])

            features.append(FeatureSet(quarter=quarter, secondsleft= seconds_left, down=down,
                                       togo=togo, yardline=yard_line, scorediff=0, yarddirection=yard_dir,
                                       formation=formation).createArray())
            labels.append(playtype)
    return features, labels

def computeML(featuresTrain, labelsTrain, featuresTest, labelsTest):
    clf = RandomForestClassifier(max_depth=15,max_features=3, min_samples_leaf=6, n_estimators=7)
    #clf = DecisionTreeClassifier(max_depth=11)
    clf.fit(featuresTrain,labelsTrain)
    out = clf.predict(featuresTest)
    print(str(clf.score(featuresTest,labelsTest))+"% accuracy.")
    return clf

def runMainInput():
    while(True):
        inp = raw_input("Enter in format (quarter,secondsleft,down,togo,yardline,yarddir[OWN or OPP], formation): ")
        features = inp.split(",")
        timeLeft = features[1]
        times = timeLeft.split(":")
        secondsLeft = int(times[0]) * 60 + int(times[1])
        featureArr = FeatureSet(quarter=features[0], secondsleft=secondsLeft, down=features[2], togo=features[3], yardline=features[4],scorediff=0, yarddirection=features[5], formation=features[6])
        out = clf.predict(featureArr.createArray())
        out2 = clf.predict_proba(featureArr.createArray())
        print str(out) + " is the predicted play"

features, labels = createFeatureLabelSets()
print("The features and labels length is: " + str(len(features)))
print("There are " + str(len(set(labels))) + " unique labels active.")
amountOfPoints = len(features)
trainingPoints = 57000
percent = float(trainingPoints)/amountOfPoints
percent*=100
print("Using " + str(trainingPoints) + " training points, or..." + str(round(percent,2)) + "% of the dataset.")
clf = computeML(features[:trainingPoints],labels[:trainingPoints],features[trainingPoints:], labels[trainingPoints:])
runMainInput()