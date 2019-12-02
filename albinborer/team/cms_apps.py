from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class TeamApphook(CMSApp):
    app_name = "Team"
    name = "Team Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["team.urls"]
