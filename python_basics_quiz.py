"""
Python Basics Quiz - 50 Questions
This quiz covers the basics of Python including:
- Variables and Data Types
- Operators
- Control Flow (if/else, loops)
- Functions
- Lists, Tuples, Sets, Dictionaries
- String Operations
- Basic Input/Output
"""

import sys

# Quiz questions with answers and explanations
QUESTIONS = [
    {
        "question": "What is the correct way to create a variable in Python?",
        "options": ["A) int x = 5", "B) x = 5", "C) var x = 5", "D) declare x = 5"],
        "answer": "B",
        "explanation": "Python uses dynamic typing, so you simply assign a value using '=' without declaring the type."
    },
    {
        "question": "Which of these is NOT a valid Python data type?",
        "options": ["A) int", "B) float", "C) char", "D) str"],
        "answer": "C",
        "explanation": "Python doesn't have a 'char' type. Single characters are simply strings of length 1."
    },
    {
        "question": "What does the 'print()' function do?",
        "options": ["A) Stores output in a file", "B) Displays output to the console", "C) Returns a value", "D) Creates a variable"],
        "answer": "B",
        "explanation": "print() displays output to the console/terminal."
    },
    {
        "question": "How do you write a single-line comment in Python?",
        "options": ["A) // comment", "B) /* comment */", "C) # comment", "D) -- comment"],
        "answer": "C",
        "explanation": "Python uses '#' for single-line comments."
    },
    {
        "question": "What is the output of: print(type(5))?",
        "options": ["A) <class 'int'>", "B) integer", "C) int", "D) number"],
        "answer": "A",
        "explanation": "type() returns the class type, which is displayed as <class 'int'>."
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A) ^", "B) **", "C) exp()", "D) pow"],
        "answer": "B",
        "explanation": "Python uses '**' for exponentiation (e.g., 2**3 = 8)."
    },
    {
        "question": "What is the result of: 10 // 3?",
        "options": ["A) 3.33", "B) 3", "C) 4", "D) 3.0"],
        "answer": "B",
        "explanation": "'//' is floor division, which returns the quotient without the remainder."
    },
    {
        "question": "What is the result of: 10 % 3?",
        "options": ["A) 3.33", "B) 3", "C) 1", "D) 0"],
        "answer": "C",
        "explanation": "'%' is the modulo operator, which returns the remainder (10 ÷ 3 = 3 remainder 1)."
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) def", "C) func", "D) define"],
        "answer": "B",
        "explanation": "Python uses 'def' to define functions."
    },
    {
        "question": "How do you write a multi-line comment in Python?",
        "options": ["A) /* comment */", "B) <!-- comment -->", "C) '''comment''' or \"\"\"comment\"\"\"", "D) ## comment"],
        "answer": "C",
        "explanation": "Python uses triple quotes (''' or \"\"\") for multi-line strings/comments."
    },
    {
        "question": "What is the correct syntax for an if statement?",
        "options": ["A) if x = 5:", "B) if (x == 5)", "C) if x == 5:", "D) if x == 5 then:"],
        "answer": "C",
        "explanation": "Python if statements use ':', comparison operator '==', and don't require parentheses."
    },
    {
        "question": "Which of these is a valid variable name in Python?",
        "options": ["A) 2variable", "B) variable-name", "C) variable_name", "D) variable name"],
        "answer": "C",
        "explanation": "Variable names can contain letters, numbers, and underscores, but cannot start with a number or contain spaces/hyphens."
    },
    {
        "question": "What does the input() function return?",
        "options": ["A) An integer", "B) A float", "C) A string", "D) Depends on the input"],
        "answer": "C",
        "explanation": "input() always returns a string. You need to convert it if you want another type."
    },
    {
        "question": "What is the output of: print('Hello' + 'World')?",
        "options": ["A) Hello World", "B) HelloWorld", "C) Hello+World", "D) Error"],
        "answer": "B",
        "explanation": "The '+' operator concatenates strings without adding a space."
    },
    {
        "question": "How do you create a list in Python?",
        "options": ["A) list = (1, 2, 3)", "B) list = {1, 2, 3}", "C) list = [1, 2, 3]", "D) list = <1, 2, 3>"],
        "answer": "C",
        "explanation": "Lists are created using square brackets []."
    },
    {
        "question": "How do you access the first element of a list 'my_list'?",
        "options": ["A) my_list[1]", "B) my_list[0]", "C) my_list.first()", "D) my_list(0)"],
        "answer": "B",
        "explanation": "Python uses 0-based indexing, so the first element is at index 0."
    },
    {
        "question": "What is the difference between a list and a tuple?",
        "options": ["A) No difference", "B) Lists use [], tuples use ()", "C) Lists are mutable, tuples are immutable", "D) Both B and C"],
        "answer": "D",
        "explanation": "Lists use square brackets and are mutable; tuples use parentheses and are immutable."
    },
    {
        "question": "How do you create a dictionary in Python?",
        "options": ["A) dict = [key:value]", "B) dict = (key:value)", "C) dict = {key:value}", "D) dict = <key:value>"],
        "answer": "C",
        "explanation": "Dictionaries are created using curly braces {} with key:value pairs."
    },
    {
        "question": "What is the output of: print(len('Python'))?",
        "options": ["A) 5", "B) 6", "C) 7", "D) Error"],
        "answer": "B",
        "explanation": "len() returns the length of a string. 'Python' has 6 characters."
    },
    {
        "question": "Which keyword is used to create a loop that iterates over a sequence?",
        "options": ["A) while", "B) for", "C) loop", "D) iterate"],
        "answer": "B",
        "explanation": "'for' loops are used to iterate over sequences like lists, strings, or ranges."
    },
    {
        "question": "What does 'range(5)' generate?",
        "options": ["A) [1, 2, 3, 4, 5]", "B) [0, 1, 2, 3, 4]", "C) [0, 1, 2, 3, 4, 5]", "D) [1, 2, 3, 4]"],
        "answer": "B",
        "explanation": "range(n) generates numbers from 0 to n-1."
    },
    {
        "question": "How do you write an else-if statement in Python?",
        "options": ["A) else if", "B) elseif", "C) elif", "D) else-if"],
        "answer": "C",
        "explanation": "Python uses 'elif' for else-if statements."
    },
    {
        "question": "What is the output of: print(bool(0))?",
        "options": ["A) 0", "B) False", "C) True", "D) None"],
        "answer": "B",
        "explanation": "In Python, 0 evaluates to False. All other numbers evaluate to True."
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A) add()", "B) append()", "C) insert()", "D) push()"],
        "answer": "B",
        "explanation": "append() adds an item to the end of a list."
    },
    {
        "question": "What is string slicing? Example: 'Python'[0:3]",
        "options": ["A) Pyt", "B) Pyth", "C) yth", "D) Pytho"],
        "answer": "A",
        "explanation": "Slicing [start:end] includes start but excludes end. [0:3] gives characters at indices 0, 1, 2."
    },
    {
        "question": "What does the 'break' statement do in a loop?",
        "options": ["A) Skips the current iteration", "B) Exits the loop entirely", "C) Pauses the loop", "D) Restarts the loop"],
        "answer": "B",
        "explanation": "'break' exits the loop entirely, regardless of the loop condition."
    },
    {
        "question": "What does the 'continue' statement do in a loop?",
        "options": ["A) Skips the rest of the current iteration", "B) Exits the loop", "C) Pauses the loop", "D) Restarts the loop"],
        "answer": "A",
        "explanation": "'continue' skips the rest of the current iteration and moves to the next one."
    },
    {
        "question": "How do you convert a string '123' to an integer?",
        "options": ["A) integer('123')", "B) int('123')", "C) to_int('123')", "D) '123'.to_int()"],
        "answer": "B",
        "explanation": "int() converts a string to an integer."
    },
    {
        "question": "What is the output of: print(3 == 3.0)?",
        "options": ["A) False", "B) True", "C) Error", "D) None"],
        "answer": "B",
        "explanation": "Python compares values, not types. 3 and 3.0 are equal in value."
    },
    {
        "question": "Which operator checks if two variables point to the same object?",
        "options": ["A) ==", "B) is", "C) equals", "D) ==="],
        "answer": "B",
        "explanation": "'is' checks identity (same object), while '==' checks equality (same value)."
    },
    {
        "question": "What is the output of: print('Python'.lower())?",
        "options": ["A) PYTHON", "B) python", "C) Python", "D) pYTHON"],
        "answer": "B",
        "explanation": "lower() converts all characters in a string to lowercase."
    },
    {
        "question": "How do you check if a value exists in a list?",
        "options": ["A) value.in(list)", "B) list.contains(value)", "C) value in list", "D) list.has(value)"],
        "answer": "C",
        "explanation": "The 'in' keyword checks if a value exists in a sequence."
    },
    {
        "question": "What is the output of: print(not True)?",
        "options": ["A) True", "B) False", "C) 0", "D) 1"],
        "answer": "B",
        "explanation": "'not' is a logical operator that reverses the boolean value."
    },
    {
        "question": "Which of these creates a set in Python?",
        "options": ["A) set = [1, 2, 3]", "B) set = (1, 2, 3)", "C) set = {1, 2, 3}", "D) set = <1, 2, 3>"],
        "answer": "C",
        "explanation": "Sets are created using curly braces {} with values (no key:value pairs)."
    },
    {
        "question": "What does the 'pass' statement do?",
        "options": ["A) Exits the function", "B) Does nothing (placeholder)", "C) Skips to next iteration", "D) Returns None"],
        "answer": "B",
        "explanation": "'pass' is a null operation that does nothing. It's used as a placeholder."
    },
    {
        "question": "What is the output of: print(5 and 10)?",
        "options": ["A) True", "B) False", "C) 5", "D) 10"],
        "answer": "D",
        "explanation": "'and' returns the last truthy value if all are truthy, otherwise the first falsy value."
    },
    {
        "question": "How do you create an empty dictionary?",
        "options": ["A) dict = []", "B) dict = ()", "C) dict = {}", "D) dict = set()"],
        "answer": "C",
        "explanation": "Empty dictionaries are created with {}."
    },
    {
        "question": "What is the output of: print('Hi' * 3)?",
        "options": ["A) Hi3", "B) HiHiHi", "C) Hi Hi Hi", "D) Error"],
        "answer": "B",
        "explanation": "The '*' operator repeats strings."
    },
    {
        "question": "Which method removes and returns the last item from a list?",
        "options": ["A) remove()", "B) delete()", "C) pop()", "D) pull()"],
        "answer": "C",
        "explanation": "pop() removes and returns the last item (or item at specified index)."
    },
    {
        "question": "What is the output of: print(list(range(2, 5)))?",
        "options": ["A) [2, 3, 4]", "B) [2, 3, 4, 5]", "C) [2, 5]", "D) [3, 4]"],
        "answer": "A",
        "explanation": "range(start, stop) generates numbers from start to stop-1."
    },
    {
        "question": "How do you get user input as an integer?",
        "options": ["A) input(int)", "B) int(input())", "C) input().int()", "D) integer(input())"],
        "answer": "B",
        "explanation": "Wrap input() with int() to convert the string input to an integer."
    },
    {
        "question": "What is the output of: print(bool([]))?",
        "options": ["A) True", "B) False", "C) []", "D) None"],
        "answer": "B",
        "explanation": "Empty lists (and other empty collections) evaluate to False."
    },
    {
        "question": "Which of these is the correct way to define a function with parameters?",
        "options": ["A) def func(a, b):", "B) function func(a, b):", "C) def func[a, b]:", "D) func(a, b):"],
        "answer": "A",
        "explanation": "Functions are defined with 'def', parameters in parentheses, and a colon."
    },
    {
        "question": "What does the 'return' statement do in a function?",
        "options": ["A) Exits the program", "B) Prints a value", "C) Exits the function and optionally returns a value", "D) Restarts the function"],
        "answer": "C",
        "explanation": "'return' exits the function and can send a value back to the caller."
    },
    {
        "question": "What is the output of: print(10 > 5 and 3 < 2)?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "B",
        "explanation": "'and' requires both conditions to be True. Since 3 < 2 is False, the result is False."
    },
    {
        "question": "How do you access the value of key 'name' in dictionary 'd'?",
        "options": ["A) d.name", "B) d['name']", "C) d('name')", "D) d->name"],
        "answer": "B",
        "explanation": "Dictionary values are accessed using square brackets with the key."
    },
    {
        "question": "What is the output of: print('a' < 'b')?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "A",
        "explanation": "Strings can be compared lexicographically. 'a' comes before 'b', so it's True."
    },
    {
        "question": "Which method splits a string into a list of words?",
        "options": ["A) split()", "B) divide()", "C) separate()", "D) break()"],
        "answer": "A",
        "explanation": "split() divides a string into a list based on a delimiter (default is whitespace)."
    },
    {
        "question": "What is the output of: print(type([1, 2, 3]))?",
        "options": ["A) <class 'array'>", "B) <class 'list'>", "C) list", "D) array"],
        "answer": "B",
        "explanation": "Lists have the type <class 'list'>."
    },
    {
        "question": "How do you round a float 3.7 to the nearest integer?",
        "options": ["A) int(3.7)", "B) round(3.7)", "C) ceil(3.7)", "D) floor(3.7)"],
        "answer": "B",
        "explanation": "round() rounds to the nearest integer. int() truncates toward zero."
    }
]

def clear_screen():
    """Clear the console screen (works on both Windows and Unix-like systems)"""
    # Using print with newlines as a safer alternative to os.system
    # This provides visual separation without shell command execution
    print('\n' * 100)

def display_question(question_num, total_questions, question_data):
    """Display a single question with its options"""
    print(f"\n{'='*70}")
    print(f"Question {question_num}/{total_questions}")
    print(f"{'='*70}")
    print(f"\n{question_data['question']}\n")
    for option in question_data['options']:
        print(f"  {option}")
    print()

def run_quiz():
    """Main quiz function that presents questions one by one"""
    print("="*70)
    print(" "*15 + "PYTHON BASICS QUIZ")
    print(" "*15 + "50 Questions")
    print("="*70)
    print("\nThis quiz covers:")
    print("  • Variables and Data Types")
    print("  • Operators")
    print("  • Control Flow (if/else, loops)")
    print("  • Functions")
    print("  • Lists, Tuples, Sets, Dictionaries")
    print("  • String Operations")
    print("  • Basic Input/Output")
    print("\nYou'll see one question at a time.")
    print("After you answer, press Enter to see the correct answer and explanation.")
    print("\nReady to begin? Press Enter to start...")
    input()
    
    score = 0
    total_questions = len(QUESTIONS)
    
    for i, question_data in enumerate(QUESTIONS, 1):
        # Display the question
        clear_screen()
        display_question(i, total_questions, question_data)
        
        # Get user's answer
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        # Validate input
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Please enter A, B, C, or D: ").strip().upper()
        
        # Check if correct
        is_correct = user_answer == question_data['answer']
        if is_correct:
            score += 1
        
        # Show answer
        print("\n" + "-"*70)
        if is_correct:
            print("✓ CORRECT!")
        else:
            print(f"✗ INCORRECT. Your answer: {user_answer}")
        
        print(f"Correct answer: {question_data['answer']}")
        print(f"\nExplanation: {question_data['explanation']}")
        print("-"*70)
        print(f"\nCurrent score: {score}/{i}")
        
        # Wait for user to continue
        if i < total_questions:
            input("\nPress Enter to continue to the next question...")
        else:
            input("\nPress Enter to see your final results...")
    
    # Display final results
    clear_screen()
    print("\n" + "="*70)
    print(" "*25 + "QUIZ COMPLETE!")
    print("="*70)
    print(f"\nFinal Score: {score}/{total_questions} ({score/total_questions*100:.1f}%)")
    print("\nPerformance Rating:")
    
    percentage = (score / total_questions) * 100
    if percentage >= 90:
        print("  🌟 EXCELLENT! You have mastered Python basics!")
    elif percentage >= 80:
        print("  ⭐ GREAT JOB! You have a strong understanding of Python basics.")
    elif percentage >= 70:
        print("  ✓ GOOD! You understand most Python basics, but review some topics.")
    elif percentage >= 60:
        print("  ○ FAIR. Consider reviewing Python basics more thoroughly.")
    else:
        print("  ✗ NEEDS IMPROVEMENT. Spend more time studying Python basics.")
    
    print("\n" + "="*70)
    print("\nTopics to review based on common mistakes:")
    print("  • Data types and type conversion")
    print("  • Operators (especially //, %, **)")
    print("  • List/Dictionary/Tuple operations")
    print("  • Control flow (if/elif/else, for/while loops)")
    print("  • String methods and slicing")
    print("\nKeep practicing! 🐍")
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted. Thanks for participating!")
        sys.exit(0)
