from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
#    path('', views.IndexView.as_view(), name='index'),
    path('create/<str:type>', views.ProjectCreate.as_view(), name='create'),
    path('<int:pk>/update', views.ProjectUpdate.as_view(), name='update'),
    path('<int:pk>/delete', views.ProjectDelete.as_view(), name='delete'),
    path('<int:pk>/', views.ProjectDetails.as_view(), name='details'),
    path('legal/create/', views.LegalEntityCreate.as_view(), name='legal_create'),
    path('legal/<int:pk>', views.LegalEntityDetails.as_view(), name='legal_details'),
    path('legal/<int:pk>/update', views.LegalEntityUpdate.as_view(), name='legal_update'),
    path('legal/<int:pk>/delete', views.LegalEntityDelete.as_view(), name='legal_delete'),
    path('legal/', views.LegalEntityList.as_view(), name='legal_list'),
    path('legal/<int:legal_entity_id>/members/add/', views.legal_member_add, name='legal_member_add'),
    path('legal/<int:legal_entity_id>/members/remove/<int:user_id>', views.legal_member_remove, name='legal_member_remove'),
    path('legal/<int:pk>/members', views.LegalEntityMemberList.as_view(), name='legal_member_list'),
    path('<int:project>/report/create/', views.ReportCreate.as_view(), name='report_create'),
    path('report/<int:pk>', views.ReportDetails.as_view(), name='report_details'),
    path('report/<int:pk>/update', views.ReportUpdate.as_view(), name='report_update'),
    path('report/<int:pk>/delete', views.ReportDelete.as_view(), name='report_delete'),
    path('<int:project>/report/list', views.ReportList.as_view(), name='report_list'),
    path('report/<int:pk>/vote-up', views.report_vote_up, name='report_vote_up'),
    path('report/<int:pk>/vote-down', views.report_vote_down, name='report_vote_down'),

    path('<int:project_id>/support/create/', views.support_create, name='support_create'),
    path('<int:project>/moneysupport/create/', views.MoneySupportCreate.as_view(), name='money_support_create'),
    path('support/<int:pk>', views.support_details, name='support_details'),
    path('moneysupport/<int:pk>', views.MoneySupportDetails.as_view(), name='money_support_details'),
    path('moneysupport/<int:pk>/update', views.MoneySupportUpdate.as_view(), name='money_support_update'),
    path('<int:project>/timesupport/create/<int:necessity>', views.TimeSupportCreate.as_view(), name='time_support_create'),
    path('timesupport/<int:pk>', views.TimeSupportDetails.as_view(), name='time_support_details'),
    path('timesupport/<int:pk>/update', views.TimeSupportUpdate.as_view(), name='time_support_update'),

    path('support/<int:pk>/<str:type>/delete', views.SupportDelete.as_view(), name='support_delete'),
    path('support/<int:pk>/<str:type>/accept', views.support_accept, name='support_accept'),
    path('support/<int:pk>/<str:type>/decline', views.support_decline, name='support_decline'),
    path('support/<int:pk>/<str:type>/delivered', views.support_delivered, name='support_delivered'),
    path('<int:project_id>/support/list', views.support_list, name='support_list'),
    path('accounts/<int:user_id>/support/list', views.user_support_list, name='user_support_list'),
    path('accounts/<int:user_id>/vote/list', views.user_vote_list, name='user_vote_list'),
    path('user-autocomplete/', views.UserAutocomplete.as_view(), name='user_autocomplete'),
    path('<int:pk>/follow', views.follow_project, name='follow_project'),
    path('<int:project>/announcement/create/', views.AnnouncementCreate.as_view(), name='announcement_create'),
    path('announcement/<int:pk>', views.AnnouncementDetails.as_view(), name='announcement_details'),
    path('announcement_update/<int:pk>/update', views.AnnouncementUpdate.as_view(), name='announcement_update'),
    path('announcement/<int:pk>/delete', views.AnnouncementDelete.as_view(), name='announcement_delete'),
    path('<int:project_id>/necessity/time/update', views.time_necessity_update, name='time_necessity_update'),
    path('<int:project_id>/necessity/thing/update', views.thing_necessity_update, name='thing_necessity_update'),
    path('<int:project_id>/necessity/time', views.TimeNecessityList.as_view(), name='time_necessity_list'),
    path('necessity/time/<int:pk>', views.TimeNecessityDetails.as_view(), name='time_necessity_details'),
    path('<int:project_id>/necessity/thing', views.ThingNecessityList.as_view(), name='thing_necessity_list'),

]
