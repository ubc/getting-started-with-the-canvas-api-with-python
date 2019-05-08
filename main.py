import dotenv
import os
import canvasapi

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://ubc.instructure.com'

canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

result = canvas_api.get_user('self')

print(result.attributes)
