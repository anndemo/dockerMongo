import time
from uuid import uuid4
from storage import MongodbService


storage = MongodbService.get_instance()

print("Zero!!!")


for row in range(5):
    hello = {
        "_id": str(uuid4()),
        "time": str(int(time.time())),
        "string": f"Hello, {row} times!"
    }
    storage.save_data(hello)

num = 0
for data in storage.get_data():
    num += 1
    print(data['string'])