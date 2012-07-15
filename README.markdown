## RackerTracker 2.0!
RackerTracker2.0 = RackerTracker1.0 + new Features() {
* Ability to specify 'competition dates', times from company lunch to company lunch
* Better admin page
 * Ability to query data in the past
 * Select Winner Animation
 * Ability to assign bages or awards

}

##TODO:
* Add a key to SelectWinner so people know which color they are.
* Badges
* Create user pages /racker/{id}
 * Display graphs of usage 
  * Possible resource: http://d3js.org/ or http://www.jqplot.com/
 * Display times won and bages (to come)
* How should picking the CompanyLunch work?
 * Pick two latest dates?
 * Have admin select dates?

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
     
