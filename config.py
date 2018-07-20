import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ACTION_NETWORK_KEY = os.environ.get('ACTION_NETWORK_KEY')
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_SECRET = os.environ.get('TWILIO_SECRET')
    TWILIO_FLOW_SID = os.environ.get('TWILIO_FLOW_SID')
    TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

    PHONE_RECIPIENT_OVERRIDE = os.environ.get('PHONE_RECIPIENT_OVERRIDE')
    REQUESTS_VERIFY = os.environ.get('REQUESTS_VERIFY')