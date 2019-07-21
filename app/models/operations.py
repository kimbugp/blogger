from app import db

class Operations():

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self