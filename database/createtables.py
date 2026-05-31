from database.initdb import db

import sys
sys.path.append('..')

from backend import app

with app.app_context():
    db.create_all()
    print("Tablolar başarıyla oluşturuldu!")
