# Name : Abigail Wangechi
# Date : 23/2/2026

class Student:
    def init(self, name, id_number, course):
        self.name = name
        self.id_number = id_number
        self.course = course

    def update_course(self, new_course):
        print(f"\n[System] Changing course from {self.course} to {new_course}...")
        self.course = new_course

    def display_info(self):
        print(f"\n--- Student Profile ---")
        print(f"Name:    {self.name}")
        print(f"ID:      {self.id_number}")
        print(f"Course:  {self.course}")
        print("-" * 23)