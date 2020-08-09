# https://docs.djangoproject.com/en/2.0/intro/tutorial01/


# python3 manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying sessions.0001_initial... OK



# python3 manage.py makemigrations polls
# Migrations for 'polls':
#   polls/migrations/0001_initial.py
#     - Create model Question
#     - Create model Choice

# python3 manage.py sqlmigrate polls 0001
# BEGIN;
# --
# -- Create model Question
# --
# CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
# --
# -- Create model Choice
# --
# CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
# CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
# COMMIT;



# python3 manage.py check
# System check identified no issues (0 silenced).


# python3 manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, polls, sessions
# Running migrations:
#   Applying polls.0001_initial... OK

#######################################
#  python3 manage.py shell
# Python 3.8.2 (default, Jul 16 2020, 14:00:26)
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from polls.models import Choice, Question
# >>> Question.objects.all()
# <QuerySet []>
# >>> from django.utils import timezone
# >>> q = Question(question_text="What's new?", pub_date=timezone.now())
# >>> q.save()
# >>> q.id
# 1
# >>> q.question_text
# "What's new?"
# >>> q.pub_date
# datetime.datetime(2020, 8, 9, 14, 53, 14, 337947, tzinfo=<UTC>)
# >>> q.question_text = "What's up?"
# >>> Question.objects.all()
# <QuerySet [<Question: Question object (1)>]>
# >>> quit()
# ➜  mysite git:(master) ✗ python3 manage.py shell
# Python 3.8.2 (default, Jul 16 2020, 14:00:26)
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from polls.models import Choice, Question
# >>> Question.objects.all()
# <QuerySet [<Question: What's new?>]>
# >>> Question.objects.filter(id=1)
# <QuerySet [<Question: What's new?>]>
# >>> Question.objects.filter(question_text__startswith='What')
# <QuerySet [<Question: What's new?>]>
# >>> from django.utils import timezone
# >>> current_year = timezone.now().year
# >>> Question.objects.get(pub_date__year=current_year)
# <Question: What's new?>
# >>> Question.objects.get(pk=1)
# <Question: What's new?>
# >>> q = Question.objects.get(pk=1)
# >>> q.was_published_recently()
# True
# >>> q.choice_set.all()
# <QuerySet []>
# >>> q.choice_set.create(choice_text='Not much', votes=0)
# <Choice: Not much>
# >>> q.choice_set.create(choice_text='The sky', votes=0)
# <Choice: The sky>
# >>> q.choice_set.create(choice_text='Just hacking again', votes=0)
# <Choice: Just hacking again>
# >>> c.question
# Traceback (most recent call last):
#   File "/usr/lib/python3.8/code.py", line 90, in runcode
#     exec(code, self.locals)
#   File "<console>", line 1, in <module>
# NameError: name 'c' is not defined
# >>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
# >>> c.question
# <Question: What's new?>
# >>> quit()
# ➜  mysite git:(master) ✗ python3 manage.py createsuperuser
# Username (leave blank to use 'cevher'): admin
# Email address: admin@localhost.com
# Password:
# Password (again):
# The password is too similar to the username.
# This password is too short. It must contain at least 8 characters.
# This password is too common.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
# ➜  mysite git:(master) ✗ python3 manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...
#
# System check identified no issues (0 silenced).
# August 09, 2020 - 18:01:40
# Django version 2.2.12, using settings 'mysite.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
# [09/Aug/2020 18:01:50] "GET /admin/ HTTP/1.1" 302 0
# [09/Aug/2020 18:01:50] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1823
# [09/Aug/2020 18:01:55] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0




