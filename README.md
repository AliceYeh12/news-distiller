# 📰 News Distiller

Browse or search the latest news in entertainment, sports, and technology, quickly and easily. Read top headlines, search for news about specific topics, and filter accordingly in a personalized news experience. Check it out [here](https://newsdistiller.herokuapp.com/)!

## Running Locally

### Clone the project.

    git clone https://github.com/AliceYeh12/news-distiller.git
    
### Set up virtual environment.

    python3 -m venv venv/
    source venv/bin/activate
    
### Install libraries and dependencies.

    pip3 install flask
    pip3 install gunicorn
    pip3 install python-dotenv
    pip3 install requests
    
### Setup debug mode.

    export FLASK_DEBUG=1
    
### Set environment variables.

    touch .env
    
Inside the .env file, add a line for the News API key:
    
    API_KEY={YOUR_API_KEY}
    
### Run.

    flask run
    
