from pydantic import BaseModel
from datetime import datetime

class BookingRequest(BaseModel):
    class_id: int
    user_name: str

class BookingResponse(BaseModel):
    booking_id: int
    class_id: int
    user_name: str
    timestamp: datetime

