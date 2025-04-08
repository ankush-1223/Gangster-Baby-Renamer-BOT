import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28201702")

API_HASH = os.environ.get("API_HASH", "31c9bbed9c688b89736d94da7e89653b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","Ankush")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://ankush23:JYzSGlbjpFezDSWH@cluster0.ulzzd1m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0:AAGIOzaCCdIG45Wf5KdFsMT3d1nu5Awcx9Q")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
