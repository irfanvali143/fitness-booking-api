from datetime import datetime, timedelta
import pytz

IST = pytz.timezone('Asia/Kolkata')

classes = [
    {
        "id": 1,
        "name": "Yoga",
        "instructor": "Alice",
        "datetime": IST.localize(datetime.now() + timedelta(days=1, hours=7)),
        "total_slots": 10,
        "available_slots": 10
    },
    {
        "id": 2,
        "name": "Zumba",
        "instructor": "Bob",
        "datetime": IST.localize(datetime.now() + timedelta(days=2, hours=10)),
        "total_slots": 15,
        "available_slots": 15
    },
    {
        "id": 3,
        "name": "HIIT",
        "instructor": "Charlie",
        "datetime": IST.localize(datetime.now() + timedelta(days=3, hours=6)),
        "total_slots": 8,
        "available_slots": 8
    },
]
