from app import *
from app.db_table import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    token = request.cookies.get("token")
    if token_valid(token):
        return redirect("/dashboard")
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            username_fetch = UserData.query.filter_by(username=username).first()
            if username_fetch and username_fetch.password == password:
                response = make_response(redirect("/dashboard"))
                token = username_fetch.token
                response.set_cookie('token', token)
                return response
            else:
                return render_template('login.html',value=True,username=username)
        else:
            return render_template('login.html')
