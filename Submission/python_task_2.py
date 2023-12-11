
import pandas as pd

def calculate_distance_matrix(dataset):
    
    df = pd.read_csv(dataset)

    
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)

    
    distance_matrix = distance_matrix + distance_matrix.T

    
    for column in distance_matrix.columns:
        distance_matrix[column] = distance_matrix[column].cumsum()

    
    for index in distance_matrix.index:
        distance_matrix.at[index, index] = 0

    return distance_matrix


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(dataset_file)

print(result_distance_matrix)

#Unrolled_distance_matrix

import pandas as pd

def calculate_distance_matrix(dataset):
    
    df = pd.read_csv(dataset)

    
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)

    
    distance_matrix = distance_matrix + distance_matrix.T

    
    for column in distance_matrix.columns:
        distance_matrix[column] = distance_matrix[column].cumsum()

    
    for index in distance_matrix.index:
        distance_matrix.at[index, index] = 0

    return distance_matrix


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(dataset_file)


import pandas as pd

def calculate_distance_matrix(dataset):
    
    df = pd.read_csv(dataset)

    
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)

    
    distance_matrix = distance_matrix + distance_matrix.T

    
    for column in distance_matrix.columns:
        distance_matrix[column] = distance_matrix[column].cumsum()

    
    for index in distance_matrix.index:
        distance_matrix.at[index, index] = 0

    return distance_matrix


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(dataset_file)

def unroll_distance_matrix(distance_matrix):
    
    melted_df = distance_matrix.reset_index().melt(id_vars=distance_matrix.index.name, var_name='id_end', value_name='distance')

    
    result_df = melted_df[melted_df.index != melted_df['id_end']]

    return result_df


result_unrolled = unroll_distance_matrix(result_distance_matrix)


print(result_unrolled)

#find_ids_within_ten_percentage_threshold

import pandas as pd

def unroll_distance_matrix(distance_matrix):
    
    melted_df = distance_matrix.reset_index().melt(id_vars=distance_matrix.index.name, var_name='id_end', value_name='distance')

    
    result_df = melted_df[melted_df.index != melted_df['id_end']]

    return result_df

def find_ids_within_ten_percentage_threshold(df, reference_value):
    
    reference_avg_distance = df[df['id_start'] == reference_value]['distance'].mean()

    
    lower_threshold = reference_avg_distance - (reference_avg_distance * 0.1)
    upper_threshold = reference_avg_distance + (reference_avg_distance * 0.1)

    
    filtered_df = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]

    
    result_list = sorted(filtered_df['id_start'].unique())

    return result_list


result_unrolled = unroll_distance_matrix(result_distance_matrix)


reference_value = 123  
result_within_threshold = find_ids_within_ten_percentage_threshold(result_unrolled, reference_value)


print("Unrolled Distance Matrix:")
print(result_unrolled)

print("\nIDs within 10% Threshold:")
print(result_within_threshold)

#calculate_toll_rate:

import pandas as pd

def calculate_distance_matrix(dataset):
    
    df = pd.read_csv(dataset)

    
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)

    
    distance_matrix = distance_matrix + distance_matrix.T

    
    for column in distance_matrix.columns:
        distance_matrix[column] = distance_matrix[column].cumsum()

    
    for index in distance_matrix.index:
        distance_matrix.at[index, index] = 0

    return distance_matrix


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(dataset_file)

def unroll_distance_matrix(distance_matrix):
    
    melted_df = distance_matrix.reset_index().melt(id_vars=distance_matrix.index.name, var_name='id_end', value_name='distance')

    
    result_df = melted_df[melted_df.index != melted_df['id_end']]

    return result_df


result_unrolled = unroll_distance_matrix(result_distance_matrix)

def calculate_toll_rate(df):
    
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    
    for vehicle_type, rate in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate

    return df



result_with_toll_rates = calculate_toll_rate(result_unrolled)


print(result_with_toll_rates)



import pandas as pd

def calculate_distance_matrix(dataset):
    
    df = pd.read_csv(dataset)

    
    distance_matrix = df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)

    
    distance_matrix = distance_matrix + distance_matrix.T

    
    for column in distance_matrix.columns:
        distance_matrix[column] = distance_matrix[column].cumsum()

    
    for index in distance_matrix.index:
        distance_matrix.at[index, index] = 0

    return distance_matrix


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(dataset_file)

def unroll_distance_matrix(distance_matrix):
    
    melted_df = distance_matrix.reset_index().melt(id_vars=distance_matrix.index.name, var_name='id_end', value_name='distance')

    
    result_df = melted_df[melted_df.index != melted_df['id_end']]

    return result_df


result_unrolled = unroll_distance_matrix(result_distance_matrix)
import pandas as pd
from datetime import datetime, timedelta, time

def calculate_time_based_toll_rates(df):
    # Define time ranges and discount factors
    time_ranges_weekdays = [
        {'start': time(0, 0, 0), 'end': time(10, 0, 0), 'factor': 0.8},
        {'start': time(10, 0, 0), 'end': time(18, 0, 0), 'factor': 1.2},
        {'start': time(18, 0, 0), 'end': time(23, 59, 59), 'factor': 0.8}
    ]

    time_ranges_weekends = [
        {'start': time(0, 0, 0), 'end': time(23, 59, 59), 'factor': 0.7}
    ]

    # Create a new DataFrame to store time-based toll rates
    result_df = pd.DataFrame()

    # Check for the actual column names in the DataFrame
    id_start_col = 'id_start' if 'id_start' in df.columns else 'id_2'  # Replace with the actual column name
    id_end_col = 'id_end' if 'id_end' in df.columns else 'id_1'  # Replace with the actual column name

    # Iterate over each unique (id_start, id_end) pair
    for (id_start, id_end), group in df.groupby([id_start_col, id_end_col]):
        # Cover a full 24-hour period and span all 7 days of the week
        start_day = group['start_timestamp'].dt.day_name().iloc[0]
        end_day = (group['start_timestamp'] + timedelta(days=1)).dt.day_name().iloc[0]

        # Initialize the DataFrame for the current pair
        pair_df = pd.DataFrame({'start_day': [start_day], 'end_day': [end_day], id_start_col: [id_start], id_end_col: [id_end]})

        # Apply time-based toll rates for weekdays
        if start_day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            for time_range in time_ranges_weekdays:
                mask = (group['start_timestamp'].dt.time >= time_range['start']) & (group['start_timestamp'].dt.time <= time_range['end'])
                pair_df[f'{time_range["start"]}-{time_range["end"]}'] = group[mask]['distance'] * time_range['factor']

        # Apply constant discount factor for weekends
        elif start_day in ['Saturday', 'Sunday']:
            for time_range in time_ranges_weekends:
                mask = (group['start_timestamp'].dt.time >= time_range['start']) & (group['start_timestamp'].dt.time <= time_range['end'])
                pair_df[f'{time_range["start"]}-{time_range["end"]}'] = group[mask]['distance'] * time_range['factor']

        # Append the result for the current pair to the main result DataFrame
        result_df = pd.concat([result_df, pair_df], ignore_index=True)

    return result_df

# Example usage
# Assuming result_unrolled is the DataFrame from the previous step
result_with_time_based_rates = calculate_time_based_toll_rates(result_unrolled)

# Print the resulting DataFrame
print(result_with_time_based_rates)

