from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name= "static")
status = {"durum1": False,
          "durum2":False}

@app.get("/", response_class = HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, 
                                                     'durum1':status["durum1"],
                                                     'durum2':status['durum2']})

@app.post("/toggle")
async def toggle(durum1: str = Form(None),
                 durum2: str = Form(None)):
    status['durum1'] = durum1 == 'on'
    status["durum2"] = durum2 == 'on'

    return RedirectResponse("/", status_code=303)