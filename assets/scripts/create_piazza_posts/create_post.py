from icecream import ic
from piazza_api import Piazza
import csv

def reminder_template(week, student_id, student_first_name, feed_groups, bypass_email = False):
    params = {
    'status': 'private',
    'folders': [week],
    'id': student_id,
    "subject": 'A reminder to submit your weekly reflection',
    "content": '''Hi {arg1},

We did not find your weekly reflection for week 1.

No worries, it is just a reminder for you to submit future weekly reflections. Your feedback really matters cause it can help us to stay synchronized with students and adjust the course materials when necessary.

Don\'t hesitate to reach out by piazza or attending office hours if you have any questions, thoughts or concerns (you are also welcome to include them in your weekly reflection), and we are always here to help!

<a href=\"https://ucsb-csw8.github.io/w22/faq/#where-do-i-find-the-weekly-reflections\" target=\"_blank\"><u>Weekly reflections on Gauchospace (due on Sunday at 9PM)</u></a>

<a href=\"https://ucsb-csw8.github.io/w22/about/#grading" target=\"_blank\"><u>Syllabus</u></a>

<a href=\"https://ucsb-csw8.github.io/w22/schedule/" target=\"_blank\"><u>Office Hours</u></a>

Best regards,
Pengfei'''.format(arg1=student_first_name),
    'type': 'note', # 'note', 'question'
    'prof_override': bypass_email,
    'config': {
        'bypass_email': bypass_email,
        'is_announcement': 0,
        'feed_groups': feed_groups
    }
    }
    return params


# args start
worklist = ['week2', 'week3']
bypass_email = True
pz_email = 'your email for piazza'
pz_psw = 'your password for piazza'
# args end


p = Piazza()
p.user_login(email=pz_email, password=pz_psw) # alternatively, use p.user_login() to enter your email/psw everytime
cs8w = p.network('kxyw0ft3mjl78d') # the course id for cs8w
all_users = cs8w.get_all_users()
all_instrs = [each for each in all_users if each['role'] in ['ta','professor'] ]
all_students = [each for each in all_users if each['role'] == 'student' ]
feed_groups = all_instrs[0]['id']
for each in all_instrs[1:]:
    feed_groups += ','+each['id']

for each_week in worklist:
    with open(each_week+'_not_submitted.csv','r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            netid = row[0]
            if netid == 'netid':
                continue
            student = [each for each in all_users if netid in each['email'] ][0]
            student_id = student['id']
            student_first_name = row[1].split(' ')[0]
            if student['name'] == '':
                print (student)
            # to do: change feed_groups to the student + his/her associated TA + professor, rather than the student + all TAs + professor
            cs8w._rpc.content_create(reminder_template(each_week, student_id, student_first_name, feed_groups+','+student_id, bypass_email))
