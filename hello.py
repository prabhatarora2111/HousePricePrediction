import csv

# Function to get user input
def get_user_input():
    name = input("Enter name: ")
    age = input("Enter age: ")
    occupation = input("Enter occupation: ")
    return name, age, occupation

# Function to add data to CSV file
def add_data_to_csv(data, csv_file):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Path to the CSV file
csv_file_path = 'user_data.csv'

# Main function
def main():
    # Get user input
    name, age, occupation = get_user_input()
    
    # Data entered by the user
    user_data = [name, age, occupation]
    
    # Add data to CSV file
    add_data_to_csv(user_data, csv_file_path)
    
    print("Data added to CSV file successfully.")

if __name__ == "__main__":
    main()