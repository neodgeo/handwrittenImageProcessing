def base64saver(fileToSave, folder):
    import base64
    import uuid 

    id = uuid.uuid4()

    print(fileToSave['name'])
    path = './' + folder + '/' + str(id) + str(fileToSave['name'])
    with open(path, 'wb') as file:
        file.write(base64.b64decode(fileToSave['content'].split(",")[1:2][0]))

    print('the file ' +id+fileToSave['name'] + ' is saved')
    return path