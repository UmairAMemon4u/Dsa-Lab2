import os
import json
from datetime import datetime

class HotelManagementSystem:
    def __init__(self):
        self.users_file = "users.json"
        self.rooms_file = "rooms.json"
        self.bookings_file = "bookings.json"
        self.current_user = None
        
        # Initialize files if they don't exist
        self.initialize_files()
    
    def initialize_files(self):
        """Initialize data files with default data if they don't exist"""
        # Initialize users file
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump({}, f)
        
        # Initialize rooms file with default rooms
        if not os.path.exists(self.rooms_file):
            default_rooms = {
                "101": {"type": "Single", "price": 1000, "status": "available"},
                "102": {"type": "Single", "price": 1000, "status": "available"},
                "103": {"type": "Double", "price": 1500, "status": "available"},
                "104": {"type": "Double", "price": 1500, "status": "available"},
                "105": {"type": "Suite", "price": 3000, "status": "available"},
                "106": {"type": "Suite", "price": 3000, "status": "available"},
                "107": {"type": "Deluxe", "price": 2000, "status": "available"},
                "108": {"type": "Deluxe", "price": 2000, "status": "available"}
            }
            with open(self.rooms_file, 'w') as f:
                json.dump(default_rooms, f, indent=4)
        
        # Initialize bookings file
        if not os.path.exists(self.bookings_file):
            with open(self.bookings_file, 'w') as f:
                json.dump({}, f)
    
    def load_data(self, filename):
        """Load data from JSON file"""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def save_data(self, filename, data):
        """Save data to JSON file"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def signup(self):
        """User signup functionality"""
        print("\n" + "="*50)
        print("           USER SIGNUP")
        print("="*50)
        
        users = self.load_data(self.users_file)
        
        username = input("Enter username: ").strip()
        if username in users:
            print("❌ Username already exists! Please try a different username.")
            return False
        
        password = input("Enter password: ").strip()
        name = input("Enter your full name: ").strip()
        email = input("Enter your email: ").strip()
        phone = input("Enter your phone number: ").strip()
        
        users[username] = {
            "password": password,
            "name": name,
            "email": email,
            "phone": phone,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.save_data(self.users_file, users)
        print("\n✅ Signup successful! You can now login.")
        return True
    
    def login(self):
        """User login functionality"""
        print("\n" + "="*50)
        print("           USER LOGIN")
        print("="*50)
        
        users = self.load_data(self.users_file)
        
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        if username in users and users[username]["password"] == password:
            self.current_user = username
            print(f"\n✅ Welcome back, {users[username]['name']}!")
            return True
        else:
            print("❌ Invalid username or password!")
            return False
    
    def view_available_rooms(self):
        """Display all available rooms"""
        print("\n" + "="*50)
        print("           AVAILABLE ROOMS")
        print("="*50)
        
        rooms = self.load_data(self.rooms_file)
        available_rooms = {k: v for k, v in rooms.items() if v["status"] == "available"}
        
        if not available_rooms:
            print("❌ No rooms available at the moment.")
            return
        
        print(f"\n{'Room No.':<10} {'Type':<15} {'Price/Night':<15} {'Status':<10}")
        print("-" * 50)
        
        for room_no, details in available_rooms.items():
            print(f"{room_no:<10} {details['type']:<15} ₹{details['price']:<14} {details['status']:<10}")
    
    def book_room(self):
        """Book a room for the current user"""
        print("\n" + "="*50)
        print("           BOOK A ROOM")
        print("="*50)
        
        rooms = self.load_data(self.rooms_file)
        bookings = self.load_data(self.bookings_file)
        
        # Show available rooms first
        self.view_available_rooms()
        
        room_no = input("\nEnter room number to book: ").strip()
        
        if room_no not in rooms:
            print("❌ Invalid room number!")
            return
        
        if rooms[room_no]["status"] != "available":
            print("❌ This room is not available!")
            return
        
        # Get booking details
        check_in = input("Enter check-in date (YYYY-MM-DD): ").strip()
        check_out = input("Enter check-out date (YYYY-MM-DD): ").strip()
        guests = input("Enter number of guests: ").strip()
        
        # Generate booking ID
        booking_id = f"BK{len(bookings) + 1:04d}"
        
        # Create booking
        bookings[booking_id] = {
            "username": self.current_user,
            "room_no": room_no,
            "room_type": rooms[room_no]["type"],
            "price": rooms[room_no]["price"],
            "check_in": check_in,
            "check_out": check_out,
            "guests": guests,
            "booking_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "confirmed"
        }
        
        # Update room status
        rooms[room_no]["status"] = "booked"
        
        # Save data
        self.save_data(self.bookings_file, bookings)
        self.save_data(self.rooms_file, rooms)
        
        print(f"\n✅ Room booked successfully!")
        print(f"Booking ID: {booking_id}")
        print(f"Room Number: {room_no}")
        print(f"Room Type: {rooms[room_no]['type']}")
        print(f"Price per night: ₹{rooms[room_no]['price']}")
    
    def view_my_bookings(self):
        """View all bookings of the current user"""
        print("\n" + "="*50)
        print("           MY BOOKINGS")
        print("="*50)
        
        bookings = self.load_data(self.bookings_file)
        user_bookings = {k: v for k, v in bookings.items() if v["username"] == self.current_user}
        
        if not user_bookings:
            print("❌ You have no bookings yet.")
            return
        
        for booking_id, details in user_bookings.items():
            print(f"\nBooking ID: {booking_id}")
            print(f"Room Number: {details['room_no']}")
            print(f"Room Type: {details['room_type']}")
            print(f"Price: ₹{details['price']}/night")
            print(f"Check-in: {details['check_in']}")
            print(f"Check-out: {details['check_out']}")
            print(f"Guests: {details['guests']}")
            print(f"Status: {details['status']}")
            print(f"Booked on: {details['booking_date']}")
            print("-" * 50)
    
    def cancel_booking(self):
        """Cancel a booking"""
        print("\n" + "="*50)
        print("           CANCEL BOOKING")
        print("="*50)
        
        bookings = self.load_data(self.bookings_file)
        rooms = self.load_data(self.rooms_file)
        
        # Show user's bookings first
        self.view_my_bookings()
        
        booking_id = input("\nEnter Booking ID to cancel: ").strip()
        
        if booking_id not in bookings:
            print("❌ Invalid Booking ID!")
            return
        
        if bookings[booking_id]["username"] != self.current_user:
            print("❌ This booking doesn't belong to you!")
            return
        
        if bookings[booking_id]["status"] == "cancelled":
            print("❌ This booking is already cancelled!")
            return
        
        # Cancel booking
        room_no = bookings[booking_id]["room_no"]
        bookings[booking_id]["status"] = "cancelled"
        rooms[room_no]["status"] = "available"
        
        # Save data
        self.save_data(self.bookings_file, bookings)
        self.save_data(self.rooms_file, rooms)
        
        print(f"\n✅ Booking {booking_id} cancelled successfully!")
        print(f"Room {room_no} is now available for booking.")
    
    def user_menu(self):
        """Display user menu after login"""
        while True:
            print("\n" + "="*50)
            print("           HOTEL MANAGEMENT SYSTEM")
            print("="*50)
            print(f"Logged in as: {self.current_user}")
            print("\n1. View Available Rooms")
            print("2. Book a Room")
            print("3. View My Bookings")
            print("4. Cancel Booking")
            print("5. Logout")
            print("="*50)
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                self.view_available_rooms()
            elif choice == "2":
                self.book_room()
            elif choice == "3":
                self.view_my_bookings()
            elif choice == "4":
                self.cancel_booking()
            elif choice == "5":
                print("\n👋 Logging out... Thank you for using our service!")
                self.current_user = None
                break
            else:
                print("❌ Invalid choice! Please try again.")
            
            input("\nPress Enter to continue...")
    
    def main_menu(self):
        """Display main menu"""
        while True:
            print("\n" + "="*50)
            print("     WELCOME TO HOTEL MANAGEMENT SYSTEM")
            print("="*50)
            print("\n1. Signup")
            print("2. Login")
            print("3. Exit")
            print("="*50)
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                self.signup()
            elif choice == "2":
                if self.login():
                    self.user_menu()
            elif choice == "3":
                print("\n👋 Thank you for visiting! Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please try again.")
            
            if choice in ["1", "2"]:
                input("\nPress Enter to continue...")

def main():
    """Main function to run the hotel management system"""
    hotel = HotelManagementSystem()
    hotel.main_menu()

if __name__ == "__main__":
    main()
