from django.urls import path
from .views import RegisterUser, LoginView, PostEventView, \
    ChangeActiveView, ChangeActiveViewFeedback, PostFeedbackView, \
    getAllEvents, getAllUser, getAllFeedback, getMyEvents, ActivateDeactivateUser
from rest_framework_simplejwt import views as jwt_views

app_name = 'blog'

urlpatterns = [
    # this is for the events creator registration
    path('register', RegisterUser),
    path('login', LoginView),
    path('refresh_token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # this is for the events creator to post, deactivate and get his own events
    path('event/create_event/', PostEventView),
    path('event/change_status/', ChangeActiveView),
    path('event/my_events/', getMyEvents),

    # this is for the users to view all events
    path('event/all_events/', getAllEvents),

    # this is for the admin to view all the events creator and disable the events creator
    path('event/all_event_creator', getAllUser),
    path('event/activate_deactivate_user', ActivateDeactivateUser),

    # this is for the user to view all the feedback and feeds his own
    path('feedback/create_feedback/', PostFeedbackView),
    path('feedback/all_feedback/', getAllFeedback),

    # this is for the admin to deactivate the feedback if it has sensitive information
    path('feedback/disable_feedback/', ChangeActiveViewFeedback),
]
