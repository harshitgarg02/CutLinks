import re
from app import *



@app.route('/dashboard')
def dashboard():
    token = request.cookies.get('token')
    query = token_valid(token)
    if query:
        links_query_obj =  Shorten_Links.query.filter_by(user_token=token)
        links = []
        redirects_count = 0
        for i in links_query_obj:
            links.append((base_url+i.shorten_link, i.destination_link, i.click_count, str(i.created_at)))
            redirects_count += i.click_count
        links_count = links_query_obj.count()
        api_calls_count = query.api_count
        return render_template('dashboard.html',api_key = query.api_key, user_name_home = query.name, isLogin = query, api_calls_count = api_calls_count, links_count = links_count, redirects_count = redirects_count, links = links)
    else:
        return redirect("/login")