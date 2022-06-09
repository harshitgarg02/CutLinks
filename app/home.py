from app import *
from app.db_table import *

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    token = request.cookies.get("token")
    isLogin = UserData.query.filter_by(token=request.cookies.get("token")).first()
    if isLogin:
        user_name_logged = isLogin.name
    else:
        user_name_logged = ""
        token = create_admin()
    if request.method == 'POST':
        url = request.form.get("url")
        custom_url = request.form.get("custom_url")
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
                return render_template('index.html', value="Custom URL already exists", url = url, custom_url=custom_url, user_name_home=user_name_logged, isLogin=isLogin)
            link = Shorten_Links(shorten_link=hash, destination_link=url, user_token=token)
            db.session.add(link)
            db.session.commit()
        return render_template('index.html', long_url = url, short_url=request.base_url+hash, user_name_home=user_name_logged, isLogin=isLogin)
    else:
        return render_template('index.html', user_name_home=user_name_logged, isLogin=isLogin)
