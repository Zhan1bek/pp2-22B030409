class string:
    def __int__(self,):
        self.my_string= ""

    def get_string(self):
        self.my_string = input()

    def print_string(self):
        print(self.my_string.upper())


my_string = string()
my_string.get_string()
my_string.print_string()
