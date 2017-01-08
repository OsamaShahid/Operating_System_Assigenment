import Queue as Queue


class Process:
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


process_count = raw_input('How many processes you have : ')
print process_count
List = []
iterator = 1
while True:
    if int(iterator) > int(process_count):
        break
    n = raw_input('Enter Name of process %d: ' % iterator)
    at = raw_input('Enter Arrival Time of process %d: ' % iterator)
    d = raw_input('Enter Duration of process %d: ' % iterator)
    obj = Process(n, at, d)
    List.append(obj)
    iterator += 1

queue = Queue.PriorityQueue()
for x in List:
    queue.put(x)

print "Gantt Chart"
del obj
counter = 0

waitingTime = 0

while not queue.empty():
    process = queue.get()
    waitingTime += counter - process.arrivalTime
    if counter == 0:
        iterator = process.arrivalTime
        counter = iterator
        print iterator,
    else:
        iterator = 1
    while int(iterator) <= int(process.duration):
        if int(iterator) == int(process.duration):
            print '_', counter,
        else:
            print '_',
        iterator += 1
        counter += 1

print 'Average Waiting Time is : ',
average_Waiting_Time = float(waitingTime) / float(process_count)
print average_Waiting_Time
