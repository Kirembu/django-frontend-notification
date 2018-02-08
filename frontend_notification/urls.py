from django.conf.urls import url, include
from frontend_notification import views

urlpatterns = [
    # User notification for Customer UI
    url(r'^user_notification/', views.notification_list),
    url(r'^user_notification/', include('notifications.urls')),
    url(r'^notification_del_read/(.+)/$', views.notification_del_read),
    # Notification Status (read/unread) for customer UI
    url(r'^update_notification/(\d*)/$', views.update_notification),
]
