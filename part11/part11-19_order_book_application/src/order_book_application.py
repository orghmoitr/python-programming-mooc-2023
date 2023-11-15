# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
    uid = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.uid += 1
        self.id = Task.uid
        self.finished = False

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def finished_status(self):
        if self.is_finished() is True:
            return "FINISHED"
        else:
            return "NOT FINISHED"

    def __str__(self):
        return (f"{self.id}: {self.description} ({self.workload} hours), "
                f"programmer {self.programmer} {self.finished_status()}")


class OrderBook:

    def __init__(self):
        self.tasks = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set([task.programmer for task in self.tasks]))

    def mark_finished(self, id: int):
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                return
        else:
            raise ValueError("invalid id")

    def finished_orders(self):
        return [task for task in self.tasks if task.is_finished() is True]

    def unfinished_orders(self):
        return [task for task in self.tasks if task.is_finished() is False]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("no such programmer")
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0
        for task in self.tasks:
            if task.programmer == programmer:
                if task.is_finished() is True:
                    finished += 1
                    finished_workload += task.workload
                else:
                    unfinished += 1
                    unfinished_workload += task.workload
        return finished, unfinished, finished_workload, unfinished_workload


class OrderBookApplication:

    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        desc = input("description: ")
        prog_load = input("programmer and workload estimate: ")
        parts = prog_load.split(" ")
        prog = parts[0]
        try:
            load = int(parts[1])
        except:
            print("erroneous input")
            return
        self.__orderbook.add_order(desc, prog, load)
        print("added!")

    def list_finished_tasks(self):
        if len(self.__orderbook.finished_orders()) == 0:
            print("no finished tasks")
            return
        for finished_task in self.__orderbook.finished_orders():
            print(finished_task)

    def list_unfinished_tasks(self):
        if len(self.__orderbook.unfinished_orders()) == 0:
            print("no unfinished tasks")
            return
        for unfinished_task in self.__orderbook.unfinished_orders():
            print(unfinished_task)

    def mark_finished(self):
        try:
            id = int(input("id: "))
        except ValueError:
            print("erroneous input")
            return

        ids = [task.id for task in self.__orderbook.all_orders()]
        if id not in ids:
            print("erroneous input")
            return
        self.__orderbook.mark_finished(id)
        print("marked as finished")
        return

    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        if programmer not in self.__orderbook.programmers():
            print("erroneous input")
            return
        f, uf, fw, ufw = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {f} not finished {uf}, hours: done {fw} scheduled {ufw}")

    def execute(self):
        self.help()
        while True:
            print()
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.list_finished_tasks()
            elif command == 3:
                self.list_unfinished_tasks()
            elif command == 4:
                self.mark_finished()
            elif command == 5:
                self.programmers()
            elif command == 6:
                self.status_of_programmer()
            else:
                self.help()


application = OrderBookApplication()
application.execute()
