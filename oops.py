class MyList:
    def __init__(self,initial_data):
        self.data = initial_data

my_list = MyList([1,2,3,4,5])
print(my_list.data)


class MyClass:

    def first_method(self):
        return "This is my first method"

    # Add method here
    def return_list(self,input_list):
        return input_list
my_instance = MyClass()
result = my_instance.return_list([1,2,3])

# NOTE: APPENDING IN CLASS THROUGH INSTANCE
class MyList:

    def __init__(self, initial_data):
        self.data = initial_data

    # Add method here
    def append(self,new_item):
        self.data.append(new_item)

my_list = MyList([1,2,3,4,5])
print(my_list.data)
my_list.append(6)
print(my_list.data)


class MyList:

    def __init__(self, initial_data):
        self.data = initial_data
        # Calculate the initial length
        self.length = 0
        for item in self.data:
            self.length += 1

    def append(self, new_item):
        self.data = self.data + [new_item]
        # Update the length here
        self.length += 1

my_list = MyList([1, 1, 2, 3, 5])
print(my_list.length)

my_list.append(8)
print(my_list.length)
