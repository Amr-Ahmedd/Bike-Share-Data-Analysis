import time
import pandas as pd
import numpy as np

def get_filters () :
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    while(True) :
        try:
            # get user input for city (chicago, new york city, washington). 
            input_city=input("specify which city do you want (Chicago,New york,Washington)\n")
            if input_city.lower() == 'chicago':
                break
            elif input_city.lower() == 'new york':
                break
            elif input_city.lower() == 'washington':
                break
            else :
                print("invalid data please check name of the city")
        except:
           print("sorry your input is wrong")
    # get user input for month (all, january, february, ... , june)            
    while(True):
            input_month=input("determine month of filteration (january,february,March,April,May,june) or 'all' for all months\n").lower()
            months = ['january','february','march','april','may','june']
            if input_month == 'all' or input_month in months :
                break
            else :
                print("invalid data please check name of the month")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):        
            input_day=input("determine day of filteration (Friday,Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday) or 'all' for all days\n").lower()
            days = ['friday','saturday','sunday','monday','tuesday','wednesday','thursday']
            if input_day == 'all' or input_day in days :
                break
            else :
                print("invalid data please check name of the day")

    print('-'*40)
    return input_city,input_month,input_day


def load_data(input_city,input_month,input_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # open excel sheet
    if input_city.lower() == 'chicago':
        df= pd.read_csv('chicago.csv')
    elif input_city.lower() == 'new york':
        df= pd.read_csv('new_york_city.csv')
    elif input_city.lower() == 'washington':
        df= pd.read_csv('washington.csv')


      # convert the Start Time and End time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # creating new columns 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filtering by month
    if input_month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        input_month = months.index(input_month) + 1    
        df = df[df['month'] == input_month]

    # filter by day 
    if input_day != 'all':
        df = df[df['day_of_week'] == input_day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    if common_month == 1 :
        print("The most common month is : January")
    if common_month == 2 :
        print("The most common month is : February")
    if common_month == 3 :
        print("The most common month is : March")
    if common_month == 4 :
        print("The most common month is : April")
    if common_month == 5 :
        print("The most common month is : May")
    if common_month == 6 :
        print("The most common month is : June")

    # display the most common day of week
    print("The most common day is : ",df['day_of_week'].mode()[0])

    # display the most common start hour
    print("The most common hour is : ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly used Start Station is : ",df['Start Station'].mode()[0])

    # display most commonly used end station
    print("most commonly used End Station is : ",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Common Station']=df['Start Station']+" - "+df['End Station']
    print("most commonly used combined station : ",df['Common Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    #time_in_hours=((df['Trip Duration'].sum())/60*60)
    print("Total travel time: ",df['Trip Duration'].sum(),"seconds")

    # display mean travel time
    print("Average travel time: ",df['Trip Duration'].mean(),"seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,input_city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print("Total users is :\n",df['User Type'].value_counts(),"\n")

    # if condtion to filter washington from counts of gender and date of birth 
    if input_city.lower()!='washington':
        # Display counts of gender 
        print("Number of gender is:\n",df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is: ',df['Birth Year'].min())
        print('The most recent year of birth is: ',df['Birth Year'].max())
        print('The most common year of birth is: ',df['Birth Year'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_head_of_data(df):
    '''Displaying 5 rows of data and ask the user if he want to see the next 5 rows'''

    answer=input("would you like to see the first 5 rows of filteration data: ")
    start_row = 0
    while(True):
        if answer.lower()== 'yes':
            print(df.iloc[start_row:start_row + 5])
            start_row=5+start_row
            answer=input("would you like to see the next 5 rows? type 'yes' to see next 5 rows or 'no' to exit: ")
        elif answer.lower()=='no':
                break
        else :
            answer=input("invalid input please type 'yes' or 'no': ").lower()

def main():
    while True:
        input_city,input_month,input_day = get_filters()
        df = load_data(input_city,input_month,input_day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,input_city)
        display_head_of_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Glad to serve you")
            break

if __name__ == "__main__":
	main()