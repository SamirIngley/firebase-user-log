
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flask-user-log.firebaseio.com/'

})

# Tutorial: https://www.youtube.com/watch?v=EiddkXBK0-o&t=654s


'''
# Creating data
ref = db.reference('/')
ref.set({
    'User':
        {
            'user1': {
                'name': 'Samir',
                'lname': 'Ingle',
                'age': 23
            },

            'user2': {
                'name': 'Yoho',
                'lname': 'Pirate',
                'age': 27
            },
        }
})
'''

'''
# updating data

# first create a db reference, inside pass the path
ref = db.reference('User')
# child reference
useref = ref.child('user1')
useref.update({
    'name': 'Bingo'
})
'''

'''
# for multiple update
ref = db.reference('User')
ref.update({
    'user1/lname': 'newLname!',
    'user2/lname': 'brandNew'
})

'''

'''
# adding value using push

ref = db.reference('User2')

useref = ref.push({
    'name': 'Bob',
    'lname': 'hello',
    'email': 'wowan@email.com',
    'age': 34
})
'''

# retrieving data

ref = db.reference('User')
print(ref.get())