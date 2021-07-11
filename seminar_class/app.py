# from student import Student
#
# student1 = Student("김우유", "컴퓨터과학과", "공과대학", 3.0, False)
# student2 = Student("이자두", "국어국문학과", "문과대학", 4.2, True)
#
# # access each instance's attribute
# #print(student1.name)
# #print(student2.department)
#
# # access class attribute
# student1.univ_name = "고려대학교"
#
# print(student1.univ_name)
# print(student2.univ_name)
#
# Student.univ_name = "고려대학교"
# print(student1.univ_name)
# print(student2.univ_name)
#
# # call object's function
# print(student2.acquire_scholarship())

# -----------------------------------------------------------
# multiple choice questions
# from question import Question
# questions_string = \
#     ["What color is the apple?\n(a) blue\n(b) red\n(c) yellow\n",
#      "What year is it?\n(a) 2020 (b) 2021 (c) 2022\n",
#      "What do I want to eat for dinner?\n(a) 삼겹살\n(b) 김치찜\n(c) 짜장면\n"]
#
# questions = [
#     Question(questions_string[0], "b"),
#     Question(questions_string[1], "b"),
#     Question(questions_string[2], "b")
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if (answer == question.answer):
#             score += 1
#     print("You scored "+str(score)+" out of "+str(len(questions))+"!")
#
# run_test(questions)

# -----------------------------------------------------------
# from chef import Chef
# chef1 = Chef()
# chef1.make_beef()
# chef1.make_special_dish()
#
# from koreanChef import KoreanChef
# koreanchef1 = KoreanChef()
# koreanchef1.make_beef()
# koreanchef1.make_bulgogi()
# koreanchef1.make_special_dish()

# -----------------------------------------------------------
