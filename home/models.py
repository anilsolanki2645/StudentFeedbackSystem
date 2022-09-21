from http.client import LENGTH_REQUIRED
from turtle import home
from unittest.util import _MAX_LENGTH
from django.db import models

class Student(models.Model):  
    enrollment = models.IntegerField(unique=True)  
    class Meta:  
        db_table = "student"

#faculty table(model)
class Lecturer(models.Model):
    semester = models.IntegerField()  
    subject1 = models.CharField(max_length=25)
    subject2 = models.CharField(max_length=25)
    subject3 = models.CharField(max_length=25)
    subject4 = models.CharField(max_length=25)
    subject5 = models.CharField(max_length=25)
    subject6 = models.CharField(max_length=25)
    
    class Meta:  
        db_table = "lecturer"
        
#myadmin table(model)  
class Myadmin(models.Model):  
    username = models.CharField(max_length=20)  
    password = models.CharField(max_length=10)  
    
    class Meta:  
        db_table = "myadmin"
        
#Sem Serve table(model)  
class Sem_serve(models.Model):  
    semserve = models.CharField(max_length=10)  
    
    class Meta:  
        db_table = "sem_serve"
        
"""------------------------------------------ IMCA1 Tables ------------------------------------------------"""

#IC1 FCO 2618601 table(model)  
class Ic1_2618601(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2618601 = models.IntegerField(2) #Punctuality & Regularity
    pe2618601 = models.IntegerField(2) #Power Of Explanation
    sk2618601 = models.IntegerField(2) #Subject Knowledge
    mt2618601 = models.IntegerField(2) #Method Of Teaching
    ms2618601 = models.IntegerField(2) #Motivation Of Subject
    pa2618601 = models.IntegerField(2) #Professionalisam/Attitude
    cs2618601 = models.IntegerField(2) #Complition Of Syllabus
    ps2618601 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic1_2618601"
        
#IC1 FOW 2618602 table(model)  
class Ic1_2618602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2618602 = models.IntegerField(2) #Punctuality & Regularity
    pe2618602 = models.IntegerField(2) #Power Of Explanation
    sk2618602 = models.IntegerField(2) #Subject Knowledge
    mt2618602 = models.IntegerField(2) #Method Of Teaching
    ms2618602 = models.IntegerField(2) #Motivation Of Subject
    pa2618602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2618602 = models.IntegerField(2) #Complition Of Syllabus
    ps2618602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic1_2618602"
        
#IC1 FOP 2618603 table(model)  
class Ic1_2618603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2618603 = models.IntegerField(2) #Punctuality & Regularity
    pe2618603 = models.IntegerField(2) #Power Of Explanation
    sk2618603 = models.IntegerField(2) #Subject Knowledge
    mt2618603 = models.IntegerField(2) #Method Of Teaching
    ms2618603 = models.IntegerField(2) #Motivation Of Subject
    pa2618603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2618603 = models.IntegerField(2) #Complition Of Syllabus
    ps2618603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic1_2618603"
        
#IC1 BM 2618604 table(model)  
class Ic1_2618604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2618604 = models.IntegerField(2) #Punctuality & Regularity
    pe2618604 = models.IntegerField(2) #Power Of Explanation
    sk2618604 = models.IntegerField(2) #Subject Knowledge
    mt2618604 = models.IntegerField(2) #Method Of Teaching
    ms2618604 = models.IntegerField(2) #Motivation Of Subject
    pa2618604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2618604 = models.IntegerField(2) #Complition Of Syllabus
    ps2618604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic1_2618604"
        
#IC1 CS 2618605 table(model)  
class Ic1_2618605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2618605 = models.IntegerField(2) #Punctuality & Regularity
    pe2618605 = models.IntegerField(2) #Power Of Explanation
    sk2618605 = models.IntegerField(2) #Subject Knowledge
    mt2618605 = models.IntegerField(2) #Method Of Teaching
    ms2618605 = models.IntegerField(2) #Motivation Of Subject
    pa2618605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2618605 = models.IntegerField(2) #Complition Of Syllabus
    ps2618605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic1_2618605"

"""------------------------------------------ IMCA1 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA2 Tables ------------------------------------------------"""

#IC2 DS 2631601 table(model)  
class Ic2_2628601(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2628601 = models.IntegerField(2) #Punctuality & Regularity
    pe2628601 = models.IntegerField(2) #Power Of Explanation
    sk2628601 = models.IntegerField(2) #Subject Knowledge
    mt2628601 = models.IntegerField(2) #Method Of Teaching
    ms2628601 = models.IntegerField(2) #Motivation Of Subject
    pa2628601 = models.IntegerField(2) #Professionalisam/Attitude
    cs2628601 = models.IntegerField(2) #Complition Of Syllabus
    ps2628601 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic2_2628601"
        
#IC2 ADVANCE C 2628602 table(model)  
class Ic2_2628602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2628602 = models.IntegerField(2) #Punctuality & Regularity
    pe2628602 = models.IntegerField(2) #Power Of Explanation
    sk2628602 = models.IntegerField(2) #Subject Knowledge
    mt2628602 = models.IntegerField(2) #Method Of Teaching
    ms2628602 = models.IntegerField(2) #Motivation Of Subject
    pa2628602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2628602 = models.IntegerField(2) #Complition Of Syllabus
    ps2628602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic2_2628602"
        
#IC2 DBMS 2628603 table(model)  
class Ic2_2628603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2628603 = models.IntegerField(2) #Punctuality & Regularity
    pe2628603 = models.IntegerField(2) #Power Of Explanation
    sk2628603 = models.IntegerField(2) #Subject Knowledge
    mt2628603 = models.IntegerField(2) #Method Of Teaching
    ms2628603 = models.IntegerField(2) #Motivation Of Subject
    pa2628603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2628603 = models.IntegerField(2) #Complition Of Syllabus
    ps2628603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic2_2628603"
        
#IC2 OS 2628604 table(model)  
class Ic2_2628604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2628604 = models.IntegerField(2) #Punctuality & Regularity
    pe2628604 = models.IntegerField(2) #Power Of Explanation
    sk2628604 = models.IntegerField(2) #Subject Knowledge
    mt2628604 = models.IntegerField(2) #Method Of Teaching
    ms2628604 = models.IntegerField(2) #Motivation Of Subject
    pa2628604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2628604 = models.IntegerField(2) #Complition Of Syllabus
    ps2628604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic2_2628604"
        
#IC2 SP 2628605 table(model)  
class Ic2_2628605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2628605 = models.IntegerField(2) #Punctuality & Regularity
    pe2628605 = models.IntegerField(2) #Power Of Explanation
    sk2628605 = models.IntegerField(2) #Subject Knowledge
    mt2628605 = models.IntegerField(2) #Method Of Teaching
    ms2628605 = models.IntegerField(2) #Motivation Of Subject
    pa2628605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2628605 = models.IntegerField(2) #Complition Of Syllabus
    ps2628605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic2_2628605"

"""------------------------------------------ IMCA2 Tables Complete ------------------------------------------------"""
        
"""------------------------------------------ IMCA3 Tables ------------------------------------------------"""

#IC3 JAVA 2638601 table(model)  
class Ic3_2638601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2638601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2638601 = models.IntegerField(default=None) #Power Of Explanation
    sk2638601 = models.IntegerField(default=None) #Subject Knowledge
    mt2638601 = models.IntegerField(null=True) #Method Of Teaching
    ms2638601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2638601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2638601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2638601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic3_2638601"
        
#IC3 BS 2638602 table(model)  
class Ic3_2638602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2638602 = models.IntegerField(2) #Punctuality & Regularity
    pe2638602 = models.IntegerField(2) #Power Of Explanation
    sk2638602 = models.IntegerField(2) #Subject Knowledge
    mt2638602 = models.IntegerField(2) #Method Of Teaching
    ms2638602 = models.IntegerField(2) #Motivation Of Subject
    pa2638602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2638602 = models.IntegerField(2) #Complition Of Syllabus
    ps2638602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic3_2638602"
        
#IC3 SOODAM 2638603 table(model)  
class Ic3_2638603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2638603 = models.IntegerField(2) #Punctuality & Regularity
    pe2638603 = models.IntegerField(2) #Power Of Explanation
    sk2638603 = models.IntegerField(2) #Subject Knowledge
    mt2638603 = models.IntegerField(2) #Method Of Teaching
    ms2638603 = models.IntegerField(2) #Motivation Of Subject
    pa2638603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2638603 = models.IntegerField(2) #Complition Of Syllabus
    ps2638603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic3_2638603"
        
#IC3 WDT 2638604 table(model)  
class Ic3_2638604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2638604 = models.IntegerField(2) #Punctuality & Regularity
    pe2638604 = models.IntegerField(2) #Power Of Explanation
    sk2638604 = models.IntegerField(2) #Subject Knowledge
    mt2638604 = models.IntegerField(2) #Method Of Teaching
    ms2638604 = models.IntegerField(2) #Motivation Of Subject
    pa2638604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2638604 = models.IntegerField(2) #Complition Of Syllabus
    ps2638604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic3_2638604"
        
#IC3 SPDS 2638605 table(model)  
class Ic3_2638605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2638605 = models.IntegerField(2) #Punctuality & Regularity
    pe2638605 = models.IntegerField(2) #Power Of Explanation
    sk2638605 = models.IntegerField(2) #Subject Knowledge
    mt2638605 = models.IntegerField(2) #Method Of Teaching
    ms2638605 = models.IntegerField(2) #Motivation Of Subject
    pa2638605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2638605 = models.IntegerField(2) #Complition Of Syllabus
    ps2638605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic3_2638605"
        
"""------------------------------------------ IMCA3 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA4 Tables ------------------------------------------------"""

#IC4 PY 2648601 table(model)  
class Ic4_2648601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2648601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2648601 = models.IntegerField(default=None) #Power Of Explanation
    sk2648601 = models.IntegerField(default=None) #Subject Knowledge
    mt2648601 = models.IntegerField(null=True) #Method Of Teaching
    ms2648601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2648601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2648601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2648601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648601"
        
#IC4 OR 2648602 table(model)  
class Ic4_2648602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648602 = models.IntegerField(2) #Punctuality & Regularity
    pe2648602 = models.IntegerField(2) #Power Of Explanation
    sk2648602 = models.IntegerField(2) #Subject Knowledge
    mt2648602 = models.IntegerField(2) #Method Of Teaching
    ms2648602 = models.IntegerField(2) #Motivation Of Subject
    pa2648602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648602 = models.IntegerField(2) #Complition Of Syllabus
    ps2648602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648602"
        
#IC4 CN 2648603 table(model)  
class Ic4_2648603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648603 = models.IntegerField(2) #Punctuality & Regularity
    pe2648603 = models.IntegerField(2) #Power Of Explanation
    sk2648603 = models.IntegerField(2) #Subject Knowledge
    mt2648603 = models.IntegerField(2) #Method Of Teaching
    ms2648603 = models.IntegerField(2) #Motivation Of Subject
    pa2648603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648603 = models.IntegerField(2) #Complition Of Syllabus
    ps2648603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648603"
        
#IC4 LR 2648604 table(model)  
class Ic4_2648604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648604 = models.IntegerField(2) #Punctuality & Regularity
    pe2648604 = models.IntegerField(2) #Power Of Explanation
    sk2648604 = models.IntegerField(2) #Subject Knowledge
    mt2648604 = models.IntegerField(2) #Method Of Teaching
    ms2648604 = models.IntegerField(2) #Motivation Of Subject
    pa2648604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648604 = models.IntegerField(2) #Complition Of Syllabus
    ps2648604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648604"
        
#IC4 SP JAVA 2648605 table(model)  
class Ic4_2648605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648605 = models.IntegerField(2) #Punctuality & Regularity
    pe2648605 = models.IntegerField(2) #Power Of Explanation
    sk2648605 = models.IntegerField(2) #Subject Knowledge
    mt2648605 = models.IntegerField(2) #Method Of Teaching
    ms2648605 = models.IntegerField(2) #Motivation Of Subject
    pa2648605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648605 = models.IntegerField(2) #Complition Of Syllabus
    ps2648605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648605"
        
"""------------------------------------------ IMCA4 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA4 Tables ------------------------------------------------"""

#IC4 PY 2648601 table(model)  
class Ic4_2648601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2648601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2648601 = models.IntegerField(default=None) #Power Of Explanation
    sk2648601 = models.IntegerField(default=None) #Subject Knowledge
    mt2648601 = models.IntegerField(null=True) #Method Of Teaching
    ms2648601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2648601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2648601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2648601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648601"
        
#IC4 OR 2648602 table(model)  
class Ic4_2648602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648602 = models.IntegerField(2) #Punctuality & Regularity
    pe2648602 = models.IntegerField(2) #Power Of Explanation
    sk2648602 = models.IntegerField(2) #Subject Knowledge
    mt2648602 = models.IntegerField(2) #Method Of Teaching
    ms2648602 = models.IntegerField(2) #Motivation Of Subject
    pa2648602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648602 = models.IntegerField(2) #Complition Of Syllabus
    ps2648602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648602"
        
#IC4 CN 2648603 table(model)  
class Ic4_2648603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648603 = models.IntegerField(2) #Punctuality & Regularity
    pe2648603 = models.IntegerField(2) #Power Of Explanation
    sk2648603 = models.IntegerField(2) #Subject Knowledge
    mt2648603 = models.IntegerField(2) #Method Of Teaching
    ms2648603 = models.IntegerField(2) #Motivation Of Subject
    pa2648603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648603 = models.IntegerField(2) #Complition Of Syllabus
    ps2648603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648603"
        
#IC4 LR 2648604 table(model)  
class Ic4_2648604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648604 = models.IntegerField(2) #Punctuality & Regularity
    pe2648604 = models.IntegerField(2) #Power Of Explanation
    sk2648604 = models.IntegerField(2) #Subject Knowledge
    mt2648604 = models.IntegerField(2) #Method Of Teaching
    ms2648604 = models.IntegerField(2) #Motivation Of Subject
    pa2648604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648604 = models.IntegerField(2) #Complition Of Syllabus
    ps2648604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648604"
        
#IC4 SP JAVA 2648605 table(model)  
class Ic4_2648605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2648605 = models.IntegerField(2) #Punctuality & Regularity
    pe2648605 = models.IntegerField(2) #Power Of Explanation
    sk2648605 = models.IntegerField(2) #Subject Knowledge
    mt2648605 = models.IntegerField(2) #Method Of Teaching
    ms2648605 = models.IntegerField(2) #Motivation Of Subject
    pa2648605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2648605 = models.IntegerField(2) #Complition Of Syllabus
    ps2648605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic4_2648605"
        
"""------------------------------------------ IMCA4 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA5 Tables ------------------------------------------------"""

#IC5 A.JAVA 2658601 table(model)  
class Ic5_2658601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2658601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2658601 = models.IntegerField(default=None) #Power Of Explanation
    sk2658601 = models.IntegerField(default=None) #Subject Knowledge
    mt2658601 = models.IntegerField(null=True) #Method Of Teaching
    ms2658601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2658601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2658601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2658601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic5_2658601"
        
#IC5 MP 2658602 table(model)  
class Ic5_2658602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2658602 = models.IntegerField(2) #Punctuality & Regularity
    pe2658602 = models.IntegerField(2) #Power Of Explanation
    sk2658602 = models.IntegerField(2) #Subject Knowledge
    mt2658602 = models.IntegerField(2) #Method Of Teaching
    ms2658602 = models.IntegerField(2) #Motivation Of Subject
    pa2658602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2658602 = models.IntegerField(2) #Complition Of Syllabus
    ps2658602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic5_2658602"
        
#IC5 SE 2658603 table(model)  
class Ic5_2658603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2658603 = models.IntegerField(2) #Punctuality & Regularity
    pe2658603 = models.IntegerField(2) #Power Of Explanation
    sk2658603 = models.IntegerField(2) #Subject Knowledge
    mt2658603 = models.IntegerField(2) #Method Of Teaching
    ms2658603 = models.IntegerField(2) #Motivation Of Subject
    pa2658603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2658603 = models.IntegerField(2) #Complition Of Syllabus
    ps2658603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic5_2658603"
        
#IC5 E.COMM 2658604 table(model)  
class Ic5_2658604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2658604 = models.IntegerField(2) #Punctuality & Regularity
    pe2658604 = models.IntegerField(2) #Power Of Explanation
    sk2658604 = models.IntegerField(2) #Subject Knowledge
    mt2658604 = models.IntegerField(2) #Method Of Teaching
    ms2658604 = models.IntegerField(2) #Motivation Of Subject
    pa2658604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2658604 = models.IntegerField(2) #Complition Of Syllabus
    ps2658604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic5_2658604"
        
#IC5 SP SPRING 2658605 table(model)  
class Ic5_2658605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2658605 = models.IntegerField(2) #Punctuality & Regularity
    pe2658605 = models.IntegerField(2) #Power Of Explanation
    sk2658605 = models.IntegerField(2) #Subject Knowledge
    mt2658605 = models.IntegerField(2) #Method Of Teaching
    ms2658605 = models.IntegerField(2) #Motivation Of Subject
    pa2658605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2658605 = models.IntegerField(2) #Complition Of Syllabus
    ps2658605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic5_2658605"
        
"""------------------------------------------ IMCA5 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA6 Tables ------------------------------------------------"""

#IC6 MIS 2668601 table(model)  
class Ic6_2668601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2668601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2668601 = models.IntegerField(default=None) #Power Of Explanation
    sk2668601 = models.IntegerField(default=None) #Subject Knowledge
    mt2668601 = models.IntegerField(null=True) #Method Of Teaching
    ms2668601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2668601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2668601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2668601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic6_2668601"
        
#IC6 ST 2668602 table(model)  
class Ic6_2668602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2668602 = models.IntegerField(2) #Punctuality & Regularity
    pe2668602 = models.IntegerField(2) #Power Of Explanation
    sk2668602 = models.IntegerField(2) #Subject Knowledge
    mt2668602 = models.IntegerField(2) #Method Of Teaching
    ms2668602 = models.IntegerField(2) #Motivation Of Subject
    pa2668602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2668602 = models.IntegerField(2) #Complition Of Syllabus
    ps2668602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic6_2668602"
        
#IC6 DM 2668603 table(model)  
class Ic6_2668603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2668603 = models.IntegerField(2) #Punctuality & Regularity
    pe2668603 = models.IntegerField(2) #Power Of Explanation
    sk2668603 = models.IntegerField(2) #Subject Knowledge
    mt2668603 = models.IntegerField(2) #Method Of Teaching
    ms2668603 = models.IntegerField(2) #Motivation Of Subject
    pa2668603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2668603 = models.IntegerField(2) #Complition Of Syllabus
    ps2668603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic6_2668603"
        
#IC6 ES 2668604 table(model)  
class Ic6_2668604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2668604 = models.IntegerField(2) #Punctuality & Regularity
    pe2668604 = models.IntegerField(2) #Power Of Explanation
    sk2668604 = models.IntegerField(2) #Subject Knowledge
    mt2668604 = models.IntegerField(2) #Method Of Teaching
    ms2668604 = models.IntegerField(2) #Motivation Of Subject
    pa2668604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2668604 = models.IntegerField(2) #Complition Of Syllabus
    ps2668604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic6_2668604"
        
#IC6 SP ASP 2668605 table(model)  
class Ic6_2668605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2668605 = models.IntegerField(2) #Punctuality & Regularity
    pe2668605 = models.IntegerField(2) #Power Of Explanation
    sk2668605 = models.IntegerField(2) #Subject Knowledge
    mt2668605 = models.IntegerField(2) #Method Of Teaching
    ms2668605 = models.IntegerField(2) #Motivation Of Subject
    pa2668605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2668605 = models.IntegerField(2) #Complition Of Syllabus
    ps2668605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic6_2668605"
        
"""------------------------------------------ IMCA6 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA7 Tables ------------------------------------------------"""

#IC7 ML 2678601 table(model)  
class Ic7_2678601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2678601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2678601 = models.IntegerField(default=None) #Power Of Explanation
    sk2678601 = models.IntegerField(default=None) #Subject Knowledge
    mt2678601 = models.IntegerField(null=True) #Method Of Teaching
    ms2678601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2678601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2678601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2678601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic7_2678601"
        
#IC7 AMP 2678602 table(model)  
class Ic7_2678602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2678602 = models.IntegerField(2) #Punctuality & Regularity
    pe2678602 = models.IntegerField(2) #Power Of Explanation
    sk2678602 = models.IntegerField(2) #Subject Knowledge
    mt2678602 = models.IntegerField(2) #Method Of Teaching
    ms2678602 = models.IntegerField(2) #Motivation Of Subject
    pa2678602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2678602 = models.IntegerField(2) #Complition Of Syllabus
    ps2678602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic7_2678602"
        
#IC7 CS 2678603 table(model)  
class Ic7_2678603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2678603 = models.IntegerField(2) #Punctuality & Regularity
    pe2678603 = models.IntegerField(2) #Power Of Explanation
    sk2678603 = models.IntegerField(2) #Subject Knowledge
    mt2678603 = models.IntegerField(2) #Method Of Teaching
    ms2678603 = models.IntegerField(2) #Motivation Of Subject
    pa2678603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2678603 = models.IntegerField(2) #Complition Of Syllabus
    ps2678603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic7_2678603"
        
#IC7 SP 2678604 table(model)  
class Ic7_2678604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2678604 = models.IntegerField(2) #Punctuality & Regularity
    pe2678604 = models.IntegerField(2) #Power Of Explanation
    sk2678604 = models.IntegerField(2) #Subject Knowledge
    mt2678604 = models.IntegerField(2) #Method Of Teaching
    ms2678604 = models.IntegerField(2) #Motivation Of Subject
    pa2678604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2678604 = models.IntegerField(2) #Complition Of Syllabus
    ps2678604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic7_2678604"
        
#IC7 BCT 2678605 table(model)  
class Ic7_2678605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2678605 = models.IntegerField(2) #Punctuality & Regularity
    pe2678605 = models.IntegerField(2) #Power Of Explanation
    sk2678605 = models.IntegerField(2) #Subject Knowledge
    mt2678605 = models.IntegerField(2) #Method Of Teaching
    ms2678605 = models.IntegerField(2) #Motivation Of Subject
    pa2678605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2678605 = models.IntegerField(2) #Complition Of Syllabus
    ps2678605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic7_2678605"
        
"""------------------------------------------ IMCA7 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA8 Tables ------------------------------------------------"""

#IC8 BDA 2688601 table(model)  
class Ic8_2688601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2688601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2688601 = models.IntegerField(default=None) #Power Of Explanation
    sk2688601 = models.IntegerField(default=None) #Subject Knowledge
    mt2688601 = models.IntegerField(null=True) #Method Of Teaching
    ms2688601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2688601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2688601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2688601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic8_2688601"
        
#IC8 AML 2688602 table(model)  
class Ic8_2688602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2688602 = models.IntegerField(2) #Punctuality & Regularity
    pe2688602 = models.IntegerField(2) #Power Of Explanation
    sk2688602 = models.IntegerField(2) #Subject Knowledge
    mt2688602 = models.IntegerField(2) #Method Of Teaching
    ms2688602 = models.IntegerField(2) #Motivation Of Subject
    pa2688602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2688602 = models.IntegerField(2) #Complition Of Syllabus
    ps2688602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic8_2688602"
        
#IC8 DAA 2688603 table(model)  
class Ic8_2688603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2688603 = models.IntegerField(2) #Punctuality & Regularity
    pe2688603 = models.IntegerField(2) #Power Of Explanation
    sk2688603 = models.IntegerField(2) #Subject Knowledge
    mt2688603 = models.IntegerField(2) #Method Of Teaching
    ms2688603 = models.IntegerField(2) #Motivation Of Subject
    pa2688603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2688603 = models.IntegerField(2) #Complition Of Syllabus
    ps2688603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic8_2688603"
        
#IC8 TW 2688604 table(model)  
class Ic8_2688604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2688604 = models.IntegerField(2) #Punctuality & Regularity
    pe2688604 = models.IntegerField(2) #Power Of Explanation
    sk2688604 = models.IntegerField(2) #Subject Knowledge
    mt2688604 = models.IntegerField(2) #Method Of Teaching
    ms2688604 = models.IntegerField(2) #Motivation Of Subject
    pa2688604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2688604 = models.IntegerField(2) #Complition Of Syllabus
    ps2688604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic8_2688604"
        
#IC8 SP 2688605 table(model)  
class Ic8_2688605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2688605 = models.IntegerField(2) #Punctuality & Regularity
    pe2688605 = models.IntegerField(2) #Power Of Explanation
    sk2688605 = models.IntegerField(2) #Subject Knowledge
    mt2688605 = models.IntegerField(2) #Method Of Teaching
    ms2688605 = models.IntegerField(2) #Motivation Of Subject
    pa2688605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2688605 = models.IntegerField(2) #Complition Of Syllabus
    ps2688605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic8_2688605"


#IC8 CF 2688607 table(model)  
class Ic8_2688607(models.Model):
    std_id = models.IntegerField(unique=True)  
    pr2688607 = models.IntegerField(2) #Punctuality & Regularity
    pe2688607 = models.IntegerField(2) #Power Of Explanation
    sk2688607 = models.IntegerField(2) #Subject Knowledge
    mt2688607 = models.IntegerField(2) #Method Of Teaching
    ms2688607 = models.IntegerField(2) #Motivation Of Subject
    pa2688607 = models.IntegerField(2) #Professionalisam/Attitude
    cs2688607 = models.IntegerField(2) #Complition Of Syllabus
    ps2688607 = models.IntegerField(2) #Paper Solution
    
    class Meta:
        db_table = "ic8_2688607"

        
"""------------------------------------------ IMCA8 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA9 Tables ------------------------------------------------"""

#IC9 DP 2698601 table(model)  
class Ic9_2698601(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr2698601 = models.IntegerField(default=None) #Punctuality & Regularity
    pe2698601 = models.IntegerField(default=None) #Power Of Explanation
    sk2698601 = models.IntegerField(default=None) #Subject Knowledge
    mt2698601 = models.IntegerField(null=True) #Method Of Teaching
    ms2698601 = models.IntegerField(null=True) #Motivation Of Subject
    pa2698601 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs2698601 = models.IntegerField(null=True) #Complition Of Syllabus
    ps2698601 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "ic9_2698601"
        
#IC9 FSD 2698602 table(model)  
class Ic9_2698602(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2698602 = models.IntegerField(2) #Punctuality & Regularity
    pe2698602 = models.IntegerField(2) #Power Of Explanation
    sk2698602 = models.IntegerField(2) #Subject Knowledge
    mt2698602 = models.IntegerField(2) #Method Of Teaching
    ms2698602 = models.IntegerField(2) #Motivation Of Subject
    pa2698602 = models.IntegerField(2) #Professionalisam/Attitude
    cs2698602 = models.IntegerField(2) #Complition Of Syllabus
    ps2698602 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic9_2698602"
        
#IC9 EIC 2698603 table(model)  
class Ic9_2698603(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2698603 = models.IntegerField(2) #Punctuality & Regularity
    pe2698603 = models.IntegerField(2) #Power Of Explanation
    sk2698603 = models.IntegerField(2) #Subject Knowledge
    mt2698603 = models.IntegerField(2) #Method Of Teaching
    ms2698603 = models.IntegerField(2) #Motivation Of Subject
    pa2698603 = models.IntegerField(2) #Professionalisam/Attitude
    cs2698603 = models.IntegerField(2) #Complition Of Syllabus
    ps2698603 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic9_2698603"
        
#IC9 PM 2698604 table(model)  
class Ic9_2698604(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2698604 = models.IntegerField(2) #Punctuality & Regularity
    pe2698604 = models.IntegerField(2) #Power Of Explanation
    sk2698604 = models.IntegerField(2) #Subject Knowledge
    mt2698604 = models.IntegerField(2) #Method Of Teaching
    ms2698604 = models.IntegerField(2) #Motivation Of Subject
    pa2698604 = models.IntegerField(2) #Professionalisam/Attitude
    cs2698604 = models.IntegerField(2) #Complition Of Syllabus
    ps2698604 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic9_2698604"
        
#IC9 SP 2698605 table(model)  
class Ic9_2698605(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr2698605 = models.IntegerField(2) #Punctuality & Regularity
    pe2698605 = models.IntegerField(2) #Power Of Explanation
    sk2698605 = models.IntegerField(2) #Subject Knowledge
    mt2698605 = models.IntegerField(2) #Method Of Teaching
    ms2698605 = models.IntegerField(2) #Motivation Of Subject
    pa2698605 = models.IntegerField(2) #Professionalisam/Attitude
    cs2698605 = models.IntegerField(2) #Complition Of Syllabus
    ps2698605 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic9_2698605"


#IC9 IOT 2698607 table(model)  
class Ic9_2698607(models.Model):
    std_id = models.IntegerField(unique=True)  
    pr2698607 = models.IntegerField(2) #Punctuality & Regularity
    pe2698607 = models.IntegerField(2) #Power Of Explanation
    sk2698607 = models.IntegerField(2) #Subject Knowledge
    mt2698607 = models.IntegerField(2) #Method Of Teaching
    ms2698607 = models.IntegerField(2) #Motivation Of Subject
    pa2698607 = models.IntegerField(2) #Professionalisam/Attitude
    cs2698607 = models.IntegerField(2) #Complition Of Syllabus
    ps2698607 = models.IntegerField(2) #Paper Solution
    
    class Meta:
        db_table = "ic9_2698607"

        
"""------------------------------------------ IMCA9 Tables Complete ------------------------------------------------"""

"""------------------------------------------ MCA1 Tables ------------------------------------------------"""

#MCA1 C-LANG 619401 table(model)  
class Mca1_619401(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr619401 = models.IntegerField(default=None) #Punctuality & Regularity
    pe619401 = models.IntegerField(default=None) #Power Of Explanation
    sk619401 = models.IntegerField(default=None) #Subject Knowledge
    mt619401 = models.IntegerField(null=True) #Method Of Teaching
    ms619401 = models.IntegerField(null=True) #Motivation Of Subject
    pa619401 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs619401 = models.IntegerField(null=True) #Complition Of Syllabus
    ps619401 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "mca1_619401"
        
#MCA1 JAVA 619402 table(model)  
class Mca1_619402(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr619402 = models.IntegerField(2) #Punctuality & Regularity
    pe619402 = models.IntegerField(2) #Power Of Explanation
    sk619402 = models.IntegerField(2) #Subject Knowledge
    mt619402 = models.IntegerField(2) #Method Of Teaching
    ms619402 = models.IntegerField(2) #Motivation Of Subject
    pa619402 = models.IntegerField(2) #Professionalisam/Attitude
    cs619402 = models.IntegerField(2) #Complition Of Syllabus
    ps619402 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca1_619402"
        
#MCA1 BM 619403 table(model)  
class Mca1_619403(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr619403 = models.IntegerField(2) #Punctuality & Regularity
    pe619403 = models.IntegerField(2) #Power Of Explanation
    sk619403 = models.IntegerField(2) #Subject Knowledge
    mt619403 = models.IntegerField(2) #Method Of Teaching
    ms619403 = models.IntegerField(2) #Motivation Of Subject
    pa619403 = models.IntegerField(2) #Professionalisam/Attitude
    cs619403 = models.IntegerField(2) #Complition Of Syllabus
    ps619403 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca1_619403"
        
#MCA1 RDBMS 619404 table(model)  
class Mca1_619404(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr619404 = models.IntegerField(2) #Punctuality & Regularity
    pe619404 = models.IntegerField(2) #Power Of Explanation
    sk619404 = models.IntegerField(2) #Subject Knowledge
    mt619404 = models.IntegerField(2) #Method Of Teaching
    ms619404 = models.IntegerField(2) #Motivation Of Subject
    pa619404 = models.IntegerField(2) #Professionalisam/Attitude
    cs619404 = models.IntegerField(2) #Complition Of Syllabus
    ps619404 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca1_619404"
        
#MCA1 WDT-PHP 619405 table(model)  
class Mca1_619405(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr619405 = models.IntegerField(2) #Punctuality & Regularity
    pe619405 = models.IntegerField(2) #Power Of Explanation
    sk619405 = models.IntegerField(2) #Subject Knowledge
    mt619405 = models.IntegerField(2) #Method Of Teaching
    ms619405 = models.IntegerField(2) #Motivation Of Subject
    pa619405 = models.IntegerField(2) #Professionalisam/Attitude
    cs619405 = models.IntegerField(2) #Complition Of Syllabus
    ps619405 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca1_619405"


#MCA1 BCC 619406 table(model)  
class Mca1_619406(models.Model):
    std_id = models.IntegerField(unique=True)  
    pr619406 = models.IntegerField(2) #Punctuality & Regularity
    pe619406 = models.IntegerField(2) #Power Of Explanation
    sk619406 = models.IntegerField(2) #Subject Knowledge
    mt619406 = models.IntegerField(2) #Method Of Teaching
    ms619406 = models.IntegerField(2) #Motivation Of Subject
    pa619406 = models.IntegerField(2) #Professionalisam/Attitude
    cs619406 = models.IntegerField(2) #Complition Of Syllabus
    ps619406 = models.IntegerField(2) #Paper Solution
    
    class Meta:
        db_table = "mca1_619406"

        
"""------------------------------------------ MCA1 Tables Complete ------------------------------------------------"""

"""------------------------------------------ MCA2 Tables ------------------------------------------------"""

#MCA2 DS 629401 table(model)  
class Mca2_629401(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr629401 = models.IntegerField(default=None) #Punctuality & Regularity
    pe629401 = models.IntegerField(default=None) #Power Of Explanation
    sk629401 = models.IntegerField(default=None) #Subject Knowledge
    mt629401 = models.IntegerField(null=True) #Method Of Teaching
    ms629401 = models.IntegerField(null=True) #Motivation Of Subject
    pa629401 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs629401 = models.IntegerField(null=True) #Complition Of Syllabus
    ps629401 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "mca2_629401"
        
#MCA2 MP 629402 table(model)  
class Mca2_629402(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr629402 = models.IntegerField(2) #Punctuality & Regularity
    pe629402 = models.IntegerField(2) #Power Of Explanation
    sk629402 = models.IntegerField(2) #Subject Knowledge
    mt629402 = models.IntegerField(2) #Method Of Teaching
    ms629402 = models.IntegerField(2) #Motivation Of Subject
    pa629402 = models.IntegerField(2) #Professionalisam/Attitude
    cs629402 = models.IntegerField(2) #Complition Of Syllabus
    ps629402 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca2_629402"
        
#MCA2 PY 629403 table(model)  
class Mca2_629403(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr629403 = models.IntegerField(2) #Punctuality & Regularity
    pe629403 = models.IntegerField(2) #Power Of Explanation
    sk629403 = models.IntegerField(2) #Subject Knowledge
    mt629403 = models.IntegerField(2) #Method Of Teaching
    ms629403 = models.IntegerField(2) #Motivation Of Subject
    pa629403 = models.IntegerField(2) #Professionalisam/Attitude
    cs629403 = models.IntegerField(2) #Complition Of Syllabus
    ps629403 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca2_629403"
        
#MCA2 CN 629404 table(model)  
class Mca2_629404(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr629404 = models.IntegerField(2) #Punctuality & Regularity
    pe629404 = models.IntegerField(2) #Power Of Explanation
    sk629404 = models.IntegerField(2) #Subject Knowledge
    mt629404 = models.IntegerField(2) #Method Of Teaching
    ms629404 = models.IntegerField(2) #Motivation Of Subject
    pa629404 = models.IntegerField(2) #Professionalisam/Attitude
    cs629404 = models.IntegerField(2) #Complition Of Syllabus
    ps629404 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca2_629404"
        
#MCA2 SP 629405 table(model)  
class Mca2_629405(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr629405 = models.IntegerField(2) #Punctuality & Regularity
    pe629405 = models.IntegerField(2) #Power Of Explanation
    sk629405 = models.IntegerField(2) #Subject Knowledge
    mt629405 = models.IntegerField(2) #Method Of Teaching
    ms629405 = models.IntegerField(2) #Motivation Of Subject
    pa629405 = models.IntegerField(2) #Professionalisam/Attitude
    cs629405 = models.IntegerField(2) #Complition Of Syllabus
    ps629405 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca2_629405"


#MCA2 JWT 629408 table(model)  
class Mca2_629408(models.Model):
    std_id = models.IntegerField(unique=True)  
    pr629408 = models.IntegerField(2) #Punctuality & Regularity
    pe629408 = models.IntegerField(2) #Power Of Explanation
    sk629408 = models.IntegerField(2) #Subject Knowledge
    mt629408 = models.IntegerField(2) #Method Of Teaching
    ms629408 = models.IntegerField(2) #Motivation Of Subject
    pa629408 = models.IntegerField(2) #Professionalisam/Attitude
    cs629408 = models.IntegerField(2) #Complition Of Syllabus
    ps629408 = models.IntegerField(2) #Paper Solution
    
    class Meta:
        db_table = "mca2_629408"

        
"""------------------------------------------ MCA2 Tables Complete ------------------------------------------------"""

"""------------------------------------------ MCA3 Tables ------------------------------------------------"""

#MCA3 DAA 639401 table(model)  
class Mca3_639401(models.Model):  
    std_id = models.IntegerField(unique=True, default=None)  
    pr639401 = models.IntegerField(default=None) #Punctuality & Regularity
    pe639401 = models.IntegerField(default=None) #Power Of Explanation
    sk639401 = models.IntegerField(default=None) #Subject Knowledge
    mt639401 = models.IntegerField(null=True) #Method Of Teaching
    ms639401 = models.IntegerField(null=True) #Motivation Of Subject
    pa639401 = models.IntegerField(null=True) #Professionalisam/Attitude
    cs639401 = models.IntegerField(null=True) #Complition Of Syllabus
    ps639401 = models.IntegerField(null=True) #Paper Solution
    
    class Meta:  
        db_table = "mca3_639401"
        
#MCA3 ML 639402 table(model)  
class Mca3_639402(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr639402 = models.IntegerField(2) #Punctuality & Regularity
    pe639402 = models.IntegerField(2) #Power Of Explanation
    sk639402 = models.IntegerField(2) #Subject Knowledge
    mt639402 = models.IntegerField(2) #Method Of Teaching
    ms639402 = models.IntegerField(2) #Motivation Of Subject
    pa639402 = models.IntegerField(2) #Professionalisam/Attitude
    cs639402 = models.IntegerField(2) #Complition Of Syllabus
    ps639402 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca3_639402"
        
#MCA3 SE 639403 table(model)  
class Mca3_639403(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr639403 = models.IntegerField(2) #Punctuality & Regularity
    pe639403 = models.IntegerField(2) #Power Of Explanation
    sk639403 = models.IntegerField(2) #Subject Knowledge
    mt639403 = models.IntegerField(2) #Method Of Teaching
    ms639403 = models.IntegerField(2) #Motivation Of Subject
    pa639403 = models.IntegerField(2) #Professionalisam/Attitude
    cs639403 = models.IntegerField(2) #Complition Of Syllabus
    ps639403 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca3_639403"
        
#MCA3 SP 639404 table(model)  
class Mca3_639404(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr639404 = models.IntegerField(2) #Punctuality & Regularity
    pe639404 = models.IntegerField(2) #Power Of Explanation
    sk639404 = models.IntegerField(2) #Subject Knowledge
    mt639404 = models.IntegerField(2) #Method Of Teaching
    ms639404 = models.IntegerField(2) #Motivation Of Subject
    pa639404 = models.IntegerField(2) #Professionalisam/Attitude
    cs639404 = models.IntegerField(2) #Complition Of Syllabus
    ps639404 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca3_639404"
        
#MCA3 CC 639407 table(model)  
class Mca3_639407(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr639407 = models.IntegerField(2) #Punctuality & Regularity
    pe639407 = models.IntegerField(2) #Power Of Explanation
    sk639407 = models.IntegerField(2) #Subject Knowledge
    mt639407 = models.IntegerField(2) #Method Of Teaching
    ms639407 = models.IntegerField(2) #Motivation Of Subject
    pa639407 = models.IntegerField(2) #Professionalisam/Attitude
    cs639407 = models.IntegerField(2) #Complition Of Syllabus
    ps639407 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca3_639407"


#MCA3 NCS 639410 table(model)  
class Mca3_639410(models.Model):
    std_id = models.IntegerField(unique=True)  
    pr639410 = models.IntegerField(2) #Punctuality & Regularity
    pe639410 = models.IntegerField(2) #Power Of Explanation
    sk639410 = models.IntegerField(2) #Subject Knowledge
    mt639410 = models.IntegerField(2) #Method Of Teaching
    ms639410 = models.IntegerField(2) #Motivation Of Subject
    pa639410 = models.IntegerField(2) #Professionalisam/Attitude
    cs639410 = models.IntegerField(2) #Complition Of Syllabus
    ps639410 = models.IntegerField(2) #Paper Solution
    
    class Meta:
        db_table = "mca3_639410"

        
"""------------------------------------------ MCA3 Tables Complete ------------------------------------------------"""

"""------------------------------------------ IMCA10 Tables ------------------------------------------------"""

#IC10 SP 4401601 table(model)  
class Ic10_4401601(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr4401601 = models.IntegerField(2) #Punctuality & Regularity
    pe4401601 = models.IntegerField(2) #Power Of Explanation
    sk4401601 = models.IntegerField(2) #Subject Knowledge
    mt4401601 = models.IntegerField(2) #Method Of Teaching
    ms4401601 = models.IntegerField(2) #Motivation Of Subject
    pa4401601 = models.IntegerField(2) #Professionalisam/Attitude
    cs4401601 = models.IntegerField(2) #Complition Of Syllabus
    ps4401601 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "ic10_4401601"

"""------------------------------------------ IMCA10 Tables Complete ------------------------------------------------"""

"""------------------------------------------ MCA4 Tables ------------------------------------------------"""

#MCA4 SP 649401 table(model)  
class Mca4_649401(models.Model):  
    std_id = models.IntegerField(unique=True)  
    pr649401 = models.IntegerField(2) #Punctuality & Regularity
    pe649401 = models.IntegerField(2) #Power Of Explanation
    sk649401 = models.IntegerField(2) #Subject Knowledge
    mt649401 = models.IntegerField(2) #Method Of Teaching
    ms649401 = models.IntegerField(2) #Motivation Of Subject
    pa649401 = models.IntegerField(2) #Professionalisam/Attitude
    cs649401 = models.IntegerField(2) #Complition Of Syllabus
    ps649401 = models.IntegerField(2) #Paper Solution
    
    class Meta:  
        db_table = "mca4_649401"

"""------------------------------------------ MCA4 Tables Complete ------------------------------------------------"""