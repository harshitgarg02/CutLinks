from app import *
from app.db_table import *

shorten_parser = reqparse.RequestParser()
shorten_parser.add_argument('api_key', type=str, help='Taken that you get when you register on our website',location='values')
shorten_parser.add_argument('long_url', type=str, help='URL that needs to be shortened.',location='values')
shorten_parser.add_argument('custom_url', type=str, help='Custom Slug if needed.',location='values')
getinfo_parser = reqparse.RequestParser()
getinfo_parser.add_argument('api_key', type=str, help='Taken that you get when you register on our website',location='values')
getinfo_parser.add_argument('short_url', type=str, help='Shortened URL Prefixed with Base URL whose data needs to be Fetched.',location='values')

class shorten(Resource):
    def post(self):
        token,url,custom_url = create_admin(), "", ""
        args = shorten_parser.parse_args()
        if args.get('api_key',""):
            temp = UserData.query.filter_by(api_key=args['api_key']).first()
            if temp:
                token = temp.token
            else:
                return {"status": 400, "message": "API Key is not valid. Either make a call without API Key or pass a valid API Key."}
        incriment_api(token)
        if args.get('long_url',""):
            url = args['long_url']
        if args.get('custom_url',""):
            custom_url = args['custom_url']
        result = shorten_link(token,url,custom_url)
        if result[0]==200:
            return {"status": 200, "message": "Request Sucessfully Executed." , "data": {"Short URL": result[1], "Destination URL": url}}
        else:
            return {"status": result[0], "message": result[1]}

class getinfo(Resource):
    def get(self):
        token = create_admin()
        args = getinfo_parser.parse_args()
        if args.get('api_key',""):
            temp = UserData.query.filter_by(api_key=args['api_key']).first()
            if temp:
                token = temp.token
            else:
                return {"status": 400, "message": "API Key is not valid. Either make a call without API Key or pass a valid API Key."}
        incriment_api(token)
        id = args.get('short_url',"/").split('/')
        id = [""] + id
        print(id)
        if id[-1]=="":
            id = id[-2]
        else:
            id = id[-1]
        result = getInfo(id)
        if result[0]==200:
            return {"status": 200, "message": "Request Sucessfully Executed." , "data": {"Short URL": base_url+id, "Destination URL": result[1], "No. of Clicks": result[2], "Created At": result[3]}}
        else:
            return {"status": result[0], "message": result[1]}

api.add_resource(shorten, '/shorten/' )
api.add_resource(getinfo, '/getinfo/' )