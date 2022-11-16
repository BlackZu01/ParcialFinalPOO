from package.parkingLot import ParkingLot
from package.auto import Auto 
from package.user import User
#  ================== How the program works? ==================

#                       [+] OPTION MENU [+]
#   How long are you going to leave your car in the parking lot?
#   1) Days
#   2) Hours
#   3) Minutes

# I created four differente user with
first_user = User(option=2, time_standing=10, car=Auto('compact'))
second_user = User(option=3, time_standing=12, car=Auto('Compact'))  # The program works even if the car 
third_user = User(option=2, time_standing=7, car=Auto('Van'))        # type was initialized with the first capital letter
fourth_user = User(option=1, time_standing=5, car=Auto('Suv'))     

usuario = User(option=1, time_standing=20, car=Auto('Van'))
usuario2 = User(option=1, time_standing=20, car=Auto('Van'))

# We instantiate the parking class
parking_state = ParkingLot()
parking_state.generateParking()

print(f'User\'s 1 bill: {parking_state.check_bill(first_user)}')
print(f'User\'s 2 bill: {parking_state.check_bill(second_user)}')
print(f'User\'s 3 bill: {parking_state.check_bill(third_user)}')
print(f'User\'s 4 bill: {parking_state.check_bill(fourth_user)}')

parking_state.assignParking(first_user, True)
parking_state.assignParking(second_user, False)
parking_state.assignParking(third_user, False)
parking_state.assignParking(fourth_user, False)

parking_state.showParkingLot()

# To see how many space are left for every kind of car (Compact, SUV, Van)
parking_state.keepTracks()