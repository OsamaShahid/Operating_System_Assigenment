import Queue as Queue


class Process:
    def __init__(self, Name, ArrivalTime, Duration, Number):
        self.name = Name
        self.arrivalTime = int(ArrivalTime)
        self.duration = int(Duration)
        self.Queue_Number = int(Number)

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
    queue_number = raw_input('Enter queue number (1,2 or 3) of process %d: ' % iterator)
    obj = Process(n, at, d, queue_number)
    List.append(obj)
    iterator += 1

queue1 = Queue.PriorityQueue()
queue2 = Queue.PriorityQueue()
queue3 = Queue.PriorityQueue()
for x in List:
    if x.Queue_Number == 1:
        queue1.put(x)
    elif x.Queue_Number == 2:
        queue2.put(x)
    elif x.Queue_Number == 3:
        queue3.put(x)

print "Gantt Chart"
del obj
counter = 0

waitingTime = 0

while not queue1.empty():
    process = queue1.get()
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


while not queue2.empty():
    process = queue2.get()
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


while not queue3.empty():
    process = queue3.get()
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
