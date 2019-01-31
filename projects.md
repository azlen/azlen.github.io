---
layout: default
title: Projects
permalink: /projects/
---

_Stuff I have made,_<br>
_Shiny, dull, smallish, big-ish;_<br>
_A graveyard, of sorts._

<div>
    {% for project in site.projects reversed %}
        <p>
            <a href="{{ project.url }}">{{ project.title }}</a> ({{ project.date | date: "%b. %Y"}})<br>
            <span class="project-description">{{ project.description }}</span>
        </p>
    {% endfor %}
</div>