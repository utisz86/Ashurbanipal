# based on https://www.geeksforgeeks.org/student-management-system-in-python/

# Data structure
class user_password:

    # Construction
    def __init__(self, rollno, username, user_code):
        self.rollno = rollno
        self.username = username
        self.user_code = user_code

    # Function to create and append a new username-password combination
    def new_combination(self, rollno, username, user_code):
        ob = user_password(rollno, username, user_code)
        data_ls.append(ob)

    # Function to display username-password combination
    def display(self, ob):
        print("Nr:       ", ob.rollno)
        print("Username: ", ob.username)
        print("Password: ", ob.user_code)

    # Search function
    def search(self, rn):
        for i in range(data_ls.__len__()):
            if(data_ls[i].rollno == rn):
                return i

    # Delete function
    def delete(self, rn):
        i = obj.search(rn)
        del data_ls[i]

    # Update Funcion
    def update(self, rn, username, user_code):
        i = obj.search(rn)
        data_ls[i].username = username
        data_ls[i].user_code = user_code



# Import last text file
data_dictionary = {}
data_ls = []
obj = user_password('', 0, 0)
with open("data_base/key_data_8.txt", 'r', newline='') as f:
    i = 0
    for line in f:
        (key, val) = line.strip('\r\n').split('; ')
        data_dictionary[key] = val
        obj.new_combination(i, key, val)
        i += 1


# Decrypt file
# TODO implement choose file
# TODO implement encryption
# TODO implement add password

# TODO delete display lines
# TODO delete dictinary structure
#print(data_dictionary)
#for i in range(data_ls.__len__()):
#    obj.display(data_ls[i])