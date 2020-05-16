"""{% extends 'index.html' %}
{% block content %}
{% for recipe in recipes %}

    {{recipe.name}}
    {{recipe.description}}
    {{recipe.time_to_prepare}}
    {{recipe.ingredients}}
    {{recipe.spices}}   
    {{recipe.cooking}}
    {{recipe.time_of_the_day}}
    {{recipe.cooked_meal}}


{% endfor %}
{% endblock %}"""


-----------------
<div class="row">
			<div class="input-field col s12"><i class="material-icons prefix">explore</i>
				<select id="region" class="region_name">
		      <option value="" disabled selected>Choose Region</option>
		      <option value="1">East Medditerenian</option>
		      <option value="2">West Medditerenian</option>
		      <option value="3">Central and South America</option>
              <option value="1">North Europe</option>
		      <option value="2">South and East Asia</option>
              <option value="2">Central Asia</option>
		      <option value="3">Pacific</option>
              <option value="3">Other(use )</option>
		    </select>
				<label>Culinary Region</label>
			</div>
		</div>
         <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">map</i>
				<textarea id="time_to_prepare" name="time_to_prepare" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">Time to prepare</label>
			</div>
		</div>
         <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">map</i>
				<textarea id="ingredients" name="ingredients" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">Ingredients and Spices</label>
			</div>
		</div>
         <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">edit</i>
				<textarea id="cooking" name="cooking" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">How to prepare and cook it?</label>
			</div>
		</div>
		</div>
			<div class="collapsible-body">
				<span>{{recipe.cooked_meal}}</span>
			</div>

-----------------------

<!-- <div class="row">
			<div class="input-field col s12"><i class="material-icons prefix">explore</i>
				<select id="region" class="region_name">
		      <option value="" disabled selected>Choose Region</option>
		      <option value="1">East Medditerenian</option>
		      <option value="2">West Medditerenian</option>
		      <option value="3">Central and South America</option>
              <option value="1">North Europe</option>
		      <option value="2">South and East Asia</option>
              <option value="2">Central Asia</option>
		      <option value="3">Pacific</option>
              <option value="3">Other(use )</option>
		    </select>
				<label>Culinary Region</label>
			</div>
		</div>
        
         <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">map</i>
				<textarea id="time_to_prepare" name="time_to_prepare" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">Time to prepare</label>
			</div>
		</div>
         <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">map</i>
				<textarea id="ingredients" name="ingredients" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">Ingredients</label>
			</div>
		</div>
         <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">map</i>
				<textarea id="spices" name="spices" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">Spices to Use</label>
			</div>
		</div>
         <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">edit</i>
				<textarea id="cooking" name="cooking" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">How to prepeare and cook it?</label>
			</div>
		</div>
                 <div class="row">
			<div class="input-field col s12">
				<i class="material-icons prefix">map</i>
				<textarea id="time_of_the_day" name="time_of_the_day" type="text" class="materialize-textarea"></textarea>
				<label for="icon_prefix">Suitable Time to Eat it</label>
			</div>
		</div> -->



<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome podvistorcheto,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
