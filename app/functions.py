from app.db_table import *
from app import *   

def generate_hash(length):
    return "%x" % random.getrandbits(4*length)


def email_valid(email):
    pattern = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    result = re.findall(pattern, email)
    return result


def password_invalid(password):
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    result = re.findall(pattern, password)
    return not result


def shorten_link(token,url,custom_url=""):
        if not url:
            return [400,"URL is empty"]
        if not url.startswith("http"):
            url = "https://" + url
        if custom_url=="":
            hash = generate_hash(5)
            while Shorten_Links.query.filter_by(shorten_link=hash).first():
                hash = generate_hash(5)
            link = Shorten_Links(shorten_link=hash, destination_link=url, user_token=token)
            db.session.add(link)
            db.session.commit()
        else:
            custom_url = slugify(custom_url)
            hash = custom_url
            while Shorten_Links.query.filter_by(shorten_link=hash).first():
                return [400,"Custom URL already exists."]
            link = Shorten_Links(shorten_link=hash, destination_link=url, user_token=token)
            db.session.add(link)
            db.session.commit()
        return [200,base_url+hash]


def getInfo(id):
    if not id:
        return [400,"URL is empty."]
    if Shorten_Links.query.filter_by(shorten_link=id).first():
        link = Shorten_Links.query.filter_by(shorten_link=id).first()
        return [200,link.destination_link,link.click_count,str(link.created_at)]
    else:
        return [400, 'URL not found in Server.']

def incriment_api(token):
    user = UserData.query.filter_by(token=token).first()
    user.api_count += 1
    db.session.commit()


def token_valid(token):
    user_name = None
    if token:
        token_fetch = UserData.query.filter_by(token=token).first()
        if token_fetch:
            user_name = token_fetch
    return user_name

def create_admin():
    isAvailable = UserData.query.filter_by(username="admin").first()
    if not isAvailable:
        admin_token = generate_hash(128)
        while UserData.query.filter_by(token=admin_token).first():
            admin_token = generate_hash(128)
        user = UserData(token = admin_token, username="admin", password=admin_password, email=admin_email, name="Admin", api_key=generate_hash(64))
        db.session.add(user)
        db.session.commit()
        return admin_token
    else:
        return isAvailable.token
    