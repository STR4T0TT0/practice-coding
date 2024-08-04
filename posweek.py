import datetime

#returns current year with the current week number
def get_current_week_number():
    today = datetime.date.today()
    week_number = today.isocalendar()[1]
    return week_number, today.year

# MonitoringPeriod sets the range of days before and after the current date
def print_ascii_calendar(monitoring_period):
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=monitoring_period)
    end_date = today + datetime.timedelta(days=monitoring_period)

    days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    current_date = start_date

    # Build the top of the table
    print("The current day is marked with an X:")
    print("╔═════╦═════╦═════╦═════╦═════╦═════╦═════╗")
    print("║ " + " ║ ".join(days_of_week) + " ║")
    print("╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣")

    # Calendar body
    week_str = "║"
    while current_date <= end_date:
        if current_date == today:
            day_str = " X "
        else:
            day_str = current_date.strftime("%d")
        
        week_str += f" {day_str: <3} ║"
        if current_date.weekday() == 6:  # End of the week
            print(week_str)
            print("╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣")
            week_str = "║"
        current_date += datetime.timedelta(days=1)

    # Fill the last week if it wasn't complete
    # and close the table
    if current_date.weekday() != 0:
        while current_date.weekday() != 0:
            week_str += "     ║"
            current_date += datetime.timedelta(days=1)
        print(week_str)
        print("╚═════╩═════╩═════╩═════╩═════╩═════╩═════╝")

if __name__ == "__main__":
    MonitoringPeriod = 13  # Set monitoring period
    week_number, year = get_current_week_number()
    print(f"Current week number: {week_number} ({year})")
    print_ascii_calendar(MonitoringPeriod)