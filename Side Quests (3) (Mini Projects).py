# I'm creating a day calculator


def day_calculator():
    while True:

        current_day = input("What's the day today? ")
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

        ccurrent_day = current_day.capitalize()
        if ccurrent_day in days:
            required_day = input("How days before or after do you want the day? ")
            try:
                required_day = int(required_day)
            except ValueError:
                print("That's not a number. Please try again!")

            cd = days.index(ccurrent_day)
            ncd = cd + 1

            if required_day <= 7:
                result_day = ncd + required_day
                if result_day == 1:
                    print("It'll be Monday! ")
                if result_day == 2:
                    print("It'll be Tuesday! ")
                if result_day == 3:
                    print("It'll be Wednesday! ")
                if result_day == 4:
                    print("It'll be Thursday! ")
                if result_day == 5:
                    print("It'll be Friday! ")
                if result_day == 6:
                    print("It'll be Saturday! ")
                if result_day == 7:
                    print("It'll be Sunday! ")

            elif required_day > 7:

                result_day = ncd + required_day
                gresult_day = result_day % 7

                if gresult_day == 1:
                    print("It'll be Monday! ")
                if gresult_day == 2:
                    print("It'll be Tuesday! ")
                if gresult_day == 3:
                    print("It'll be Wednesday! ")
                if gresult_day == 4:
                    print("It'll be Thursday! ")
                if gresult_day == 5:
                    print("It'll be Friday! ")
                if gresult_day == 6:
                    print("It'll be Saturday! ")
                if gresult_day == 0:
                    print(f"It'll be {ccurrent_day}! ")
            break

        elif ccurrent_day not in days:
            print("You've entered an incorrect day. It may be a spell error. ")
            print("Please try again by entering any of the 7 days of the week properly!")


day_calculator()
