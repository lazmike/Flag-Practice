"""
Define a new type Permission that stores three user permissions: read, write, and/or execute
This type should be an enumeration able to support bitwise operations
Define a type called User that takes two arguments at instantiation: name and user_role
Internally, the User class sets a permissions attribute depending on the specified user_group:
- admin: read, write, and execute
- user: read
- manager: read, write
- support: execute
The User class also implements (or ideally inherits) read(file), write(file, content), and execute(file)
methods which are permission-checked, e.g. a User instance belonging to the support user_role
will not be able to write, but only execute
For ease of operation, assume that the read/write/execute functionality pertains to a python script
Instances of User should have an informative string representation
As an extra challenge, try to allow some polymorphism in the user_role so that it's possible to instantiate by both
string roles as well as integers, e.g. User("A", user_role=2) would imply WRITE-only permissions, whereas User("B",
user_role=6) would imply WRITE and EXEC, because 2**1 + 2**2 = 2 + 4 = 6
"""

from enum import auto, Flag
class Permission(Flag):
    
    READ = auto()       #1              list.Permission to see values assigned
    WRITE = auto()      #2
    EXECUTE = auto()    #4
    
class User:
    
    def __init__(self, name, user_role):
        self.name = name
        self.user_role = user_role
        self.permissions = Permission(0)
        if type(self.user_role) != int:
            self.user_role = self.user_role.lower()
        if self.user_role == 'a' or self.user_role == 'admin' or self.user_role == 'administrator' or self.user_role == 7:
            self.user_role = "admin"
            self.permissions = Permission(7)
        elif self.user_role == 'm' or self.user_role == 'manager' or self.user_role == 3:
            self.user_role = "manager"
            self.permissions = Permission(3)
        elif self.user_role == 's' or self.user_role == 'support' or self.user_role == 4:
            self.user_role = "support"
            self.permissions = Permission(4)
        else:
            print("Invalid input. Default user type 'user' is given!")
            self.user_role = 'user'
            self.permissions = Permission(1)
        
    def __repr__(self):
        return f"{type(self).__name__}({self.permissions})"
            
    def __contains__(self, item):
        if type(item) == Permission:
            return self.permissions & item
        
    def read(self, file):                         
        if Permission.READ not in self.permissions:
            return "You do not have permission to read files"
        with open(file, 'r') as op:
            print(op.readlines())
            op.close()
      
    def write(self, file, content):
        if Permission.WRITE not in self.permissions:
            return "You do not have permission to write files"
        wr = open(file, 'a')
        wr.write(content)
        print("Your content has been written")
        wr.close()
        
    def execute(self, jammies_test):
        if Permission.EXECUTE not in self.permissions:
            return "You do not have permission to execute files"
        import jammies_test

    #user_role as integer should encompass the Permissions (1, 2, 3, 4, 5, 6, 7)
    #if a nonsense user role is entered, we give it a default of 1 (read)
    #trying to use a function we are not permitted to throws an error
    
admin_user = User("Mike", 'admin')

    
    
            
        
    

