class Garage:
    def __init__(self, tickets=[], parking_spaces = [], current_Ticket = {'paid': False}, user_choice = []):  
        self.user_choice = user_choice
        self.tickets = tickets 
        self.parking_spaces = parking_spaces                                     #Adrian, Buhay, Robin collective effort
        self.current_Ticket = current_Ticket

    def take_Ticket(self):                                                       #Adrian + Buhay = Navigator!! Robin was driver!
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
            

            
    def pay_4_parking(self):                                                             #Robin
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

    def leave_garage(self):                                                                #Buhay
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

    def run_Garage(self):                                                                 #Adrian
        self.take_Ticket()
        if self.user_choice == ['Y']:
            print('running pay 4 parking\n')
            self.pay_4_parking()
            print('running leave garage.')
            self.leave_garage()
        else:
            print("didn't pay, not running either method.")

parking = Garage()
parking.run_Garage()