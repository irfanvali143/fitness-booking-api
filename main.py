from fastapi import FastAPI, HTTPException, Query
from seed import classes
from models import BookingRequest, BookingResponse
from datetime import datetime
from typing import List
import pytz

app = FastAPI()

bookings = []  # store bookings in memory
booking_id_counter = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fitness Booking API"}

@app.get("/classes")
def get_classes(timezone: str = "Asia/Kolkata"):
    try:
        tz = pytz.timezone(timezone)
    except Exception:
        tz = pytz.timezone("Asia/Kolkata")

    formatted_classes = []
    for c in classes:
        class_copy = c.copy()
        class_copy["datetime"] = c["datetime"].astimezone(tz).isoformat()
        formatted_classes.append(class_copy)

    return formatted_classes

@app.post("/book", response_model=BookingResponse)
def book_class(booking: BookingRequest):
    global booking_id_counter

    selected_class = next((c for c in classes if c["id"] == booking.class_id), None)
    if not selected_class:
        raise HTTPException(status_code=404, detail="Class not found")

    if selected_class["available_slots"] <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    selected_class["available_slots"] -= 1

    new_booking = {
        "booking_id": booking_id_counter,
        "class_id": booking.class_id,
        "user_name": booking.user_name,
        "user_email": booking.user_email,  # <-- include this!
        "timestamp": datetime.now()
    }

    bookings.append(new_booking)
    booking_id_counter += 1
    return new_booking

@app.get("/bookings")
def get_bookings_by_email(email: str = Query(...)):
    user_bookings = [b for b in bookings if b.get("user_email") == email]
    return user_bookings
