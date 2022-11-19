import datetime

from deta import Deta

from asgi import request_handler as rh
from asgi.models.request import Request
from asgi.models.response import Response
from utils.property_reader import YamlReader

app_configuration = YamlReader.get_configuration()
deta_client = Deta(project_key=app_configuration['deta']['project']['key'], project_id=app_configuration['deta']['project']['id'])
web_drive = deta_client.Drive("web")


app = rh.RequestHandler()


@app.put(path="/test-put")
async def put_test(request: Request, response: Response):
    service = deta_client.Base(name="test-put")
    data = request.dict_body
    res = service.put(data)
    await response.send_json(res)


@app.get(path="/test-get")
async def get_test(request: Request, response: Response):
    service = deta_client.Base(name="test-get-new-framework")
    key = "11"
    res = service.get(key)
    await response.send_json(res)


@app.get(path="/test/{path_parameter}/somevalue/{second_value}")
async def path_parameters_test(request: Request, response: Response):
    print(request.path_parameters)
    await response.send("ok")


@app.get(path="/deta_fetch")
async def deta_fetch_test(request: Request, response: Response):
    service = deta_client.Base(name="fetch-example-table")
    from_epoch = datetime.datetime.now() - datetime.timedelta(minutes=600)
    query = {"created?gt": int(from_epoch.timestamp())}
    await response.send_json(service.fetch(query).__dict__)


@app.get(path="/{resource:path}")
async def resources(request: Request, response: Response):
    resource = request.path
    if not request.path or request.path == "/":
        resource = "index.html"
    res = web_drive.get(resource)
    if res:
        await response.send_chunks(res.iter_chunks())
    else:
        await response.redirect(path="/")
