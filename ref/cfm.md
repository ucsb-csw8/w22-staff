---
title: Chief Feedback Manager Responsibilities
nav_exclude: true
layout: default
---

# How-to for the Chief Feedback Manager

Hi! Hope you feel good about your new role and responsibilities because they are very cool and highly important! 

First - if you will ever have any doubts - feel free to ask the instructor or anyone in the team, you will be surprised how helpful and nice they are. 

Second, we hope that the notes below will give you an idea of where to start. Throughout the term, please help us update them by modifying this page on GitHub (use the link at the bottom of this page).

---

## Official Responsibilities
{% assign roles = site.roles | where: 'roleabbr', 'CFM' %}
{% for role in roles %}
{{ role }}
{% endfor %}

---

## Notes

### Getting Started

Before the start of the quarter, work with the CLO to verify that you:
* have the correct permissions on Gauchospace to post assignments and grades
* know where/how to access the results of the reflections
* are able to access a document where you'll be collecting the weekly reflection summaries/highlights

### Questions/prompts for reflections

We have a nice question bank of reflection prompts from previous quarters.

Certain weeks require specific reflection (e.g., mid-term evaluation).
- Use the shared template and previous terms' reflections to assemble each week's prompts.
- Ask the team if we need to collect any additional feedback.

The forms are released on Gauchospace on {{ site.reflections_release }}.

This quarter, we are using Google forms in order to distribute the reflections.
* CLO will prepare the form and provide the link.
* Notify the CLO of any changes to the questions based on the team's feedback.

Set in the "Responses" settings:
* The form needs to collect the emails
* Always email the respondents a copy of their response
* Restrict to users in University of California, Santa Barbara and its trusted organizations
* Limit to 1 response

For the form:
* Title it "CSW8 (W22) Reflection (Week X)", replacing X
* The first question should be "How do you feel about the material this week?" with the options:
```
     Too easy
     Just right
     Kind of challenging
     Too challenging
```

* The last question should always be "Last question: Any other feedback?"

### To release the reflection form
* Go to the specific tab on Gauchospace and use "+ Add an activity or resource" button at the bottom of the tab.
* Create a "URL" assignment (if creating this assignment in advance add the [FAQ link](https://ucsb-csw8.github.io/w22/faq/#where-do-i-find-the-weekly-reflections))


### Grade the reflections

Google forms allows you to save the CSV: go to the "Responses" tab, click on the green icon for the Google sheets.

When you get a CSV list of the reflection responses, create a copy of it to upload to Gauchospace:
* add a "Grade" column and give everyone who submitted the reflection full points 
    * check Gauchospace gradebook to see what the max grade is set to
    * verify that all reflections have the same max score
* in the "Email" column, replace "@ucsb.edu" with an empty string (you can optionally rename "Email" to "Username")
    * Gauchospace is not consistent on which students have the `@umail` and which have `@ucsb` addresses, so forcing the spreadsheet to be one or the other will miss some students

Upload the CSV to Gauchospace (see ["How to upload grades to Gauchospace"]({{ site.url }}{{ site.baseurl }}/howto)).
* map the username to the NetID 
* map the "Challenge level" responses to the Feedback for that week's reflection


### Process the feedback

Read through the feedback, tagging it with the following sample categories: 
* “Thank you”
* "Question"
* “Request/Suggestion”
* "Complaint"
* “Notable thought”

Assemble a list of the common challenging concepts and the corresponding questions and add the feedback to the [reflection summary document in the reflections folder]({{ site.reflections_dir }}).

Draft the insights in [the doc provided there]({{ site.reflections_dir }}) in preparation to the public forum post and/or individual follow-up.

Message CLO when they are ready

Run a [script](#) to get the emails of those who missed the reflection.
- Follow-up with the students to check-in with them (a private message via Piazza, also include Instructors)
- For those who missed two or more reflections in a row, ask CLO to send them an email


### Post the results on the forum

When making a post, include
* a graph of the challenge level
* a summary of the themes
* Q&A with references
* encouragement / resources


---

Hope you will have an amazing mentoring semester! Have the best of luck! :-)


---

#### Acknowledgement
Notes have been updated by YKK based on the notes from Roman Beltiukov.
