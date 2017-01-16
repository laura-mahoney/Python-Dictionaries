"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Oject orientation provides three main design advantages: Abstraction, Encapsulation, and Polymorphism.
-Abstraction means not having to understand how each part is working in order to use the whole. 
-Encapsulation involves the bundling of similar functions or actions, or containment of
similar ideas. 
-Polymorphism means similar components are interchangeable. 

2. What is a class?
A class is a python construct that is used to organize data and provide a blueprint for
constructing objects. 

3. What is an instance attribute?
An instance attribute is an attribute of an object created within a class. 

4. What is a method?
A method is a function defined within a class or subclass. 

5. What is an instance in object orientation?
An instance or instance of a class is the object we create using the class as a blueprint. It
is also considered an "individual occurance" of a class. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
A class attribute is a characteristic or label that will pertain to all objects within a class. An 
instance attribute only applies to the instance of that object. For example, if you have a family class that creates
members of a family, a class attribute might be a surname all members share. An instance attribute of a family member x
might be a unique personality trait that is not shared with anyone else in the family. If family member x
gets moody when sleepy,he or she will have a moody instance attribute. 

"""


# Parts 2 through 5:
# Create your classes and class methods



#Part 1. 
class Students(object): 

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


    def make_student_data(self):
        student_dictionary = {
        "first_name": self.first_name,
        "last_name": self.last_name,
        "address": self.address
        }

        return student_dictionary

# Jasmine = Students("Jasmine", "Debugger", "0101 Computer Street")



#Part 2. 
class Questions(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_evaluate(self):
        answer = raw_input(self.question) 
        if answer == self.correct_answer:
            return True
        else: 
            return False


# Question1 = Questions("What is the capital of Alberta?", "Edmonton")



#Part 3. 
class Exam(object): 
    def __init__(self, name):
        self.name = name
        self.questions = []


# Exam1 = Exam("Midterm")

    def add_question(self, question, correct_answer):
        make_question = Questions(question, correct_answer)
        self.questions.append(make_question)


    def administer(self):
        self.score = 0
        for question in self.questions: 
            if question.ask_evaluate(): 
                self.score +=1
        return self.score / len(self.questions) * 100




#Part 4.


def take_test(exam1, student1):

    result = exam1.administer()
    student1.score = result 

    print "{}, you received a {}".format(student1.first_name, student1.score)


def example():
    new_exam = Exam("California")
    new_exam.add_question("Capital of CA?", "Sacramento")
    new_exam.add_question("Year of the gold rush?", "1849")
    new_student = Students("Laura", "Mahoney", "200 Wayne Ave")

    take_test(new_exam, new_student)



#Part 5

class Quiz(Exam):
    def administer(self):
        self.score = 0
        for question in self.questions: 
            if question.ask_evaluate(): 
                self.score +=1
        
        if self.score >= (len(self.questions) * .5):
            return True
        else: 
            return False
        

def take_quiz(quiz1, student1):

    result = quiz1.administer()
    student1.score = result 

    print "{}, you received a {}".format(student1.first_name, student1.score)


def quiz_example():
    new_quiz = Quiz("California")
    new_quiz.add_question("Capital of CA?", "Sacramento")
    new_quiz.add_question("Year of the gold rush?", "1849")
    new_student = Students("Laura", "Mahoney", "200 Wayne Ave")

    take_quiz(new_quiz, new_student)








