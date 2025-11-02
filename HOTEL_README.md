# Hotel Management System

A simple and easy-to-use Hotel Management System built with Python using file handling for data persistence.

## Features

### 🔐 Authentication System
- **User Signup**: Create a new account with username, password, name, email, and phone
- **User Login**: Secure login system to access hotel services

### 🏨 Hotel Management Features
- **View Available Rooms**: Browse all available rooms with details (room number, type, price)
- **Book a Room**: Reserve a room with check-in/check-out dates and guest count
- **View My Bookings**: See all your current and past bookings
- **Cancel Booking**: Cancel your reservations and free up rooms

### 💾 Data Persistence
All data is stored in JSON files:
- `users.json` - User account information
- `rooms.json` - Room details and availability status
- `bookings.json` - Booking records

## Room Types & Pricing

| Room Type | Price per Night |
|-----------|----------------|
| Single    | ₹1,000         |
| Double    | ₹1,500         |
| Deluxe    | ₹2,000         |
| Suite     | ₹3,000         |

## How to Run

1. Make sure you have Python installed (Python 3.6 or higher)

2. Run the program:
```bash
python hotel_management.py
```

3. Follow the on-screen menu to:
   - Create an account (Signup)
   - Login with your credentials
   - Book rooms, view bookings, and manage reservations

## Usage Guide

### First Time Users
1. Select option `1` (Signup) from the main menu
2. Enter your details (username, password, name, email, phone)
3. After successful signup, select option `2` (Login)
4. Enter your username and password

### Booking a Room
1. After login, select option `2` (Book a Room)
2. View the list of available rooms
3. Enter the room number you want to book
4. Provide check-in date, check-out date, and number of guests
5. You'll receive a booking ID for your reservation

### Viewing Your Bookings
1. Select option `3` (View My Bookings)
2. See all your bookings with details including booking ID, room info, dates, and status

### Cancelling a Booking
1. Select option `4` (Cancel Booking)
2. View your bookings and note the Booking ID
3. Enter the Booking ID you want to cancel
4. The room will become available again

## File Structure

```
hotel_management.py     # Main application file
users.json             # User accounts database
rooms.json             # Room inventory database
bookings.json          # Booking records database
```

## Default Rooms

The system comes pre-configured with 8 rooms:
- Rooms 101-102: Single rooms
- Rooms 103-104: Double rooms
- Rooms 105-106: Suite rooms
- Rooms 107-108: Deluxe rooms

## Notes

- All data is stored locally in JSON files
- Passwords are stored in plain text (for educational purposes only)
- The system automatically creates data files on first run
- Each booking gets a unique booking ID (e.g., BK0001, BK0002)
- Cancelled bookings remain in the system with "cancelled" status

## Future Enhancements

Possible improvements:
- Password encryption
- Payment integration
- Room service orders
- Admin panel for hotel staff
- Billing and invoice generation
- Guest feedback system
- Room maintenance tracking

---

**Enjoy using the Hotel Management System! 🏨**
