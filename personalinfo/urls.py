from django.urls import path
from .views import (
	IndexView,
	CertificateView,
	PortfolioView,
	change_lang,
)



app_name = "personalinfo"

urlpatterns = [
	path('', IndexView.as_view(), name="home"),
	path('certificate/<int:pk>', CertificateView.as_view(), name="certificate-detail"),
	path('portfolio/<int:pk>', PortfolioView.as_view(), name="portfolio-detail"),
	path('change-lang', change_lang, name="change-lang"),
	]



