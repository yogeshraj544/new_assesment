import pandas as pd

def generate_car_matrix(dataset):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset)

    # Pivot the DataFrame
    result_df = df.pivot(index='id_1', columns='id_2', values='car')

    # Fill NaN values with 0
    result_df = result_df.fillna(0)

    # Set diagonal values to 0
    for index in result_df.index:
        result_df.at[index, index] = 0

    return result_df

# Example usage
dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_matrix = generate_car_matrix(dataset_file)

# Print the resulting DataFrame
print(result_matrix)


import pandas as pd

def get_bus_indexes(dataset):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset)

    # Calculate the mean value of the 'bus' column
    mean_bus_value = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()

    # Sort the indices in ascending order
    sorted_bus_indexes = sorted(bus_indexes)

    return sorted_bus_indexes

# Example usage
dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_indexes = get_bus_indexes(dataset_file)

# Print the resulting list of indices
print(result_indexes)


import pandas as pd

def filter_routes(dataset):
    
    df = pd.read_csv(dataset)


    route_avg_truck = df.groupby('route')['truck'].mean()

    
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    sorted_routes = sorted(selected_routes)

    return sorted_routes


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_routes = filter_routes(dataset_file)


print(result_routes)

#multiply_matrix
import pandas as pd
def generate_car_matrix(dataset):
    
    df = pd.read_csv(dataset)

    
    result_df = df.pivot(index='id_1', columns='id_2', values='car')

    
    result_df = result_df.fillna(0)

    
    for index in result_df.index:
        result_df.at[index, index] = 0

    return result_df


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_matrix = generate_car_matrix(dataset_file)
def multiply_matrix(input_df):
    
    modified_df = input_df.copy()

    
    modified_df = modified_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    
    modified_df = modified_df.round(1)

    return modified_df


result_matrix = generate_car_matrix(r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-1.csv')


modified_matrix = multiply_matrix(result_matrix)


print(modified_matrix)


import pandas as pd

def check_timestamp_completeness(df):
    
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], format='%A %H:%M:%S')

    
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], format='%A %H:%M:%S')

    
    df['duration'] = (df['end_timestamp'] - df['start_timestamp']).dt.total_seconds()

    
    completeness_check = df.groupby(['id', 'id_2']).apply(lambda group: check_completeness(group)).reset_index(drop=True)

    return completeness_check

def check_completeness(group):
    
    full_day_coverage = group['duration'].sum() >= 24 * 60 * 60  
    spans_all_days = set(group['start_timestamp'].dt.dayofweek.unique()) == set(range(7))

    
    print(f'ID: {group["id"].iloc[0]}, ID_2: {group["id_2"].iloc[0]}, Full Day Coverage: {full_day_coverage}, Spans All Days: {spans_all_days}')

    
    return full_day_coverage and spans_all_days


dataset_file = r'C:\Users\RAJARAMAN\Documents\MapUp-Data-Assessment-F\datasets\dataset-2.csv'
df = pd.read_csv(dataset_file)

completeness_series = check_timestamp_completeness(df)

print(completeness_series)


