import time

name = input('What is your name: ')
age = int(input('How old are you: '))
should_continue = True
name_output = "Твоето име е {}" 
clock_out = "Точното време е {}" 
age_out = "Ти си на {}" 
time_out = "Няма такова меню"
isOwner = False
timestamp_dict = {} 
def set_timestamp(choose):
     timestamp_dict[choose] = time.strftime("%H:%M:%S")
          

def print_each_letter(name):
    for letter in name:
        print(letter)

def print_info():
    print('1 е колко е часа')
    print('2 какво ми е името')
    print('3 на колко съм години')
    print('4 за изход')

while should_continue:
    print_info()  
    choose = int(input('Избери опция от 1 до 3: '))
    set_timestamp(choose) 
    match choose:
        case 1:
            current_time = time.strftime("%H:%M:%S")
            print(clock_out.format(current_time))
        case 2:
            name_string = name_output.format(name)
            isOwner = "Dilyan" in name_string
            if not isOwner:
                print('Ei pedal kuv si ti e? ')    
                print_each_letter(name)
        case 3:
            print(age_out.format(age))
        case 4:           
            should_continue = False
            print(timestamp_dict)
        case _:
            print(time_out)

           
            







