from app import *
from app.db_table import *

@app.route('/logout')
def logout():
    token = request.cookies.get("token")
    response = make_response(redirect("/login"))
    response.set_cookie('token', '', expires=0)
    return response