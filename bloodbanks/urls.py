from .views import HomePageView, donor_view, donor_detail_view, donor_update, donor_public_detail_view
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('donors/', donor_view, name="donor"),
    path('donors_view/', donor_detail_view, name="donor_detail"),
    path('donors_p_view/', donor_public_detail_view, name="donor_public_detail"),
    path('update_donor_details/', donor_update, name="donor_update"),

]
