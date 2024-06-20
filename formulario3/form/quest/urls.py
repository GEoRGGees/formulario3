from django.urls import path
from . import views

urlpatterns = [
    
    path('step1/', views.step1_view, name='step1'),
    path('step2/', views.step2_view, name='step2'),
    path('step3/', views.step3_view, name='step3'),
    path('step4/', views.step4_view, name='step4'),
    path('step5/', views.step5_view, name='step5'),
    path('step6/', views.step6_view, name='step6'),
    path('step7/', views.step7_view, name='step7'),
    path('step8/', views.step8_view, name='step8'),
    path('step10/', views.step10_view, name='step10'),
    path('step11/', views.step11_view, name='step11'),
    path('step12/', views.step12_view, name='step12'),
    path('done/', views.done_view, name='done'),
]
