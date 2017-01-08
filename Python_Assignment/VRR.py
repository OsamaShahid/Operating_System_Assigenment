import Queue as Queue


class Process:
    def __init__(self,Name,ArrivalTime,Duration):
        self.name = Name
        self.arrivalTime = int(ArrivalTime)
        self.duration = int(Duration)
        self.finish_Time = int(0)
        self.waiting_Time = int(0)
        self.time_Quantum = int(0)
        self.progress = int(0)
        self.total_Waiting_Time = int(0)

    def get_Name(self):
        return self.name

    def getArrival_Time(self):
        return self.arrivalTime

    def get_Duration(self):
        return self.duration

    def __cmp__(self, other):
        return cmp(int(self.arrivalTime), int(other.arrivalTime))

    def printProcess(self):
        print self.name
        print self.arrivalTime
        print self.duration
        print self.finish_Time


class ProcessWaiting:
    def __init__(self,Name,ArrivalTime,Duration):
        self.name = Name
        self.arrivalTime = int(ArrivalTime)
        self.duration = int(Duration)
        self.finish_Time = int(0)
        self.waiting_Time = int(0)
        self.time_Quantum = int(0)
        self.progress = int(0)
        self.total_Waiting_Time = int(0)

    def get_Name(self):
        return self.name

    def getArrival_Time(self):
        return self.arrivalTime

    def get_Duration(self):
        return self.duration

    def __cmp__(self, other):
        return cmp(int(self.waiting_Time), int(other.waiting_Time))

    def printProcess(self):
        print self.name
        print self.arrivalTime
        print self.duration
        print self.finish_Time


process_Count = raw_input('How many processes you have : ')
print process_Count
List = []
counter = 1

while True:
    if int(counter) > int(process_Count):
        break
    n = raw_input('Enter Name of process %d: ' % counter)
    at = raw_input('Enter Arrival Time of process %d: ' % counter)
    d = raw_input('Enter Duration of process %d: ' % counter)
    obj = Process(n, at, d)
    List.append(obj)
    counter += 1

time_Quantum = raw_input('Enter time quantem : ')
# i am considering that every process will go for I/O after every 3 sec of its lifetime for 7 seconds

print "Gantt Chart"
arrival_Queue = Queue.PriorityQueue()


for temporary in List:
    arrival_Queue.put(temporary)
var = arrival_Queue.get()

waiting_Time = 0

ready_Queue = Queue.Queue(Process)
ob = Process(var.name, var.arrivalTime, var.duration)
ready_Queue.put(ob)
counter = 0


while not arrival_Queue.empty():
    var = arrival_Queue.get()
    if int(var.arrivalTime) == counter:
        ob = Process(var.name, var.arrivalTime, var.duration)
        ready_Queue.put(ob)
    else:
        arrival_Queue.put(var)
        break

waiting_Queue = Queue.PriorityQueue(ProcessWaiting)
auxiliary_Queue = Queue.Queue(ProcessWaiting)

while not ready_Queue.empty() or not waiting_Queue.empty() or not auxiliary_Queue.empty():

    while not waiting_Queue.empty():

            var = waiting_Queue.get()

            if int(var.waiting_Time) == counter:
                auxiliary_Queue.put(var)

            else:
                waiting_Queue.put(var)
                break

    while not auxiliary_Queue.empty():

            var = auxiliary_Queue.get()

            if int(var.waiting_Time) == counter:
                while var.time_Quantum > 0 and var.duration > 0 and var.progress < 3:
                    print '_',
                    var.time_Quantum -= 1
                    counter += 1
                    var.progress += 1
                    var.duration -= 1

                if var.duration == 0:
                    print counter, var.name,
                    var.finish_Time = counter
                    waiting_Time += var.finish_Time - var.arrivalTime - var.total_Waiting_Time

                elif var.progress == 3:
                    var.progress = 0
                    var.waiting_Time = counter + 7
                    print counter, var.name,
                    tmp = ProcessWaiting(var.name, var.arrivalTime, var.duration)
                    tmp.total_Waiting_Time += 7
                    tmp.progress = 0
                    tmp.waiting_Time = var.waiting_Time
                    waiting_Queue.put(tmp)


                else:
                    print counter, var.name,
                    var.waiting_Time = 0
                    ready_Queue.put(var)

            else:
                auxiliary_Queue.put(var)
                break

    while not arrival_Queue.empty():

            var = arrival_Queue.get()

            if int(var.arrivalTime) == counter:
                ob = Process(var.name, var.arrivalTime, var.duration)
                ready_Queue.put(ob)

            else:
                arrival_Queue.put(var)
                break

    if not ready_Queue.empty():
        process = ready_Queue.get()

        if counter == 0:
            iterator = process.arrivalTime
            counter = iterator
            print iterator,

        else:
            iterator = 1

        if process.time_Quantum == 0:
            process.time_Quantum = int(time_Quantum)

        duration = int(process.duration)

        while int(iterator) <= duration:

            while not waiting_Queue.empty():

                var = waiting_Queue.get()

                if int(var.waiting_Time) == counter:
                    auxiliary_Queue.put(var)

                else:
                    waiting_Queue.put(var)
                    break

            while not auxiliary_Queue.empty():

                var = auxiliary_Queue.get()

                if int(var.waiting_Time) == counter:
                    while var.time_Quantum > 0 and var.duration > 0 and var.progress < 3:
                        print '_',
                        var.time_Quantum -= 1
                        counter += 1
                        var.progress += 1
                        var.duration -= 1

                    if var.duration == 0:
                        print counter, var.name,
                        var.finish_Time = counter
                        waiting_Time += var.finish_Time - var.arrivalTime - var.total_Waiting_Time

                    elif var.progress == 3:
                        var.progress = 0
                        var.waiting_Time = counter + 7
                        print counter, var.name,
                        tmp = ProcessWaiting(var.name, var.arrivalTime, var.duration)
                        tmp.progress = 0
                        tmp.total_Waiting_Time += 7
                        tmp.waiting_Time = var.waiting_Time
                        waiting_Queue.put(tmp)

                    else:
                        var.waiting_Time = 0
                        ready_Queue.put(var)

                else:
                    auxiliary_Queue.put(var)
                    break

            while not arrival_Queue.empty():

                var = arrival_Queue.get()

                if int(var.arrivalTime) == counter:
                    ob = Process(var.name, var.arrivalTime, var.duration)
                    ready_Queue.put(ob)

                else:
                    arrival_Queue.put(var)
                    break

            if process.progress == 3:

                process.progress = 0
                process.waiting_Time = 7 + counter
                print counter, process.name,
                tmp = ProcessWaiting(process.name, process.arrivalTime, process.duration)
                tmp.progress = 0
                tmp.total_Waiting_Time += 7
                tmp.waiting_Time = process.waiting_Time
                waiting_Queue.put(tmp)
                break

            if process.time_Quantum == 0:

                ready_Queue.put(process)
                break

            process.duration -= 1
            process.time_Quantum -= 1
            process.progress += 1

            if int(iterator) == duration:
                print '_', counter + 1, process.name,
                process.finish_Time = counter + 1
                waiting_Time += process.finish_Time - process.arrivalTime - process.total_Waiting_Time

            else:
                print '_',

            iterator += 1
            counter += 1

    else:
        print '.',
        counter += 1

print 'Average waiting time is : ',
averageTime = float(waiting_Time) / float(process_Count)
print averageTime,



