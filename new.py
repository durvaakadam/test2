class User:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def run(self):
        act = "driving" if self.age >= 18 else "school"
        print(f"{self.name} did {act}")
        print(("Adult" if self.age >= 18 else "Minor") + " activity:", act)


users = [User("Alice", 25), User("Bob", 15)]
for u in users: u.run()
