class Bill:
    def __int__(self):
        self.money = 0

    def __add__(self, count):

        self.money += count

    def buy(self, count, name):

        pass

leo_bill = Bill()
print(leo_bill.money)

leo_bill.add(10)
leo_bill.add(20)

print(leo_bill.money)

kate_bill = Bill()
print(kate_bill.money)

kate_bill.add(1)
print(kate_bill.money)

print("zhenya", leo_bill.money)