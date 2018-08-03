import sys, time, json, io

from flask import Blueprint, Response, request, send_file
from flask_restful import Api, Resource

from app import logger
from app.api.file_watcher import FileWatcher

mod = Blueprint('api', __name__)
api = Api(mod)

class Hello(Resource):
    def get(self):
        logger.debug('asdfdsf')
        return 'blah'

class FileRetriever(Resource):
    def get(self):
        args = request.args
        logger.debug(args)
        data = b''
        with open(args['filename'], 'rb') as fin:
            data = io.BytesIO(fin.read())
            data.seek(0)
        return send_file(
            data,
            mimetype='image/jpeg',
            as_attachment=True,
            attachment_filename='%s.jpg' % 'a')

class ServerNotification(Resource):
    def get(self):
        def event_stream():
            fw = FileWatcher()
            fw.watch('./test/')
            try: 
                while True:
                    fw.reset()
                    evt_desc = fw.wait()
                    yield 'data: {}\n\n'.format(json.dumps(evt_desc))
            except:
                fw.stop()
        return Response(event_stream(), mimetype="text/event-stream")

api.add_resource(Hello, '/Hello')
api.add_resource(FileRetriever, '/FileRetriever')
api.add_resource(ServerNotification, '/ServerNotification')