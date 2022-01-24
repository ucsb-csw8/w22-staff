---
title: Chief Grades Manager Responsibilities
nav_exclude: true
layout: default
---

# How-to for a Chief Grades Manager

Hi! Hope you feel good about your new role and responsibilities because they are highly important! 

First - if you will ever have any doubts - feel free to ask the instructor or anyone in the team, you will be surprised how helpful and nice they are. 

Second, we hope that the notes below will give you an idea of where to start. Throughout the term, please help us update them by modifying this page on GitHub (use the link at the bottom of this page).

---

## Official Responsibilities
{% assign roles = site.roles | where: 'roleabbr', 'CGM' %}
{% for role in roles %}
{{ role }}
{% endfor %}

---


### Grades transfer
The grades transfer procedure is needed as we use different platforms (like zyBooks and Gradescope) and students use Gauchospace as the main source of their grades. So, after each deadline, you need to help transfer grades from those platforms to the Gauchospace.

On zyBooks, there are Lab, Participation, and Challenge Activities. Grades placeholders for them exist in Gauchospace, and after every deadline, you need to transfer PAs, CAs, LAs, and potentially Breakout activities "participation scores" separately (ask your CLO - Instructor of Record (IoR)).

Video instruction located [here](https://drive.google.com/file/d/1P7uaesu-VjjnIVgnOuAn_MbLlpd2TD8V/view?usp=sharing) (ensure you have access, ask your IoR).

Text version of the algorithm:
1. Go to the zyBooks, open the Report tab (on the right pane).
1. Select the **correct deadline date and time** (be careful with timezones if you are remote) and then select the corresponding week/chapter on the left. You usually can export one week at once, as during Gauchospace uploading, you'll need to provide certain week placeholders.
1. Check the box to include the time spent on the activities.
1. **Verify** that you have the "Entire class" selected.
1. Download CSV report

Upload the CSV to Gauchospace (see ["How to upload grades to Gauchospace"]({{ site.url }}{{ site.baseurl }}/howto)).
4. Go to Gauchospace, open Grades - Import, import the CSV
5. Match needed placeholders with the columns from the CSV (usually like "CA 6" with "CA Total").
    * Use the time spent on the category as the "feedback for" that category grade item
6. Submit import process.
7. Repeat the steps above for each week.

### Extensions
Winter 2022 - check the extensions form to know which grades to re-upload.

Check-in with the CFM to verify that the reflection grades have been processed.

---

#### Acknowledgement
Original draft was created by Roman Beltiukov during F21.
Updated by YKK to align with this quarter (W22).
