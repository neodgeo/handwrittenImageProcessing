def base64saver(fileToSave, folder):
    import base64
    import uuid 

    id = uuid.uuid4()

    path = './' + folder + '/' + str(id) + '.png'
    with open(path, 'wb') as file:
        file.write(base64.b64decode(fileToSave['content']))

    print('the file ' +str(id)+ '.png is saved')
    return folder + '/' + str(id) + '.png'