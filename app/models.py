from app import db

class Box(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(128), index=True)
    name = db.Column(db.String(128), index=True)
    district = db.Column(db.String(128), index=True)

    voters = db.relationship('Voter', backref='pollingstation', lazy='dynamic')

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.Integer, index=True, unique=True)
    address_no = db.Column(db.String(64), index=True)
    address_st = db.Column(db.String(254), index=True)
    address_town = db.Column(db.String(128), index=True)
    electoral_div = db.Column(db.String(254), index=True)
    voting_rights = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)

    box_id = db.Column(db.Integer, db.ForeignKey('box.id'))
    contacts = db.relationship('Contact', backref='voter', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.first_name, self.last_name)


class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)

    contacts = db.relationship('Contact', backref='volunteer', lazy='dynamic')

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=db.func.now())
    result = db.Column(db.String(64), index=True)
    support_lvl = db.Column(db.Integer, index=True)
    notes = db.Column(db.String(1024), index=True)

    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.id'))
    voter_id = db.Column(db.Integer, db.ForeignKey('voter.id'))

