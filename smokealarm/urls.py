from django.conf.urls.defaults import patterns, url


urlpatterns = patterns("smokealarm.views",
    url(r"^$", "report", name="smokealarm_report"),
)
