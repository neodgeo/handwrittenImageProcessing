#!/root/.virtualenvs/OpenCV-master-py3/bin/python
from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields
from base64saver import base64saver
from segmentation import to_lines, to_words, result, read_image

import numpy as np
import os
import json

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation') #,doc=False

app.register_blueprint(blueprint)

app.config['SWAGGER_UI_JSONEDITOR'] = True

a_doc = api.model('wordDetection', {'content' : fields.String('The content base64 encoded'), 'name' : fields.String('Name of the file')})
 

@api.route('/wordDetection')
class Manager(Resource):

    @api.expect(a_doc)
    def post(self):
        request = api.payload 
        fileSave = base64saver(request, 'jd')
        if fileSave:

            image = read_image(fileSave)

            s = ""

            lines = to_lines(image)
            for line in lines:
                words = to_words(line)
                for word in words:
                    # print(word.shape)
                    w, prob = result(word, model)
                    s = s + " " + w

            
            return {'success' : 'true','data' : s}

        else:
            return {'error' : 'file not saved'}, 401 



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)