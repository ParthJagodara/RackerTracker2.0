## RackerTracker 2.0!
RackerTracker2.0 = RackerTracker1.0 + new Features() {
* Ability to specify 'competition dates', times from company lunch to company lunch
* Better admin page
 * Ability to query data in the past
 * Select Winner Animation
 * Ability to assign bages or awards

}

##TODO:
* /ajax/workouts shouldn't return rackers with 0 workouts
* Badges
* Create user pages /racker/{id} or use modal on standings page
 * Display graphs of usage 
  * Possible resource: http://d3js.org/, http://www.jqplot.com/, or raphaeljs.com
 * Display number of times won and badges

## Instruction to create SQLite Database

Create the table definitions, then sync the DB.

This should be done every time a new class is added to the model.

<pre><code>python manage.py sql rackertracker

python manage.py syncdb</code></pre>

If this fails, you may need to reset the tables

<pre><code>python manage.py reset rackertracker</code></pre>

NOTE!

Currently, you need to add two company lunches to the database.

If they don't exist, the website will not work.

I don't think there will ever be a case where there isn't two company dates.

Although, validation would be nice.

## How to start the Django server

<pre>python manage.py runserver 0.0.0.0:8000</pre>

## Set up a super admin

Open django shell in the directory containing manage.py

<pre>python manage.py shell</pre>

To set up a user with superuser permissions,

<pre><code>>>>from django.contrib.auth.models import User
>>>user = User.objects.create_user('username', 'email@email.com', 'password')
>>>user.is_staff = True
>>>user.is_superuser = True
>>>user.save()</code></pre>
     
