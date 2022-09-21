from unicodedata import name
from django.urls import path
from home import views
from home.views import myadmin

urlpatterns = [
    path("", views.index, name='home'),
    
    #student validation
    path("insert_student",views.insert_student, name="insert_student"),
    path("delete_student",views.delete_student, name="delete_student"),
    
    #developer
    path("Success", views.successic3, name="Success"),
    path("developer", views.developer, name="developer"),
    
    #admin path
    path("myadmin", views.myadmin, name="myadmin"),
    path("serve", views.sem_serve, name="serve"),
    path("logout", views.admin_logout, name="logout"),
    path("clicklogout", views.clicklogout, name="clicklogout"),
    path("change_password", views.change_password, name="change_password"),
    
    #### url setup for update faculty ####
    path("update_fac", views.update_faculty, name="update_fac"),
    path("ic1update", views.update_ic1, name="ic1update"),
    path("ic2update", views.update_ic2, name="ic2update"),
    path("ic3update", views.update_ic3, name="ic3update"),
    path("ic4update", views.update_ic4, name="ic4update"),
    path("ic5update", views.update_ic5, name="ic5update"),
    path("ic6update", views.update_ic6, name="ic6update"),
    path("ic7update", views.update_ic7, name="ic7update"),
    path("ic8update", views.update_ic8, name="ic8update"),
    path("ic9update", views.update_ic9, name="ic9update"),
    path("ic10update", views.update_ic10, name="ic10update"),
    path("mca1update", views.update_mca1, name="mca1update"),
    path("mca2update", views.update_mca2, name="mca2update"),
    path("mca3update", views.update_mca3, name="mca3update"),
    path("mca4update", views.update_mca4, name="mca4update"),
    
    #student path IMCA1
    path("IMCA1", views.ic1, name="IMCA1"),
    path("feedbackic1", views.ic1_main, name="feedbackic1"),
    
    #operation path for IMCA1
    path("imca1total", views.imca1total, name="imca1total"),
    path("delete_dbs_ic1", views.delete_dbs_ic1, name="delete_dbs_ic1"),
    path("ic1report2618601", views.ic1_report_2618601, name="ic1report2618601"),
    path("ic1report2618602", views.ic1_report_2618602, name="ic1report2618602"),
    path("ic1report2618603", views.ic1_report_2618603, name="ic1report2618603"),
    path("ic1report2618604", views.ic1_report_2618604, name="ic1report2618604"),
    path("ic1report2618605", views.ic1_report_2618605, name="ic1report2618605"),
    
    #student path IMCA2
    path("IMCA2", views.ic2, name="IMCA2"),
    path("feedbackic2", views.ic2_main, name="feedbackic2"),
    
    #operation path for IMCA2
    path("imca2total", views.imca2total, name="imca2total"),
    path("delete_dbs_ic2", views.delete_dbs_ic2, name="delete_dbs_ic2"),
    path("ic2report2628601", views.ic2_report_2628601, name="ic2report2628601"),
    path("ic2report2628602", views.ic2_report_2628602, name="ic2report2628602"),
    path("ic2report2628603", views.ic2_report_2628603, name="ic2report2628603"),
    path("ic2report2628604", views.ic2_report_2628604, name="ic2report2628604"),
    path("ic2report2628605", views.ic2_report_2628605, name="ic2report2628605"),
    
    #student path IMCA3
    path("IMCA3", views.ic3, name="IMCA3"),
    path("feedbackic3", views.ic3_main, name="feedbackic3"),
    
    #operation path for IMCA3
    path("imca3total", views.imca3total, name="imca3total"),
    path("delete_dbs_ic3", views.delete_dbs_ic3, name="delete_dbs_ic3"),
    path("ic3report2638601", views.ic3_report_2638601, name="ic3report2638601"),
    path("ic3report2638602", views.ic3_report_2638602, name="ic3report2638602"),
    path("ic3report2638603", views.ic3_report_2638603, name="ic3report2638603"),
    path("ic3report2638604", views.ic3_report_2638604, name="ic3report2638604"),
    path("ic3report2638605", views.ic3_report_2638605, name="ic3report2638605"),
    
    #student path IMCA4
    path("IMCA4", views.ic4, name="IMCA4"),
    path("feedbackic4", views.ic4_main, name="feedbackic4"),
    
    #operation path for IMCA4
    path("imca4total", views.imca4total, name="imca4total"),
    path("delete_dbs_ic4", views.delete_dbs_ic4, name="delete_dbs_ic4"),
    path("ic4report2648601", views.ic4_report_2648601, name="ic4report2648601"),
    path("ic4report2648602", views.ic4_report_2648602, name="ic4report2648602"),
    path("ic4report2648603", views.ic4_report_2648603, name="ic4report2648603"),
    path("ic4report2648604", views.ic4_report_2648604, name="ic4report2648604"),
    path("ic4report2648605", views.ic4_report_2648605, name="ic4report2648605"),
    
    #student path IMCA5
    path("IMCA5", views.ic5, name="IMCA5"),
    path("feedbackic5", views.ic5_main, name="feedbackic5"),
    
    #operation path for IMCA5
    path("imca5total", views.imca5total, name="imca5total"),
    path("delete_dbs_ic5", views.delete_dbs_ic5, name="delete_dbs_ic5"),
    path("ic5report2658601", views.ic5_report_2658601, name="ic5report2658601"),
    path("ic5report2658602", views.ic5_report_2658602, name="ic5report2658602"),
    path("ic5report2658603", views.ic5_report_2658603, name="ic5report2658603"),
    path("ic5report2658604", views.ic5_report_2658604, name="ic5report2658604"),
    path("ic5report2658605", views.ic5_report_2658605, name="ic5report2658605"),
    
    #student path IMCA6
    path("IMCA6", views.ic6, name="IMCA6"),
    path("feedbackic6", views.ic6_main, name="feedbackic6"),
    
    #operation path for IMCA6
    path("imca6total", views.imca6total, name="imca6total"),
    path("delete_dbs_ic6", views.delete_dbs_ic6, name="delete_dbs_ic6"),
    path("ic6report2668601", views.ic6_report_2668601, name="ic6report2668601"),
    path("ic6report2668602", views.ic6_report_2668602, name="ic6report2668602"),
    path("ic6report2668603", views.ic6_report_2668603, name="ic6report2668603"),
    path("ic6report2668604", views.ic6_report_2668604, name="ic6report2668604"),
    path("ic6report2668605", views.ic6_report_2668605, name="ic6report2668605"),
    
    #student path IMCA7
    path("IMCA7", views.ic7, name="IMCA7"),
    path("feedbackic7", views.ic7_main, name="feedbackic7"),
    
    #operation path for IMCA7
    path("imca7total", views.imca7total, name="imca7total"),
    path("delete_dbs_ic7", views.delete_dbs_ic7, name="delete_dbs_ic7"),
    path("ic7report2678601", views.ic7_report_2678601, name="ic7report2678601"),
    path("ic7report2678602", views.ic7_report_2678602, name="ic7report2678602"),
    path("ic7report2678603", views.ic7_report_2678603, name="ic7report2678603"),
    path("ic7report2678604", views.ic7_report_2678604, name="ic7report2678604"),
    path("ic7report2678605", views.ic7_report_2678605, name="ic7report2678605"),
    
    #student path IMCA8
    path("IMCA8", views.ic8, name="IMCA8"),
    path("feedbackic8", views.ic8_main, name="feedbackic8"),
    
    #operation path for IMCA8
    path("imca8total", views.imca8total, name="imca8total"),
    path("delete_dbs_ic8", views.delete_dbs_ic8, name="delete_dbs_ic8"),
    path("ic8report2688601", views.ic8_report_2688601, name="ic8report2688601"),
    path("ic8report2688602", views.ic8_report_2688602, name="ic8report2688602"),
    path("ic8report2688603", views.ic8_report_2688603, name="ic8report2688603"),
    path("ic8report2688604", views.ic8_report_2688604, name="ic8report2688604"),
    path("ic8report2688605", views.ic8_report_2688605, name="ic8report2688605"),
    path("ic8report2688607", views.ic8_report_2688607, name="ic8report2688607"),
    
    #student path IMCA9
    path("IMCA9", views.ic9, name="IMCA9"),
    path("feedbackic9", views.ic9_main, name="feedbackic9"),
    
    #operation path for IMCA8
    path("imca9total", views.imca9total, name="imca9total"),
    path("delete_dbs_ic9", views.delete_dbs_ic9, name="delete_dbs_ic9"),
    path("ic9report2698601", views.ic9_report_2698601, name="ic9report2698601"),
    path("ic9report2698602", views.ic9_report_2698602, name="ic9report2698602"),
    path("ic9report2698603", views.ic9_report_2698603, name="ic9report2698603"),
    path("ic9report2698604", views.ic9_report_2698604, name="ic9report2698604"),
    path("ic9report2698605", views.ic9_report_2698605, name="ic9report2698605"),
    path("ic9report2698607", views.ic9_report_2698607, name="ic9report2698607"),
    
    #student path MCA1
    path("MCA1", views.mca1, name="MCA1"),
    path("feedbackmca1", views.mca1_main, name="feedbackmca1"),
    
    #operation path for MCA1
    path("mca1total", views.mca1total, name="mca1total"),
    path("delete_dbs_mca1", views.delete_dbs_mca1, name="delete_dbs_mca1"),
    path("mca1report619401", views.mca1_report_619401, name="mca1report619401"),
    path("mca1report619402", views.mca1_report_619402, name="mca1report619402"),
    path("mca1report619403", views.mca1_report_619403, name="mca1report619403"),
    path("mca1report619404", views.mca1_report_619404, name="mca1report619404"),
    path("mca1report619405", views.mca1_report_619405, name="mca1report619405"),
    path("mca1report619406", views.mca1_report_619406, name="mca1report619406"),
    
    #student path MCA2
    path("MCA2", views.mca2, name="MCA2"),
    path("feedbackmca2", views.mca2_main, name="feedbackmca2"),
    
    #operation path for MCA2
    path("mca2total", views.mca2total, name="mca2total"),
    path("delete_dbs_mca2", views.delete_dbs_mca2, name="delete_dbs_mca2"),
    path("mca2report629401", views.mca2_report_629401, name="mca2report629401"),
    path("mca2report629402", views.mca2_report_629402, name="mca2report629402"),
    path("mca2report629403", views.mca2_report_629403, name="mca2report629403"),
    path("mca2report629404", views.mca2_report_629404, name="mca2report629404"),
    path("mca2report629405", views.mca2_report_629405, name="mca2report629405"),
    path("mca2report629408", views.mca2_report_629408, name="mca2report629408"),
    
    #student path MCA3
    path("MCA3", views.mca3, name="MCA3"),
    path("feedbackmca3", views.mca3_main, name="feedbackmca3"),
    
    #operation path for MCA3
    path("mca3total", views.mca3total, name="mca3total"),
    path("delete_dbs_mca3", views.delete_dbs_mca3, name="delete_dbs_mca3"),
    path("mca3report639401", views.mca3_report_639401, name="mca3report639401"),
    path("mca3report639402", views.mca3_report_639402, name="mca3report639402"),
    path("mca3report639403", views.mca3_report_639403, name="mca3report639403"),
    path("mca3report639404", views.mca3_report_639404, name="mca3report639404"),
    path("mca3report639407", views.mca3_report_639407, name="mca3report639407"),
    path("mca3report639410", views.mca3_report_639410, name="mca3report639410"),

    #student path IMCA10
    path("IMCA10", views.ic10, name="IMCA10"),
    path("feedbackic10", views.ic10_main, name="feedbackic10"),
    
    #operation path for IMCA10
    path("imca10total", views.imca10total, name="imca10total"),
    path("delete_dbs_ic10", views.delete_dbs_ic10, name="delete_dbs_ic10"),
    path("ic10report4401601", views.ic10_report_4401601, name="ic10report4401601"),
    
    #student path MCA4
    path("MCA4", views.mca4, name="MCA4"),
    path("feedbackmca4", views.mca4_main, name="feedbackmca4"),
    
    #operation path for MCA4
    path("mca4total", views.mca4total, name="mca4total"),
    path("delete_dbs_mca4", views.delete_dbs_mca4, name="delete_dbs_mca4"),
    path("mca4report649401", views.mca4_report_649401, name="mca4report649401"),
]