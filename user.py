class user:

    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        # print("\n")
        print("'\n'First Name : " + self.first_name , "'\n'Last Name : " + self.last_name, "'\n'Email : " + self.email, "'\n'Age : " + str(self.age) + "'\n'Member status : " + str(self.is_rewards_member), "'\n'Gold Points : " + str(self.gold_card_points))
        return self

    def enroll(self, new_member = True, gold_points = 200):
        self.is_rewards_member = new_member
        self.gold_card_points = gold_points
        return self
    
    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self

tom = user("Tom", "Biscotti", "TomtheMan00@gmail.com", 34)
jerry = user("Jerry", "Timberland", "Jerrynator55@gmail.com", 41)
pete = user("Pete", "Lothe", "PeteLothe0101@gmail.com", 25)


print(tom.enroll())
print(tom.spend_points(50))
print(tom.display_info())
print(jerry.enroll())
print(jerry.spend_points(80))
print(jerry.display_info())
print(tom.display_info(), jerry.display_info(), pete.display_info())