"""Main function"""

from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from backend import TEMPLATE_DIR
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Log INFO and above
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


main_app = APIRouter()

logging.info(f"[PA_MAIN] Loading Template {TEMPLATE_DIR}")
print(f"[PA_MAIN] Loading Template {TEMPLATE_DIR}", flush=True)


tpl = Jinja2Templates(TEMPLATE_DIR)


@main_app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    """Testing"""
    return tpl.TemplateResponse("index.html", {"request": request})


@main_app.get("/ping", response_class=PlainTextResponse)
def ping() -> str:
    """Ping test"""
    return "pong"
