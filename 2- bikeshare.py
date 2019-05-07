import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities = set(city.lower() for city in ("Chicago", "New York", "Washington"))
    
    while True:
        city = input("Which City?")
        if city.lower() in cities: 
            break 
        print("Sorry, didn't recognize your answer, try again")
      
            
    
    
    # get user input for month (all, january, february, ... , june)
    months = set(month.lower() for month in ("all", "January", "February", "March", "April", "May", "June"))
                                           
    while True:
        month = input("Which Month?")
        if month.lower() in months: 
            break
        print("Sorry, didn't recognize your answer, try again")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = set(day.lower() for day in ("All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
   
               
    while True:
        day = input("which day? or all day?")
        if day.lower() in days:
            break
        print("sorry kindly try again")                   
               
    
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
    

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
  

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # produce a column called month and weekday
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name    
    
    # produce a column called hour
    df['hour']=df['Start Time'].dt.hour
    
   
    if month !='all':
         months = ['january', 'february', 'march', 'april', 'may', 'june']
         month = months.index(month) + 1
         df = df[df['month'] == month]     
 
    
    if day !='all':
        df=df[df['day']==day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df["month"].mode()[0]
    print("the most common month is:", most_common_month)
    
    # display the most common day of week
    common_day = df["day"].mode()[0]
    print("Them most common day is:",common_day)

    # display the most common start hour
    common_hour = df["hour"].mode()[0]
    print("the most common hour is:" ,common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    com_start = df["Start Station"].mode()[0]
    print("the most common start is:" ,com_start)

    # display most commonly used end station
    com_end = df["End Station"].mode()[0]
    print("the most common end is:",com_end)

    # display most frequent combination of start station and end station trip
    com_combi = df["End Station"] + df["Start Station"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df["Trip Duration"].sum()
    print ("the total travel time is:", travel_time)

    # display mean travel time
    mean_time = df["Trip Duration"].mean()
    print ("the mean travel time is:", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df["User Type"].value_counts()
    print("there are so many users:", count_user)

    # Display counts of gender
    try:
        print('The counts of gender are:', df['Gender'].value_counts())
    except KeyError:
        print('No information in the washington list')
        pass
    
    try:
        print ("early birth is:", df["Birth Year"].max())
    except KeyError:
        print('No information in the washington list')
        pass    
    
    try:
        print ("the most recent birth is:", df["Birth Year"].min())
    except KeyError:
        print('No information in the washington list')
        pass   
    
    try:
        print ("the most common birth is:", df["Birth Year"].mode()[0])
    except KeyError:
        print('No information in the washington list')
        pass   

    # Display earliest, most recent, and most common year of birth
    # early_birth = df["Birth Year"].max()
    # recent_birth = df["Birth Year"].min()
    # common_birth = df["Birth Year"].mode()[0]
    # print (" early birth, recent birth, common birth is:", early_birth, recent_birth, common_birth)
     
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def display(df):
    ## show raw data on the screen. every time 5 lines. 
    n = 5    
    while True:
        raw = input("do you wish to see 5 lines more of raw data?")
        if raw.lower() =="yes":
            n += 5
            print(df.iloc[n-5: n,  : ])
            True
        else:
             break 


    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()