#! ~/anaconda3/envs/se4g/bin/python
#Initialization of the application
from flaskblog import create_app


app = create_app()

if __name__ == '__main__':
   app.run(debug=True)

