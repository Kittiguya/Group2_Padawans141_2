class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        pass  # Initialize Car properties

class Spot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        pass  # Initialize Spot properties

    def park_car(self, car):
        self.car = car
        pass  # Logic to park a car in the spot

    def remove_car(self):                                                   #dont touch this yet. 
        pass  # Logic to remove a car from the spot

class Ticket:
    def __init__(self, car, spot):
        self.car = car
        self.spot = spot
        pass  # Initialize Ticket properties

class Garage:
    def __init__(self, tickets=[], parking_spaces = [], current_Ticket = {'paid': False}, user_choice = []):
        self.user_choice = user_choice
        self.tickets = tickets 
        self.parking_spaces = parking_spaces
        self.current_Ticket = current_Ticket
        #self.capacity = capacity
        pass  # Initialize Garage properties
        #test

    def take_Ticket(self):        
        while True:
            ticket_amount = 10
            parking_spaces = 10
            user_inp = input('Are you parking with us today? Type Y for yes, N for no ').upper()
            if user_inp == 'Y': 
                self.tickets = [ticket_amount -1]
                self.parking_spaces = [ticket_amount -1]
                print(f'Thanks for parking with us! {self.tickets} out {ticket_amount} tickets remaining! {self.parking_spaces} out of {parking_spaces} spaces remaining!')
                self.user_choice = ['Y']
                break
            elif user_inp == 'N':
                print('Please Leave now!')
                break
            else:
                print('Please input Y for yes, N for no to continue!')
            

            
    def pay_4_parking(self):
        while True:
            user_list = []
            user_amount = input('How much are you paying for this ticket?')
            user_list.append(user_amount)
            if not user_amount:
                print('Please enter a value to pay next time!')
            else:
                print(f'Your ticket has been paid! You only have 15 minutes!')
                self.current_Ticket['paid']=True
                break
            pass

    def leave_garage(self):
        current_Tickets = 9
        current_Spaces = 9
        if self.current_Ticket['paid']==True:
            print('Your 15 minutes are up! Thank you! Have a nice day!!')
        else: 
            user_amount = input('How much are you paying for this ticket? ')
            print('Thank you! Have a nice day!!')
            self.tickets = [current_Tickets +1]
            self.parking_spaces = [current_Spaces +1]
            print(f'{self.tickets} tickets and {self.parking_spaces} parking spaces')

    def park_car(self, car):
        pass  # Logic to park a car in the garage

    def retrieve_car(self, ticket):
        pass  # Logic to retrieve a car from the garage

    def run_Garage(self):
        self.take_Ticket()
        if self.user_choice == ['Y']:
            print('running pay 4 parking\n')
            self.pay_4_parking()
            print('running leave garage.')
            self.leave_garage()
        else:
            print("didn't pay, not running either method.")


def main():
    pass  # Runner code to interact with the parking lot system

parking = Garage()
# parking.take_Ticket()
# parking.leave_garage()
#parking.pay_4_parking()
#print('Switching method to leave garage')5

parking.run_Garage()

if __name__ == "__main__":
    main()