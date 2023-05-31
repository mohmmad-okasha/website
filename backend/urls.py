from django.urls import path
from rest_framework import routers
from . import api
# from . import views


router = routers.DefaultRouter()
router.register('subjects', api.subjects)
router.register('links', api.links)
router.register('settings', api.settings)

urlpatterns = router.urls
urlpatterns += [
    # to login
    path("login/", api.login, name="login"),
    # to upload files
    path("upload_file/", api.FileUploadView.as_view(), name='upload_file'),
    # to get max id
    path("get_max_id/", api.get_max_id, name="get_max_id"),
    # to remove file
    path("remove_file/", api.remove_file, name="remove_file"),


    # subjects
    path("subject_delete/<int:id>", api.subjects.destroy, name="subject_delete"),

    # to get subject id
    path("get_subject_id/", api.get_subject_id, name="get_subject_id"),

    # to get subject links
    path("get_links/", api.get_links, name="get_links"),

]
