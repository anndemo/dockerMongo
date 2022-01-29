import time
from uuid import uuid4
from storage import MongodbService, os
from dotenv import load_dotenv

load_dotenv()

storage = MongodbService.get_instance()

print("0!!!")


# for row in range(10):
#     hello = {
#         "_id": str(uuid4()),
#         "time": str(int(time.time())),
#         "string": f"Hello, {row} times!"
#     }
#     storage.save_data(hello)

# num = int(os.environ.get("NUMBER"))

num = int(os.getenv("OTHER_NUM"))

for i, data in zip(range(num), storage.get_data()):
    num += 1
    print(data['string'])

