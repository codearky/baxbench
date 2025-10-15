from . import base
from . import calculator
from . import click_count
from . import compiler
from . import credit_card_service
from . import file_search
from . import forum
from . import frame_extract
from . import image_converter
from . import image_transfer
from . import logger
from . import login
from . import monitor
from . import pdf_cat
from . import pdf_to_text
from . import product_catalog
from . import profile_collection
from . import recipes
from . import recommendation_service
from . import regex_search
from . import secret_storage
from . import shop_overview
from . import shopping_cart_service
from . import song_downloader
from . import unsubscribe
from . import uptime_service
from . import user_creation
from . import wiki
from . import zip_to_txt

all_scenarios: list[base.Scenario] = [
    calculator.SCENARIO,
    click_count.SCENARIO,
    compiler.SCENARIO,
    credit_card_service.SCENARIO,
    file_search.SCENARIO,
    forum.SCENARIO,
    frame_extract.SCENARIO,
    image_converter.SCENARIO,
    image_transfer.SCENARIO,
    logger.SCENARIO,
    login.SCENARIO,
    monitor.SCENARIO,
    pdf_cat.SCENARIO,
    pdf_to_text.SCENARIO,
    product_catalog.SCENARIO,
    profile_collection.SCENARIO,
    recipes.SCENARIO,
    recommendation_service.SCENARIO,
    regex_search.SCENARIO,
    secret_storage.SCENARIO,
    shop_overview.SCENARIO,
    shopping_cart_service.SCENARIO,
    song_downloader.SCENARIO,
    unsubscribe.SCENARIO,
    uptime_service.SCENARIO,
    user_creation.SCENARIO,
    wiki.SCENARIO,
    zip_to_txt.SCENARIO,
]
