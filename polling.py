#Average function
def getAverage(a):
    ave=getTotal(a)/getSum(a)
    return ave


def getTotal(a):
    total = 0.0
    for i in range(len(a)):
        total += a[i]*(i+1)

    return total


def getSum(a):
    sumv=0  
    for i in a:
        sumv=sumv+i
    return sumv

#max and min function
def getPoints(P):
    maximum= max(P)
    
    return maximum

def getPoints(P):
    minimum= min(P)
    return minimum
    


#set topics and ratings function
def setTopics():
    TopicsNo= input("Set the number of topics to be rated: ")
    topicsList= list()
    for i in range(1,TopicsNo+1):
        request=raw_input( "Type in Topic " + str(i) + ": ")
        topicsList.append(request)
    return topicsList


def setRatings(causes):
    ratings = list()
    
    for i in range(len(causes)):
        sampList = list()
        for j in range(10):
            sampList.append(0)
        ratings.append(sampList)
        
    sentinel = 'y'
    print "Enter ratings for the following"
    while(sentinel=='y'):
        for i in range(len(causes)):
            rating = input("%s: "%(causes[i]))
            
            ratings[i][rating-1] += 1

        sentinel = raw_input("Create another entry? (y/n)")

    return ratings


def first(x,y,z,h):
    print "\nValues in a tabular form"
    print "-------------------------------------------------------------------------------------------------------------------------"
    print "|Topics\t|",
    for i in range(1,11):
        print "\t%d|"%(i), 
    print "\tAverage\t|\tTotal\t|"
    print "-------------------------------------------------------------------------------------------------------------------------"

    for i in range(len(x)):
        print "|%s\t|"%(x[i]),
        for j in range(10):
            print "\t%d|"%(y[i][j]),

        print "\t%f|\t%d\t|"%(z[i], h[i])
        print "-------------------------------------------------------------------------------------------------------------------------"


def getMax(y):
    maxim= 0
    for i in range (len(y)):
        if (y[i]>y[maxim]):
            maxim=i
    return maxim


def getMin(y):
    minim= 0
    for i in range (len(y)):
        if (y[i]<y[minim]):
            minim=i
    return minim
averages=list()
totals = list()

topics = setTopics()
ratings = setRatings(topics)

for i in ratings:
    eachAve= getAverage(i)
    eachTotal = getTotal(i)
    averages.append(eachAve)
    totals.append(eachTotal)
#print totals
#print averages

first(topics,ratings,averages,totals)
t=getMax(totals)
g=getMin(totals)
#print totals[t]

print "The Topic with the maximum rating is " + topics[t]
#print totals[g]
print "The Topic with the minimum rating is " + topics[g]






