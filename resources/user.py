from flask_restful import Resource, reqparse
from models.user_model import UserModel


class UsersRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field can not be left blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field can not be left blank!"
    )
    def post(self):
        data = UsersRegister.parser.parse_args()

        user = UserModel.find_by_username(data['username'])
        if user:
            return {"message": "This user already exists"}, 400
    
        user = UserModel(**data)
        user.save_to_db()

        return {'message':"User created"}, 201