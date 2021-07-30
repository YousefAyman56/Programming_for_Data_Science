import pandas as pd
import datetime as datetime
import numpy as np
import time
from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True : 
        city = input("please choose a city you would like to see data for Chicago , New york city , Washington :  \n").lower()
    
        if city not in CITY_DATA :
            print("You choose the wrong city !\n")
            
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True : 
        month = input("Please enter the month you want to filter by 'eg : january,february,.....june' or you can enter 'all' to display all months  \n").lower()
    
        if month != 'all' and month not in months:
            print("invalid input The month is wrong retry again please !")
        else:
            break
        


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True : 
        day = input("which day you want filter by or you can enter 'all' to display all days 'PLEASE WRITE THE FULL VALID DAY NAME' :  \n" ).lower()
    
        if day != 'all' and day not in days:
            print("invalid input The day is not correct retry again please !")
        else:
            break

    print('-'*40)
    # Display The answers
    print("Dear user, Here is your submiited answers \n ")
    print (tabulate([[city , month , day]] , headers=["City", "Month", "Day"]))
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all' :
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != "all" :
        df = df[df['day_of_week'] == day.title()]
    
    return df



def display_data(df):
    '''
    Display a rows of data according to the user repond

    Args: pd.set_option()
    
    '''
    pd.set_option('expand_frame_repr', False)
    count = 0 
    ans = input('would you like to check the first 5 rows of data "yes/no" \n').lower()
    
    while ans != "no" and ans != "yes" :
            print("error input! please retry again\n")
            ans = input('would you like to check the first 5 rows of data "yes/no" \n').lower()
            if ans == "no" or ans == "yes" :
                break
            
    while True : 

        if ans == 'yes':
            print(df[count:count+5])
            print("\n")
            ans = input('would you like to check another 5 rows of data "yes/no" \n').lower()
            print("\n")
            count += 5
        else:
            break


           
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", months[most_common_month - 1])

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


   
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f"The most common popular trip is : {popular_trip.mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_travel_time.days
    hours = (total_travel_time.seconds)//(60*60)
    minutes = (total_travel_time.seconds)%(60*60) //60
    seconds = (total_travel_time.seconds)%(60*60) %60
    
    print("The Total Travel Time is :\n")
    print(tabulate([[days , hours , minutes , seconds ]] , headers=["days" , "hours" , "minutes" , "seconds"]))
    print("\n")
    
    
    # display mean travel time
    mean_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = mean_travel_time.days
    hours = (mean_travel_time.seconds)//(60*60)
    minutes = (mean_travel_time.seconds)%(60*60) //60
    seconds = (mean_travel_time.seconds)%(60*60) %60
    
    print("The average Travel Time is :\n")
    print(tabulate([[days , hours , minutes , seconds ]] , headers=["days" , "hours" , "minutes" , "seconds"]))
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_counts = df['User Type'].value_counts()
    print(f"The counts of user types is :\n{user_counts}\n")

    # Display counts of gender
    if 'Gender' in df : 
        gender = df['Gender'].value_counts()
        print("The count of male and female gender is \n")
        print(tabulate([[gender[0] , gender[1]]] , headers=["Male" , "Female"]))
        print("\n")
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df :
        earliest_birth = round(df['Birth Year'].min())
        most_recent_birth = round(df['Birth Year'].max())
        most_common_birth = round(df['Birth Year'].mode()[0])
        print('Earliest birth  is: {}\n'.format(earliest_birth))
        print('Most recent birth  is: {}\n'.format(most_recent_birth))
        print('Most common birth is : {}\n'.format(most_common_birth) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        while restart.lower() != "no" and restart.lower() != "yes" :
            print("error input! please retry again\n")
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == "no" or restart.lower() == "yes" :
                break
            
        if restart.lower() != "yes" :
            break



if __name__ == "__main__":
	main()
