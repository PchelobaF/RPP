import datetime

class Receipt:
    def __init__(self, number = 0, date_time = "11.11.1111 11:11", sum = 0, item_name = "item0"):
        self.number = number
        self.date_time = date_time
        self.sum = sum
        self.item_name = item_name
    
    def __repr__(self):
        return f'Receipt(number={self.number}, date_time={self.date_time}, sum={self.sum}, item_name={self.item_name})'

    def __setattr__(self, name, value):
        if name == "number":
            if not isinstance(value, int):
                raise TypeError("The 'number' attribute must be of type 'int'")
            else:
                self.__dict__[name] = int(value)
        elif name == "date_time":
            try:
                value = datetime.datetime.strptime(value, '%d.%m.%Y %H:%M')
                self.__dict__[name] = value
            except ValueError:
                raise TypeError("The 'date_time' attribute must be of type 'datetime.datetime'")
        elif name == "sum":
            if not isinstance(value, (int, float)):
                raise TypeError("The 'sum' attribute must be of type 'int' or 'float'")
            else:
                self.__dict__[name] = float(value)
        elif name == "item_name":
            if not isinstance(value, str):
                raise TypeError("The 'item_name' attribute must be of type 'str'")
            else:
                self.__dict__[name] = value
        
class ReceiptCollection(Receipt):
    receipts = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        for receipt in self.receipts:
            yield receipt

    def __getitem__(self, index):
        return self.receipts[index]

    def __len__(self):
        return len(self.receipts)
    
    def add_receipt(self, number, date_time, sum, item_name):
        self.receipts.append(Receipt(number, date_time, sum, item_name))

    # def get_receipts_by_sum(self, sum):
    #     return [receipt for receipt in self.receipts if receipt.sum == sum]

    # def get_receipts_by_item_name(self, item_name):
    #     return (receipt for receipt in self.receipts if receipt.item_name == item_name)

receipt = ReceiptCollection()
receipt.add_receipt(2, "01.02.2022 12:00", 600, "item1")
receipt.add_receipt(3, "01.03.2022 12:00", 300, "item1")
receipt.add_receipt(2, "01.02.2022 12:00", 600, "item3")

for i in receipt:
    print(i, sep="\n")

# print(type(receipt[1].date_time),receipt[1].date_time, sep="\n")