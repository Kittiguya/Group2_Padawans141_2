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
    def __init__(self, tickets=[], parking_spaces = [], current_Ticket = {'paid': False}):
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
                break
            elif user_inp == 'N':
                print('Please Leave now! Have a nice day!')
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
                print(f'Your ticket has been paid! You only have 15 minutes! {user_list}')
                self.current_Ticket['paid']=True
                print(f'{self.current_Ticket}')
                break
            #if amount_paid == 5
            pass

    def leave_garage(self):
        current_Tickets = 9
        current_Spaces = 9
        if self.current_Ticket['paid']==True:
            print('Thank you! Have a nice day!!')
        else: 
            user_amount = input('How much are you paying for this ticket?')
            print('Thank you! Have a nice day!!')
            self.tickets = [current_Tickets +1]
            self.parking_spaces = [current_Spaces +1]
            print(f'{self.tickets} tickets and {self.parking_spaces} parking spaces')

    def park_car(self, car):
        pass  # Logic to park a car in the garage

    def retrieve_car(self, ticket):
        pass  # Logic to retrieve a car from the garage

def main():
    pass  # Runner code to interact with the parking lot system

parking = Garage()
parking.take_Ticket()
parking.leave_garage()
#parking.pay_4_parking()
#print('Switching method to leave garage')5

if __name__ == "__main__":
    main()




############ Buhay's Pull Request #################################
## Please test out the code below. Not sure how to inject my additions/changes for the first repo for this new repo without getting dizzy; my bad! =/ #
## Will check again mañana! ##
    

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary
    
class Garage:
    def __init__(self, tickets = 10, parking_spaces = 10):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}
        

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
        
    def take_ticket(self):        
        while True:
            user_inp = input('Are you parking with us today? Type Y for yes, N for no ').upper()
            if user_inp == 'Y': 
                tickets = self.tickets - 1
                spaces = self.parking_spaces - 1
                print(f'Thanks for parking with us! {tickets} out {self.tickets} tickets remaining! {spaces} out of {self.parking_spaces} spaces remaining!')
                break
            elif user_inp == 'N':
                print('Please Leave now!')
                break
            else:
                print('Please input Y for yes, N for no to continue!')

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True  
                        
    def pay_4_parking(self):
        paid = input("Enter '5' to pay for parking. ")
        if paid == '5':
            print("Thank you for your payment. You have 15 minutes to park.")
            self.current_ticket[paid] = True
            print(self.current_ticket)
        else:
            print("Please pay to park or leave.")

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)
            
    def leave_garage(self):
            tickets = self.tickets + 1
            spaces = self.parking_spaces + 1
            print(f"Upon exit, the garage now has {self.tickets} tickets and {self.parking_spaces} spaces.")
            print("Thank you for parking. Have a nice day!") 


    def run_garage(self):
        self.take_ticket()
        self.pay_4_parking()
        


parking = Garage()
parking.run_garage()
parking.leave_garage()

