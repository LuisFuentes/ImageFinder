# Original Blueprint design

#from flask import Flask
#from pageSearch.pagesearch import simple_page

#app = Flask(__name__)
#app.register_blueprint(simple_page)
#app.run(debug=True)



from pageSearch import app
app.run(debug=True)
