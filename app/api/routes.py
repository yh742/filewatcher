import sys, time, json, io, os

from flask import Blueprint, Response, request, send_file
from flask_restful import Api, Resource

from app import config, logger
from app.api.file_watcher import FileWatcher

mod = Blueprint('api', __name__)
api = Api(mod)

# initialize file watcher to WATCH_FOLDER
file_watcher = FileWatcher()
file_watcher.watch(config['WATCH_FOLDER'])

class Hello(Resource):
    def get(self):
        logger.debug('Hello!')
        return 'blah'

class FileRetriever(Resource):
    def get(self):
        args = request.args
        logger.debug(args)
        logger.debug(os.getcwd())
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
            logger.debug('connected to event stream')
            try: 
                while True:
                    evt_desc = file_watcher.wait()
                    logger.debug('Dumping Object: {}'.format(evt_desc))
                    yield 'data: {}\n\n'.format(json.dumps(evt_desc['src_path']))
            except Exception as e:
                logger.debug('exception occured: ' + str(e))
        return Response(event_stream(), mimetype="text/event-stream")


api.add_resource(Hello, '/Hello')
api.add_resource(FileRetriever, '/FileRetriever')
api.add_resource(ServerNotification, '/ServerNotification')