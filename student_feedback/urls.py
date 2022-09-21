from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('semester/', include('home.urls')),
    #path('admin/', admin.site.urls),
    path('', include('home.urls')),
    
    path('Success/', include('home.urls')),
    path('developer/',include('home.urls')), 
    
    #Admin path
    path('myadmin/',include('home.urls')),
    path('serve/',include('home.urls')),
    path('logout/',include('home.urls')),
    
    #### url setup for update faculty ####
    path('update_fac/',include('home.urls')),
    path('ic1update/',include('home.urls')),
    path('ic2update/',include('home.urls')),
    path('ic3update/',include('home.urls')),
    path('ic4update/',include('home.urls')),
    path('ic5update/',include('home.urls')),
    path('ic6update/',include('home.urls')),
    path('ic7update/',include('home.urls')),
    path('ic8update/',include('home.urls')),
    path('ic9update/',include('home.urls')),
    path('ic10update/',include('home.urls')),
    path('mca1update/',include('home.urls')),
    path('mca2update/',include('home.urls')),
    path('mca3update/',include('home.urls')),
    path('mca4update/',include('home.urls')),
    
    #Student path for IMCA-1
    path('IMCA1/', include('home.urls')),
    path('feedbackic1/', include('home.urls')),
    
    #operation path for IMCA1
    path('imca1total/', include('home.urls')),
    path('ic1report2618601/',include('home.urls')),
    path('ic1report2618602/',include('home.urls')),
    path('ic1report2618603/',include('home.urls')),
    path('ic1report2618604/',include('home.urls')),
    path('ic1report2618605/',include('home.urls')),
    path('delete_dbs_ic1/',include('home.urls')),
    
    #Student path for IMCA-2
    path('IMCA2/', include('home.urls')),
    path('feedbackic2/', include('home.urls')),
    
    #operation path for IMCA2
    path('imca2total/', include('home.urls')),
    path('ic2report2628601/',include('home.urls')),
    path('ic2report2628602/',include('home.urls')),
    path('ic2report2628603/',include('home.urls')),
    path('ic2report2628604/',include('home.urls')),
    path('ic2report2628605/',include('home.urls')),
    path('delete_dbs_ic2/',include('home.urls')),
    
    #Student path for IMCA-3
    path('IMCA3/', include('home.urls')),
    path('feedbackic3/', include('home.urls')),

    #operation path for IMCA3
    path('imca3total/', include('home.urls')),
    path('ic3report2638601/',include('home.urls')),
    path('ic3report2638602/',include('home.urls')),
    path('ic3report2638603/',include('home.urls')),
    path('ic3report2638604/',include('home.urls')),
    path('ic3report2638605/',include('home.urls')),
    path('delete_dbs_ic3/',include('home.urls')),
    
    #Student path for IMCA-4
    path('IMCA4/', include('home.urls')),
    path('feedbackic4/', include('home.urls')),

    #operation path for IMCA4
    path('imca4total/', include('home.urls')),
    path('ic4report2648601/',include('home.urls')),
    path('ic4report2648602/',include('home.urls')),
    path('ic4report2648603/',include('home.urls')),
    path('ic4report2648604/',include('home.urls')),
    path('ic4report2648605/',include('home.urls')),
    path('delete_dbs_ic4/',include('home.urls')),
    
    #Student path for IMCA-5
    path('IMCA5/', include('home.urls')),
    path('feedbackic5/', include('home.urls')),

    #operation path for IMCA5
    path('imca5total/', include('home.urls')),
    path('ic5report2658601/',include('home.urls')),
    path('ic5report2658602/',include('home.urls')),
    path('ic5report2658603/',include('home.urls')),
    path('ic5report2658604/',include('home.urls')),
    path('ic5report2658605/',include('home.urls')),
    path('delete_dbs_ic5/',include('home.urls')),
    
    #Student path for IMCA-6
    path('IMCA6/', include('home.urls')),
    path('feedbackic6/', include('home.urls')),

    #operation path for IMCA6
    path('imca6total/', include('home.urls')),
    path('ic6report2668601/',include('home.urls')),
    path('ic6report2668602/',include('home.urls')),
    path('ic6report2668603/',include('home.urls')),
    path('ic6report2668604/',include('home.urls')),
    path('ic6report2668605/',include('home.urls')),
    path('delete_dbs_ic6/',include('home.urls')),
    
    #Student path for IMCA-7
    path('IMCA7/', include('home.urls')),
    path('feedbackic7/', include('home.urls')),

    #operation path for IMCA7
    path('imca7total/', include('home.urls')),
    path('ic7report2678601/',include('home.urls')),
    path('ic7report2678602/',include('home.urls')),
    path('ic7report2678603/',include('home.urls')),
    path('ic7report2678604/',include('home.urls')),
    path('ic7report2678605/',include('home.urls')),
    path('delete_dbs_ic7/',include('home.urls')),
    
    #Student path for IMCA-8
    path('IMCA8/', include('home.urls')),
    path('feedbackic8/', include('home.urls')),

    #operation path for IMCA8
    path('imca8total/', include('home.urls')),
    path('ic8report2688601/',include('home.urls')),
    path('ic8report2688602/',include('home.urls')),
    path('ic8report2688603/',include('home.urls')),
    path('ic8report2688604/',include('home.urls')),
    path('ic8report2688605/',include('home.urls')),
    path('ic8report2688607/',include('home.urls')),
    path('delete_dbs_ic8/',include('home.urls')),   
]
