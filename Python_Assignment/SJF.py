import Queue as Queue


class ProcessA:
    def __init__(self,Name,ArrivalTime,Duration):
        self.name = Name
        self.arrivalTime = int(ArrivalTime)
        self.duration = Duration

    def getName(self):
        return self.name

    def getArrivalTime(self):
        return self.arrivalTime

    def getDuration(self):
        return self.duration

    def __cmp__(self, other):
        return cmp(int(self.arrivalTime), int(other.arrivalTime))

    def printProcess(self):
        print self.name
        print self.arrivalTime
        print self.duration


class ProcessR:
    def __init__(self,Name,ArrivalTime,Duration):
        self.name = Name
        self.arrivalTime = int(ArrivalTime)
        self.duration = Duration

    def getName(self):
        return self.name

    def getArrivalTime(self):
        return self.arrivalTime

    def getDuration(self):
        return self.duration

    def __cmp__(self, other):
        return cmp(int(self.duration), int(other.duration))

    def printProcess(self):
        print self.name
        print self.arrivalTime
        print self.duration


process_count = raw_input('How many processes you have : ')
print process_count
List = []
iterator = 1

while True :
    if int(iterator) > int(process_count) :
        break
    n = raw_input('Enter Name of process %d: ' % iterator)
    at = raw_input('Enter Arrival Time of process %d: ' % iterator)
    d = raw_input('Enter Duration of process %d: ' % iterator)
    obj = ProcessA(n, at, d)
    List.append(obj)
    iterator += 1

print "Gantt Chart"

# queue prioritized on the basis of arrival time
queueA = Queue.PriorityQueue()
for x in List:
    queueA.put(x)

var = queueA.get()
ob = ProcessR(var.name, var.arrivalTime, var.duration)
# queue prioritized on the basis of duration
queueR = Queue.PriorityQueue()
queueR.put(ob)
counter = 0

waitingTime = 0

while not queueA.empty():
    var = queueA.get()
    if int(var.arrivalTime) == counter:
        ob = ProcessR(var.name, var.arrivalTime, var.duration)
        queueR.put(ob)
    else:
        queueA.put(var)
        break

while not queueR.empty():
    process = queueR.get()

    if counter == 0:
        iterator = process.arrivalTime
        counter = iterator
        print iterator,
    else:
        iterator = 1

    waitingTime += counter - process.arrivalTime

    while int(iterator) <= int(process.duration):

        while not queueA.empty():
            var = queueA.get()
            if int(var.arrivalTime) == counter:
                ob = ProcessR(var.name, var.arrivalTime, var.duration)
                queueR.put(ob)
            else:
                queueA.put(var)
                break

        if int(iterator) == int(process.duration):
            print '_', counter,
        else:
            print '_',

        iterator += 1
        counter += 1


print 'Average Waiting Time is : ',
average_Waiting_Time = float(waitingTime) / float(process_count)
print average_Waiting_Time
