from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('create/', views.news_post_create_view, name='news_post_create'),
    path('news/', views.news_posts_view, name='news_posts'),
    path('update/<uuid:id>/', views.news_post_update_view, name='news_post_update'),
    path('delete/<uuid:id>/', views.news_post_delete_view, name='news_post_delete'),

    path('departments/iu_1/', views.iu_1_view, name="iu_1"),
    path('departments/iu_2/', views.iu_2_view, name="iu_2"),
    path('departments/iu_3/', views.iu_3_view, name="iu_3"),
    path('departments/iu_4/', views.iu_4_view, name="iu_4"),
    path('departments/iu_5/', views.iu_5_view, name="iu_5"),
    path('departments/iu_6/', views.iu_6_view, name="iu_6"),
    path('departments/iu_7/', views.iu_7_view, name="iu_7"),
    path('departments/iu_8/', views.iu_8_view, name="iu_8"),
    path('departments/iu_9/', views.iu_9_view, name="iu_9"),
    path('departments/iu_10/', views.iu_10_view, name="iu_10"),
    path('departments/iu_11/', views.iu_11_view, name="iu_11"),
    path('departments/iu_12/', views.iu_12_view, name="iu_12"),

    path('students/deans_office_schedule/', views.deans_office_schedule_view, name="deans_office_schedule"),
    path('students/student_council/', views.student_council_view, name="student_council"),
    path('students/session_countdown_timer/', views.session_countdown_timer_view, name="session_countdown_timer"),

    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

]
