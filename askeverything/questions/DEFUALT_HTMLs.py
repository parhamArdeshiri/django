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

    <link rel="stylesheet" href="{% static 'questions/asked-question.css' %}">
    
    <style>
                            .Answer0{
                        background-color: #3498db;
                        border-radius: 10px;
                        border: 0 solid rgb(0, 0, 0);
                        width: 340px;
                        height: 25px;
                        position: absolute;
                        top: 61px;
                        left: 10px;
                        box-shadow: 5px 5px 5px rgba(180, 180, 180, 60%);
                    }.Answer1{
                        background-color: #3498db;
                        border-radius: 10px;
                        border: 0 solid rgb(0, 0, 0);
                        width: 340px;
                        height: 25px;
                        position: absolute;
                        top: 131px;
                        left: 10px;
                        box-shadow: 5px 5px 5px rgba(180, 180, 180, 60%);
                    }
                            </style>
    
</head>
<body bgcolor="#e0e4e8">

    <div class="lside">

        <h2 style="margin-top: 5px;margin-left: 22px">other questions in this category</h2>
    
        {% for question in other_questions %}
            {% if question != None %}
                <question><a href="/questions/{{ category.pk }}/{{ question.pk }}">title: {{ question.title }} | created time: {{ question.created_time }}</a></question>
                <pre> </pre>
            {% endif %}
        {% endfor %}
        
        <pre style="font-size: 5px"> </pre>
    
    </div>

    <div class="midside">
        
        <div class="q">
        <h1 id="title">title:{{question.title}}</h1>
        <h1 id="text" style="font-size: 48px">text: </h1>
        <br>

        <!--<div class="Q">
                {% for line in LinedQuestion %}
                    <h1 class="line">{{ line }}</h1> <br>
                {% endfor %}
        </div>-->
        {% for line in LinedQuestion %}
                    <h1 class="line">{{ line }}</h1> <br>
        {% endfor %}
            <h5 id="ct" style="position: absolute;left: 330px;">created time: {{question.created_time}}</h5>
        </div>
    </div>    
    <div class="rside">
    
        <h2 style="margin-top: 5px;margin-left: 43px">answers of this question</h2>
    
        {% for text in LinedAnswers %}
            <h4>
                <div class="Answer{{ forloop.counter0 }}"
                            
        
                        {% for line in text %}
                            <span style="white-space: pre;">  {{ line }}</span>
                        {% endfor %}
                    
                    <pre> </pre>
                </div>
            </h4>
        {% endfor %}
    
    </div>

    <script src="{% static 'questions/asked-question.js' %}"></script>

</body>
</html>




"""
}