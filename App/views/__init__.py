# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from .staff import staff_views
from .review import review_views
from .student import student_views


views = [user_views, index_views, auth_views] 
views.extend([staff_views, review_views, student_views])