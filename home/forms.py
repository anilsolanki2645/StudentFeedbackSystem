from django import forms
from home.models import Student
from home.models import Sem_serve

from home.models import Ic1_2618601, Ic1_2618602, Ic1_2618603, Ic1_2618604, Ic1_2618605
from home.models import Ic2_2628601, Ic2_2628602, Ic2_2628603, Ic2_2628604, Ic2_2628605
from home.models import Ic3_2638601, Ic3_2638602, Ic3_2638603, Ic3_2638604, Ic3_2638605
from home.models import Ic4_2648601, Ic4_2648602, Ic4_2648603, Ic4_2648604, Ic4_2648605
from home.models import Ic5_2658601, Ic5_2658602, Ic5_2658603, Ic5_2658604, Ic5_2658605
from home.models import Ic6_2668601, Ic6_2668602, Ic6_2668603, Ic6_2668604, Ic6_2668605
from home.models import Ic7_2678601, Ic7_2678602, Ic7_2678603, Ic7_2678604, Ic7_2678605
from home.models import Ic8_2688601, Ic8_2688602, Ic8_2688603, Ic8_2688604, Ic8_2688605, Ic8_2688607
from home.models import Ic9_2698601, Ic9_2698602, Ic9_2698603, Ic9_2698604, Ic9_2698605, Ic9_2698607

from home.models import Mca1_619401, Mca1_619402, Mca1_619403, Mca1_619404, Mca1_619405, Mca1_619406
from home.models import Mca2_629401, Mca2_629402, Mca2_629403, Mca2_629404, Mca2_629405, Mca2_629408
from home.models import Mca3_639401, Mca3_639402, Mca3_639403, Mca3_639404, Mca3_639407, Mca3_639410

from home.models import Ic10_4401601
from home.models import Mca4_649401

class StudentForm(forms.ModelForm):  
    class Meta:   
        model = Student
        fields = "__all__"
        
#Sem Serve form
class Sem_serve_Form(forms.ModelForm):
    class Meta:
        model = Sem_serve
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA1-----------------------------------------------------"""
#IC1 FCO 2618601 form
class Ic1_2618601_Form(forms.ModelForm):
    class Meta:
        model = Ic1_2618601
        fields = "__all__"

#IC1 FOW 2618602 form
class Ic1_2618602_Form(forms.ModelForm):
    class Meta:
        model = Ic1_2618602
        fields = "__all__"
        
#IC1 FOP 2618603 form
class Ic1_2618603_Form(forms.ModelForm):
    class Meta:
        model = Ic1_2618603
        fields = "__all__"
        
#IC1 BM 2618604 form
class Ic1_2618604_Form(forms.ModelForm):
    class Meta:
        model = Ic1_2618604
        fields = "__all__"
        
#IC1 CS 2618605 form
class Ic1_2618605_Form(forms.ModelForm):
    class Meta:
        model = Ic1_2618605
        fields = "__all__"

"""-----------------------------------------Form for IMCA1 Complete-----------------------------------------------------"""    

"""-----------------------------------------Form for IMCA2-----------------------------------------------------"""
#IC2 DS 2628601 form
class Ic2_2628601_Form(forms.ModelForm):
    class Meta:
        model = Ic2_2628601
        fields = "__all__"

#IC2 ADVANCE C 2628602 form
class Ic2_2628602_Form(forms.ModelForm):
    class Meta:
        model = Ic2_2628602
        fields = "__all__"
        
#IC2 DBMS 2628603 form
class Ic2_2628603_Form(forms.ModelForm):
    class Meta:
        model = Ic2_2628603
        fields = "__all__"
        
#IC2 OS 2628604 form
class Ic2_2628604_Form(forms.ModelForm):
    class Meta:
        model = Ic2_2628604
        fields = "__all__"
        
#IC2 SP 2628605 form
class Ic2_2628605_Form(forms.ModelForm):
    class Meta:
        model = Ic2_2628605
        fields = "__all__"

"""-----------------------------------------Form for IMCA2 Complete-----------------------------------------------------"""    

"""-----------------------------------------Form for IMCA3-----------------------------------------------------"""
#IC3 JAVA 2638601 form
class Ic3_2638601_Form(forms.ModelForm):
    class Meta:
        model = Ic3_2638601
        fields = "__all__"

#IC3 BS 2638602 form
class Ic3_2638602_Form(forms.ModelForm):
    class Meta:
        model = Ic3_2638602
        fields = "__all__"
        
#IC3 SOODAM 2638603 form
class Ic3_2638603_Form(forms.ModelForm):
    class Meta:
        model = Ic3_2638603
        fields = "__all__"
        
#IC3 WDT 2638604 form
class Ic3_2638604_Form(forms.ModelForm):
    class Meta:
        model = Ic3_2638604
        fields = "__all__"
        
#IC3 SPDS 2638605 form
class Ic3_2638605_Form(forms.ModelForm):
    class Meta:
        model = Ic3_2638605
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA3 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for IMCA4-----------------------------------------------------"""
#IC4 PY 2648601 form
class Ic4_2648601_Form(forms.ModelForm):
    class Meta:
        model = Ic4_2648601
        fields = "__all__"

#IC4 OR 2648602 form
class Ic4_2648602_Form(forms.ModelForm):
    class Meta:
        model = Ic4_2648602
        fields = "__all__"
        
#IC4 CN 2648603 form
class Ic4_2648603_Form(forms.ModelForm):
    class Meta:
        model = Ic4_2648603
        fields = "__all__"
        
#IC4 LR 2648604 form
class Ic4_2648604_Form(forms.ModelForm):
    class Meta:
        model = Ic4_2648604
        fields = "__all__"
        
#IC4 SP JAVA 2648605 form
class Ic4_2648605_Form(forms.ModelForm):
    class Meta:
        model = Ic4_2648605
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA4 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for IMCA5-----------------------------------------------------"""
#IC5 A.JAVA 2658601 form
class Ic5_2658601_Form(forms.ModelForm):
    class Meta:
        model = Ic5_2658601
        fields = "__all__"

#IC5 MP 2658602 form
class Ic5_2658602_Form(forms.ModelForm):
    class Meta:
        model = Ic5_2658602
        fields = "__all__"
        
#IC5 SE 2658603 form
class Ic5_2658603_Form(forms.ModelForm):
    class Meta:
        model = Ic5_2658603
        fields = "__all__"
        
#IC5 E.COMM 2658604 form
class Ic5_2658604_Form(forms.ModelForm):
    class Meta:
        model = Ic5_2658604
        fields = "__all__"
        
#IC5 SP SPRING 2658605 form
class Ic5_2658605_Form(forms.ModelForm):
    class Meta:
        model = Ic5_2658605
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA5 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for IMCA6-----------------------------------------------------"""
#IC6 MIS 2668601 form
class Ic6_2668601_Form(forms.ModelForm):
    class Meta:
        model = Ic6_2668601
        fields = "__all__"

#IC6 ST 2668602 form
class Ic6_2668602_Form(forms.ModelForm):
    class Meta:
        model = Ic6_2668602
        fields = "__all__"
        
#IC6 DM 2668603 form
class Ic6_2668603_Form(forms.ModelForm):
    class Meta:
        model = Ic6_2668603
        fields = "__all__"
        
#IC6 ES 2668604 form
class Ic6_2668604_Form(forms.ModelForm):
    class Meta:
        model = Ic6_2668604
        fields = "__all__"
        
#IC6 SP ASP 2668605 form
class Ic6_2668605_Form(forms.ModelForm):
    class Meta:
        model = Ic6_2668605
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA6 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for IMCA7-----------------------------------------------------"""
#IC7 ML 2678601 form
class Ic7_2678601_Form(forms.ModelForm):
    class Meta:
        model = Ic7_2678601
        fields = "__all__"

#IC7 AMP 2678602 form
class Ic7_2678602_Form(forms.ModelForm):
    class Meta:
        model = Ic7_2678602
        fields = "__all__"
        
#IC7 CS 2678603 form
class Ic7_2678603_Form(forms.ModelForm):
    class Meta:
        model = Ic7_2678603
        fields = "__all__"
        
#IC7 SP 2678604 form
class Ic7_2678604_Form(forms.ModelForm):
    class Meta:
        model = Ic7_2678604
        fields = "__all__"
        
#IC7 BCT 2678605 form
class Ic7_2678605_Form(forms.ModelForm):
    class Meta:
        model = Ic7_2678605
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA7 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for IMCA8-----------------------------------------------------"""
#IC8 BDA 2688601 form
class Ic8_2688601_Form(forms.ModelForm):
    class Meta:
        model = Ic8_2688601
        fields = "__all__"

#IC8 AML 2688602 form
class Ic8_2688602_Form(forms.ModelForm):
    class Meta:
        model = Ic8_2688602
        fields = "__all__"
        
#IC8 DAA 2688603 form
class Ic8_2688603_Form(forms.ModelForm):
    class Meta:
        model = Ic8_2688603
        fields = "__all__"
        
#IC8 TW 2688604 form
class Ic8_2688604_Form(forms.ModelForm):
    class Meta:
        model = Ic8_2688604
        fields = "__all__"
        
#IC8 SP 2688605 form
class Ic8_2688605_Form(forms.ModelForm):
    class Meta:
        model = Ic8_2688605
        fields = "__all__"

#IC8 CF 2688607 form
class Ic8_2688607_Form(forms.ModelForm):
    class Meta:
        model = Ic8_2688607
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA8 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for IMCA9-----------------------------------------------------"""
#IC9 DP 2698601 form
class Ic9_2698601_Form(forms.ModelForm):
    class Meta:
        model = Ic9_2698601
        fields = "__all__"

#IC9 FSD 2698602 form
class Ic9_2698602_Form(forms.ModelForm):
    class Meta:
        model = Ic9_2698602
        fields = "__all__"
        
#IC9 EIC 2698603 form
class Ic9_2698603_Form(forms.ModelForm):
    class Meta:
        model = Ic9_2698603
        fields = "__all__"
        
#IC9 PM 2698604 form
class Ic9_2698604_Form(forms.ModelForm):
    class Meta:
        model = Ic9_2698604
        fields = "__all__"
        
#IC9 SP 2698605 form
class Ic9_2698605_Form(forms.ModelForm):
    class Meta:
        model = Ic9_2698605
        fields = "__all__"

#IC9 IOT 2698607 form
class Ic9_2698607_Form(forms.ModelForm):
    class Meta:
        model = Ic9_2698607
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA9 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for MCA1 -----------------------------------------------------"""
#MCA1 C-LANG 619401 form
class Mca1_619401_Form(forms.ModelForm):
    class Meta:
        model = Mca1_619401
        fields = "__all__"

#MCA1 JAVA 619402 form
class Mca1_619402_Form(forms.ModelForm):
    class Meta:
        model = Mca1_619402
        fields = "__all__"
        
#MCA1 BM 619403 form
class Mca1_619403_Form(forms.ModelForm):
    class Meta:
        model = Mca1_619403
        fields = "__all__"
        
#MCA1 RDBMS 619404 form
class Mca1_619404_Form(forms.ModelForm):
    class Meta:
        model = Mca1_619404
        fields = "__all__"
        
#MCA1 WDT-PHP 619405 form
class Mca1_619405_Form(forms.ModelForm):
    class Meta:
        model = Mca1_619405
        fields = "__all__"

#MCA1 BCC 619406 form
class Mca1_619406_Form(forms.ModelForm):
    class Meta:
        model = Mca1_619406
        fields = "__all__"
        
"""-----------------------------------------Form for MCA1 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for MCA2 -----------------------------------------------------"""
#MCA2 DS 629401 form
class Mca2_629401_Form(forms.ModelForm):
    class Meta:
        model = Mca2_629401
        fields = "__all__"

#MCA2 MP 629402 form
class Mca2_629402_Form(forms.ModelForm):
    class Meta:
        model = Mca2_629402
        fields = "__all__"
        
#MCA2 PY 629403 form
class Mca2_629403_Form(forms.ModelForm):
    class Meta:
        model = Mca2_629403
        fields = "__all__"
        
#MCA2 CN 629404 form
class Mca2_629404_Form(forms.ModelForm):
    class Meta:
        model = Mca2_629404
        fields = "__all__"
        
#MCA2 SP 629405 form
class Mca2_629405_Form(forms.ModelForm):
    class Meta:
        model = Mca2_629405
        fields = "__all__"

#MCA2 JWT 629408 form
class Mca2_629408_Form(forms.ModelForm):
    class Meta:
        model = Mca2_629408
        fields = "__all__"
        
"""-----------------------------------------Form for MCA2 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for MCA3 -----------------------------------------------------"""
#MCA3 DAA 639401 form
class Mca3_639401_Form(forms.ModelForm):
    class Meta:
        model = Mca3_639401
        fields = "__all__"

#MCA3 ML 639402 form
class Mca3_639402_Form(forms.ModelForm):
    class Meta:
        model = Mca3_639402
        fields = "__all__"
        
#MCA3 SE 639403 form
class Mca3_639403_Form(forms.ModelForm):
    class Meta:
        model = Mca3_639403
        fields = "__all__"
        
#MCA3 SP 639404 form
class Mca3_639404_Form(forms.ModelForm):
    class Meta:
        model = Mca3_639404
        fields = "__all__"
        
#MCA3 CC 639407 form
class Mca3_639407_Form(forms.ModelForm):
    class Meta:
        model = Mca3_639407
        fields = "__all__"

#MCA3 NCS 639410 form
class Mca3_639410_Form(forms.ModelForm):
    class Meta:
        model = Mca3_639410
        fields = "__all__"
        
"""-----------------------------------------Form for MCA3 Complete-----------------------------------------------------"""

        
"""-----------------------------------------Form for IMCA10 -----------------------------------------------------"""
#IC10 SP 4401601 form
class Ic10_4401601_Form(forms.ModelForm):
    class Meta:
        model = Ic10_4401601
        fields = "__all__"
        
"""-----------------------------------------Form for IMCA10 Complete-----------------------------------------------------"""

"""-----------------------------------------Form for MCA4 -----------------------------------------------------"""
#MCA4 SP 649401 form
class Mca4_649401_Form(forms.ModelForm):
    class Meta:
        model = Mca4_649401
        fields = "__all__"
        
"""-----------------------------------------Form for MCA4 Complete-----------------------------------------------------"""