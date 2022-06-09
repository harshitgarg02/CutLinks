from app import *
from app.db_table import *



@app.route('/register', methods=['GET', 'POST'])
def register():
    token = request.cookies.get("token")
    if token_valid(token):
        return redirect("/dashboard")
    else:
        if request.method == 'POST':
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            name = request.form['name']
            username_fetch = UserData.query.filter_by(username = username).first()
            email_fetch = UserData.query.filter_by(email = email).first()
            if username_fetch:
                return render_template('register.html', value="Username already Exists!", name=name, email=email, password=password)
            elif email_fetch:
                return render_template('register.html', value="Email already Registered!",name=name, username=username, password=password)
            elif not email_valid(email):
                return render_template('register.html', value="Email is Invalid!", name=name, username=username, password=password)
            elif password_invalid(password):
                return render_template('register.html', value="Password must be at least 8 characters long and contain at least one number, one special character, one uppercase and one lowercase letter!", name=name, username=username, email=email)
            else:
                token = generate_hash(128)
                while UserData.query.filter_by(token = token).first():
                    token = generate_hash(128)
                api_key = generate_hash(64)
                while UserData.query.filter_by(api_key = api_key).first():
                    api_key = generate_hash(64)
                if name=="":
                    name = "User"
                user = UserData(token= token, username=username, password=password, email=email, name=name, api_key= api_key)
                db.session.add(user)
                db.session.commit()
                response = make_response(redirect("/dashboard"))
                response.set_cookie('token', token)
                return response
        else:
            return render_template('register.html')