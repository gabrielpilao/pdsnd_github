import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
list_of_options = ['month', 'weekday', 'both', 'none']

list_of_options2 = [1, 2, 3, 4, 5, 6]

list_of_options3 = ['monday', 'tuesday', 'wednesdey', 'thursday', 'friday']


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Which city would you like to see data from?').lower()
        if city in CITY_DATA:
            break
        else:
            print('I\'m sorry, we don\'t have the data for this city,'
                  'please select one of the following:'
                  '\n chicago\n new york city\n washington')
            continue

    while True:
        option = input('Ok, would you like to filter you data by month,'
                       'weekday, both or none?').lower()
        if option in list_of_options:
            break
        else:
            print('I\'m sorry, this is not a valid option please select either'
                  ':month, weekday, both or none')
            continue

    if option == 'both':
        while True:
            try:
                month = int(input('Okay. Now, from which month would you'
                                  'like your data? (please give it as an'
                                  'integer. Ex:3'))
                break
            except (ValueError, TypeError):
                        print('I\'m sorry, this is not a valid option please'
                              'select one of the following: 1,2,3,4,5,6')
                        continue
            if month in list_of_options2:
                break
            else:
                print('I\'m sorry, this is not a valid option please'
                      'select one of the following: 1,2,3,4,5,6')
                continue

        while True:
            try:
                weekday = input('And which day of the week?').lower()
                break
            except (ValueError, TypeError):
                print('I\'m sorry, this is not a valid option please'
                      'select a valid week day')
                continue
            if weekday in list_of_options3:
                break
            else:
                print('I\'m sorry, this is not a valid option'
                      'please select a valid week day')

    elif option == 'month':
        while True:
            try:
                month = int(input('Okay. Now, from which month would you'
                                  'like your data? (please give it as an'
                                  'integer. Ex:3'))
                weekday = 'none'
                break
            except (ValueError, TypeError):
                print('I\'m sorry, this is not a valid option please'
                      'select one of the following: 1,2,3,4,5,6')
                continue
            if month in list_of_options2:
                break
            else:
                print('I\'m sorry, this is not a valid option please'
                      'select one of the following: 1,2,3,4,5,6')
            continue

    elif option == 'weekday':
        while True:
            try:
                weekday = input('And which day of the week?').lower()
                month = 'none'
                break
            except (ValueError, TypeError):
                print('I\'m sorry, this is not a valid option'
                      'please select a valid week day')
            if weekday in list_of_options3:
                break
            else:
                print('I\'m sorry, this is not a valid option'
                      'please select a valid week day')
                continue

    elif option == 'none':
        month = 'none'
        weekday = 'none'

    print('-' * 40)
    return city, month, weekday


def load_data(city, month, weekday):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'none':
        df = df[df['month'] == int(month)]
    if weekday != 'none':
        df = df[df['day_of_week'] == weekday.title()]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print('The most popular month to travel is {}'.format(popular_month))

    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most popular week day to travel is {}'
          .format(popular_day_of_week))

    popular_start_hour = df['hour'].mode()[0]
    print('The most popular hour to travel is {}'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    return popular_month, popular_day_of_week, popular_start_hour


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_st_station = df['Start Station'].mode()[0]
    print('The most popular start station is {}'.format(popular_st_station))
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is {}'.format(popular_end_station))
    popular_start_and_end_station = df.groupby
    (['Start Station', 'End Station'])
    ['Start Station', 'End Station'].size().idxmax()
    print('The most popular combination of start and end station is {}'
          .format(popular_start_and_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    return popular_st_station, popular_end_station,
    popular_start_and_end_station


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time for this period is {} minutes'.
          format(total_travel_time / 60))
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time for this period is {} minutes'.
          format(mean_travel_time / 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    return total_travel_time, mean_travel_time


def user_stats(df, city):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('The count per user type is {}'.format(user_types))

    if city != 'washington':

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        gender_counts = df['Gender'].value_counts()
        print('The count of user per gender is {}'.format(gender_counts))

        early_birth_year = df['Birth Year'].max()
        print('The earliest birth year of a user is {}'.
              format(early_birth_year))
        most_birth_year = df['Birth Year'].mode()[0]
        print('The birth year of the largest amount of users is {}'.
              format(most_birth_year))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)

        return user_types, gender_counts, early_birth_year, most_birth_year


def display_data(df):
    i = 0
    while True:
        raw_data = input('Would you like to see raw data?')
        if raw_data == 'yes':
            print(df.iloc[i:i + 5])
            i += 5
            continue
        elif raw_data == 'no':
            break


def main():
    while True:
        city, month, weekday = get_filters()
        df = load_data(city, month, weekday)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
