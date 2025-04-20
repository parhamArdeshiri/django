defualt_htmls = {
    'asked-question':
"""

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Question {{ question.pk }}</title>

    <link rel="stylesheet" href="{% static 'questions/back, asked-question.css' %}">

    <!---->
    
</head>
<body bgcolor="#e0e4e8">
    
    <div class="vl1"><span style="white-space: pre;"> </span></div>
    <div class="vl2"><span style="white-space: pre;"> </span></div>

    {% for category in categories %}
        <category><a href="/questions/{{category.pk}}/">{{ category.pk }}.{{ category.name }}</a></category><br>
    {% endfor %}
    
    <div class="q">
        <h2 id="title">title:{{question.title}}</h2>
        <h1 id="text">text: </h1>
        <br>

        <div class="Q">
            <h4>
                {% for line in LinedQuestion %}
                    {{ line }} <br>
                {% endfor %}
            </h4>
        </div>
            
        <h5 id="ct" style="position: absolute;left: 690px;top: --toppx;">created time: {{question.created_time}}</h5>
    </div>

    
    {% for text in LinedAnswers %}
        <h4>
            <div class="Answer{{ forloop.counter0 }}">
                        
    
                    {% for line in text %}
                        <span style="white-space: pre;">  {{ line }}</span>
                    {% endfor %}
                
                <br>
            </div>
        </h4>
    {% endfor %}
    
    {% for question in questions %}
            <question><a href="/questions/{{ category.pk }}/{{ question.pk }}">title: {{ question.title }} | created time: {{ question.created_time }}</a></question>
    {% endfor %}

    <form action="/questions/{{ question.pk }}/answers/add/" method="GET">
            
            <br>
            <input type="submit" value="Add answer">

    </form>

    <script src="{% static 'questions/asked-question.js' %}"></script>

</body>
</html>

""",
'add-answer-to-a-question':
"""
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Question {{ question.pk }}</title>

    <!---->

</head>
<body bgcolor="#e0e4e8">
    
    <div class="vl1"></div>
    <div class="vl2"></div>
    
    <div class="q">
        <h2 id="title">title:{{question.title}}</h2>
        <h1 id="text">text: </h1>
        <br>

        <div class="Q">
            <h4>
                {% for line in LinedQuestion %}
                    {{ line }} <br>
                {% endfor %}
            </h4>
        </div>
            
        <h5 id="ct" style="position: absolute;left: 690px;top: 290px;">created time: {{question.created_time}}</h5>
    </div>

    
    {% for text in LinedAnswers %}
        <h4>
            <div class="Answer{{ forloop.counter0 }}">
                        
    
                    {% for line in text %}
                        <span style="white-space: pre;">  {{ line }}</span>
                    {% endfor %}
                
                <br>
                <h6>{{ answer.created_time }}</h6>
            </div>
        </h4>
    {% endfor %}

    <form action="/questions/{{ question.pk }}/answers/add/" method="POST">

        {% csrf_token %}
        {{ form.as_p }}

        <input type="submit" value="Add" id="addbtn">

    </form>

    <script src="{% static 'questions/add-answer-to-question.js' %}"></script>

</body>
</html>



"""
}
