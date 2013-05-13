from django.conf.urls import patterns, url


urlpatterns = patterns("smokealarm.views",
    url(r"^$", "report", name="smokealarm_report"),
)
