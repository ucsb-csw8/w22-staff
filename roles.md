---
layout: page
title: Roles
description: A listing of all roles.
---

# Team RRR: Roles, Responsibilities, Resources
{:.no_toc}

We - the Teaching Assistants (TAs), Undergraduate Learning Assistants (ULAs) and Prof. K - are what we will collectively refer to as "Mentors".
These pages use the terms "mentors" and "team" interchangeably.

Each mentor has one or more role listed below.

* Roles and their information shown below are in the `_roles` collection.
* The role link leads to the respective `roleabbr.md` file in the `ref` folder (e.g., `cco.md` file outlines considerations for that role).


---

{% assign roles = site.roles %}
{% for role in roles %}
{{ role }}
{% endfor %}

