class CourseManagement:
    def	__init__(self):
        self.active_students = set()
        self.student_records = []

    def enroll_student(self, student_id, student_name):
        self.active_students.add(student_id)
        self.student_records.append((student_id, student_name))
        self.student_records.sort()



    def binary_search(self, student_id):
        low, high = 0, len(self.student_records) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.student_records[mid][0] == student_id:
                return self.student_records[mid]
            elif self.student_records[mid][0] < student_id:
                low = mid + 1
            else:
                high = mid - 1
        return None



cm = CourseManagement()
cm.enroll_student(101, "Avreet")
cm.enroll_student(102, "Ammay")
cm.enroll_student(103, "Dhristi")

print(cm.active_students)
print(cm.binary_search(101))

