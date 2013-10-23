from m2x.feeds import HasFeedMixin
from m2x.resource import Collection, Item


class Blueprint(Item, HasFeedMixin):
    PATH = 'blueprints/{id}'


class Blueprints(Collection):
    PATH = 'blueprints'
    ITEMS_KEY = 'blueprints'
    ITEM_CLASS = Blueprint
