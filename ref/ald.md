---
title: Assistant Lab Developer Responsibilities
nav_exclude: true
layout: default
---

# How-to for Assistant Lab Developer from an Assistant Lab Developer

Hi! Hope you feel good about your new role and responsibilities because they are so cool and really important!

First - if you will ever have any doubts - feel free to ask the instructor or anyone in the team, you will be surprised how helpful and nice they are. 

Second, we hope that the notes below will give you an idea of where to start. Throughout the term, please help us update them by modifying this page on GitHub (use the link at the bottom of this page).

---

## Official Responsibilities
{% assign roles = site.roles | where: 'roleabbr', 'ALD' %}
{% for role in roles %}
{{ role }}
{% endfor %}

---

I would really advise you to read the [responsibilities for the CLD]({{ site.url }}{{ site.baseurl }}/ref/cld), since you have similar responsibilities.

## Notes

### Getting Started

Before the start of the quarter, work with the CLO to verify that you:
* have the correct permissions in zyBooks to add/edit labs and tests
* are aware of the limitations of the zyBooks Markdown
* have access to previous labs / know where to find them
* know where to find the lab slides template and are able to edit that folder


So let's start:

### Make sure that slides address common challenges and misconceptions, and contain helpful examples.
#### Helpful notes
1. Read the ZyBooks week, solve the PA, CA, so that you are aware of the concepts that were covered.
2. Check the Breakout Room activities and the rest of the labs so you see the real code that students will have to use.
3. Ask the CLO about the previous year's examples. They are not always relevant, but they can give you a starting point.
4. Follow the same pattern for each week's presentation slides, e.g., announcements-deadlines-notes.
5. Use the same presentation style provided in the template (when week 5 is all red and sparkling, and week 6 is only-black-text - that can be distracting), though relevant changes and fun colors are good
6. Follow the [general presentation guidelines](https://ucsb-teaching-cs.github.io/s21/hw/teaching_demo/#presentation-guidelines) - not too much text, no font less than 18 pts, highlighted examples, etc.
7. Work with other mentors to make this presentation relevant to your specific term. Ask on a common chat what others think we need to add there.
8. Make sure that everyone who will lead the sections is aware of the presentation location and content.
9. Every mentor can add some slides to the presentation if it is necessary, but a common template with correct deadlines is very important.
    - if something gets fixed on the slides, make sure that the change gets shared with the others (via the Slack channel) to ensure the other labs stay consistent

### Useful numbers and dates
Follow the suggested schedule; roughly, it means:
1. Prepare presentation draft with the labs by Monday
    1. Store it in the shared space for all mentors in the same folder, so it is easy to find it.
    1. Notify everyone on slack/by email when the presentation is ready
2. Adjust it after the lecture on Tuesday
5. 3-5 slides are just enough, do not create more - need to give more time for students to work together/ask questions
6. 15 minutes of talk is the maximum that we have - otherwise, students have too little time to work together and solve the labs
7. Code examples are good when they follow the rules of python and the suggested style guidelines, and are highlighted the same as in a real IDE
   - no single- or two-letter variables called "a"/"b", etc
   - no variables called "list"/"set" etc - students will copy code from here!
   - code is runnable!
   - no unexpected capital letters for "print()", etc. - be careful with autocorrect
8. Draw diagrams and prepare reference lists
9. Help look over the [Lab guidelines]({{ site.url }}{{ site.baseurl }}/guidelines#lab-guidelines) to verify that everything is in order.


Hope you will have an amazing mentoring term! Have the best of luck!


---

#### Acknowledgement
Original draft was created by Liubov Kurafeeva during F21.
Updated by YKK to align with this quarter (W22).
