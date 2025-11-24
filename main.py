import random
import time

# -----------------------------
# Simple in-memory "database"
# -----------------------------
AVAILABLE_TRAINS = [
    {
        "train_no": "12001",
        "name": "Express A",
        "from": "Mumbai",
        "to": "Pune",
        "base_fare": 300
    },
    {
        "train_no": "12002",
        "name": "Express B",
        "from": "Delhi",
        "to": "Jaipur",
        "base_fare": 450
    },
    {
        "train_no": "12003",
        "name": "Express C",
        "from": "Chennai",
        "to": "Bengaluru",
        "base_fare": 400
    }
]

SEAT_PREFERENCES = ["Lower", "Middle", "Upper", "Side Lower", "Side Upper"]
FOOD_PREFERENCES = ["Veg", "Non-Veg", "No Food"]
PAYMENT_METHODS = ["UPI", "Credit Card", "Debit Card", "Net Banking"]


# -----------------------------
# Helper functions
# -----------------------------
def generate_pnr():
    return "PNR" + str(random.randint(1000000000, 9999999999))


def calculate_total_fare(base_fare, food_choice):
    food_charge = 0
    if food_choice in ("Veg", "Non-Veg"):
        food_charge = 100
    return base_fare + food_charge


def choose_train():
    print("\nAvailable Trains:")
    for i, train in enumerate(AVAILABLE_TRAINS, start=1):
        print(f"{i}. {train['train_no']} - {train['name']} "
              f"({train['from']} -> {train['to']}) | Base Fare: ₹{train['base_fare']}")
    while True:
        choice = input("Enter train number (e.g., 12001): ").strip()
        for train in AVAILABLE_TRAINS:
            if train["train_no"] == choice:
                return train
        print("Invalid train number. Please try again.")


def choose_option_from_list(options, prompt_text):
    print(f"\n{prompt_text}")
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    while True:
        try:
            choice = int(input("Enter choice number: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")


def get_passenger_details():
    print("\nEnter Passenger Details")
    name = input("Name: ").strip()
    while True:
        try:
            age = int(input("Age: ").strip())
            if age <= 0:
                print("Age must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for age.")

    seat_pref = choose_option_from_list(SEAT_PREFERENCES, "Seat Preference:")
    food_pref = choose_option_from_list(FOOD_PREFERENCES, "Food Preference:")
    return {
        "name": name,
        "age": age,
        "seat_pref": seat_pref,
        "food_pref": food_pref
    }


def mock_payment_gateway(amount):
    print("\n=== Payment Gateway ===")
    print(f"Amount to be paid: ₹{amount}")
    method = choose_option_from_list(PAYMENT_METHODS, "Select Payment Method:")
    print(f"Processing {method} payment...")
    time.sleep(1.5)
    # In a real system, integrate with actual gateway APIs here.
    print("Payment successful!")
    transaction_id = "TXN" + str(random.randint(1000000, 9999999))
    return {
        "method": method,
        "transaction_id": transaction_id,
        "status": "SUCCESS"
    }


def print_ticket(booking):
    print("\n=========== E-TICKET ===========")
    print(f"PNR: {booking['pnr']}")
    print(f"Passenger Name : {booking['passenger']['name']}")
    print(f"Age            : {booking['passenger']['age']}")
    print(f"Seat Pref.     : {booking['passenger']['seat_pref']}")
    print(f"Food Pref.     : {booking['passenger']['food_pref']}")
    print("-------------------------------")
    print(f"Train No       : {booking['train']['train_no']}")
    print(f"Train Name     : {booking['train']['name']}")
    print(f"From           : {booking['train']['from']}")
    print(f"To             : {booking['train']['to']}")
    print("-------------------------------")
    print(f"Base Fare      : ₹{booking['train']['base_fare']}")
    print(f"Total Fare     : ₹{booking['total_fare']}")
    print("-------------------------------")
    print(f"Payment Status : {booking['payment']['status']}")
    print(f"Payment Method : {booking['payment']['method']}")
    print(f"Transaction ID : {booking['payment']['transaction_id']}")
    print("================================")
    print("Thank you for booking with us!")


def main():
    print("===================================")
    print("   Simple Train Ticket Booking     ")
    print("===================================")

    # 1. Choose train
    train = choose_train()

    # 2. Get passenger details
    passenger = get_passenger_details()

    # 3. Calculate fare
    total_fare = calculate_total_fare(train["base_fare"], passenger["food_pref"])

    # 4. Show summary before payment
    print("\nBooking Summary (Before Payment):")
    print(f"Passenger: {passenger['name']}, Age: {passenger['age']}")
    print(f"Train   : {train['train_no']} - {train['name']}")
    print(f"Route   : {train['from']} -> {train['to']}")
    print(f"Seat    : {passenger['seat_pref']}")
    print(f"Food    : {passenger['food_pref']}")
    print(f"Total Fare to Pay: ₹{total_fare}")

    confirm = input("Confirm booking and proceed to payment? (y/n): ").strip().lower()
    if confirm != "y":
        print("Booking cancelled by user.")
        return

    # 5. Payment
    payment_info = mock_payment_gateway(total_fare)

    # 6. Generate PNR & final booking record
    pnr = generate_pnr()
    booking = {
        "pnr": pnr,
        "train": train,
        "passenger": passenger,
        "total_fare": total_fare,
        "payment": payment_info
    }

    # 7. Print ticket
    print_ticket(booking)


if __name__ == "__main__":
    main()
