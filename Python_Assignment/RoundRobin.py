import Queue as Queue


class Process:
    def __init__(self,Name,ArrivalTime,Duration):
        self.name = Name
        self.arrivalTime = int(ArrivalTime)
        self.duration = int(Duration)
        self.finish_Time = 0


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
        print self.finish_Time


process_Count = raw_input('How many processes you have : ')
print process_Count
List = []
counter = 1

while(True):
    if(int(counter) > int(process_Count)):
        break
    n = raw_input('Enter Name of process %d: ' % counter)
    at = raw_input('Enter Arrival Time of process %d: ' % counter)
    d = raw_input('Enter Duration of process %d: ' % counter)
    obj = Process(n, at, d)
    List.append(obj)
    counter += 1

time_Quantum = raw_input('Enter time quantem : ')

print "Gantt Chart"

queueA = Queue.PriorityQueue()

for temporary in List:
    queueA.put(temporary)

var = queueA.get()
ready_Queue = Queue.Queue(Process)
ob = Process(var.name, var.arrivalTime, var.duration)
ready_Queue.put(ob)
counter = 0

while not queueA.empty():
    var = queueA.get()
    if int(var.arrivalTime) == counter:
        ob = Process(var.name, var.arrivalTime, var.duration)
        ready_Queue.put(ob)
    else:
        queueA.put(var)
        break

while not ready_Queue.empty():

    process = ready_Queue.get()

    if counter == 0:
        iterator = process.arrivalTime
        counter = iterator
        print iterator,

    else:
        iterator = 1

    duration = int(process.duration)

    while int(iterator) <= duration:

        while not queueA.empty():
            var = queueA.get()
            if int(var.arrivalTime) == counter:
                ob = Process(var.name, var.arrivalTime, var.duration)
                ready_Queue.put(ob)
            else:
                queueA.put(var)
                break

        if int(iterator) > int(time_Quantum):
            ready_Queue.put(process)
            print counter,process.name,
            break

        process.duration -= 1

        if int(iterator) == duration:
            print '_', counter + 1, process.name,
        else:
            print '_',

        iterator += 1
        counter += 1

