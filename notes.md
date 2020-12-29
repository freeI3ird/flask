## Flask Notes

### Environment Variables 
1. export FLASK_APP = file_name.py
2. export FLASK_DEBUG = 1 
	- turn on debug mode
	- No need to restart server after making changes.

### Running flask
1. from terminal
	- flask run 
2. from script
	- app = Flask(__name__)
	- app.run(debug=True)
	
### Templates 
1. Rendering Template: Using the template to produce/make/provide final output
2. `from flask import render_template` It is a function 
    - `render_template(template_name)`
        - Argument to this function is the name of template file in 
        the `templates` folder. There must be a folder with name `templates`
        - This function call is useful for static pages only. 
    - Dynamic Pages 
        - We want to add some data from our side into the template
        - `render_template(template_name, posts=data)`
            - This argument name *posts* will be available in the context 
            of the template and we can use its data there.
    - Template Engine in flask is *JINJA-2*, this allows us to write 
        code inside the html.
        - `{% Code block: Write code here  %}`
            - ```
              {% for post in posts %}
              {% endfor %}
              ```
          
        - `{{ Block: To print variables, directly write variables here }}`
        - Creating a block with a specific name 
            ```
            {% block block_name %} 
            {% endblock block_name %} 
            ```
            - here `block` is a keyword
        - Inherit the other template 
            - `{% extends "template_name.html" %}`
            - Then we can override the blocks inherited from parent template.
            - Inheritance allows us to re-use the same content, we don't have to write same thing
            everywhere. 
            - Power of Inheritance: If we need to change something then we will change it at one place
             and it will be reflected at all other places.
             
    
            
    
