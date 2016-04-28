# exam code, dude



To install this on your computer, run:

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
This installs your Python dependencies. Then you need to run your database
migrations with

```
python manage.py migrate
```

This will create a file called `db.sqlite3`, which is ignored in your
`.gitignore` file.

Now you're ready to run the application.Then you can run it with the following

```
python manage.py runserver localhost:5000
```
