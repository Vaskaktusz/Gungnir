import settings
from gungnir import urls
from gungnir import wsdl

if __name__ == "__main__":
    wsdl.Flask(__name__).run(**settings.settings, errors=urls.errors, urls=urls.urls, url_prefix=urls.url_prefix)
