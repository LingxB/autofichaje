from dotenv import load_dotenv, find_dotenv
import os


def load_envar():
    load_dotenv(find_dotenv(raise_error_if_not_found=True, usecwd=True))


def get_envar(key):
    return os.environ.get(key)