# Restaurant finder

Simple restaurant finder using Django

### Features
* Geolocate restaurant based on address
* List restaurant based on food ratings

### Installation

#### 1. Virtualenv

You should have virtualenv installed on your system. Simple create a virtualenv with projectname.

```$ virtualenv projectname```

### 2. Set up Database

Install Postgres and Postgis

```sudo apt-get install postgresql-9.5, postgresql-9.5-postgis postgresql-server-dev-9.5binutils libproj-dev gdal-bin```

Define your database credentials in settings.py file

### 3. Download

cd into the projectname folder and clone this repo

```git clone git@github.com:Manisha38/restaurant-finder.git```

### 4. Requirements

Finally some requirements for this project are mentioned in requirements.txt in project root directory. Install it using pip

```$ pip install -r requirments.txt```

### Secret Key

Create and activate the Google Maps JavaScript API, which generates a API key. Copy this key in ```settings.py``` file in place of google-app-secret-key .

```GOOGLE_MAP_API_KEY = "google-app-secret-key"```

### Go!

Migrate to database and run

``` python manage makemigrations
python manage migrate
python manage runserver
```


