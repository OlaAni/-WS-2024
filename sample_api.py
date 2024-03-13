from flask import Flask
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from flask_restful import reqparse
import graphene
import requests

app = Flask(__name__)
api = Api(app)



class index(Resource):
    def get(self):
        return {'getProducts': 'A complete JSON list of products is returned to the user and is stored in a local MongoDB database.',
                'getTitles': 'Return a list of product titles only.',
                'insertProduct': 'The user should be able to call this API endpoint using Postman and send across a product id, product title and product cost that will then be stored in the MongoDB database.',
                }
api.add_resource(index, '/')


class getProducts(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.products
        collection = db.products_data
        results = dumps(collection.find())

        return json.loads(results)
api.add_resource(getProducts, '/getProducts')

class Product(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    price = graphene.Decimal()

class Query(graphene.ObjectType):
    products = graphene.List(Product)
    
    def resolve_products(root, info):
        data = requests.get('http://127.0.0.1:5000/getProducts')

        json_content = json.loads(data.text)
        print("Json: ",json_content)

        # extractedTitle = json_content[0].get('title','')
        # print(extractedTitle)
        # return Product(title=extractedTitle)

        extractedTitles = [product['title'] for product in json_content]
        products_list = [Product(title=title) for title in extractedTitles]

        return products_list
    
class getTitles(Resource):
    def get(self):
        schema = graphene.Schema(query=Query)

        query = """
            {
                products {
                    title
                }
            }
        """

        results = schema.execute(query)
        print("final: ",results)
 
        return json.dumps(results.data["products"])
api.add_resource(getTitles, '/getTitles')

class insertProduct(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.products
        collection = db.products_data
        # Record to be inserted
        parser = reqparse.RequestParser()

        res = parser.add_argument('id', type=int, location='args')
        args = parser.parse_args()
        id = args['id']

        res = parser.add_argument('title', type=str, location='args')
        args = parser.parse_args()
        title = args['title']

        res = parser.add_argument('price', type=float, location='args')
        args = parser.parse_args()
        price = args['price']


        newRecord= {"id":id,"title": title, "price": price}
        res = collection.insert_one(newRecord)
        
        return {"status":"inserted"}
api.add_resource(insertProduct, '/insertProduct')

# class GetOne(Resource):
#     def get(self):
#         client = MongoClient("mongodb://root:example@localhost:27017/")
#         db = client.sales
#         collection = db.sales_data
#         # ID of the object
#         id = '65c4ba83f1edb9b32d909d9f'
#         query = {"_id": ObjectId(id)}
#         filter = {"_id": 0}
#         # find it
#         results = collection.find_one(query, filter)
#         print(results)
#         # dump to JSON
#         results = dumps(results)
#         #return
#         return json.loads(results)
# api.add_resource(GetOne, '/getOne')
# class GetProducts(Resource):
#     def get(self):
#         return {'id': '1221'}       
# api.add_resource(GetProducts, '/getProducts')



# class getSingleById(Resource):
#     def get(self):
#         client = MongoClient("mongodb://root:example@localhost:27017/")
#         db = client.sales
#         collection = db.sales_data

#         parser = reqparse.RequestParser()
#         res = parser.add_argument('id', type=str, location='args')
#         args = parser.parse_args()
#         id = args['id']

#         res = parser.add_argument('phoneNumber', type=str, location='args')
#         args = parser.parse_args()
#         phoneNumber = args['phoneNumber']
        
#         query = {"_id": ObjectId(id)}
#         filter = {"_id": 0}
#         results = collection.find_one(query, filter)

#         if(phoneNumber.isnumeric() and not phoneNumber.isspace()):
#             results["status"] = "valid"
#         else:
#             results["status"] = "false"

#         results = dumps(results)
        
#         return json.loads(results)


# api.add_resource(getSingleById, '/getSingleById')



            
if __name__ == '__main__':
    app.run(debug=True)
