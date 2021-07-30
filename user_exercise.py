
import random

# Create mock users with randomized data every execution
def build_users(first_name_list, last_name_list):
    users = []
    random.shuffle(first_name_list)
    random.shuffle(last_name_list)
    for index in range(len(first_name_list)):
        mock_user = {}
        mock_user["first"] = first_name_list[index]
        mock_user["last"] = last_name_list[index]
        mock_user["age"] = random.randint(20,60)
        users.append(mock_user)
    return users

# print user data in pretty format
def print_users_data(user_list):
    for user in user_list:
        print("firstname: " + user["first"])
        print("lastname: " + user["last"])
        print("age: " + str(user["age"]) + "\n")

# Returns a given users full name in format: first last - ex. Jane Doe
def get_user_name(user_given):
    return str(user_given["first"] + " " + user_given["last"])

def find_maximum(list_of_numbers):
    if list_of_numbers:
        max_number = list_of_numbers[0]
        for number in list_of_numbers:
            if number > max_number:
                max_number = number 
        return max_number
    else:
        return "INVALID LIST"

def main():
    first_names = ["Bob", "Jane", "Anne", "John", "Eric", "Paul"]
    last_names = ["Smith", "Gray", "Doe", "Brown", "Williams", "Garcia"]
    users = build_users(first_names,last_names)
    print_users_data(users)

    # Create list of user ages and find maximum age value
    age_list = []
    for user in users: 
        age_list.append(user["age"])
    print(age_list)
    max_age = find_maximum(age_list)
    print("Oldest Age is: " + str(max_age))

    # Find all users with maximum age, print they're formmatted name
    people_with_max_age = []
    for user in users:
        if user["age"] == max_age:
            people_with_max_age.append(get_user_name(user))
    print("The oldest people are: " + ", ".join(people_with_max_age))

    # how to write above block of code in a more complex way
    # combined_names_of_max_age = ""
    # for user_name in people_with_max_age:
    #     if len(people_with_max_age) > 1:
    #         if user_name != people_with_max_age[-1]:
    #             combined_names_of_max_age += user_name + ", "
    #         else:
    #             combined_names_of_max_age += user_name
    #     else:
    #         combined_names_of_max_age += user_name

    # #print("User/users that are oldest age are: " + ", ".join(people_with_max_age))
    # print("User/users that are oldest age are: " + combined_names_of_max_age)

if __name__ == "__main__":
    main()
