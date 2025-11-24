# Project Statement: Train Ticket Booking System in Python

## Objective

Develop a simple **train ticket booking system** using Python that runs in the command line.  
The system should collect passenger details, allow selection of train, seat, and food preferences, and simulate a payment process before generating an e-ticket.

## Functional Requirements

1. **Train Selection**
   - The system must maintain a small, predefined list of trains.
   - Each train should have:
     - Train number
     - Train name
     - Source station
     - Destination station
     - Base fare

2. **Passenger Details Input**
   - The system must ask the user for:
     - Passenger name
     - Passenger age
   - Basic validation should be applied (e.g., age must be a positive number).

3. **Seat Preference**
   - The user should be able to select a seat preference from a list such as:
     - Lower
     - Middle
     - Upper
     - Side Lower
     - Side Upper

4. **Food Preference**
   - The user should be able to select a food preference from a list such as:
     - Veg
     - Non-Veg
     - No Food
   - If Veg/Non-Veg is selected, an extra food charge is added to the total fare.

5. **Fare Calculation**
   - The system should calculate the total fare as:
     - `Total Fare = Base Fare + Food Charge (if any)`

6. **Payment Gateway (Mock)**
   - The system should simulate a payment gateway.
   - The user must:
     - Choose a payment method (UPI, Credit Card, Debit Card, Net Banking).
   - The payment should always succeed in this simple project.
   - A fake transaction ID should be generated.

7. **Ticket Generation**
   - After payment is successful:
     - A unique PNR number must be generated.
     - A ticket should be displayed with:
       - PNR
       - Passenger details
       - Train details
       - Seat preference
       - Food preference
       - Fare details
       - Payment status, method, and transaction ID

## Non-Functional Requirements

- The interface should be simple and text-based (command line).
- Code should be readable and structured using functions.
- No external frameworks are required.

## Scope for Enhancement

- Add multiple passengers in a single booking.
- Persist data in files or a database.
- Implement booking cancellation and PNR search.
- Add seat availability and coach allocation logic.
- Build a GUI or web-based front end on top of this logic.
