def menu():
    main_menu = input("""
   press  1 --> To accessPhonebook
   press 2 --> To accessMessages
   press 3 -->To Chat
   press 4 --> To acess Call register
   press  5 --> Tones
   press  6 --> To access  Settings
   press 7 --> To divert call
   press 8 --> To access Games
   press  9 --> To access calculator
   press 10 --> To access Reminders
   press  11 -->To access Clock
    press 12 --> To accessProfiles
    press 12 --> To access Sim Services""")
    match main_menu:
        case "1":
           phone_book()
        case "2":
            messages()
        case "3":
            print("Chat")
        case "4":
            call_register()
        case "5":
            tones()
        case "6":
            settings()
        case "7":
            print("call divert")
        case "8":
            print("Games")
        case "9":
            print("Calcutor")
        case "10":
            print("Reminders")
        case "11":
            clock()
        case "12":
            print("Profiles")
        case "13":
            print("sim services")
        case _:
            main_menu()
def phone_book():
   phone_book = input("""
   press 1 --> To search phonebook
   press 2 --> To go Services
   press 3 --> To Add name
   press 4 --> To erase contact
   press 5 --> To edit contact
   press 6 --> To assign ringing tone
   press 7 --> To send dials
   press 8 --> To see options 
   press 9 --> To get speed dials
   press 10 --> To set voice tags""")
   match phone_book:
        case "1":
            print("Search")
        case "2":
            print("Service Nos")
        case "3":
            print(" name")
        case "4":
            print(" contact erased")
        case "5":
            print("Contact edited")
        case "6":
            print("Tone has been assigned")
        case "7":
            print(" b'card sent")
        case "8":
            options()
        case "9":
            print("Speed dials")
        case "10":
            print("Voice tags")
        case _:
            phone_book()



def options():
   options =  input("""
   press 1 --> To set type of view
   press  2-->  To seeMemory status""")

   match options:
        case "1":
            print("Type of view")
        case "2":
            print(" Your Memory status is")
        case _:
            options()
def messages():
    messages = input("""
   press 1 --> To write messages
   press 2 --> To access inbox
   press 3 --> To access outbox
   press 4 --> To add pictures to messages
   press 5 --> To access Templates
   press 6 --> To access smileys
   press 7 --> To access message settings
   press 8 --> To access info services
   press 9 --> To access Voice mailbox number
   press 10 --> To access Service command editor""")
    match messages:
        case "1":
            print(" messages")
        case "2":
            print("Inbox ")
        case "3":
            print("Outbox")
        case "4":
            print("Picture messages")
        case "5":
            print("Templates")
        case "6":
            print("Smileys")
        case "7":
            message_settings()
        case "8":
            print("Info service")
        case "9":
            print("Voice mailbox number")
        case "10":
            print("Service command editor")
        case _:
            messages()

def message_settings():
    message_settings = input("""
   press 1 --> Set1
    press 2 --> common""")
    match message_settings:
        case "1":
            set1()
        case "2":
            common3()
        case _:
            message_settings()

def set1():
    set1 = print("""
    1 --> mwssage centre number
    2 --> message sent as 
    3 message validity""")
    match set1:
        case "1":
            print("Message centre number")
        case "2":
            print("Message sent as")
        case "3":
            print("Message validity")

def common3():
    common = print("""
   press 1 --> To get delivery reports
   press 2 --> To reply via same centre
   press 3 --> To access character support""")
    match common:
        case "1":
            print("Delivery reports")
        case "2":
            print("You have replied via  same centre")
        case "3":
            print("Character support")
        case _:
            common3()


def call_register():
    call_register = input("""
   press 1 --> Missed call
   press 2 --> Received calls
   press 3 --> Dialed calls
   press 4 --> Recent call list erased
   press 5 -->  call duration
   press 6 --> Cost of your call is
   press 7 --> The cost for this call is
   press 8 -->  prepaid credit""")
    match call_register:
        case "1":
            print("Missed calls ")
        case "2":
            print("Received calls")
        case "3":
            print("Dialed calls")
        case "4":
            print("Erase recent call list ")
        case "5":
            show_call_duration()
        case "6":
            show_call_cost()
        case "7":
            call_cost_settings()
        case "8":
            print("Prepaid credit")
        case _:
            call_register()

def show_call_duration():
    call_duration = input("""
   press 1 --> lastcall duration
  press  2 -->  All calls duration
   press 3 --> Recieved calls duration
   press 4 --> Dialed calls duration
  press  5 --> Timers cleared""")
    match call_duration:
        case "1":
            print("Your last call duration is ")
        case "2":
            print("All your call duration is ")
        case "3":
            print("Your recieved  call duration is")
        case "4":
            print("Your dialed calls duration is")
        case "5":
            print("Your timers have been cleared")
        case _:
            show_call_duration()



def show_call_cost():
    call_cost = input("""
   press 1 --> To see the cost of your last call
    press 2 --> To get the cost of all your calls
    press 3--> To clear counters""")
    match call_cost:
        case "1":
            print("The cost of of your last call is")
        case "2":
            print("The cost of all your calls is")
        case "3":
            print("You have cleared all counters")
        case _:
            show_call_cost()

def call_cost_settings():
    cost_settings = input("""
    press 1 --> To set call cost limit
    press 2 --> To show cost in""")
    match cost_settings:
        case "1":
            print("Your call cost limit have been set to")
        case "2":
            print("Cost in is ")
        case _:
            call_cost_settings()


def tones():
    tones = input("""
    press 1 --> To set Your ringing tones
    press 2 --> To To increase or decrease ringing volume
    press 3 --> To set incoming alert tones
    press 4 --> To set composer tone
    press 5 --> To set message alert tone
    press 6 --> To set keypad tones
    press 7 --> To set warning and games tone
    press 8 --> To set Vibrating alert
    pres 9 --> To set screen saver""")
    match tones:
        case "1":
            print(" Ringing tone has been set to")
        case "2":
            print("volume increased")
        case "3":
            print("Incoming call alert has been set on vibration")
        case "4":
            print("Composer tone has been set to")
        case "5":
            print("Message alert tone hase been set to")
        case "6":
            print("Keypad tones has been set to")
        case "7":
            print("Warning and games alert tones has bee set to")
        case "8":
            print("vibrating alert set")
        case "9":
            print("Screen saver")
        case _:
            tones()

def settings():
    settings = input("""
    press 1 --> To get calls setting
    press 2 --> To get phone settings
    press 3 --> To get security settings
    press 3 --> To restore factory settings""")
    match settings:
        case "1":
            call_settings()
        case "2":
            phone_settings()
        case "3":
            security_settings()
        case "4":
            print("factory setting restored")
        case _:
            settings()

def call_settings():
    call_setting = input("""
    press 1 --> To set automatic redial
    press 2 --> To set speed dialing
    press 3 --> To set call waiting options
    press 4 --> To set your own number sending
    press 5 --> To set the phone line in use
    press 6 --> To set The automatic answer""")
    match call_setting:
        case "1":
            print("Your automatic redial has been set")
        case "2":
            print("Your speed dialing has been set to")
        case "3":
            print("Your call waiting option is")
        case "4":
            print("Yor number sending option is")
        case "5":
            print("The phone line in use is")
        case "6":
            print("Your automatic answer is ")
        case _:
            call_settings()


def phone_settings():
    phone_setting = input("""
    press 1 --> To set phone to the language of your choice
    press 2 --> To set phone info display
    press 3 --> To set welcome note
    press 4 --> To select network
    press 5 --> To set lights
    press 6 --> To confirm Sim service settings""")
    match phone_setting:
        case "1":
            print("Your phone language option is")
        case "2":
            print("cell info displayed")
        case "3":
            print("Wellcome note displayed")
        case "4":
            print("You have selected this network")
        case "5":
            print("Light set to")
        case "6":
            print("sim services action")
        case _:
            phone_settings()

def security_settings():
    security_setting = input("""
    press 1 --> To set pin code request
    press 2 --> To set call barring service
    press 3 --> To set Fixed dialing
    press 4 --> To set closed user group
    press 5 --> To set Phone security
    press 6 --> To change access codes""")
    match security_setting:
        case "1":
            print("pin code request has been set ")
        case "2":
            print("Call barring service has bee set")
        case "3":
            print("Fixed dialing set")
        case "4":
            print("Closed user group set")
        case "5":
            print("Phone securty has been set to")
        case "6":
            print("Access code has been changed to")
        case _:
            security_settings()


def clock():
    clock = input("""
    press 1 --> To set Alarm clock
    press 2 --> To set clock
    press 3 --> To set date
    press 4 --> For Stopwatch
    press 5 --> To set countdown timer
    press 5 --> For auto update of date and time""")
    match clock:
        case "1":
            print("Alarm have been set to")
        case "2":
            print("Clock has been set")
        case "3":
            print("Date has been set")
        case "4":
            print("Stopwatch")
        case "5":
            print("Countdown timer has began")
        case "6":
            print("Auto update of date and time")
        case _:
            clock()


if __name__ == "__main__":
    menu()