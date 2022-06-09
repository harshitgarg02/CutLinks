from app import *
from app.db_table import *

@app.route('/<id>')
def url_redirect(id):
    if Shorten_Links.query.filter_by(shorten_link=id).first():
        link = Shorten_Links.query.filter_by(shorten_link=id).first()
        link.click_count += 1
        db.session.commit()
        return redirect(link.destination_link)
    else:
        return render_template('404.html')