class Check:
    def __init__(self, phone_numbers, links, number_to_check):
        self.phone_numbers = phone_numbers
        self.links = links
        self.number_to_check = number_to_check
        self.init = 0
    def number(self):
        i = 0
        found = False
        while i<len(self.phone_numbers)-1:
            if self.phone_numbers[i] == self.number_to_check:
                print(f"Number found at {self.links[i]}")
                i = len(self.phone_numbers)
                found = True
            i += 1
        if not found:
            print("number not found, try manually searching through exceptions: \n")
            self.get_exceptions()


    def get_exceptions(self):
        for i in range(0, len(self.phone_numbers)):
            if self.phone_numbers[i] == 'EXCEPT':
                print(f"Try: {self.links[i]}")

