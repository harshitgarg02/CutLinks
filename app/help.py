from app import *


@app.route('/about')
def about():
    query = token_valid(request.cookies.get("token"))
    user_name_home = ""
    if query:
        user_name_home = query.name
    return render_template('about.html', user_name_home = user_name_home, isLogin = query )

@app.route('/api')
def api():
    query = token_valid(request.cookies.get("token"))
    user_name_home = ""
    if query:
        user_name_home = query.name
    return render_template('api.html', user_name_home = user_name_home, isLogin = query )