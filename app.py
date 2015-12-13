# coding: utf-8


import json
import sys
import code

from io import BytesIO, StringIO
from tornado import ioloop, web, template, gen
from tornado.concurrent import return_future


@return_future
def _eval(request, callback):
    ns = {}
    to_eval = json.loads(request.body.decode('utf-8'))['toEval']
    out, err = sys.stdout, sys.stderr
    fake_stdout, fake_stderr = StringIO(), StringIO()
    sys.stdout, sys.stderr = fake_stdout, fake_stderr
    console = code.InteractiveConsole(locals=ns)
    for statement in to_eval.split("\n"):
        if statement:
            console.push(statement)
        else:
            console.push('\n')
    sys.stdout, sys.stderr = out, err

    out_result, err_result = fake_stdout.getvalue(), fake_stderr.getvalue()

    callback({"out": out_result,
              "err": err_result
              })


loader = template.Loader('templates')


class MainHandler(web.RequestHandler):

    def get(self):
        self.write(loader.load("main.html").generate())


class EvalHandler(web.RequestHandler):

    @gen.coroutine
    def post(self):
        response = yield _eval(self.request)
        self.write(response)


def make_app():
    return web.Application([
        (r"/", MainHandler),
        (r"/eval", EvalHandler),
        (r'/static/(.*)', web.StaticFileHandler, {'path': 'static/'}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    ioloop.IOLoop.current().start()
