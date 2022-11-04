from django.urls import path
from .views import (
ExamView,
AssignmentCreateView,
AssignmentView,
AssignmentDeleteView,
ExamCreateView,
ExamListView,
AssignmentSubmissionView,
ExamDeleteView,
ExamSubmissionView,
ExamSubmissionListView,
ExamScoreView,
AssignmentSubmissionListView,
AssignmentScoreView,
AssignmentSubmissionDelete,
ExamSubmissionDelete

)
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"

urlpatterns = [
                  path('exam/', ExamView.as_view(), name='exam'),
                  path('assignment-create/', AssignmentCreateView.as_view(), name='assignment-create'),
                  path('assignment/', AssignmentView.as_view(), name='assignment-list'),
                  path('<pk>/delete/', AssignmentDeleteView.as_view(), name='delete-assignment'),
                  path('exam-create/', ExamCreateView.as_view(), name='exam-create'),
                  path('exam-list/', ExamListView.as_view(), name='exam-list'),
                  path('<pk>/delete/', ExamDeleteView.as_view(), name='delete-exam'),
                  path('assignment-submission/', AssignmentSubmissionView.as_view(), name='assignment-submission'),
                  path('<pk>/assignment-submit-score/', AssignmentScoreView.as_view(), name='assignment-score'),
                  path('exam-submission/', ExamSubmissionView.as_view(), name='exam-submission'),
                  path('exam-submission-list/', ExamSubmissionListView.as_view(), name='exam-submission-list'),
                  path('<pk>/exam-submit-score/',ExamScoreView.as_view(), name='exam-score'),
                  path('assignment-submission-list/', AssignmentSubmissionListView.as_view(), name='assignment-submission-list'),
                  path('<pk>/assginment-submit-delete/', AssignmentSubmissionDelete.as_view(), name='assignment-submission-delete'),
                  path('<pk>/assignment-submit-delete/', ExamSubmissionDelete.as_view(), name='exam-submission-delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)