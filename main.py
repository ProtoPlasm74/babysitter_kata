def main():
    start_time = starting_hour_input()
    end_time = ending_hour_input()
    total_payment = babysitter_payment_calculator(
        starting_hour=start_time, ending_hour=end_time)
    hours_worked = end_time - start_time
    print("You have worked a total of " + str(hours_worked) +
          " hours, and were payed $" + str(total_payment))


def starting_hour_input():
    while True:
        starting_hour = int(input("At what hour did you start babysitting? "))
        if starting_hour in range(5, 10):
            starting_hour -= 5
            return starting_hour
        else:
            print("Enter a time between 5pm and 9pm as an integer")


def ending_hour_input():
    while True:
        ending_hour = int(input("At what hour did you end babysitting? "))
        if ending_hour in range(1, 5):
            ending_hour += 12
        if ending_hour in range(9, 17):
            ending_hour -= 5
            return ending_hour
        else:
            print("Enter a time between 9pm and 4am as an integer")


def babysitter_payment_calculator(starting_hour, ending_hour):
    total_payment = 0
    for hour in range(starting_hour, ending_hour):
        if hour in range(0, 4):
            total_payment += 12
        if hour in range(4, 7):
            total_payment += 8
        if hour in range(7, 11):
            total_payment += 16
    return total_payment


if __name__ == "__main__":
    main()
