Superhero API

Welcome to the Superhero API! This API allows you to manage superheroes and their powers. You can create, read, update, and delete heroes and their powers.

Table of Contents

- Installation
- Usage
- Endpoints
- Database
- Running Tests
-Deployment

Installation

1. Clone the repository:

   ```sh
https://github.com/Moringa-SDF-PTO5/superheroes-chrispine-ochieng

   cd superhero-api

2.Create and activate a virtual environment:

   python -m venv venv
   
   source venv/bin/activate  
   
   On Windows use `venv\Scripts\activate`
   

3. Install the dependencies:
4. 
   pip install -r requirements.txt

5. Set up the database:

   flask db init
   
   flask db migrate
   
   flask db upgrade

7. Seed the database with initial data:


   python seeds.py

## Usage

1. Run the application:

   flask run

2. Access the application:

   Open your web browser and navigate to `(http://127.0.0.1:5000/)`. You should see the "Welcome to Superhero API" message.

Endpoints

Heroes

- GET /heroes

  Returns a list of all heroes.

- GET /heroes/<id>

  Returns a single hero by ID.

Powers

- GET /powers

  Returns a list of all powers.

- GET /powers/<id>

  Returns a single power by ID.

- PATCH /powers/<id>

  Updates a power's description. Requires a JSON body with a `description` field.

Hero Powers

- POST /hero_powers

  Creates a new hero power association. Requires a JSON body with `hero_id`, `power_id`, and `strength`.

Database

This application uses SQLite as its database. The database schema includes three tables:

- heroes: Stores hero information.

- powers: Stores power information.

- hero_powers: Stores the many-to-many relationship between heroes and powers, including the `strength` of the power for the hero.

Running Tests

1. Install testing dependencies:

   pip install -r requirements-dev.txt

2. Run the tests:

   python -m unittest discover tests
   
Deployment

To deploy your application, you can use Gunicorn, a WSGI HTTP server for UNIX. Here are the steps to deploy using Gunicorn:

1. Create a `wsgi.py` file:

   from app import app

   if __name__ == "__main__":
       app.run()

2. Install Gunicorn:
3. 
   pip install gunicorn

4. Run your application with Gunicorn:
5. 
   gunicorn --bind 0.0.0.0:8000 wsgi:app
   ```

6. Access the application:

   Open your web browser and navigate to `http://127.0.0.1:5000`. You should see the "Welcome to Superhero API" message.

Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Replace `yourusername` in the clone URL with your actual GitHub username. This README file provides a comprehensive guide to installing, using, and deploying your Flask application.application.
