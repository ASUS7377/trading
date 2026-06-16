from django.urls import path
from .views import add_task, administrator_view, toggle_task, toggle_task
from .views import dashboard
from .views import profile_view
from .views import add_trade
from .views import trades_history
from .views import calendar_view
from .views import statistics_view
from .views import trade_detail
from .views import login_view
from .views import logout_view
from .views import create_user_view
from .views import welcome_view
from .views import edit_trade
from .views import delete_trade
from .views import user_detail_view
from .views import edit_user_view
from .views import delete_user_view
from journal import views
from .views import todo_view
from .views import *

urlpatterns = [
    path(
        '',
        landing_page,
        name='landing'
    ),
    
    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'profile/',
        profile_view,
        name='profile'
    ),

    path(
        'trades/add/',
        add_trade,
        name='add_trade'
    ),

    path(
        'history/',
        trades_history,
        name='history'
    ),

    path(
        'calendar/',
        calendar_view,
        name='calendar'
    ),

    path(
        'calendar/<int:year>/<int:month>/',
        calendar_view,
        name='calendar_month'
    ),

    path(
        'statistics/',
        statistics_view,
        name='statistics'
    ),
    
    path(
        'trade/<int:pk>/edit/',
        edit_trade,
        name='edit_trade'
    ),

    path(
        'trade/<int:pk>/delete/',
        delete_trade,
        name='delete_trade'
    ),

    path(
    'trade/<int:pk>/',
    trade_detail,
    name='trade_detail'
    ),

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),
    path(
        'administrator/',
        administrator_view,
        name='administrator'
    ),

    path(
        'administrator/create-user/',
        create_user_view,
        name='create_user'
    ),

    path(
        'welcome/',
        welcome_view,
        name='welcome'
    ),

    path(
        'administrator/user/<int:user_id>/',
        user_detail_view,
        name='user_detail'
    ),

    path(
        'administrator/user/<int:user_id>/edit/',
        edit_user_view,
        name='edit_user'
    ),

    path(
        'administrator/user/<int:user_id>/delete/',
        delete_user_view,
        name='delete_user'
    ),

    path(
        'update-goal/',
        views.update_goal_view,
        name='update_goal'
    ),

    path(
        'export-excel/',
        views.export_trades_excel,
        name='export_excel'
    ),

    path(
        'todo/',
        todo_view,
        name='todo'
    ),
    
    path(
        'todo/add/',
        add_task,
        name='add_task'
    ),

    path(
        'todo/toggle/<int:task_id>/',
        toggle_task,
        name='toggle_task'
    ),

    path(
        'todo/delete/<int:task_id>/',
        delete_task,
        name='delete_task'
    ),


]