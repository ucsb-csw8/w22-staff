---
title: Chief Lab Developer Responsibilities
nav_exclude: true
layout: default
---

# How-to for a Chief Lab Developer from a Chief Lab Developer

Hi! Hope you feel good about your new role and responsibilities because they are very cool and highly important! 

First - if you will ever have any doubts - feel free to ask the instructor or anyone in the team, you will be surprised how helpful and nice they are. 

Second, we hope that the notes below will give you an idea of where to start. Throughout the term, please help us update them by modifying this page on GitHub (use the link at the bottom of this page).

---

## Official Responsibilities
{% assign roles = site.roles | where: 'roleabbr', 'CLD' %}
{% for role in roles %}
{{ role }}
{% endfor %}

---

Note that the CLD are very similar to the [responsibilities for the ALD]({{ site.url }}{{ site.baseurl }}/ref/ald), so the notes for these roles to be synchronized and updated in tandem.

## Notes

### Getting Started

Before the start of the quarter, work with the CLO to verify that you:
* have the correct permissions in zyBooks to add/edit labs and tests
* are aware of the limitations of the zyBooks Markdown
* have access to previous labs / know where to find them
* know where to find the lab slides template and are able to edit that folder

So let's start:
### 1. Assemble labs and lab activities / add to zyBooks, listing the learning objectives for each.

Since this is the main thing to do, I will have slightly more text here, in which I want to share my own experience. 

#### 1.1. Numbers and dates.
There are suggested numbers and dates collected from our and the instructor's experience. 
1. Prepare the labs' drafts by the weekends of the previous week. So you and other mentors have some time to check the wordings and try to solve them.
2. Finalize them just after the first lecture each week (see if maybe some specific themes or patterns of concepts were discussed)
3. Release them one day before the sections, morning or in the middle of the day - e.g. 1 pm, is best
2. Have approximately 6-10 labs: 2-3 simple, 2-3 moderate, 2 hard (+1 whenever we need to provide extra practice for specific concepts). 
3. Have 1 breakout room activity. Try not to have it be very complicated but it should try to use the most important learning objectives of the week. 
* Note - for someone, breakout rooms activities will be the first labs of the week (i.e., they won't start on the other labs earlier), but it is in the labs that they get to practice their understanding.
4. Always have a few optional labs. Sometimes you can move the old labs in this area, if you created enough new ones. 
* Try to have both - very simple and nice optional labs and hard and tricky ones for the advanced students to have fun with. 
* Too many optional labs are not very good as well: 3-5 is just right.

#### 1.2. Check current labs and modify them
1. Read the corresponding ZyBooks week and write down what concepts will be covered this week (e.g., `for` with `range`, only `range`, `if`/`else`/`elif`, f-strings, etc.)
2. Look through the current labs. Check that they are understandable and simple to go through. (not too difficult in the beginning, not too simple in the end, but always clear). Check that only the learned concepts are used (ZyBooks themes sometimes rearrange and change - be sure not to ask students to solve a lab with "`sep`" in `print` parameter when they did not learn it)
3. Modify the current lab slightly - modify wordings of output, make it more fun. E.g. old: "The average value is N" -> "N is the average value for the list `coins`". By this, you will later be able to understand that lab solution was spiled from the previous quarter (_YK: ask Liu what she means by this_ :-)).
4. If you know how to make the lab concept more "real-life" - **do it**. E.g., the lab talks about distances from Santa Barbara to the surrounding, but now UCSB is located in LA - modify the lab accordingly. Add your experience. Make it relevant to you/students - contextualizing the concepts makes them more valuable and easier to cope with.
5. Check how many labs use each concept - we need to have labs on each concept and we need to have a uniform distribution of complexity of concepts over the labs.
6. If you need to modify a "ZYBooks maintained" lab - just copy it (see [the relevant link here]({{ site.url }}{{ site.baseurl }}/howto#zybooks)), move the maintained one to unused or other relevant section (check with the CLO) and rename the new one to not have "Copy of LAB" in the title.
7. Be sure that each lab has "Learning objectives" sections that clearly tell what students will learn to do. Read more about learning objectives [here](https://ucsb-teaching-cs.github.io/s21/hw/teaching_demo/#select-your-topicconcept-and-determine-the-learning-goals).
    * Verify that you followed the other suggested [Lab Guidelines]({{ site.url }}{{ site.baseurl }}/guidelines#lab-guidelines).

#### 1.3. Create new ones
After reviewing the old labs you know what concepts were covered and what not and what difficulties (easy, medium, hard) are presented. If you feel that something is missing, or you just have an amazing real-life experience with the discussed concept - feel free to create your own lab.
1. Copy the old lab or create a new one (find these buttons at the end of the zyBook's chapter, if you do have relevant access; see the relevant links under [the "How to" section]({{ site.url }}{{ site.baseurl }}/howto#zybooks))
2. Create a code solution for your lab - **make sure that your solution uses the features you are asking students to use** - they should be outlined in the learning objectives
3. Create tests for your lab. More tests - better. In the final score, only % of solved would matter.
    - Even for very simple tasks you can use UnitTest - that is a very good practice
    - Compare output tests
Many students misuse the knowledge about tests to hardcode them into the solutions. Make hidden tests (advanced option in tests) and make your output in unit tests helpful but not direct. Make random unit tests.
4. Create the instructions for your solution. Add there the "history" of the problem, but not too much. Make sure that it is clear how to follow your instructions. Check the second meanings of the words. Try to find the weak parts and cover them.
5. Add a few hints of tricky concepts in the end.
6. Create learning objectives part (which is first) so students and future mentors are aware of what will be going on here
7. Note - good code has functions that solve the core problem and an if-name-main area that use the functions, reads the input, outputs the result, etc.

#### 1.4. Add more tests, always add more tests
It is never too many tests for the lab - add a few new hidden ones, or play with the amazing unit tests possibilities. Check the code below (note, ZyBooks tests my slightly differ, but you will be able to adapt it):
```python
import random
import sys
from io import StringIO
# import student file. Do NOT import the function directly
# Importing the function directly doesn't work if it's misspelled
import main

# Below is a correct function. You can copy it from the solution area, but make sure that it is really correct!
# Do not hardcode the numbers for tests - it is really hard to debug them when something is incorrect
def _correct_function(text, chars):
    # whatever solution is
    counter = 0
    for char in chars:
        counter += text.count(char)
    return counter

def _correct_function_print(text, chars):
    # If you need to collect not only output, but print area from student
    counter = 0
    for char in chars:
        counter += text.count(char)
    return counter

def test_function(feedback):
    text_example = "You are so talented"
    # Try to randomize your test if possible
    chars = [chr(random.randint(ord("a"), ord("z"))) for _ in range(10)]#["a", " ", "o"]
    _chars = chars.copy() # if you will need to check that initial list is not modified
    
    # Define the string (strings inside one variable) that will be what student read via input()
    to_input = f"inpit1\ninput2\n"
    
    # Save the previous area where print() will go, and create our own
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    # Assign the new area where from student will get their input()
    example_input = to_input  # This is the line that we created
    old_stdin = sys.stdin
    s = StringIO(example_input)
    sys.stdin = s
    
    try:
        student_result = main.calculate_chars(text_example, chars)
    except AttributeError:
        feedback.write("We can not find your function, do you named it right?")
        return False # That means tests failed
    except Exception as e:
        feedback.write(f"You have an error in your function - please check it manually\n{e}")
        return False
    finally:
        # restore the print() and input() area anyway, or all tests will fails
        sys.stdout = old_stdout
        sys.stdin = old_stdin
    # Save what student printed in their function
    student_print = mystdout.getvalue()
    
    expected_result = _correct_function(text_example, _chars) #the copy of list if you need to chek it later
    expected_print = _correct_function_print(text_example, _chars) #or somehow other create the "print" line
    
    if student_result is None:
        feedback.write(f"Do you have a return value in all branches of your function?")
        return False
    
    if expected_result != student_result:
        feedback.write(f"We expected to see {expected_result}, but get {student_result}\n"
                       f"Something went wrong!")
        # Or add less specific description of problem here
        return False
    
    # if student_print != expected_print:
    if student_print != "": # if it is nothing to be printed inside
        feedback.write(f"You was not asked to print something in function!")
        return False
        
    if chars != _chars:
        feedback.write(f"You modified the given list, this is wrong!")
        return False
    
    #If all previous chek passed - the test passed    
    feedback.write(f"You passed the test!")
    return True
```

1. You won't always need everything from the example above - it is a summarizing one, but the more you check - the better.
2. Randomize the tests!!! You have all powers of the random module, such as ```random.randint(), random.choice()``` and others to make it impossible to just hardcore values to pass the test.
3. It is not as hard to record the output and provide the input for user code if you need it. Do remember that first run will go with the first import, so you might want to surround the import with try-except or other blocks

### 2. Ask mentor colleagues to solve the lab and check that the wording is clear and understandable
That is the very important part because when you make the labs you feel like they are easy and understandable, but it is a trick of your mind. Ask for help in our amazing team - if every mentor reads the instructions and understands it and can solve the lab and is not able to trick the tests - then your lab is superb!


### 3. Release the labs
For all labs of this week, you need to release them one by one: go on the page of the lab, and on the right upper corner press the "Visible to students" button at the right time.
* Make sure the wording and tests are correct before that.
* Note that you won't be able to release the lab if there are _no tests_. You need at least one for zyBooks to allow the release.

It would be amazing if you can open a few labs before the release date, e.g., on Monday, but you need to accurately check them before that. (all pipelines with prepare-check-ask-to-check-others should work before the release, always!) 

Do not release not optional lab before the lecture if your instructor does not state otherwise.

### 4. Prepare the presentation for sections
See what concepts and patterns are to be used in breakout rooms and other hard labs and adjust them as examples and provide this info to ALD.

Hope you will have an amazing mentoring semester! Have the best of luck!


---

#### Acknowledgement
Original draft was created by Liubov Kurafeeva during F21.
Updated by YKK to align with this quarter (W22).
