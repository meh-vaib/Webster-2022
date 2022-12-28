
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
path("about/", views.about, name="AboutUs"),
path("contact/", views.contact, name="ContactUs"),
path("tracker/", views.tracker, name="TrackingStatus"),

path("search/", views.search, name="Search"),
path("productview/", views.productView, name="ProductView"),
path("checkout/", views.checkout, name="Checkout"),
path("anvils/",views.anvil ,name="Anvil"),
path("hammer/",views.hammer ,name="Hammer"),
path("nuts/",views.nuts ,name="Nuts"),
path("chains/",views.chains ,name="Chains"),
path("misc/",views.misc ,name="Misc"),
path("forms/contact.php",views.contact ,name="Form"),
]