# # Using Queue Structures to
# import queue
# import multiprocessing
# import time
# import threading
# import random
#
#
#
# #Creating queue ds
# q=queue.Queue()
# print(q.queue)
#
# #Adding elements-->enqueue
# for i in range(7):
#     q.put(i)
# print(q.queue)
#
# #Checking for an empty queue--> Returns bool val.
# print(q.empty())
#
# #Removing elements-->dequeue
# while not q.empty():
#     print(q.get())
# print(q.queue)
#
# #Stacks in form of Queue
# q=queue.LifoQueue()
#
# #Adding elements-->push
# for i in range(7):
#     q.put(i)
# print(q.queue)
#
# #Checking for an empty stack-based queue--> Returns bool val.
# print(q.empty())
#
# #Removing elements-->pop
# while not q.empty():
#     print(q.get())
# print(q.queue)
#
# #Priority Queue
# q=queue.PriorityQueue()
#
# #Order of Insertion doesn't matter when removing them
# q.put(5)
# q.put(4)
# q.put(1)
# q.put(3)
# q.put(2)
#
# print(q.queue)
# #Removes based on highest priority(Lowest no.)
# while not q.empty():
#     print(q.get())
#
# #Multithreading with Queues
# q1=queue.Queue()
#
# q1.put(6)
# print(q1.get())
#
# print(q1.empty())
#
#
# #To keep queues thread-safe, we can use Producer-Consumer logic so as to keep count of the items
#
#
#
# counter=1
# more_to_come=True
#
# # class Producer(threading.Thread):
# #     def __init__(self,queue):
# #         threading.Thread.__init__(self)
# #         self.queue=queue
# #
# #     def run(self):
# #
# #         global counter
# #         global more_to_come
# #
# #         for i in range(5):
# #             time.sleep(random.randrange(2,5))
# #             item="New Item #"+str(counter)
# #
# #             self.queue.put(item)
# #             counter+=1
# #
# #             print("\nProduced:",item)
# #
# #         more_to_come=False
# #
# # class Consumer(threading.Thread()):
# #
# #     def __iter__(self,queue):
# #         threading.Thread.__init__(self)
# #         self.queue=queue
# #
# #     def run(self):
# #
# #         while more_to_come:
# #             item=self.queue.get(timeout=10)
# #             time.sleep(random.random())
# #             print(threading.current_thread().getName()," popped:",item)
# #
# #         print(threading.current_thread().getName(), " existing...")
# #
# # q2=queue.Queue()
# #
# # producer_thread=Producer(q2)
# # consumer_thread=Consumer(q2)
# #
# # producer_thread.start()
# # consumer_thread.start()
# #
# # print(producer_thread.join())
# # print(consumer_thread.join())
#
#
# # def Square(n):
# #
# #     time.sleep(1)
# #     res=n*n
# #     print(f"The square of number {n} is {res}")
# #
# # numbers=[1,2,3,4]
# #
# # start_time=time.time()
# #
# # for i in numbers:
# #     Square(i)
# #
# # end_time=time.time()
# #
# # print(end_time-start_time)
#
# # import os
# # from multiprocessing import Process,current_process
# #
# # def Square2(n):
# #
# #     time.sleep(1)
# #     res=n*n
# #     process_id=os.getpid()
# #     print("Process id: ",process_id)
# #     print(f"The square of number {n} is {res}")
# #
# # numbers=[1,2,3,4]
# # start_time=time.time()
# # for i,num in enumerate(numbers):
# #     process=Process(target=Square2,args=(num, ))
# #     process.start()
# #
# # process.join()
# # end_time=time.time()
# #
# # for i in numbers:
# #     Square2(i)
#
#
# #Multithreading VS Multiprocessing
# #
# # def Square3(numbers):
# #     for i in numbers:
# #         print(f"The square of {i} is: {i**2}")
# # def Cube(numbers):
# #     for i in numbers:
# #         print(f"The cube of {i} is: {i**3}")
# #
# # num_list=[1,2,3]
# #
# # p1=multiprocessing.Process(target=Square3,args=(num_list,))
# # p2=multiprocessing.Process(target=Cube,args=(num_list,))
# #
# # p1.start()
# # p2.start()
# #
# # p1.join()
# # p2.join()
# #
# # print("\nCompleted...\n\n")
#
# sq_res=[]
# num_list=[2,3,8]
# # MULTIPROCESSING
#
# # def Square4(numbers):
# #
# #     global sq_res
# #
# #     for i in numbers:
# #         print(f"Square of {i} is: {i**2}")
# #         sq_res.append(i**2)
# #
# # p1=multiprocessing.Process(target=Square4,args=(num_list,))
# #
# # p1.start()
# # p1.join()
# #
# # print("\nResult: ",sq_res)
# #
# # print("\nCompleted")
# #
# # def Square4(numbers):
# #
# #     global sq_res
# #
# #     for i in numbers:
# #         print(f"Square of {i} is: {i**2}")
# #         sq_res.append(i**2)
# #
# #     print("\nWithin the process. Result: ",sq_res)
# #
# # p1=multiprocessing.Process(target=Square4,args=(num_list,))
# #
# # p1.start()
# # p1.join()
# #
# # print("\nCompleted")
#
#
# #MULTITHREADING - Threads can be effectively used for better shared memory and variables
#
# def Square4(numbers):
#
#     global sq_res
#
#     for i in numbers:
#         print(f"Square of {i} is: {i**2}")
#         sq_res.append(i**2)
#
# p1=threading.Thread(target=Square4,args=(num_list,))
#
# p1.start()
# p1.join()
#
# print("\nResult: ",sq_res)
#
# print("\nCompleted")
#
# #MULTIPROCESSING USING SHARED MEMORY
#
# # res=[]
# # def Square4(numbers):
# #
# #     global res
# #
# #     for i in numbers:
# #         res.append(i**2)
# #
# #     print("\nChild process result: ",res)
# #
# # p1=multiprocessing.Process(target=Square4,args=(num_list,))
# #
# # p1.start()
# # p1.join()
#
# # num_list=[1,2,3,4]
# #
# # def sq_list(numlist, result, sq_sum):
# #
# #     for idx,num in enumerate(numlist):
# #         result[idx]=num**2
# #
# #     sq_sum.value=sum(result)
# #
# # result=multiprocessing.Array('i',4)
# # # First Arg.: Type ==> i(integer) represents the type of data to be stored in the array
# #                             # Second Arg.: No. of elements in the shared array(4 in this case)
# #
# # sq_sum=multiprocessing.Value('i')
# #
# # p=multiprocessing.Process(target=sq_list,args=(num_list,result,sq_sum))
# #
# # p.start()
# # p.join()
# #
# # print(list(result))
# # print(sq_sum.value)
#
# #MULTIPROCESSING USING MANAGER CLASS
# # The previous method had the restriction by the type of child process and parent process
# # Now, we try Manager Class/Server Process Manager.
#
# # def get_data(data_list):
# #     for data in data_list:
# #         print(f"Name: {data[0]}\nScore: {data[1]}")
# #
# # def append_data(new_data,data_list):
# #     data_list.append(new_data)
# #     print("New Data appended: \n")
# #
# # database=([('Maura',70),('Alexis',79),('Pete',96)])
# #
# # new_data=('Leroy',87)
# #
# # p1=multiprocessing.Process(target=append_data,args=(new_data,database))
# # p2=multiprocessing.Process(target=get_data,args=(database,))
# #
# # p1.start()
# # p1.join()
# #
# # #Prints New Data Appended
# #
# # p2.start()
# # p2.join()
#
# #Prints the list of 3 tuples in the form of Name\nScore
# #
# # with multiprocessing.Manager() as manager:
# #
# #     database=(manager.list([('Maura',70),('Alexis',79),('Pete',96)]))
# #     new_data=('Leroy',87)
# #
# #     p1=multiprocessing.Process(target=append_data,args=(new_data,database))
# #     p2=multiprocessing.Process(target=get_data,args=(database,))
# #
# #     p1.start()
# #     p1.join()
# #
# #     p2.start()
# #     p2.join()
# #
# #     print("Data available to the manager: ",database)
#
# #SYNCHRONIZING CONCURRENT PROCESSES WITH LOCKS
#
# # def deposit_without_mp(balance,amount):
# #     for i in range(100):
# #         time.sleep(0.01)
# #         balance+=amount
# #     return balance
# #
# #
# # def withdraw_without_mp(balance,amount):
# #     for i in range(100):
# #         time.sleep(0.01)
# #         balance-=amount
# #     return balance
# #
# # balance=600
# # balance=deposit_without_mp(balance,5)
# # balance=withdraw_without_mp(balance,5)
# #
# # print(balance) #--> 600
#
# # def deposit_without_locks(balance,amount):
# #     for i in range(100):
# #         time.sleep(0.01)
# #         balance.value+=amount
# #
# # def withdraw_without_locks(balance,amount):
# #     for i in range(100):
# #         time.sleep(0.01)
# #         balance.value-=amount
# #
# # balance=multiprocessing.Value('i',600)
# #
# # d=multiprocessing.Process(target=deposit_without_locks,args=(balance,5))
# # w=multiprocessing.Process(target=withdraw_without_locks,args=(balance,5))
# #
# # d.start()
# # w.start()
# #
# # d.join()
# # w.join()
# #
# # print(balance.value) # prints random value based on who reads more stale values than the other one
#
# # TO GET A CORRECT AMOUNT, Eliminates the race condn. and gives consistent result
#
# # def deposit_with_locks(balance,amount,lock):
# #     for i in range(100):
# #         time.sleep(0.01)
# #         lock.acquire()
# #         balance.value+=amount
# #         lock.release()
# #
# # def withdraw_with_locks(balance,amount,lock):
# #     for i in range(100):
# #         time.sleep(0.01)
# #         lock.acquire()
# #         balance.value-=amount
# #         lock.release()
# #
# # balance=multiprocessing.Value('i',600)
# # lock=multiprocessing.Lock()
# #
# # d=multiprocessing.Process(target=deposit_with_locks,args=(balance,5,lock))
# # w=multiprocessing.Process(target=withdraw_with_locks,args=(balance,5,lock))
# #
# # d.start()
# # w.start()
# #
# # d.join()
# # w.join()
# #
# # print(balance.value) # Result --> 600
#
# #Alternatives for Locks:- Semaphores,Bounded Sema.,Events, etc. synchronization mechanisms
#
# #INTER-PROCESS COMMUNICATION IN PYTHON
#
# def is_even(numbers,q):
#     for n in numbers:
#         if n%2==0:
#             q.put(n)
#
# def print_numbers(q):
#     while not q.empty():
#         print(q.get())
#
# q=multiprocessing.Queue() #Process-safe as threads are used
#
# p1=multiprocessing.Process(target=is_even,args=(range(10),q))
# p2=multiprocessing.Process(target=print_numbers,args=(q,))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join() # prints 0 \n 2 \n .... 8
#
# def sender(connection, greets):
#     for greet in greets:
#         connection.send(greet)
#     connection.close()
#
# def recipient(connection):
#     while True:
#         greet=connection.recv()
#         if greet=='STOP':
#             break
#         print(greet)
#
# msgs=["Hello","Hola","Guten Tag","STOP"]
# sending_pipe,receiving_pipe=multiprocessing.Pipe()
#
# p1=multiprocessing.Process(target=sender,args=(sending_pipe,msgs))
# p2=multiprocessing.Process(target=recipient,args=(receiving_pipe,))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
a=[1,2,3,4,5,6]

for a[-1] in a:
    print(a[-1])
