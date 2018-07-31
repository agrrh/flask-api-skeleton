import uuid
from flask import Flask, jsonify


class API(object):
    """Routing high-level logic."""
    def __init__(self, config):
        self.config = config

        self.app = Flask(__name__)

        self.__routes_define()

    def __routes_define(self):
        @self.app.route("/", methods=['GET'])
        def index():
            """Index page. Return list of available routes as human-readable text message."""
            index = []

            for route in self.app.url_map._rules:
                if route.endpoint != 'static':
                    methods = '|'.join([_ for _ in route.methods if _ not in ('HEAD', 'OPTIONS')])
                    index.append((methods, route.rule, "\n  ", route.endpoint))
            index = sorted(index, key=lambda r: r[2])

            index = "\n\n".join([' '.join(route) for route in index])

            return index

        @self.app.route("/uuid/random", methods=['GET'])
        def uuid_get_random():
            """Return random UUID."""
            return jsonify(uuid.uuid4())

    def run(self):
        self.app.run(
            debug=self.config.debug,
            threaded=True,
            host=self.config.host,
            port=self.config.port
        )
