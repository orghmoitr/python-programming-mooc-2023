# Write your solution here:

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


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
