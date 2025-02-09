from django.urls import path
from reminder_app.dfr_views.user_crud import UserListAPIView, UserUpdateAPIView, UserDetailAPIView, UserAddAPIView, \
    UserDeleteAPIView
from reminder_app.dfr_views.note_crud import NoteListAPIView, NoteUpdateAPIView, NoteDetailAPIView, NoteAddAPIView, \
    NoteDeleteAPIView
from reminder_app.views.home import GuestHomePage, AuthedUserHomePage
from reminder_app.views.registration import RegistrationPage
from reminder_app.views.authorization import AuthorizationPage
from reminder_app.views.account import AccountPage
from reminder_app.views.dashboard import DashboardPage
from reminder_app.views.change_account_data import ChangeAccountDataPage
from reminder_app.views.dashboard_filter import DashboardCompletedPage, DashboardUncompletedPage

app_name = 'reminder_app'

urlpatterns = [
    # api urls / user CRUD
    path('api/v1/useradd/', UserAddAPIView.as_view(), name="add-user"),
    path('api/v1/userlist/', UserListAPIView.as_view(), name="user-list"),
    path('api/v1/userdetail/<int:pk>/', UserDetailAPIView.as_view(), name="user-detail"),
    path('api/v1/userupdate/<int:pk>/', UserUpdateAPIView.as_view(), name="update-user"),
    path('api/v1/userdelete/<int:pk>/', UserDeleteAPIView.as_view(), name="delete-user"),
    # --- --- --- ---

    # api urls / notes CRUD
    path('api/v1/noteadd/', NoteAddAPIView.as_view(), name="add-note"),
    path('api/v1/notelist/', NoteListAPIView.as_view(), name="note-list"),
    path('api/v1/notedetail/<int:pk>/', NoteDetailAPIView.as_view(), name="note-detail"),
    path('api/v1/noteupdate/<int:pk>/', NoteUpdateAPIView.as_view(), name="update-note"),
    path('api/v1/notedelete/<int:pk>/', NoteDeleteAPIView.as_view(), name="delete-note"),
    # --- --- --- ---

    # site urls:

    # home
    path('', GuestHomePage.as_view(), name="guest-home"),
    path('homeauthed/<str:token>', AuthedUserHomePage.as_view(), name="authed-user-home"),
    # --- --- --- ---

    # reg and auth
    path('registration', RegistrationPage.as_view(), name="registration"),
    path('authorization', AuthorizationPage.as_view(), name="authorization"),
    # --- --- --- ---

    # account and change_account_data
    path('account/<str:token>', AccountPage.as_view(), name="account"),
    path('changeaccountdata/<str:data_to_change>/<str:token>', ChangeAccountDataPage.as_view(), name="account-data-change"),
    # --- --- --- ---

    # dashboard
    path('dashboard/<str:token>', DashboardPage.as_view(), name="dashboard"),
    path('completedtasks/<str:token>', DashboardCompletedPage.as_view(), name="dashboard-completed-filter"),
    path('uncompletedtasks/<str:token>', DashboardUncompletedPage.as_view(), name="dashboard-uncompleted-filter"),
    # --- --- --- ---

]
