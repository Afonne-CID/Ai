##OPEN API STUFF
OPENAI_API_KEY = "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"

## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
