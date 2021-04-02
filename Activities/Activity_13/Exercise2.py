want_to_continue = True
while want_to_continue:
    ticket_number = input("Enter the 6 digit ticket number: ")
    if len(ticket_number) != 6:
        print(f"{ticket_number}; is an invalid ticket number")
    else:
        mod_ticket_number = int(ticket_number[:-1])
        remainder = mod_ticket_number % 7
        if remainder == int(ticket_number[-1]):
            with open("tickets.txt", 'a') as f:
                with open("tickets.txt") as ff:
                    if str(ticket_number) in ff.read():
                        print(f"{ticket_number}; is a valid ticket number and already present in file")
                    else:
                        f.write(f"{ticket_number} ; is a valid ticket number\n")
                        print(f"{ticket_number}; is a valid ticket number")
        else:
            print(f"{ticket_number}; is an invalid ticket number")
    status = input("\nDo you want to continue?(Y/N) ")
    if status.lower() != "y":
        want_to_continue = False
