from tabulate import tabulate
import time


class HairAppScheduler(object):
    '''The program prompts for user input. It accepts 3 command types:
        1. List: listing of all appointments
        2. Schedule: schedules a new hair appointment
        3. Exit: the hairdresser is done with the program;
        upon exit, all existing state will be
        destroyed (i.e. the program does not persist
        the appointments in between program runs)'''

    def __init__(self):
        '''Set object variables'''
        self.schedule = {}
        self.client = []
        self.appointime_times = []
        self.headers = ['Name', 'Phone', 'Type', 'Time']

        # Accepts user command and will continue running until user exits 
        while True:
            self.display_instructions()
            command = input('>> Type a command: ')
            if command == 'exit':
                print('\n--> Closed Hair Appointment Scheduler \n')
                break
            elif command:
                self.process_command(command)
            else:
                self.display_instructions()
                input('>> Type a command: ')

    def display_instructions(self):
        '''Displays list of command explanation'''
        print('\n ------------------- ')
        print(' Commands Available:')
        print(' ------------------- ')
        print(' list -- show a list of all appointments')
        print(' schedule -- schedule a new appointment')
        print(' exit -- exit the scheduler \n')

    def process_command(self, command):
        '''Calls next function based on user input'''
        if command == 'list':
            self.list_all_appointments()
        elif command == 'schedule':
            self.add_new_appointment()
        else:
            return

    def list_all_appointments(self):
        '''Displays table of scheduled appointments'''
        if not self.schedule:
            print('\n--> There are no appointments scheduled.')
            return
        else:
            print('\n')
            print(tabulate([[k, ] + v for k, v in self.schedule.items()],
                  headers=self.headers))
            return

    def add_new_appointment(self):
        '''Collects input infomation and save to lists '''
        if self.client:
            self.client = []
        # Get client name, can be anything no limits
        client_name = input('>> Enter Client\'s Full Name: ')
        self.client.append(client_name)
        # Get client phone number
        client_contact = self.get_phone_number()
        self.client.append(client_contact)
        # Get appointment type, cut or shampoo and cut 
        appt_type = self.appointment_type()
        self.client.append(appt_type)
        # Get appointment time and adds appointment time to all appointment list
        appt_time = self.appointime_time()  
        self.appointime_times.append(appt_time)
        self.client.append(appt_time)
        # Add user to scheduled list
        self.schedule[self.client[0]] = self.client[1::]
        print(f'\n-->Added {self.client[0]} to the schedule')

    def get_phone_number(self):
        '''Get phone number from user and check if valid format'''
        while True:
            client_phone = input('>> Enter Phone Number (ie 4155555555): ')
            if len(client_phone) == 10 and client_phone.isdigit():
                return client_phone
            else:
                print(f'\n --> {client_phone} is not a valid phone numer')

    def appointment_type(self):
        '''Get appointment type from user'''
        while True:
            print('\n What kind of appointment? (Type a or b)')
            print(' --------------------------------------- ')
            print('   a) Haircut (30 mins) \n   b) Shampoo & Haircut (1 hr) \n')
            appt_type = input('>> Select an option (i.e. a): ')
            if appt_type == 'a':
                return 'Haircu† (30 mins)'
            elif appt_type == 'b':
                return 'Shampoo & Haircut (1 hr)'
            else:
                print(f'\n--> {appt_type} is not a valid response')

    def appointime_time(self):
        '''Get appointment time from user and check if valid format'''
        valid_minutes = ['00', '15', '30', '45']
        while True:
            print('\n--> Scheduled time can only be 00, 15, 30 or 45 minutes (i.e 10:15AM, 01:30PM)')
            appt_time = input('>> Enter appointment time HH:MM (AM/PM): ')

            valid_time = self.valid_time_format(appt_time)
            avail_time = self.is_time_available(appt_time)
            check_mins = None

            if valid_time:
                check_mins = appt_time[3] + appt_time[4]
            if check_mins in valid_minutes and valid_time and avail_time:
                return appt_time
            elif not avail_time: 
                print(f'\n--> {appt_time} is not available')
            else:
                print(f'\n--> {appt_time} is not a valid time')

    def is_time_available(self, desired_time):
        '''Boolean, check if appointment time is available'''
        if desired_time in self.appointime_times:
            return False
        else:
            return True

    def valid_time_format(self, input_time):
        '''Boolean, check if time format is valid'''
        try:
            time.strptime(input_time, '%H:%M%p')
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    HairAppScheduler()