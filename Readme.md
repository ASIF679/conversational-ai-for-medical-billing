####
Medical AI Agent

A conversational AI system designed to automate medical appointment booking, patient handling, and reminders through intelligent tool-calling and database integration.

####

In order to run app 
use 
####
uvicorn app.main:app --reload
####

####
to insert seed_data in Database use 
'pythin -m app seed_data'

####
In order to Run Migrations
alembic revision --autogenerate -m "initial schema"

####

####
APply Migrations
'alembic upgrade head'

### when ever modify datbabase :::::
alembic revision --autogenerate -m "update"
alembic upgrade head
#####