class Student:
    def __init__(self, quiz, midterm, final):
        self.quiz = quiz
        self.midterm = midterm
        self.final = final

    def calculate_overall_score(self):
        overall_quiz = (self.quiz / 20) * 15
        overall_midterm = (self.midterm / 50) * 35
        overall_final = (self.final / 100) * 50
        overall = overall_quiz + overall_midterm + overall_final
        return overall

    def final_letter_grade(self, all_scores):
        if 90 < all_scores <= 100:
            return "A"
        if 80 < all_scores <= 90:
            return "B"
        if 70 < all_scores <= 80:
            return "C"
        if 60 < all_scores <= 70:
            return "D"
        if 0 <= all_scores <= 60:
            return "F"


assessment = Student(17, 45, 92)

overall_marks = assessment.calculate_overall_score()
print("Overall marks: " + str(overall_marks))

final_grade = assessment.final_letter_grade(overall_marks)
print("Grade: " + str(final_grade))
