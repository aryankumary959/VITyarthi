Train Ticket Booking System
Description
This Python project is a simple console application for booking train tickets. Users can choose trains, enter passenger details, select seat and food preferences, and simulate payment to receive a formatted e-ticket. The code is meant for beginners or anyone who wants to understand interactive CLI programs in Python.

Table of Contents
Features:

1)Requirements

2)Installation

3)Usage

4)Examples

5)Customization

6)Roadmap

7)Credits

8)Support

Features
Choose a train from a pre-set list.

Input passenger name, age.

Select seat preference: Lower, Middle, Upper, Side Lower, Side Upper.

Select food preference: Veg, Non-Veg, No Food. Extra charge for meal.

Simulated payment (UPI, Credit Card, Debit Card, Net Banking).

Generates a random PNR and fake transaction ID.

Prints all details in a clear e-ticket format.

Requirements
Python 3.7 or newer

No additional Python modules required

Installation
Download or copy train_booking.py to your computer.

Make sure you have Python installed:

text
python --version
No external dependencies needed.

Usage
Open your terminal and navigate to the script location.

Run:

text
python train_booking.py
Follow the prompts:

Select a train by its number.

Enter your name and age.

Choose your seat and food preference.

Confirm and complete payment.

View your e-ticket details in the terminal.

Examples
Enter your name ("Rita Sharma") and age ("28").

Choose "Express B" (12002: Delhi → Jaipur).

Pick "Upper Berth" and "Non-Veg" as preferences.

Pay using "Debit Card".

See auto-generated PNR and transaction receipt.

Customization
To add more trains, edit the AVAILABLE_TRAINS list in the script.

Change seat or food options by updating SEAT_PREFERENCES and FOOD_PREFERENCES.

Extend payment simulation or integrate actual payment APIs for advanced versions.

For multiple passengers, modify the passenger input section to accept lists.

Roadmap
Support for multi-passenger bookings.

Persist bookings to a file or database.

Booking cancellation and PNR search.

GUI or web-based front-end (Tkinter, Flask/Django).

Credits
Developed by [ARYAN KUMAR YADAV].
Inspired by Python CLI project tutorials and beginner-level coding guides.

**SCREENSHOTS**
<img width="663" height="1014" alt="image" src="https://github.com/user-attachments/assets/52f64a67-b1f6-4d0f-aeaa-74e761e62915" />
<img width="565" height="713" alt="image" src="https://github.com/user-attachments/assets/05bd7b79-c38c-4ba0-8b07-5047f9eac9b3" />
