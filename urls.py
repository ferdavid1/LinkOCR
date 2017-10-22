from django.conf.urls import url 

import views

urlpatterns = [
	url(r'^linkocr/views', views.open)
]