---
layout: page
title: How to
description: A listing of all how-to guides.
---

# How-to Resources
{:.no_toc}

* Guides and their information shown below are in the `_howto` collection.

# Quick access links

## Gauchospace

### Grades
* ["How to upload grades to Gauchospace"](https://help.lsit.ucsb.edu/hc/en-us/articles/202561544-How-do-I-upload-a-spreadsheet-of-grades-into-the-GauchoSpace-gradebook-)
* [Manually Override Points for a Specific Question in Quiz](https://help.lsit.ucsb.edu/hc/en-us/articles/360042449951-Manually-Override-Points-for-a-Specific-Question-in-Quiz) (as much as possible refrain from using this: instead, add the other correct options to the list of correct answers)

### Quizzes
Here are the official Gauchospace reference pages for quizzes:
* [Quiz Reference Guide for Gauchospace](https://help.lsit.ucsb.edu/hc/en-us/articles/204491504-Quiz-Reference-Guide-for-Gauchospace)
* [Revealing Quiz Scores and Feedback Only After a Quiz Closes](https://help.lsit.ucsb.edu/hc/en-us/articles/360052427312-Revealing-Quiz-Scores-and-Feedback-Only-After-a-Quiz-Closes) (uncheck all options for "After the quiz is closed" until all responses have been checked and options have been adjusted, and then set the review option for "After the quiz is closed" retroactively.)
* [Understanding Quiz Statistics](https://help.lsit.ucsb.edu/hc/en-us/articles/360056425031-Understanding-Quiz-Statistics)
* [Quiz Tips: How to create multiple choice quiz questions in Gauchospace using Word](https://help.lsit.ucsb.edu/hc/en-us/articles/214732228-Quiz-Tips-How-to-create-multiple-choice-quiz-questions-in-Gauchospace-using-Word)
* see above how to [Manually Override Points for a Specific Question in Quiz](#) (as much as possible refrain from using this: instead, add the other correct options to the list of correct answers)

## Gradescope

<https://help.gradescope.com/>

## zyBooks

See the relevant guidelines under [the Guidelines section]({{ site.url }}{{ site.baseurl }}/guidelines#zybook)
* [How to create a new zyLab](https://zybooks.zendesk.com/hc/en-us/articles/360012355613-How-to-create-a-new-zyLab)
* [How to copy a new zyLab](https://zybooks.zendesk.com/hc/en-us/articles/360015181913-How-to-copy-a-zyLab)
* [Configure zyBook](https://zybooks.zendesk.com/hc/en-us/articles/360007903633-How-to-configure-your-zyBook)
* [Create a test using zyBooks test banks](https://zybooks.zendesk.com/hc/en-us/articles/360018781373)

---

## Our custom guides, setup, and considerations

{% assign guides = site.howto %}
{% for guide in guides %}
{{ guide }}
{% endfor %}

