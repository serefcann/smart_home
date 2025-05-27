from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name= "static")
status = {"oturma_isik": False,
          "oturma_kapi":False,
          "koridor_isik":False,
          'yatak_isik':False,
          'yatak_kapi':False}

@app.get("/", response_class = HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, 
                                                     'oturma_isik':status["oturma_isik"],
                                                     'oturma_kapi':status['oturma_kapi'],
                                                     'koridor_isik':status['koridor_isik'],
                                                     'yatak_isik':status['yatak_isik'],
                                                     'yatak_kapi':status['yatak_kapi']})

@app.post("/toggle")
async def toggle(
    oturma_isik: str = Form(None),
    oturma_kapi: str = Form(None),
    koridor_isik: str = Form(None),
    yatak_isik: str = Form(None),
    yatak_kapi: str = Form(None),
):
    status["oturma_isik"] = oturma_isik == 'on' # on ise True degilse False
    status['oturma_kapi'] = oturma_kapi == 'on'
    status['koridor_isik'] = koridor_isik == 'on'
    status['yatak_isik'] = yatak_isik == 'on'
    status['yatak_kapi'] = yatak_kapi == 'on'
    

    return RedirectResponse("/", status_code=303)