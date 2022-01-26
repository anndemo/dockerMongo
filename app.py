import time
from uuid import uuid4
from storage import MongodbService, os


storage = MongodbService.get_instance()

print("Zero!!!")


for row in range(10):
    hello = {
        "_id": str(uuid4()),
        "time": str(int(time.time())),
        "string": f"Hello, {row} times!"
    }
    storage.save_data(hello)

num = int(os.environ.get("NUMBER"))

for i, data in zip(range(num), storage.get_data()):
    num += 1
    print(data['string'])

