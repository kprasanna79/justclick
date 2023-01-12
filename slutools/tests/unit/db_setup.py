from slutools.models import User
from slutools import db

db.drop_all()
db.create_all()
u1 = User(username='kumaravelp',email='prasanna.kumaravel@health.slu.edu',password_hash='India123',
          name='Prasanna K', group='ITS',active=1)
db.session.add(u1)
db.session.commit()