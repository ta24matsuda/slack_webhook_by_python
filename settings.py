# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

WH = os.environ.get("SLACK_WEBHOOK") # 環境変数の値をWHに代入