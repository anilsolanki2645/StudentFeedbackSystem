import os
from datetime import date
from django.db.models import Sum
from django.http import HttpResponse
from home.models import Lecturer
from home.models import Myadmin
from home.models import Sem_serve
from django.shortcuts import render, redirect

from home.forms import Ic1_2618601_Form, Ic1_2618602_Form, Ic1_2618603_Form, Ic1_2618604_Form, Ic1_2618605_Form
from home.models import Ic1_2618601, Ic1_2618602, Ic1_2618603, Ic1_2618604, Ic1_2618605

from home.forms import Ic2_2628601_Form, Ic2_2628602_Form, Ic2_2628603_Form, Ic2_2628604_Form, Ic2_2628605_Form
from home.models import Ic2_2628601, Ic2_2628602, Ic2_2628603, Ic2_2628604, Ic2_2628605

from home.forms import Ic3_2638601_Form, Ic3_2638602_Form, Ic3_2638603_Form, Ic3_2638604_Form, Ic3_2638605_Form
from home.models import Ic3_2638601, Ic3_2638602, Ic3_2638603, Ic3_2638604, Ic3_2638605

from home.forms import Ic4_2648601_Form, Ic4_2648602_Form, Ic4_2648603_Form, Ic4_2648604_Form, Ic4_2648605_Form
from home.models import Ic4_2648601, Ic4_2648602, Ic4_2648603, Ic4_2648604, Ic4_2648605

from home.forms import Ic5_2658601_Form, Ic5_2658602_Form, Ic5_2658603_Form, Ic5_2658604_Form, Ic5_2658605_Form
from home.models import Ic5_2658601, Ic5_2658602, Ic5_2658603, Ic5_2658604, Ic5_2658605

from home.forms import Ic6_2668601_Form, Ic6_2668602_Form, Ic6_2668603_Form, Ic6_2668604_Form, Ic6_2668605_Form
from home.models import Ic6_2668601, Ic6_2668602, Ic6_2668603, Ic6_2668604, Ic6_2668605

from home.forms import Ic7_2678601_Form, Ic7_2678602_Form, Ic7_2678603_Form, Ic7_2678604_Form, Ic7_2678605_Form
from home.models import Ic7_2678601, Ic7_2678602, Ic7_2678603, Ic7_2678604, Ic7_2678605

from home.forms import Ic8_2688601_Form, Ic8_2688602_Form, Ic8_2688603_Form, Ic8_2688604_Form, Ic8_2688605_Form, Ic8_2688607_Form
from home.models import Ic8_2688601, Ic8_2688602, Ic8_2688603, Ic8_2688604, Ic8_2688605, Ic8_2688607

from home.forms import Ic9_2698601_Form, Ic9_2698602_Form, Ic9_2698603_Form, Ic9_2698604_Form, Ic9_2698605_Form, Ic9_2698607_Form
from home.models import Ic9_2698601, Ic9_2698602, Ic9_2698603, Ic9_2698604, Ic9_2698605, Ic9_2698607

from home.forms import Mca1_619401_Form, Mca1_619402_Form, Mca1_619403_Form, Mca1_619404_Form, Mca1_619405_Form, Mca1_619406_Form
from home.models import Mca1_619401, Mca1_619402, Mca1_619403, Mca1_619404, Mca1_619405, Mca1_619406

from home.forms import Mca2_629401_Form, Mca2_629402_Form, Mca2_629403_Form, Mca2_629404_Form, Mca2_629405_Form, Mca2_629408_Form
from home.models import Mca2_629401, Mca2_629402, Mca2_629403, Mca2_629404, Mca2_629405, Mca2_629408

from home.forms import Mca3_639401_Form, Mca3_639402_Form, Mca3_639403_Form, Mca3_639404_Form, Mca3_639407_Form, Mca3_639410_Form
from home.models import Mca3_639401, Mca3_639402, Mca3_639403, Mca3_639404, Mca3_639407, Mca3_639410

from home.forms import Ic10_4401601_Form
from home.models import Ic10_4401601

from home.forms import Mca4_649401_Form
from home.models import Mca4_649401

from home.forms import StudentForm
from home.models import Student

"""-----------------------------------Global variable for Imca 1 ----------------------------------------"""

#calculation for FCO_2618601
additionpr_2618601 = Ic1_2618601.objects.aggregate(total=Sum('pr2618601'))
additionpe_2618601 = Ic1_2618601.objects.aggregate(total=Sum('pe2618601'))
additionsk_2618601 = Ic1_2618601.objects.aggregate(total=Sum('sk2618601'))
additionmt_2618601 = Ic1_2618601.objects.aggregate(total=Sum('mt2618601'))
additionms_2618601 = Ic1_2618601.objects.aggregate(total=Sum('ms2618601'))
additionpa_2618601 = Ic1_2618601.objects.aggregate(total=Sum('pa2618601'))
additioncs_2618601 = Ic1_2618601.objects.aggregate(total=Sum('cs2618601'))
additionps_2618601 = Ic1_2618601.objects.aggregate(total=Sum('ps2618601'))
total_2618601 = Ic1_2618601.objects.aggregate(total=Sum('pr2618601')+Sum('pe2618601')+Sum('sk2618601')
                                              +Sum('mt2618601')+Sum('ms2618601')+Sum('pa2618601')+
                                              Sum('cs2618601')+Sum('ps2618601'))
    
#calculation for FOW_2618602
additionpr_2618602 = Ic1_2618602.objects.aggregate(total=Sum('pr2618602'))
additionpe_2618602 = Ic1_2618602.objects.aggregate(total=Sum('pe2618602'))
additionsk_2618602 = Ic1_2618602.objects.aggregate(total=Sum('sk2618602'))
additionmt_2618602 = Ic1_2618602.objects.aggregate(total=Sum('mt2618602'))
additionms_2618602 = Ic1_2618602.objects.aggregate(total=Sum('ms2618602'))
additionpa_2618602 = Ic1_2618602.objects.aggregate(total=Sum('pa2618602'))
additioncs_2618602 = Ic1_2618602.objects.aggregate(total=Sum('cs2618602'))
additionps_2618602 = Ic1_2618602.objects.aggregate(total=Sum('ps2618602'))
total_2618602 = Ic1_2618602.objects.aggregate(total=Sum('pr2618602')+Sum('pe2618602')+Sum('sk2618602')
                                             +Sum('mt2618602')+Sum('ms2618602')+Sum('pa2618602')+
                                             Sum('cs2618602')+Sum('ps2618602'))
    
#calculation for FOP_2618603
additionpr_2618603 = Ic1_2618603.objects.aggregate(total=Sum('pr2618603'))
additionpe_2618603 = Ic1_2618603.objects.aggregate(total=Sum('pe2618603'))
additionsk_2618603 = Ic1_2618603.objects.aggregate(total=Sum('sk2618603'))
additionmt_2618603 = Ic1_2618603.objects.aggregate(total=Sum('mt2618603'))
additionms_2618603 = Ic1_2618603.objects.aggregate(total=Sum('ms2618603'))
additionpa_2618603 = Ic1_2618603.objects.aggregate(total=Sum('pa2618603'))
additioncs_2618603 = Ic1_2618603.objects.aggregate(total=Sum('cs2618603'))
additionps_2618603 = Ic1_2618603.objects.aggregate(total=Sum('ps2618603'))
total_2618603 = Ic1_2618603.objects.aggregate(total=Sum('pr2618603')+Sum('pe2618603')+Sum('sk2618603')
                                             +Sum('mt2618603')+Sum('ms2618603')+Sum('pa2618603')+
                                             Sum('cs2618603')+Sum('ps2618603'))
    
#calculation for BM_2618604
additionpr_2618604 = Ic1_2618604.objects.aggregate(total=Sum('pr2618604'))
additionpe_2618604 = Ic1_2618604.objects.aggregate(total=Sum('pe2618604'))
additionsk_2618604 = Ic1_2618604.objects.aggregate(total=Sum('sk2618604'))
additionmt_2618604 = Ic1_2618604.objects.aggregate(total=Sum('mt2618604'))
additionms_2618604 = Ic1_2618604.objects.aggregate(total=Sum('ms2618604'))
additionpa_2618604 = Ic1_2618604.objects.aggregate(total=Sum('pa2618604'))
additioncs_2618604 = Ic1_2618604.objects.aggregate(total=Sum('cs2618604'))
additionps_2618604 = Ic1_2618604.objects.aggregate(total=Sum('ps2618604'))
total_2618604 = Ic1_2618604.objects.aggregate(total=Sum('pr2618604')+Sum('pe2618604')+Sum('sk2618604')
                                             +Sum('mt2618604')+Sum('ms2618604')+Sum('pa2618604')+
                                             Sum('cs2618604')+Sum('ps2618604'))
    
#calculation for CS_2618605
additionpr_2618605 = Ic1_2618605.objects.aggregate(total=Sum('pr2618605'))
additionpe_2618605 = Ic1_2618605.objects.aggregate(total=Sum('pe2618605'))
additionsk_2618605 = Ic1_2618605.objects.aggregate(total=Sum('sk2618605'))
additionmt_2618605 = Ic1_2618605.objects.aggregate(total=Sum('mt2618605'))
additionms_2618605 = Ic1_2618605.objects.aggregate(total=Sum('ms2618605'))
additionpa_2618605 = Ic1_2618605.objects.aggregate(total=Sum('pa2618605'))
additioncs_2618605 = Ic1_2618605.objects.aggregate(total=Sum('cs2618605'))
additionps_2618605 = Ic1_2618605.objects.aggregate(total=Sum('ps2618605'))
total_2618605 = Ic1_2618605.objects.aggregate(total=Sum('pr2618605')+Sum('pe2618605')+Sum('sk2618605')
                                             +Sum('mt2618605')+Sum('ms2618605')+Sum('pa2618605')+
                                             Sum('cs2618605')+Sum('ps2618605'))
    
#row parameters PR total calculation
totalpr_ic1 = additionpr_2618601['total'] + additionpr_2618602['total'] + additionpr_2618603['total'] + additionpr_2618604['total'] + additionpr_2618605['total']
#row parameters PE total calculation
totalpe_ic1 = additionpe_2618601['total'] + additionpe_2618602['total'] + additionpe_2618603['total'] + additionpe_2618604['total'] + additionpe_2618605['total']
#row parameters PR total calculation
totalsk_ic1 = additionsk_2618601['total'] + additionsk_2618602['total'] + additionsk_2618603['total'] + additionsk_2618604['total'] + additionsk_2618605['total']
#row parameters PE total calculation
totalmt_ic1 = additionmt_2618601['total'] + additionmt_2618602['total'] + additionmt_2618603['total'] + additionmt_2618604['total'] + additionmt_2618605['total']
#row parameters PR total calculation
totalms_ic1 = additionms_2618601['total'] + additionms_2618602['total'] + additionms_2618603['total'] + additionms_2618604['total'] + additionms_2618605['total']
#row parameters PE total calculation
totalpa_ic1 = additionpa_2618601['total'] + additionpa_2618602['total'] + additionpa_2618603['total'] + additionpa_2618604['total'] + additionpa_2618605['total']
#row parameters PR total calculation
totalcs_ic1 = additioncs_2618601['total'] + additioncs_2618602['total'] + additioncs_2618603['total'] + additioncs_2618604['total'] + additioncs_2618605['total']
#row parameters PE total calculation
totalps_ic1 = additionps_2618601['total'] + additionps_2618602['total'] + additionps_2618603['total'] + additionps_2618604['total'] + additionps_2618605['total']

#All Total Of IMCA 1 
all_total_ic1 = totalpr_ic1 + totalpe_ic1 + totalsk_ic1 + totalmt_ic1 + totalms_ic1 + totalpa_ic1 + totalcs_ic1 + totalps_ic1
    
#Attend Student
count_ic1 = Ic1_2618601.objects.count()
count_ic1-=1

"""-----------------------------------Global variable for Imca 1 Complete----------------------------------------"""

"""-----------------------------------Global variable for Imca 2 ----------------------------------------"""

#calculation for DS_2628601
additionpr_2628601 = Ic2_2628601.objects.aggregate(total=Sum('pr2628601'))
additionpe_2628601 = Ic2_2628601.objects.aggregate(total=Sum('pe2628601'))
additionsk_2628601 = Ic2_2628601.objects.aggregate(total=Sum('sk2628601'))
additionmt_2628601 = Ic2_2628601.objects.aggregate(total=Sum('mt2628601'))
additionms_2628601 = Ic2_2628601.objects.aggregate(total=Sum('ms2628601'))
additionpa_2628601 = Ic2_2628601.objects.aggregate(total=Sum('pa2628601'))
additioncs_2628601 = Ic2_2628601.objects.aggregate(total=Sum('cs2628601'))
additionps_2628601 = Ic2_2628601.objects.aggregate(total=Sum('ps2628601'))
total_2628601 = Ic2_2628601.objects.aggregate(total=Sum('pr2628601')+Sum('pe2628601')+Sum('sk2628601')
                                              +Sum('mt2628601')+Sum('ms2628601')+Sum('pa2628601')+
                                              Sum('cs2628601')+Sum('ps2628601'))
    
#calculation for ADVACE C_2628602
additionpr_2628602 = Ic2_2628602.objects.aggregate(total=Sum('pr2628602'))
additionpe_2628602 = Ic2_2628602.objects.aggregate(total=Sum('pe2628602'))
additionsk_2628602 = Ic2_2628602.objects.aggregate(total=Sum('sk2628602'))
additionmt_2628602 = Ic2_2628602.objects.aggregate(total=Sum('mt2628602'))
additionms_2628602 = Ic2_2628602.objects.aggregate(total=Sum('ms2628602'))
additionpa_2628602 = Ic2_2628602.objects.aggregate(total=Sum('pa2628602'))
additioncs_2628602 = Ic2_2628602.objects.aggregate(total=Sum('cs2628602'))
additionps_2628602 = Ic2_2628602.objects.aggregate(total=Sum('ps2628602'))
total_2628602 = Ic2_2628602.objects.aggregate(total=Sum('pr2628602')+Sum('pe2628602')+Sum('sk2628602')
                                             +Sum('mt2628602')+Sum('ms2628602')+Sum('pa2628602')+
                                             Sum('cs2628602')+Sum('ps2628602'))
    
#calculation for DBMS_2628603
additionpr_2628603 = Ic2_2628603.objects.aggregate(total=Sum('pr2628603'))
additionpe_2628603 = Ic2_2628603.objects.aggregate(total=Sum('pe2628603'))
additionsk_2628603 = Ic2_2628603.objects.aggregate(total=Sum('sk2628603'))
additionmt_2628603 = Ic2_2628603.objects.aggregate(total=Sum('mt2628603'))
additionms_2628603 = Ic2_2628603.objects.aggregate(total=Sum('ms2628603'))
additionpa_2628603 = Ic2_2628603.objects.aggregate(total=Sum('pa2628603'))
additioncs_2628603 = Ic2_2628603.objects.aggregate(total=Sum('cs2628603'))
additionps_2628603 = Ic2_2628603.objects.aggregate(total=Sum('ps2628603'))
total_2628603 = Ic2_2628603.objects.aggregate(total=Sum('pr2628603')+Sum('pe2628603')+Sum('sk2628603')
                                             +Sum('mt2628603')+Sum('ms2628603')+Sum('pa2628603')+
                                             Sum('cs2628603')+Sum('ps2628603'))
    
#calculation for OS_2628604
additionpr_2628604 = Ic2_2628604.objects.aggregate(total=Sum('pr2628604'))
additionpe_2628604 = Ic2_2628604.objects.aggregate(total=Sum('pe2628604'))
additionsk_2628604 = Ic2_2628604.objects.aggregate(total=Sum('sk2628604'))
additionmt_2628604 = Ic2_2628604.objects.aggregate(total=Sum('mt2628604'))
additionms_2628604 = Ic2_2628604.objects.aggregate(total=Sum('ms2628604'))
additionpa_2628604 = Ic2_2628604.objects.aggregate(total=Sum('pa2628604'))
additioncs_2628604 = Ic2_2628604.objects.aggregate(total=Sum('cs2628604'))
additionps_2628604 = Ic2_2628604.objects.aggregate(total=Sum('ps2628604'))
total_2628604 = Ic2_2628604.objects.aggregate(total=Sum('pr2628604')+Sum('pe2628604')+Sum('sk2628604')
                                             +Sum('mt2628604')+Sum('ms2628604')+Sum('pa2628604')+
                                             Sum('cs2628604')+Sum('ps2628604'))
    
#calculation for SP_2628605
additionpr_2628605 = Ic2_2628605.objects.aggregate(total=Sum('pr2628605'))
additionpe_2628605 = Ic2_2628605.objects.aggregate(total=Sum('pe2628605'))
additionsk_2628605 = Ic2_2628605.objects.aggregate(total=Sum('sk2628605'))
additionmt_2628605 = Ic2_2628605.objects.aggregate(total=Sum('mt2628605'))
additionms_2628605 = Ic2_2628605.objects.aggregate(total=Sum('ms2628605'))
additionpa_2628605 = Ic2_2628605.objects.aggregate(total=Sum('pa2628605'))
additioncs_2628605 = Ic2_2628605.objects.aggregate(total=Sum('cs2628605'))
additionps_2628605 = Ic2_2628605.objects.aggregate(total=Sum('ps2628605'))
total_2628605 = Ic2_2628605.objects.aggregate(total=Sum('pr2628605')+Sum('pe2628605')+Sum('sk2628605')
                                             +Sum('mt2628605')+Sum('ms2628605')+Sum('pa2628605')+
                                             Sum('cs2628605')+Sum('ps2628605'))
    
#row parameters PR total calculation
totalpr_ic2 = additionpr_2628601['total'] + additionpr_2628602['total'] + additionpr_2628603['total'] + additionpr_2628604['total'] + additionpr_2628605['total']
#row parameters PE total calculation
totalpe_ic2 = additionpe_2628601['total'] + additionpe_2628602['total'] + additionpe_2628603['total'] + additionpe_2628604['total'] + additionpe_2628605['total']
#row parameters PR total calculation
totalsk_ic2 = additionsk_2628601['total'] + additionsk_2628602['total'] + additionsk_2628603['total'] + additionsk_2628604['total'] + additionsk_2628605['total']
#row parameters PE total calculation
totalmt_ic2 = additionmt_2628601['total'] + additionmt_2628602['total'] + additionmt_2628603['total'] + additionmt_2628604['total'] + additionmt_2628605['total']
#row parameters PR total calculation
totalms_ic2 = additionms_2628601['total'] + additionms_2628602['total'] + additionms_2628603['total'] + additionms_2628604['total'] + additionms_2628605['total']
#row parameters PE total calculation
totalpa_ic2 = additionpa_2628601['total'] + additionpa_2628602['total'] + additionpa_2628603['total'] + additionpa_2628604['total'] + additionpa_2628605['total']
#row parameters PR total calculation
totalcs_ic2 = additioncs_2628601['total'] + additioncs_2628602['total'] + additioncs_2628603['total'] + additioncs_2628604['total'] + additioncs_2628605['total']
#row parameters PE total calculation
totalps_ic2 = additionps_2628601['total'] + additionps_2628602['total'] + additionps_2628603['total'] + additionps_2628604['total'] + additionps_2628605['total']

#All Total Of IMCA 2
all_total_ic2 = totalpr_ic2 + totalpe_ic2 + totalsk_ic2 + totalmt_ic2 + totalms_ic2 + totalpa_ic2 + totalcs_ic2 + totalps_ic2
    
#Attend Student
count_ic2 = Ic2_2628601.objects.count()
count_ic2-=1

"""-----------------------------------Global variable for Imca 2 Complete----------------------------------------"""

"""----------------------------------- Global variable for Imca 3 ----------------------------------------"""

#calculation for Java_2638601
additionpr_2638601 = Ic3_2638601.objects.aggregate(total=Sum('pr2638601'))
additionpe_2638601 = Ic3_2638601.objects.aggregate(total=Sum('pe2638601'))
additionsk_2638601 = Ic3_2638601.objects.aggregate(total=Sum('sk2638601'))
additionmt_2638601 = Ic3_2638601.objects.aggregate(total=Sum('mt2638601'))
additionms_2638601 = Ic3_2638601.objects.aggregate(total=Sum('ms2638601'))
additionpa_2638601 = Ic3_2638601.objects.aggregate(total=Sum('pa2638601'))
additioncs_2638601 = Ic3_2638601.objects.aggregate(total=Sum('cs2638601'))
additionps_2638601 = Ic3_2638601.objects.aggregate(total=Sum('ps2638601'))
total_2638601 = Ic3_2638601.objects.aggregate(total=Sum('pr2638601')+Sum('pe2638601')+Sum('sk2638601')
                                              +Sum('mt2638601')+Sum('ms2638601')+Sum('pa2638601')+
                                              Sum('cs2638601')+Sum('ps2638601'))
    
#calculation for BS_2638602
additionpr_2638602 = Ic3_2638602.objects.aggregate(total=Sum('pr2638602'))
additionpe_2638602 = Ic3_2638602.objects.aggregate(total=Sum('pe2638602'))
additionsk_2638602 = Ic3_2638602.objects.aggregate(total=Sum('sk2638602'))
additionmt_2638602 = Ic3_2638602.objects.aggregate(total=Sum('mt2638602'))
additionms_2638602 = Ic3_2638602.objects.aggregate(total=Sum('ms2638602'))
additionpa_2638602 = Ic3_2638602.objects.aggregate(total=Sum('pa2638602'))
additioncs_2638602 = Ic3_2638602.objects.aggregate(total=Sum('cs2638602'))
additionps_2638602 = Ic3_2638602.objects.aggregate(total=Sum('ps2638602'))
total_2638602 = Ic3_2638602.objects.aggregate(total=Sum('pr2638602')+Sum('pe2638602')+Sum('sk2638602')
                                             +Sum('mt2638602')+Sum('ms2638602')+Sum('pa2638602')+
                                             Sum('cs2638602')+Sum('ps2638602'))
    
#calculation for SOODAM_2638603
additionpr_2638603 = Ic3_2638603.objects.aggregate(total=Sum('pr2638603'))
additionpe_2638603 = Ic3_2638603.objects.aggregate(total=Sum('pe2638603'))
additionsk_2638603 = Ic3_2638603.objects.aggregate(total=Sum('sk2638603'))
additionmt_2638603 = Ic3_2638603.objects.aggregate(total=Sum('mt2638603'))
additionms_2638603 = Ic3_2638603.objects.aggregate(total=Sum('ms2638603'))
additionpa_2638603 = Ic3_2638603.objects.aggregate(total=Sum('pa2638603'))
additioncs_2638603 = Ic3_2638603.objects.aggregate(total=Sum('cs2638603'))
additionps_2638603 = Ic3_2638603.objects.aggregate(total=Sum('ps2638603'))
total_2638603 = Ic3_2638603.objects.aggregate(total=Sum('pr2638603')+Sum('pe2638603')+Sum('sk2638603')
                                             +Sum('mt2638603')+Sum('ms2638603')+Sum('pa2638603')+
                                             Sum('cs2638603')+Sum('ps2638603'))
    
#calculation for WDT_2638604
additionpr_2638604 = Ic3_2638604.objects.aggregate(total=Sum('pr2638604'))
additionpe_2638604 = Ic3_2638604.objects.aggregate(total=Sum('pe2638604'))
additionsk_2638604 = Ic3_2638604.objects.aggregate(total=Sum('sk2638604'))
additionmt_2638604 = Ic3_2638604.objects.aggregate(total=Sum('mt2638604'))
additionms_2638604 = Ic3_2638604.objects.aggregate(total=Sum('ms2638604'))
additionpa_2638604 = Ic3_2638604.objects.aggregate(total=Sum('pa2638604'))
additioncs_2638604 = Ic3_2638604.objects.aggregate(total=Sum('cs2638604'))
additionps_2638604 = Ic3_2638604.objects.aggregate(total=Sum('ps2638604'))
total_2638604 = Ic3_2638604.objects.aggregate(total=Sum('pr2638604')+Sum('pe2638604')+Sum('sk2638604')
                                             +Sum('mt2638604')+Sum('ms2638604')+Sum('pa2638604')+
                                             Sum('cs2638604')+Sum('ps2638604'))
    
#calculation for SPDS_2638605
additionpr_2638605 = Ic3_2638605.objects.aggregate(total=Sum('pr2638605'))
additionpe_2638605 = Ic3_2638605.objects.aggregate(total=Sum('pe2638605'))
additionsk_2638605 = Ic3_2638605.objects.aggregate(total=Sum('sk2638605'))
additionmt_2638605 = Ic3_2638605.objects.aggregate(total=Sum('mt2638605'))
additionms_2638605 = Ic3_2638605.objects.aggregate(total=Sum('ms2638605'))
additionpa_2638605 = Ic3_2638605.objects.aggregate(total=Sum('pa2638605'))
additioncs_2638605 = Ic3_2638605.objects.aggregate(total=Sum('cs2638605'))
additionps_2638605 = Ic3_2638605.objects.aggregate(total=Sum('ps2638605'))
total_2638605 = Ic3_2638605.objects.aggregate(total=Sum('pr2638605')+Sum('pe2638605')+Sum('sk2638605')
                                             +Sum('mt2638605')+Sum('ms2638605')+Sum('pa2638605')+
                                             Sum('cs2638605')+Sum('ps2638605'))
    
#row parameters PR total calculation
totalpr_ic3 = additionpr_2638601['total'] + additionpr_2638602['total'] + additionpr_2638603['total'] + additionpr_2638604['total'] + additionpr_2638605['total']
#row parameters PE total calculation
totalpe_ic3 = additionpe_2638601['total'] + additionpe_2638602['total'] + additionpe_2638603['total'] + additionpe_2638604['total'] + additionpe_2638605['total']
#row parameters PR total calculation
totalsk_ic3 = additionsk_2638601['total'] + additionsk_2638602['total'] + additionsk_2638603['total'] + additionsk_2638604['total'] + additionsk_2638605['total']
#row parameters PE total calculation
totalmt_ic3 = additionmt_2638601['total'] + additionmt_2638602['total'] + additionmt_2638603['total'] + additionmt_2638604['total'] + additionmt_2638605['total']
#row parameters PR total calculation
totalms_ic3 = additionms_2638601['total'] + additionms_2638602['total'] + additionms_2638603['total'] + additionms_2638604['total'] + additionms_2638605['total']
#row parameters PE total calculation
totalpa_ic3 = additionpa_2638601['total'] + additionpa_2638602['total'] + additionpa_2638603['total'] + additionpa_2638604['total'] + additionpa_2638605['total']
#row parameters PR total calculation
totalcs_ic3 = additioncs_2638601['total'] + additioncs_2638602['total'] + additioncs_2638603['total'] + additioncs_2638604['total'] + additioncs_2638605['total']
#row parameters PE total calculation
totalps_ic3 = additionps_2638601['total'] + additionps_2638602['total'] + additionps_2638603['total'] + additionps_2638604['total'] + additionps_2638605['total']

#All Total Of IMCA 3 
all_total_ic3 = totalpr_ic3 + totalpe_ic3 + totalsk_ic3 + totalmt_ic3 + totalms_ic3 + totalpa_ic3 + totalcs_ic3 + totalps_ic3
    
#Attend Student
count_ic3 = Ic3_2638601.objects.count()
count_ic3-=1

"""-----------------------------------Global variable for Imca 3 Complete----------------------------------------"""

"""----------------------------------- Global variable for Imca 4 ----------------------------------------"""

#calculation for PY_2648601
additionpr_2648601 = Ic4_2648601.objects.aggregate(total=Sum('pr2648601'))
additionpe_2648601 = Ic4_2648601.objects.aggregate(total=Sum('pe2648601'))
additionsk_2648601 = Ic4_2648601.objects.aggregate(total=Sum('sk2648601'))
additionmt_2648601 = Ic4_2648601.objects.aggregate(total=Sum('mt2648601'))
additionms_2648601 = Ic4_2648601.objects.aggregate(total=Sum('ms2648601'))
additionpa_2648601 = Ic4_2648601.objects.aggregate(total=Sum('pa2648601'))
additioncs_2648601 = Ic4_2648601.objects.aggregate(total=Sum('cs2648601'))
additionps_2648601 = Ic4_2648601.objects.aggregate(total=Sum('ps2648601'))
total_2648601 = Ic4_2648601.objects.aggregate(total=Sum('pr2648601')+Sum('pe2648601')+Sum('sk2648601')
                                              +Sum('mt2648601')+Sum('ms2648601')+Sum('pa2648601')+
                                              Sum('cs2648601')+Sum('ps2648601'))
    
#calculation for OR_2648602
additionpr_2648602 = Ic4_2648602.objects.aggregate(total=Sum('pr2648602'))
additionpe_2648602 = Ic4_2648602.objects.aggregate(total=Sum('pe2648602'))
additionsk_2648602 = Ic4_2648602.objects.aggregate(total=Sum('sk2648602'))
additionmt_2648602 = Ic4_2648602.objects.aggregate(total=Sum('mt2648602'))
additionms_2648602 = Ic4_2648602.objects.aggregate(total=Sum('ms2648602'))
additionpa_2648602 = Ic4_2648602.objects.aggregate(total=Sum('pa2648602'))
additioncs_2648602 = Ic4_2648602.objects.aggregate(total=Sum('cs2648602'))
additionps_2648602 = Ic4_2648602.objects.aggregate(total=Sum('ps2648602'))
total_2648602 = Ic4_2648602.objects.aggregate(total=Sum('pr2648602')+Sum('pe2648602')+Sum('sk2648602')
                                             +Sum('mt2648602')+Sum('ms2648602')+Sum('pa2648602')+
                                             Sum('cs2648602')+Sum('ps2648602'))
    
#calculation for CN_2648603
additionpr_2648603 = Ic4_2648603.objects.aggregate(total=Sum('pr2648603'))
additionpe_2648603 = Ic4_2648603.objects.aggregate(total=Sum('pe2648603'))
additionsk_2648603 = Ic4_2648603.objects.aggregate(total=Sum('sk2648603'))
additionmt_2648603 = Ic4_2648603.objects.aggregate(total=Sum('mt2648603'))
additionms_2648603 = Ic4_2648603.objects.aggregate(total=Sum('ms2648603'))
additionpa_2648603 = Ic4_2648603.objects.aggregate(total=Sum('pa2648603'))
additioncs_2648603 = Ic4_2648603.objects.aggregate(total=Sum('cs2648603'))
additionps_2648603 = Ic4_2648603.objects.aggregate(total=Sum('ps2648603'))
total_2648603 = Ic4_2648603.objects.aggregate(total=Sum('pr2648603')+Sum('pe2648603')+Sum('sk2648603')
                                             +Sum('mt2648603')+Sum('ms2648603')+Sum('pa2648603')+
                                             Sum('cs2648603')+Sum('ps2648603'))
    
#calculation for LR_2648604
additionpr_2648604 = Ic4_2648604.objects.aggregate(total=Sum('pr2648604'))
additionpe_2648604 = Ic4_2648604.objects.aggregate(total=Sum('pe2648604'))
additionsk_2648604 = Ic4_2648604.objects.aggregate(total=Sum('sk2648604'))
additionmt_2648604 = Ic4_2648604.objects.aggregate(total=Sum('mt2648604'))
additionms_2648604 = Ic4_2648604.objects.aggregate(total=Sum('ms2648604'))
additionpa_2648604 = Ic4_2648604.objects.aggregate(total=Sum('pa2648604'))
additioncs_2648604 = Ic4_2648604.objects.aggregate(total=Sum('cs2648604'))
additionps_2648604 = Ic4_2648604.objects.aggregate(total=Sum('ps2648604'))
total_2648604 = Ic4_2648604.objects.aggregate(total=Sum('pr2648604')+Sum('pe2648604')+Sum('sk2648604')
                                             +Sum('mt2648604')+Sum('ms2648604')+Sum('pa2648604')+
                                             Sum('cs2648604')+Sum('ps2648604'))
    
#calculation for SPJAVA_2648605
additionpr_2648605 = Ic4_2648605.objects.aggregate(total=Sum('pr2648605'))
additionpe_2648605 = Ic4_2648605.objects.aggregate(total=Sum('pe2648605'))
additionsk_2648605 = Ic4_2648605.objects.aggregate(total=Sum('sk2648605'))
additionmt_2648605 = Ic4_2648605.objects.aggregate(total=Sum('mt2648605'))
additionms_2648605 = Ic4_2648605.objects.aggregate(total=Sum('ms2648605'))
additionpa_2648605 = Ic4_2648605.objects.aggregate(total=Sum('pa2648605'))
additioncs_2648605 = Ic4_2648605.objects.aggregate(total=Sum('cs2648605'))
additionps_2648605 = Ic4_2648605.objects.aggregate(total=Sum('ps2648605'))
total_2648605 = Ic4_2648605.objects.aggregate(total=Sum('pr2648605')+Sum('pe2648605')+Sum('sk2648605')
                                             +Sum('mt2648605')+Sum('ms2648605')+Sum('pa2648605')+
                                             Sum('cs2648605')+Sum('ps2648605'))
    
#row parameters PR total calculation
totalpr_ic4 = additionpr_2648601['total'] + additionpr_2648602['total'] + additionpr_2648603['total'] + additionpr_2648604['total'] + additionpr_2648605['total']
#row parameters PE total calculation
totalpe_ic4 = additionpe_2648601['total'] + additionpe_2648602['total'] + additionpe_2648603['total'] + additionpe_2648604['total'] + additionpe_2648605['total']
#row parameters PR total calculation
totalsk_ic4 = additionsk_2648601['total'] + additionsk_2648602['total'] + additionsk_2648603['total'] + additionsk_2648604['total'] + additionsk_2648605['total']
#row parameters PE total calculation
totalmt_ic4 = additionmt_2648601['total'] + additionmt_2648602['total'] + additionmt_2648603['total'] + additionmt_2648604['total'] + additionmt_2648605['total']
#row parameters PR total calculation
totalms_ic4 = additionms_2648601['total'] + additionms_2648602['total'] + additionms_2648603['total'] + additionms_2648604['total'] + additionms_2648605['total']
#row parameters PE total calculation
totalpa_ic4 = additionpa_2648601['total'] + additionpa_2648602['total'] + additionpa_2648603['total'] + additionpa_2648604['total'] + additionpa_2648605['total']
#row parameters PR total calculation
totalcs_ic4 = additioncs_2648601['total'] + additioncs_2648602['total'] + additioncs_2648603['total'] + additioncs_2648604['total'] + additioncs_2648605['total']
#row parameters PE total calculation
totalps_ic4 = additionps_2648601['total'] + additionps_2648602['total'] + additionps_2648603['total'] + additionps_2648604['total'] + additionps_2648605['total']

#All Total Of IMCA 4 
all_total_ic4 = totalpr_ic4 + totalpe_ic4 + totalsk_ic4 + totalmt_ic4 + totalms_ic4 + totalpa_ic4 + totalcs_ic4 + totalps_ic4
    
#Attend Student
count_ic4 = Ic4_2648601.objects.count()
count_ic4-=1

"""-----------------------------------Global variable for Imca 4 Complete----------------------------------------"""

"""----------------------------------- Global variable for Imca 5 ----------------------------------------"""

#calculation for A.JAVA_2658601
additionpr_2658601 = Ic5_2658601.objects.aggregate(total=Sum('pr2658601'))
additionpe_2658601 = Ic5_2658601.objects.aggregate(total=Sum('pe2658601'))
additionsk_2658601 = Ic5_2658601.objects.aggregate(total=Sum('sk2658601'))
additionmt_2658601 = Ic5_2658601.objects.aggregate(total=Sum('mt2658601'))
additionms_2658601 = Ic5_2658601.objects.aggregate(total=Sum('ms2658601'))
additionpa_2658601 = Ic5_2658601.objects.aggregate(total=Sum('pa2658601'))
additioncs_2658601 = Ic5_2658601.objects.aggregate(total=Sum('cs2658601'))
additionps_2658601 = Ic5_2658601.objects.aggregate(total=Sum('ps2658601'))
total_2658601 = Ic5_2658601.objects.aggregate(total=Sum('pr2658601')+Sum('pe2658601')+Sum('sk2658601')
                                              +Sum('mt2658601')+Sum('ms2658601')+Sum('pa2658601')+
                                              Sum('cs2658601')+Sum('ps2658601'))
    
#calculation for MP_2658602
additionpr_2658602 = Ic5_2658602.objects.aggregate(total=Sum('pr2658602'))
additionpe_2658602 = Ic5_2658602.objects.aggregate(total=Sum('pe2658602'))
additionsk_2658602 = Ic5_2658602.objects.aggregate(total=Sum('sk2658602'))
additionmt_2658602 = Ic5_2658602.objects.aggregate(total=Sum('mt2658602'))
additionms_2658602 = Ic5_2658602.objects.aggregate(total=Sum('ms2658602'))
additionpa_2658602 = Ic5_2658602.objects.aggregate(total=Sum('pa2658602'))
additioncs_2658602 = Ic5_2658602.objects.aggregate(total=Sum('cs2658602'))
additionps_2658602 = Ic5_2658602.objects.aggregate(total=Sum('ps2658602'))
total_2658602 = Ic5_2658602.objects.aggregate(total=Sum('pr2658602')+Sum('pe2658602')+Sum('sk2658602')
                                             +Sum('mt2658602')+Sum('ms2658602')+Sum('pa2658602')+
                                             Sum('cs2658602')+Sum('ps2658602'))
    
#calculation for SE_2658603
additionpr_2658603 = Ic5_2658603.objects.aggregate(total=Sum('pr2658603'))
additionpe_2658603 = Ic5_2658603.objects.aggregate(total=Sum('pe2658603'))
additionsk_2658603 = Ic5_2658603.objects.aggregate(total=Sum('sk2658603'))
additionmt_2658603 = Ic5_2658603.objects.aggregate(total=Sum('mt2658603'))
additionms_2658603 = Ic5_2658603.objects.aggregate(total=Sum('ms2658603'))
additionpa_2658603 = Ic5_2658603.objects.aggregate(total=Sum('pa2658603'))
additioncs_2658603 = Ic5_2658603.objects.aggregate(total=Sum('cs2658603'))
additionps_2658603 = Ic5_2658603.objects.aggregate(total=Sum('ps2658603'))
total_2658603 = Ic5_2658603.objects.aggregate(total=Sum('pr2658603')+Sum('pe2658603')+Sum('sk2658603')
                                             +Sum('mt2658603')+Sum('ms2658603')+Sum('pa2658603')+
                                             Sum('cs2658603')+Sum('ps2658603'))
    
#calculation for E.COMM_2658604
additionpr_2658604 = Ic5_2658604.objects.aggregate(total=Sum('pr2658604'))
additionpe_2658604 = Ic5_2658604.objects.aggregate(total=Sum('pe2658604'))
additionsk_2658604 = Ic5_2658604.objects.aggregate(total=Sum('sk2658604'))
additionmt_2658604 = Ic5_2658604.objects.aggregate(total=Sum('mt2658604'))
additionms_2658604 = Ic5_2658604.objects.aggregate(total=Sum('ms2658604'))
additionpa_2658604 = Ic5_2658604.objects.aggregate(total=Sum('pa2658604'))
additioncs_2658604 = Ic5_2658604.objects.aggregate(total=Sum('cs2658604'))
additionps_2658604 = Ic5_2658604.objects.aggregate(total=Sum('ps2658604'))
total_2658604 = Ic5_2658604.objects.aggregate(total=Sum('pr2658604')+Sum('pe2658604')+Sum('sk2658604')
                                             +Sum('mt2658604')+Sum('ms2658604')+Sum('pa2658604')+
                                             Sum('cs2658604')+Sum('ps2658604'))
    
#calculation for SP SPRING_2658605
additionpr_2658605 = Ic5_2658605.objects.aggregate(total=Sum('pr2658605'))
additionpe_2658605 = Ic5_2658605.objects.aggregate(total=Sum('pe2658605'))
additionsk_2658605 = Ic5_2658605.objects.aggregate(total=Sum('sk2658605'))
additionmt_2658605 = Ic5_2658605.objects.aggregate(total=Sum('mt2658605'))
additionms_2658605 = Ic5_2658605.objects.aggregate(total=Sum('ms2658605'))
additionpa_2658605 = Ic5_2658605.objects.aggregate(total=Sum('pa2658605'))
additioncs_2658605 = Ic5_2658605.objects.aggregate(total=Sum('cs2658605'))
additionps_2658605 = Ic5_2658605.objects.aggregate(total=Sum('ps2658605'))
total_2658605 = Ic5_2658605.objects.aggregate(total=Sum('pr2658605')+Sum('pe2658605')+Sum('sk2658605')
                                             +Sum('mt2658605')+Sum('ms2658605')+Sum('pa2658605')+
                                             Sum('cs2658605')+Sum('ps2658605'))
    
#row parameters PR total calculation
totalpr_ic5 = additionpr_2658601['total'] + additionpr_2658602['total'] + additionpr_2658603['total'] + additionpr_2658604['total'] + additionpr_2658605['total']
#row parameters PE total calculation
totalpe_ic5 = additionpe_2658601['total'] + additionpe_2658602['total'] + additionpe_2658603['total'] + additionpe_2658604['total'] + additionpe_2658605['total']
#row parameters PR total calculation
totalsk_ic5 = additionsk_2658601['total'] + additionsk_2658602['total'] + additionsk_2658603['total'] + additionsk_2658604['total'] + additionsk_2658605['total']
#row parameters PE total calculation
totalmt_ic5 = additionmt_2658601['total'] + additionmt_2658602['total'] + additionmt_2658603['total'] + additionmt_2658604['total'] + additionmt_2658605['total']
#row parameters PR total calculation
totalms_ic5 = additionms_2658601['total'] + additionms_2658602['total'] + additionms_2658603['total'] + additionms_2658604['total'] + additionms_2658605['total']
#row parameters PE total calculation
totalpa_ic5 = additionpa_2658601['total'] + additionpa_2658602['total'] + additionpa_2658603['total'] + additionpa_2658604['total'] + additionpa_2658605['total']
#row parameters PR total calculation
totalcs_ic5 = additioncs_2658601['total'] + additioncs_2658602['total'] + additioncs_2658603['total'] + additioncs_2658604['total'] + additioncs_2658605['total']
#row parameters PE total calculation
totalps_ic5 = additionps_2658601['total'] + additionps_2658602['total'] + additionps_2658603['total'] + additionps_2658604['total'] + additionps_2658605['total']

#All Total Of IMCA 5 
all_total_ic5 = totalpr_ic5 + totalpe_ic5 + totalsk_ic5 + totalmt_ic5 + totalms_ic5 + totalpa_ic5 + totalcs_ic5 + totalps_ic5
    
#Attend Student
count_ic5 = Ic5_2658601.objects.count()
count_ic5-=1

"""-----------------------------------Global variable for Imca 5 Complete----------------------------------------"""

"""----------------------------------- Global variable for Imca 6 ----------------------------------------"""

#calculation for MIS_2668601
additionpr_2668601 = Ic6_2668601.objects.aggregate(total=Sum('pr2668601'))
additionpe_2668601 = Ic6_2668601.objects.aggregate(total=Sum('pe2668601'))
additionsk_2668601 = Ic6_2668601.objects.aggregate(total=Sum('sk2668601'))
additionmt_2668601 = Ic6_2668601.objects.aggregate(total=Sum('mt2668601'))
additionms_2668601 = Ic6_2668601.objects.aggregate(total=Sum('ms2668601'))
additionpa_2668601 = Ic6_2668601.objects.aggregate(total=Sum('pa2668601'))
additioncs_2668601 = Ic6_2668601.objects.aggregate(total=Sum('cs2668601'))
additionps_2668601 = Ic6_2668601.objects.aggregate(total=Sum('ps2668601'))
total_2668601 = Ic6_2668601.objects.aggregate(total=Sum('pr2668601')+Sum('pe2668601')+Sum('sk2668601')
                                              +Sum('mt2668601')+Sum('ms2668601')+Sum('pa2668601')+
                                              Sum('cs2668601')+Sum('ps2668601'))
    
#calculation for ST_2668602
additionpr_2668602 = Ic6_2668602.objects.aggregate(total=Sum('pr2668602'))
additionpe_2668602 = Ic6_2668602.objects.aggregate(total=Sum('pe2668602'))
additionsk_2668602 = Ic6_2668602.objects.aggregate(total=Sum('sk2668602'))
additionmt_2668602 = Ic6_2668602.objects.aggregate(total=Sum('mt2668602'))
additionms_2668602 = Ic6_2668602.objects.aggregate(total=Sum('ms2668602'))
additionpa_2668602 = Ic6_2668602.objects.aggregate(total=Sum('pa2668602'))
additioncs_2668602 = Ic6_2668602.objects.aggregate(total=Sum('cs2668602'))
additionps_2668602 = Ic6_2668602.objects.aggregate(total=Sum('ps2668602'))
total_2668602 = Ic6_2668602.objects.aggregate(total=Sum('pr2668602')+Sum('pe2668602')+Sum('sk2668602')
                                             +Sum('mt2668602')+Sum('ms2668602')+Sum('pa2668602')+
                                             Sum('cs2668602')+Sum('ps2668602'))
    
#calculation for DM_2668603
additionpr_2668603 = Ic6_2668603.objects.aggregate(total=Sum('pr2668603'))
additionpe_2668603 = Ic6_2668603.objects.aggregate(total=Sum('pe2668603'))
additionsk_2668603 = Ic6_2668603.objects.aggregate(total=Sum('sk2668603'))
additionmt_2668603 = Ic6_2668603.objects.aggregate(total=Sum('mt2668603'))
additionms_2668603 = Ic6_2668603.objects.aggregate(total=Sum('ms2668603'))
additionpa_2668603 = Ic6_2668603.objects.aggregate(total=Sum('pa2668603'))
additioncs_2668603 = Ic6_2668603.objects.aggregate(total=Sum('cs2668603'))
additionps_2668603 = Ic6_2668603.objects.aggregate(total=Sum('ps2668603'))
total_2668603 = Ic6_2668603.objects.aggregate(total=Sum('pr2668603')+Sum('pe2668603')+Sum('sk2668603')
                                             +Sum('mt2668603')+Sum('ms2668603')+Sum('pa2668603')+
                                             Sum('cs2668603')+Sum('ps2668603'))
    
#calculation for ES_2668604
additionpr_2668604 = Ic6_2668604.objects.aggregate(total=Sum('pr2668604'))
additionpe_2668604 = Ic6_2668604.objects.aggregate(total=Sum('pe2668604'))
additionsk_2668604 = Ic6_2668604.objects.aggregate(total=Sum('sk2668604'))
additionmt_2668604 = Ic6_2668604.objects.aggregate(total=Sum('mt2668604'))
additionms_2668604 = Ic6_2668604.objects.aggregate(total=Sum('ms2668604'))
additionpa_2668604 = Ic6_2668604.objects.aggregate(total=Sum('pa2668604'))
additioncs_2668604 = Ic6_2668604.objects.aggregate(total=Sum('cs2668604'))
additionps_2668604 = Ic6_2668604.objects.aggregate(total=Sum('ps2668604'))
total_2668604 = Ic6_2668604.objects.aggregate(total=Sum('pr2668604')+Sum('pe2668604')+Sum('sk2668604')
                                             +Sum('mt2668604')+Sum('ms2668604')+Sum('pa2668604')+
                                             Sum('cs2668604')+Sum('ps2668604'))
    
#calculation for SP ASP_2668605
additionpr_2668605 = Ic6_2668605.objects.aggregate(total=Sum('pr2668605'))
additionpe_2668605 = Ic6_2668605.objects.aggregate(total=Sum('pe2668605'))
additionsk_2668605 = Ic6_2668605.objects.aggregate(total=Sum('sk2668605'))
additionmt_2668605 = Ic6_2668605.objects.aggregate(total=Sum('mt2668605'))
additionms_2668605 = Ic6_2668605.objects.aggregate(total=Sum('ms2668605'))
additionpa_2668605 = Ic6_2668605.objects.aggregate(total=Sum('pa2668605'))
additioncs_2668605 = Ic6_2668605.objects.aggregate(total=Sum('cs2668605'))
additionps_2668605 = Ic6_2668605.objects.aggregate(total=Sum('ps2668605'))
total_2668605 = Ic6_2668605.objects.aggregate(total=Sum('pr2668605')+Sum('pe2668605')+Sum('sk2668605')
                                             +Sum('mt2668605')+Sum('ms2668605')+Sum('pa2668605')+
                                             Sum('cs2668605')+Sum('ps2668605'))
    
#row parameters PR total calculation
totalpr_ic6 = additionpr_2668601['total'] + additionpr_2668602['total'] + additionpr_2668603['total'] + additionpr_2668604['total'] + additionpr_2668605['total']
#row parameters PE total calculation
totalpe_ic6 = additionpe_2668601['total'] + additionpe_2668602['total'] + additionpe_2668603['total'] + additionpe_2668604['total'] + additionpe_2668605['total']
#row parameters PR total calculation
totalsk_ic6 = additionsk_2668601['total'] + additionsk_2668602['total'] + additionsk_2668603['total'] + additionsk_2668604['total'] + additionsk_2668605['total']
#row parameters PE total calculation
totalmt_ic6 = additionmt_2668601['total'] + additionmt_2668602['total'] + additionmt_2668603['total'] + additionmt_2668604['total'] + additionmt_2668605['total']
#row parameters PR total calculation
totalms_ic6 = additionms_2668601['total'] + additionms_2668602['total'] + additionms_2668603['total'] + additionms_2668604['total'] + additionms_2668605['total']
#row parameters PE total calculation
totalpa_ic6 = additionpa_2668601['total'] + additionpa_2668602['total'] + additionpa_2668603['total'] + additionpa_2668604['total'] + additionpa_2668605['total']
#row parameters PR total calculation
totalcs_ic6 = additioncs_2668601['total'] + additioncs_2668602['total'] + additioncs_2668603['total'] + additioncs_2668604['total'] + additioncs_2668605['total']
#row parameters PE total calculation
totalps_ic6 = additionps_2668601['total'] + additionps_2668602['total'] + additionps_2668603['total'] + additionps_2668604['total'] + additionps_2668605['total']

#All Total Of IMCA 6
all_total_ic6 = totalpr_ic6 + totalpe_ic6 + totalsk_ic6 + totalmt_ic6 + totalms_ic6 + totalpa_ic6 + totalcs_ic6 + totalps_ic6
    
#Attend Student
count_ic6 = Ic6_2668601.objects.count()
count_ic6-=1

"""-----------------------------------Global variable for Imca 6 Complete----------------------------------------"""

"""----------------------------------- Global variable for Imca 7 ----------------------------------------"""

#calculation for ML_2678601
additionpr_2678601 = Ic7_2678601.objects.aggregate(total=Sum('pr2678601'))
additionpe_2678601 = Ic7_2678601.objects.aggregate(total=Sum('pe2678601'))
additionsk_2678601 = Ic7_2678601.objects.aggregate(total=Sum('sk2678601'))
additionmt_2678601 = Ic7_2678601.objects.aggregate(total=Sum('mt2678601'))
additionms_2678601 = Ic7_2678601.objects.aggregate(total=Sum('ms2678601'))
additionpa_2678601 = Ic7_2678601.objects.aggregate(total=Sum('pa2678601'))
additioncs_2678601 = Ic7_2678601.objects.aggregate(total=Sum('cs2678601'))
additionps_2678601 = Ic7_2678601.objects.aggregate(total=Sum('ps2678601'))
total_2678601 = Ic7_2678601.objects.aggregate(total=Sum('pr2678601')+Sum('pe2678601')+Sum('sk2678601')
                                              +Sum('mt2678601')+Sum('ms2678601')+Sum('pa2678601')+
                                              Sum('cs2678601')+Sum('ps2678601'))
    
#calculation for AMP_2678602
additionpr_2678602 = Ic7_2678602.objects.aggregate(total=Sum('pr2678602'))
additionpe_2678602 = Ic7_2678602.objects.aggregate(total=Sum('pe2678602'))
additionsk_2678602 = Ic7_2678602.objects.aggregate(total=Sum('sk2678602'))
additionmt_2678602 = Ic7_2678602.objects.aggregate(total=Sum('mt2678602'))
additionms_2678602 = Ic7_2678602.objects.aggregate(total=Sum('ms2678602'))
additionpa_2678602 = Ic7_2678602.objects.aggregate(total=Sum('pa2678602'))
additioncs_2678602 = Ic7_2678602.objects.aggregate(total=Sum('cs2678602'))
additionps_2678602 = Ic7_2678602.objects.aggregate(total=Sum('ps2678602'))
total_2678602 = Ic7_2678602.objects.aggregate(total=Sum('pr2678602')+Sum('pe2678602')+Sum('sk2678602')
                                             +Sum('mt2678602')+Sum('ms2678602')+Sum('pa2678602')+
                                             Sum('cs2678602')+Sum('ps2678602'))
    
#calculation for CS_2678603
additionpr_2678603 = Ic7_2678603.objects.aggregate(total=Sum('pr2678603'))
additionpe_2678603 = Ic7_2678603.objects.aggregate(total=Sum('pe2678603'))
additionsk_2678603 = Ic7_2678603.objects.aggregate(total=Sum('sk2678603'))
additionmt_2678603 = Ic7_2678603.objects.aggregate(total=Sum('mt2678603'))
additionms_2678603 = Ic7_2678603.objects.aggregate(total=Sum('ms2678603'))
additionpa_2678603 = Ic7_2678603.objects.aggregate(total=Sum('pa2678603'))
additioncs_2678603 = Ic7_2678603.objects.aggregate(total=Sum('cs2678603'))
additionps_2678603 = Ic7_2678603.objects.aggregate(total=Sum('ps2678603'))
total_2678603 = Ic7_2678603.objects.aggregate(total=Sum('pr2678603')+Sum('pe2678603')+Sum('sk2678603')
                                             +Sum('mt2678603')+Sum('ms2678603')+Sum('pa2678603')+
                                             Sum('cs2678603')+Sum('ps2678603'))
    
#calculation for SP_2678604
additionpr_2678604 = Ic7_2678604.objects.aggregate(total=Sum('pr2678604'))
additionpe_2678604 = Ic7_2678604.objects.aggregate(total=Sum('pe2678604'))
additionsk_2678604 = Ic7_2678604.objects.aggregate(total=Sum('sk2678604'))
additionmt_2678604 = Ic7_2678604.objects.aggregate(total=Sum('mt2678604'))
additionms_2678604 = Ic7_2678604.objects.aggregate(total=Sum('ms2678604'))
additionpa_2678604 = Ic7_2678604.objects.aggregate(total=Sum('pa2678604'))
additioncs_2678604 = Ic7_2678604.objects.aggregate(total=Sum('cs2678604'))
additionps_2678604 = Ic7_2678604.objects.aggregate(total=Sum('ps2678604'))
total_2678604 = Ic7_2678604.objects.aggregate(total=Sum('pr2678604')+Sum('pe2678604')+Sum('sk2678604')
                                             +Sum('mt2678604')+Sum('ms2678604')+Sum('pa2678604')+
                                             Sum('cs2678604')+Sum('ps2678604'))
    
#calculation for BCT_2678605
additionpr_2678605 = Ic7_2678605.objects.aggregate(total=Sum('pr2678605'))
additionpe_2678605 = Ic7_2678605.objects.aggregate(total=Sum('pe2678605'))
additionsk_2678605 = Ic7_2678605.objects.aggregate(total=Sum('sk2678605'))
additionmt_2678605 = Ic7_2678605.objects.aggregate(total=Sum('mt2678605'))
additionms_2678605 = Ic7_2678605.objects.aggregate(total=Sum('ms2678605'))
additionpa_2678605 = Ic7_2678605.objects.aggregate(total=Sum('pa2678605'))
additioncs_2678605 = Ic7_2678605.objects.aggregate(total=Sum('cs2678605'))
additionps_2678605 = Ic7_2678605.objects.aggregate(total=Sum('ps2678605'))
total_2678605 = Ic7_2678605.objects.aggregate(total=Sum('pr2678605')+Sum('pe2678605')+Sum('sk2678605')
                                             +Sum('mt2678605')+Sum('ms2678605')+Sum('pa2678605')+
                                             Sum('cs2678605')+Sum('ps2678605'))
    
#row parameters PR total calculation
totalpr_ic7 = additionpr_2678601['total'] + additionpr_2678602['total'] + additionpr_2678603['total'] + additionpr_2678604['total'] + additionpr_2678605['total']
#row parameters PE total calculation
totalpe_ic7 = additionpe_2678601['total'] + additionpe_2678602['total'] + additionpe_2678603['total'] + additionpe_2678604['total'] + additionpe_2678605['total']
#row parameters PR total calculation
totalsk_ic7 = additionsk_2678601['total'] + additionsk_2678602['total'] + additionsk_2678603['total'] + additionsk_2678604['total'] + additionsk_2678605['total']
#row parameters PE total calculation
totalmt_ic7 = additionmt_2678601['total'] + additionmt_2678602['total'] + additionmt_2678603['total'] + additionmt_2678604['total'] + additionmt_2678605['total']
#row parameters PR total calculation
totalms_ic7 = additionms_2678601['total'] + additionms_2678602['total'] + additionms_2678603['total'] + additionms_2678604['total'] + additionms_2678605['total']
#row parameters PE total calculation
totalpa_ic7 = additionpa_2678601['total'] + additionpa_2678602['total'] + additionpa_2678603['total'] + additionpa_2678604['total'] + additionpa_2678605['total']
#row parameters PR total calculation
totalcs_ic7 = additioncs_2678601['total'] + additioncs_2678602['total'] + additioncs_2678603['total'] + additioncs_2678604['total'] + additioncs_2678605['total']
#row parameters PE total calculation
totalps_ic7 = additionps_2678601['total'] + additionps_2678602['total'] + additionps_2678603['total'] + additionps_2678604['total'] + additionps_2678605['total']

#All Total Of IMCA 7 
all_total_ic7 = totalpr_ic7 + totalpe_ic7 + totalsk_ic7 + totalmt_ic7 + totalms_ic7 + totalpa_ic7 + totalcs_ic7 + totalps_ic7
    
#Attend Student
count_ic7 = Ic7_2678601.objects.count()
count_ic7-=1

"""-----------------------------------Global variable for Imca 7 Complete----------------------------------------"""

"""----------------------------------- Global variable for Imca 8 ----------------------------------------"""

#calculation for BDA_2688601
additionpr_2688601 = Ic8_2688601.objects.aggregate(total=Sum('pr2688601'))
additionpe_2688601 = Ic8_2688601.objects.aggregate(total=Sum('pe2688601'))
additionsk_2688601 = Ic8_2688601.objects.aggregate(total=Sum('sk2688601'))
additionmt_2688601 = Ic8_2688601.objects.aggregate(total=Sum('mt2688601'))
additionms_2688601 = Ic8_2688601.objects.aggregate(total=Sum('ms2688601'))
additionpa_2688601 = Ic8_2688601.objects.aggregate(total=Sum('pa2688601'))
additioncs_2688601 = Ic8_2688601.objects.aggregate(total=Sum('cs2688601'))
additionps_2688601 = Ic8_2688601.objects.aggregate(total=Sum('ps2688601'))
total_2688601 = Ic8_2688601.objects.aggregate(total=Sum('pr2688601')+Sum('pe2688601')+Sum('sk2688601')
                                              +Sum('mt2688601')+Sum('ms2688601')+Sum('pa2688601')+
                                              Sum('cs2688601')+Sum('ps2688601'))
    
#calculation for AML_2688602
additionpr_2688602 = Ic8_2688602.objects.aggregate(total=Sum('pr2688602'))
additionpe_2688602 = Ic8_2688602.objects.aggregate(total=Sum('pe2688602'))
additionsk_2688602 = Ic8_2688602.objects.aggregate(total=Sum('sk2688602'))
additionmt_2688602 = Ic8_2688602.objects.aggregate(total=Sum('mt2688602'))
additionms_2688602 = Ic8_2688602.objects.aggregate(total=Sum('ms2688602'))
additionpa_2688602 = Ic8_2688602.objects.aggregate(total=Sum('pa2688602'))
additioncs_2688602 = Ic8_2688602.objects.aggregate(total=Sum('cs2688602'))
additionps_2688602 = Ic8_2688602.objects.aggregate(total=Sum('ps2688602'))
total_2688602 = Ic8_2688602.objects.aggregate(total=Sum('pr2688602')+Sum('pe2688602')+Sum('sk2688602')
                                             +Sum('mt2688602')+Sum('ms2688602')+Sum('pa2688602')+
                                             Sum('cs2688602')+Sum('ps2688602'))
    
#calculation for DAA_2688603
additionpr_2688603 = Ic8_2688603.objects.aggregate(total=Sum('pr2688603'))
additionpe_2688603 = Ic8_2688603.objects.aggregate(total=Sum('pe2688603'))
additionsk_2688603 = Ic8_2688603.objects.aggregate(total=Sum('sk2688603'))
additionmt_2688603 = Ic8_2688603.objects.aggregate(total=Sum('mt2688603'))
additionms_2688603 = Ic8_2688603.objects.aggregate(total=Sum('ms2688603'))
additionpa_2688603 = Ic8_2688603.objects.aggregate(total=Sum('pa2688603'))
additioncs_2688603 = Ic8_2688603.objects.aggregate(total=Sum('cs2688603'))
additionps_2688603 = Ic8_2688603.objects.aggregate(total=Sum('ps2688603'))
total_2688603 = Ic8_2688603.objects.aggregate(total=Sum('pr2688603')+Sum('pe2688603')+Sum('sk2688603')
                                             +Sum('mt2688603')+Sum('ms2688603')+Sum('pa2688603')+
                                             Sum('cs2688603')+Sum('ps2688603'))
    
#calculation for TW_2688604
additionpr_2688604 = Ic8_2688604.objects.aggregate(total=Sum('pr2688604'))
additionpe_2688604 = Ic8_2688604.objects.aggregate(total=Sum('pe2688604'))
additionsk_2688604 = Ic8_2688604.objects.aggregate(total=Sum('sk2688604'))
additionmt_2688604 = Ic8_2688604.objects.aggregate(total=Sum('mt2688604'))
additionms_2688604 = Ic8_2688604.objects.aggregate(total=Sum('ms2688604'))
additionpa_2688604 = Ic8_2688604.objects.aggregate(total=Sum('pa2688604'))
additioncs_2688604 = Ic8_2688604.objects.aggregate(total=Sum('cs2688604'))
additionps_2688604 = Ic8_2688604.objects.aggregate(total=Sum('ps2688604'))
total_2688604 = Ic8_2688604.objects.aggregate(total=Sum('pr2688604')+Sum('pe2688604')+Sum('sk2688604')
                                             +Sum('mt2688604')+Sum('ms2688604')+Sum('pa2688604')+
                                             Sum('cs2688604')+Sum('ps2688604'))
    
#calculation for SP_2688605
additionpr_2688605 = Ic8_2688605.objects.aggregate(total=Sum('pr2688605'))
additionpe_2688605 = Ic8_2688605.objects.aggregate(total=Sum('pe2688605'))
additionsk_2688605 = Ic8_2688605.objects.aggregate(total=Sum('sk2688605'))
additionmt_2688605 = Ic8_2688605.objects.aggregate(total=Sum('mt2688605'))
additionms_2688605 = Ic8_2688605.objects.aggregate(total=Sum('ms2688605'))
additionpa_2688605 = Ic8_2688605.objects.aggregate(total=Sum('pa2688605'))
additioncs_2688605 = Ic8_2688605.objects.aggregate(total=Sum('cs2688605'))
additionps_2688605 = Ic8_2688605.objects.aggregate(total=Sum('ps2688605'))
total_2688605 = Ic8_2688605.objects.aggregate(total=Sum('pr2688605')+Sum('pe2688605')+Sum('sk2688605')
                                             +Sum('mt2688605')+Sum('ms2688605')+Sum('pa2688605')+
                                             Sum('cs2688605')+Sum('ps2688605'))

#calculation for CF_2688607
additionpr_2688607 = Ic8_2688607.objects.aggregate(total=Sum('pr2688607'))
additionpe_2688607 = Ic8_2688607.objects.aggregate(total=Sum('pe2688607'))
additionsk_2688607 = Ic8_2688607.objects.aggregate(total=Sum('sk2688607'))
additionmt_2688607 = Ic8_2688607.objects.aggregate(total=Sum('mt2688607'))
additionms_2688607 = Ic8_2688607.objects.aggregate(total=Sum('ms2688607'))
additionpa_2688607 = Ic8_2688607.objects.aggregate(total=Sum('pa2688607'))
additioncs_2688607 = Ic8_2688607.objects.aggregate(total=Sum('cs2688607'))
additionps_2688607 = Ic8_2688607.objects.aggregate(total=Sum('ps2688607'))
total_2688607 = Ic8_2688607.objects.aggregate(total=Sum('pr2688607')+Sum('pe2688607')+Sum('sk2688607')
                                              +Sum('mt2688607')+Sum('ms2688607')+Sum('pa2688607')+
                                              Sum('cs2688607')+Sum('ps2688607'))
    
#row parameters PR total calculation
totalpr_ic8 = additionpr_2688601['total'] + additionpr_2688602['total'] + additionpr_2688603['total'] + additionpr_2688604['total'] + additionpr_2688605['total'] + additionpr_2688607['total']
#row parameters PE total calculation
totalpe_ic8 = additionpe_2688601['total'] + additionpe_2688602['total'] + additionpe_2688603['total'] + additionpe_2688604['total'] + additionpe_2688605['total'] + additionpe_2688607['total']
#row parameters PR total calculation
totalsk_ic8 = additionsk_2688601['total'] + additionsk_2688602['total'] + additionsk_2688603['total'] + additionsk_2688604['total'] + additionsk_2688605['total'] + additionsk_2688607['total']
#row parameters PE total calculation
totalmt_ic8 = additionmt_2688601['total'] + additionmt_2688602['total'] + additionmt_2688603['total'] + additionmt_2688604['total'] + additionmt_2688605['total'] + additionmt_2688607['total']
#row parameters PR total calculation
totalms_ic8 = additionms_2688601['total'] + additionms_2688602['total'] + additionms_2688603['total'] + additionms_2688604['total'] + additionms_2688605['total'] + additionms_2688607['total']
#row parameters PE total calculation
totalpa_ic8 = additionpa_2688601['total'] + additionpa_2688602['total'] + additionpa_2688603['total'] + additionpa_2688604['total'] + additionpa_2688605['total'] + additionpa_2688607['total']
#row parameters PR total calculation
totalcs_ic8 = additioncs_2688601['total'] + additioncs_2688602['total'] + additioncs_2688603['total'] + additioncs_2688604['total'] + additioncs_2688605['total'] + additioncs_2688607['total']
#row parameters PE total calculation
totalps_ic8 = additionps_2688601['total'] + additionps_2688602['total'] + additionps_2688603['total'] + additionps_2688604['total'] + additionps_2688605['total'] + additionps_2688607['total']

#All Total Of IMCA 8
all_total_ic8 = totalpr_ic8 + totalpe_ic8 + totalsk_ic8 + totalmt_ic8 + totalms_ic8 + totalpa_ic8 + totalcs_ic8 + totalps_ic8
    
#Attend Student
count_ic8 = Ic8_2688601.objects.count()
count_ic8-=1

"""-----------------------------------Global variable for Imca 8 Complete----------------------------------------"""

"""----------------------------------- Global variable for Imca 9 ----------------------------------------"""

#calculation for DP_2698601
additionpr_2698601 = Ic9_2698601.objects.aggregate(total=Sum('pr2698601'))
additionpe_2698601 = Ic9_2698601.objects.aggregate(total=Sum('pe2698601'))
additionsk_2698601 = Ic9_2698601.objects.aggregate(total=Sum('sk2698601'))
additionmt_2698601 = Ic9_2698601.objects.aggregate(total=Sum('mt2698601'))
additionms_2698601 = Ic9_2698601.objects.aggregate(total=Sum('ms2698601'))
additionpa_2698601 = Ic9_2698601.objects.aggregate(total=Sum('pa2698601'))
additioncs_2698601 = Ic9_2698601.objects.aggregate(total=Sum('cs2698601'))
additionps_2698601 = Ic9_2698601.objects.aggregate(total=Sum('ps2698601'))
total_2698601 = Ic9_2698601.objects.aggregate(total=Sum('pr2698601')+Sum('pe2698601')+Sum('sk2698601')
                                              +Sum('mt2698601')+Sum('ms2698601')+Sum('pa2698601')+
                                              Sum('cs2698601')+Sum('ps2698601'))
    
#calculation for FSD_2698602
additionpr_2698602 = Ic9_2698602.objects.aggregate(total=Sum('pr2698602'))
additionpe_2698602 = Ic9_2698602.objects.aggregate(total=Sum('pe2698602'))
additionsk_2698602 = Ic9_2698602.objects.aggregate(total=Sum('sk2698602'))
additionmt_2698602 = Ic9_2698602.objects.aggregate(total=Sum('mt2698602'))
additionms_2698602 = Ic9_2698602.objects.aggregate(total=Sum('ms2698602'))
additionpa_2698602 = Ic9_2698602.objects.aggregate(total=Sum('pa2698602'))
additioncs_2698602 = Ic9_2698602.objects.aggregate(total=Sum('cs2698602'))
additionps_2698602 = Ic9_2698602.objects.aggregate(total=Sum('ps2698602'))
total_2698602 = Ic9_2698602.objects.aggregate(total=Sum('pr2698602')+Sum('pe2698602')+Sum('sk2698602')
                                             +Sum('mt2698602')+Sum('ms2698602')+Sum('pa2698602')+
                                             Sum('cs2698602')+Sum('ps2698602'))
    
#calculation for EIC_2698603
additionpr_2698603 = Ic9_2698603.objects.aggregate(total=Sum('pr2698603'))
additionpe_2698603 = Ic9_2698603.objects.aggregate(total=Sum('pe2698603'))
additionsk_2698603 = Ic9_2698603.objects.aggregate(total=Sum('sk2698603'))
additionmt_2698603 = Ic9_2698603.objects.aggregate(total=Sum('mt2698603'))
additionms_2698603 = Ic9_2698603.objects.aggregate(total=Sum('ms2698603'))
additionpa_2698603 = Ic9_2698603.objects.aggregate(total=Sum('pa2698603'))
additioncs_2698603 = Ic9_2698603.objects.aggregate(total=Sum('cs2698603'))
additionps_2698603 = Ic9_2698603.objects.aggregate(total=Sum('ps2698603'))
total_2698603 = Ic9_2698603.objects.aggregate(total=Sum('pr2698603')+Sum('pe2698603')+Sum('sk2698603')
                                             +Sum('mt2698603')+Sum('ms2698603')+Sum('pa2698603')+
                                             Sum('cs2698603')+Sum('ps2698603'))
    
#calculation for PM_2698604
additionpr_2698604 = Ic9_2698604.objects.aggregate(total=Sum('pr2698604'))
additionpe_2698604 = Ic9_2698604.objects.aggregate(total=Sum('pe2698604'))
additionsk_2698604 = Ic9_2698604.objects.aggregate(total=Sum('sk2698604'))
additionmt_2698604 = Ic9_2698604.objects.aggregate(total=Sum('mt2698604'))
additionms_2698604 = Ic9_2698604.objects.aggregate(total=Sum('ms2698604'))
additionpa_2698604 = Ic9_2698604.objects.aggregate(total=Sum('pa2698604'))
additioncs_2698604 = Ic9_2698604.objects.aggregate(total=Sum('cs2698604'))
additionps_2698604 = Ic9_2698604.objects.aggregate(total=Sum('ps2698604'))
total_2698604 = Ic9_2698604.objects.aggregate(total=Sum('pr2698604')+Sum('pe2698604')+Sum('sk2698604')
                                             +Sum('mt2698604')+Sum('ms2698604')+Sum('pa2698604')+
                                             Sum('cs2698604')+Sum('ps2698604'))
    
#calculation for SP_2698605
additionpr_2698605 = Ic9_2698605.objects.aggregate(total=Sum('pr2698605'))
additionpe_2698605 = Ic9_2698605.objects.aggregate(total=Sum('pe2698605'))
additionsk_2698605 = Ic9_2698605.objects.aggregate(total=Sum('sk2698605'))
additionmt_2698605 = Ic9_2698605.objects.aggregate(total=Sum('mt2698605'))
additionms_2698605 = Ic9_2698605.objects.aggregate(total=Sum('ms2698605'))
additionpa_2698605 = Ic9_2698605.objects.aggregate(total=Sum('pa2698605'))
additioncs_2698605 = Ic9_2698605.objects.aggregate(total=Sum('cs2698605'))
additionps_2698605 = Ic9_2698605.objects.aggregate(total=Sum('ps2698605'))
total_2698605 = Ic9_2698605.objects.aggregate(total=Sum('pr2698605')+Sum('pe2698605')+Sum('sk2698605')
                                             +Sum('mt2698605')+Sum('ms2698605')+Sum('pa2698605')+
                                             Sum('cs2698605')+Sum('ps2698605'))

#calculation for IOT_2698607
additionpr_2698607 = Ic9_2698607.objects.aggregate(total=Sum('pr2698607'))
additionpe_2698607 = Ic9_2698607.objects.aggregate(total=Sum('pe2698607'))
additionsk_2698607 = Ic9_2698607.objects.aggregate(total=Sum('sk2698607'))
additionmt_2698607 = Ic9_2698607.objects.aggregate(total=Sum('mt2698607'))
additionms_2698607 = Ic9_2698607.objects.aggregate(total=Sum('ms2698607'))
additionpa_2698607 = Ic9_2698607.objects.aggregate(total=Sum('pa2698607'))
additioncs_2698607 = Ic9_2698607.objects.aggregate(total=Sum('cs2698607'))
additionps_2698607 = Ic9_2698607.objects.aggregate(total=Sum('ps2698607'))
total_2698607 = Ic9_2698607.objects.aggregate(total=Sum('pr2698607')+Sum('pe2698607')+Sum('sk2698607')
                                              +Sum('mt2698607')+Sum('ms2698607')+Sum('pa2698607')+
                                              Sum('cs2698607')+Sum('ps2698607'))
    
#row parameters PR total calculation
totalpr_ic9 = additionpr_2698601['total'] + additionpr_2698602['total'] + additionpr_2698603['total'] + additionpr_2698604['total'] + additionpr_2698605['total'] + additionpr_2698607['total']
#row parameters PE total calculation
totalpe_ic9 = additionpe_2698601['total'] + additionpe_2698602['total'] + additionpe_2698603['total'] + additionpe_2698604['total'] + additionpe_2698605['total'] + additionpe_2698607['total']
#row parameters PR total calculation
totalsk_ic9 = additionsk_2698601['total'] + additionsk_2698602['total'] + additionsk_2698603['total'] + additionsk_2698604['total'] + additionsk_2698605['total'] + additionsk_2698607['total']
#row parameters PE total calculation
totalmt_ic9 = additionmt_2698601['total'] + additionmt_2698602['total'] + additionmt_2698603['total'] + additionmt_2698604['total'] + additionmt_2698605['total'] + additionmt_2698607['total']
#row parameters PR total calculation
totalms_ic9 = additionms_2698601['total'] + additionms_2698602['total'] + additionms_2698603['total'] + additionms_2698604['total'] + additionms_2698605['total'] + additionms_2698607['total']
#row parameters PE total calculation
totalpa_ic9 = additionpa_2698601['total'] + additionpa_2698602['total'] + additionpa_2698603['total'] + additionpa_2698604['total'] + additionpa_2698605['total'] + additionpa_2698607['total']
#row parameters PR total calculation
totalcs_ic9 = additioncs_2698601['total'] + additioncs_2698602['total'] + additioncs_2698603['total'] + additioncs_2698604['total'] + additioncs_2698605['total'] + additioncs_2698607['total']
#row parameters PE total calculation
totalps_ic9 = additionps_2698601['total'] + additionps_2698602['total'] + additionps_2698603['total'] + additionps_2698604['total'] + additionps_2698605['total'] + additionps_2698607['total']

#All Total Of IMCA 8
all_total_ic9 = totalpr_ic9 + totalpe_ic9 + totalsk_ic9 + totalmt_ic9 + totalms_ic9 + totalpa_ic9 + totalcs_ic9 + totalps_ic9
    
#Attend Student
count_ic9 = Ic9_2698601.objects.count()
count_ic9-=1

"""-----------------------------------Global variable for Imca 9 Complete----------------------------------------"""

"""----------------------------------- Global variable for Mca 1 ----------------------------------------"""

#calculation for C-LANG_619401
additionpr_619401 = Mca1_619401.objects.aggregate(total=Sum('pr619401'))
additionpe_619401 = Mca1_619401.objects.aggregate(total=Sum('pe619401'))
additionsk_619401 = Mca1_619401.objects.aggregate(total=Sum('sk619401'))
additionmt_619401 = Mca1_619401.objects.aggregate(total=Sum('mt619401'))
additionms_619401 = Mca1_619401.objects.aggregate(total=Sum('ms619401'))
additionpa_619401 = Mca1_619401.objects.aggregate(total=Sum('pa619401'))
additioncs_619401 = Mca1_619401.objects.aggregate(total=Sum('cs619401'))
additionps_619401 = Mca1_619401.objects.aggregate(total=Sum('ps619401'))
total_619401 = Mca1_619401.objects.aggregate(total=Sum('pr619401')+Sum('pe619401')+Sum('sk619401')
                                              +Sum('mt619401')+Sum('ms619401')+Sum('pa619401')+
                                              Sum('cs619401')+Sum('ps619401'))
    
#calculation for JAVA_619402
additionpr_619402 = Mca1_619402.objects.aggregate(total=Sum('pr619402'))
additionpe_619402 = Mca1_619402.objects.aggregate(total=Sum('pe619402'))
additionsk_619402 = Mca1_619402.objects.aggregate(total=Sum('sk619402'))
additionmt_619402 = Mca1_619402.objects.aggregate(total=Sum('mt619402'))
additionms_619402 = Mca1_619402.objects.aggregate(total=Sum('ms619402'))
additionpa_619402 = Mca1_619402.objects.aggregate(total=Sum('pa619402'))
additioncs_619402 = Mca1_619402.objects.aggregate(total=Sum('cs619402'))
additionps_619402 = Mca1_619402.objects.aggregate(total=Sum('ps619402'))
total_619402 = Mca1_619402.objects.aggregate(total=Sum('pr619402')+Sum('pe619402')+Sum('sk619402')
                                             +Sum('mt619402')+Sum('ms619402')+Sum('pa619402')+
                                             Sum('cs619402')+Sum('ps619402'))
    
#calculation for BM_619403
additionpr_619403 = Mca1_619403.objects.aggregate(total=Sum('pr619403'))
additionpe_619403 = Mca1_619403.objects.aggregate(total=Sum('pe619403'))
additionsk_619403 = Mca1_619403.objects.aggregate(total=Sum('sk619403'))
additionmt_619403 = Mca1_619403.objects.aggregate(total=Sum('mt619403'))
additionms_619403 = Mca1_619403.objects.aggregate(total=Sum('ms619403'))
additionpa_619403 = Mca1_619403.objects.aggregate(total=Sum('pa619403'))
additioncs_619403 = Mca1_619403.objects.aggregate(total=Sum('cs619403'))
additionps_619403 = Mca1_619403.objects.aggregate(total=Sum('ps619403'))
total_619403 = Mca1_619403.objects.aggregate(total=Sum('pr619403')+Sum('pe619403')+Sum('sk619403')
                                             +Sum('mt619403')+Sum('ms619403')+Sum('pa619403')+
                                             Sum('cs619403')+Sum('ps619403'))
    
#calculation for RDBMS_619404
additionpr_619404 = Mca1_619404.objects.aggregate(total=Sum('pr619404'))
additionpe_619404 = Mca1_619404.objects.aggregate(total=Sum('pe619404'))
additionsk_619404 = Mca1_619404.objects.aggregate(total=Sum('sk619404'))
additionmt_619404 = Mca1_619404.objects.aggregate(total=Sum('mt619404'))
additionms_619404 = Mca1_619404.objects.aggregate(total=Sum('ms619404'))
additionpa_619404 = Mca1_619404.objects.aggregate(total=Sum('pa619404'))
additioncs_619404 = Mca1_619404.objects.aggregate(total=Sum('cs619404'))
additionps_619404 = Mca1_619404.objects.aggregate(total=Sum('ps619404'))
total_619404 = Mca1_619404.objects.aggregate(total=Sum('pr619404')+Sum('pe619404')+Sum('sk619404')
                                             +Sum('mt619404')+Sum('ms619404')+Sum('pa619404')+
                                             Sum('cs619404')+Sum('ps619404'))
    
#calculation for WDT-PHP_619405
additionpr_619405 = Mca1_619405.objects.aggregate(total=Sum('pr619405'))
additionpe_619405 = Mca1_619405.objects.aggregate(total=Sum('pe619405'))
additionsk_619405 = Mca1_619405.objects.aggregate(total=Sum('sk619405'))
additionmt_619405 = Mca1_619405.objects.aggregate(total=Sum('mt619405'))
additionms_619405 = Mca1_619405.objects.aggregate(total=Sum('ms619405'))
additionpa_619405 = Mca1_619405.objects.aggregate(total=Sum('pa619405'))
additioncs_619405 = Mca1_619405.objects.aggregate(total=Sum('cs619405'))
additionps_619405 = Mca1_619405.objects.aggregate(total=Sum('ps619405'))
total_619405 = Mca1_619405.objects.aggregate(total=Sum('pr619405')+Sum('pe619405')+Sum('sk619405')
                                             +Sum('mt619405')+Sum('ms619405')+Sum('pa619405')+
                                             Sum('cs619405')+Sum('ps619405'))

#calculation for BCC_619406
additionpr_619406 = Mca1_619406.objects.aggregate(total=Sum('pr619406'))
additionpe_619406 = Mca1_619406.objects.aggregate(total=Sum('pe619406'))
additionsk_619406 = Mca1_619406.objects.aggregate(total=Sum('sk619406'))
additionmt_619406 = Mca1_619406.objects.aggregate(total=Sum('mt619406'))
additionms_619406 = Mca1_619406.objects.aggregate(total=Sum('ms619406'))
additionpa_619406 = Mca1_619406.objects.aggregate(total=Sum('pa619406'))
additioncs_619406 = Mca1_619406.objects.aggregate(total=Sum('cs619406'))
additionps_619406 = Mca1_619406.objects.aggregate(total=Sum('ps619406'))
total_619406 = Mca1_619406.objects.aggregate(total=Sum('pr619406')+Sum('pe619406')+Sum('sk619406')
                                              +Sum('mt619406')+Sum('ms619406')+Sum('pa619406')+
                                              Sum('cs619406')+Sum('ps619406'))
    
#row parameters PR total calculation
totalpr_mca1 = additionpr_619401['total'] + additionpr_619402['total'] + additionpr_619403['total'] + additionpr_619404['total'] + additionpr_619405['total'] + additionpr_619406['total']
#row parameters PE total calculation
totalpe_mca1 = additionpe_619401['total'] + additionpe_619402['total'] + additionpe_619403['total'] + additionpe_619404['total'] + additionpe_619405['total'] + additionpe_619406['total']
#row parameters PR total calculation
totalsk_mca1 = additionsk_619401['total'] + additionsk_619402['total'] + additionsk_619403['total'] + additionsk_619404['total'] + additionsk_619405['total'] + additionsk_619406['total']
#row parameters PE total calculation
totalmt_mca1 = additionmt_619401['total'] + additionmt_619402['total'] + additionmt_619403['total'] + additionmt_619404['total'] + additionmt_619405['total'] + additionmt_619406['total']
#row parameters PR total calculation
totalms_mca1 = additionms_619401['total'] + additionms_619402['total'] + additionms_619403['total'] + additionms_619404['total'] + additionms_619405['total'] + additionms_619406['total']
#row parameters PE total calculation
totalpa_mca1 = additionpa_619401['total'] + additionpa_619402['total'] + additionpa_619403['total'] + additionpa_619404['total'] + additionpa_619405['total'] + additionpa_619406['total']
#row parameters PR total calculation
totalcs_mca1 = additioncs_619401['total'] + additioncs_619402['total'] + additioncs_619403['total'] + additioncs_619404['total'] + additioncs_619405['total'] + additioncs_619406['total']
#row parameters PE total calculation
totalps_mca1 = additionps_619401['total'] + additionps_619402['total'] + additionps_619403['total'] + additionps_619404['total'] + additionps_619405['total'] + additionps_619406['total']

#All Total Of IMCA 8
all_total_mca1 = totalpr_mca1 + totalpe_mca1 + totalsk_mca1 + totalmt_mca1 + totalms_mca1 + totalpa_mca1 + totalcs_mca1 + totalps_mca1
    
#Attend Student
count_mca1 = Mca1_619401.objects.count()
count_mca1-=1

"""-----------------------------------Global variable for Mca 1 Complete----------------------------------------"""

"""----------------------------------- Global variable for Mca 2 ----------------------------------------"""

#calculation for DS_629401
additionpr_629401 = Mca2_629401.objects.aggregate(total=Sum('pr629401'))
additionpe_629401 = Mca2_629401.objects.aggregate(total=Sum('pe629401'))
additionsk_629401 = Mca2_629401.objects.aggregate(total=Sum('sk629401'))
additionmt_629401 = Mca2_629401.objects.aggregate(total=Sum('mt629401'))
additionms_629401 = Mca2_629401.objects.aggregate(total=Sum('ms629401'))
additionpa_629401 = Mca2_629401.objects.aggregate(total=Sum('pa629401'))
additioncs_629401 = Mca2_629401.objects.aggregate(total=Sum('cs629401'))
additionps_629401 = Mca2_629401.objects.aggregate(total=Sum('ps629401'))
total_629401 = Mca2_629401.objects.aggregate(total=Sum('pr629401')+Sum('pe629401')+Sum('sk629401')
                                              +Sum('mt629401')+Sum('ms629401')+Sum('pa629401')+
                                              Sum('cs629401')+Sum('ps629401'))
    
#calculation for MP_629402
additionpr_629402 = Mca2_629402.objects.aggregate(total=Sum('pr629402'))
additionpe_629402 = Mca2_629402.objects.aggregate(total=Sum('pe629402'))
additionsk_629402 = Mca2_629402.objects.aggregate(total=Sum('sk629402'))
additionmt_629402 = Mca2_629402.objects.aggregate(total=Sum('mt629402'))
additionms_629402 = Mca2_629402.objects.aggregate(total=Sum('ms629402'))
additionpa_629402 = Mca2_629402.objects.aggregate(total=Sum('pa629402'))
additioncs_629402 = Mca2_629402.objects.aggregate(total=Sum('cs629402'))
additionps_629402 = Mca2_629402.objects.aggregate(total=Sum('ps629402'))
total_629402 = Mca2_629402.objects.aggregate(total=Sum('pr629402')+Sum('pe629402')+Sum('sk629402')
                                             +Sum('mt629402')+Sum('ms629402')+Sum('pa629402')+
                                             Sum('cs629402')+Sum('ps629402'))
    
#calculation for PY_629403
additionpr_629403 = Mca2_629403.objects.aggregate(total=Sum('pr629403'))
additionpe_629403 = Mca2_629403.objects.aggregate(total=Sum('pe629403'))
additionsk_629403 = Mca2_629403.objects.aggregate(total=Sum('sk629403'))
additionmt_629403 = Mca2_629403.objects.aggregate(total=Sum('mt629403'))
additionms_629403 = Mca2_629403.objects.aggregate(total=Sum('ms629403'))
additionpa_629403 = Mca2_629403.objects.aggregate(total=Sum('pa629403'))
additioncs_629403 = Mca2_629403.objects.aggregate(total=Sum('cs629403'))
additionps_629403 = Mca2_629403.objects.aggregate(total=Sum('ps629403'))
total_629403 = Mca2_629403.objects.aggregate(total=Sum('pr629403')+Sum('pe629403')+Sum('sk629403')
                                             +Sum('mt629403')+Sum('ms629403')+Sum('pa629403')+
                                             Sum('cs629403')+Sum('ps629403'))
    
#calculation for CN_629404
additionpr_629404 = Mca2_629404.objects.aggregate(total=Sum('pr629404'))
additionpe_629404 = Mca2_629404.objects.aggregate(total=Sum('pe629404'))
additionsk_629404 = Mca2_629404.objects.aggregate(total=Sum('sk629404'))
additionmt_629404 = Mca2_629404.objects.aggregate(total=Sum('mt629404'))
additionms_629404 = Mca2_629404.objects.aggregate(total=Sum('ms629404'))
additionpa_629404 = Mca2_629404.objects.aggregate(total=Sum('pa629404'))
additioncs_629404 = Mca2_629404.objects.aggregate(total=Sum('cs629404'))
additionps_629404 = Mca2_629404.objects.aggregate(total=Sum('ps629404'))
total_629404 = Mca2_629404.objects.aggregate(total=Sum('pr629404')+Sum('pe629404')+Sum('sk629404')
                                             +Sum('mt629404')+Sum('ms629404')+Sum('pa629404')+
                                             Sum('cs629404')+Sum('ps629404'))
    
#calculation for SP_629405
additionpr_629405 = Mca2_629405.objects.aggregate(total=Sum('pr629405'))
additionpe_629405 = Mca2_629405.objects.aggregate(total=Sum('pe629405'))
additionsk_629405 = Mca2_629405.objects.aggregate(total=Sum('sk629405'))
additionmt_629405 = Mca2_629405.objects.aggregate(total=Sum('mt629405'))
additionms_629405 = Mca2_629405.objects.aggregate(total=Sum('ms629405'))
additionpa_629405 = Mca2_629405.objects.aggregate(total=Sum('pa629405'))
additioncs_629405 = Mca2_629405.objects.aggregate(total=Sum('cs629405'))
additionps_629405 = Mca2_629405.objects.aggregate(total=Sum('ps629405'))
total_629405 = Mca2_629405.objects.aggregate(total=Sum('pr629405')+Sum('pe629405')+Sum('sk629405')
                                             +Sum('mt629405')+Sum('ms629405')+Sum('pa629405')+
                                             Sum('cs629405')+Sum('ps629405'))

#calculation for JWT_629408
additionpr_629408 = Mca2_629408.objects.aggregate(total=Sum('pr629408'))
additionpe_629408 = Mca2_629408.objects.aggregate(total=Sum('pe629408'))
additionsk_629408 = Mca2_629408.objects.aggregate(total=Sum('sk629408'))
additionmt_629408 = Mca2_629408.objects.aggregate(total=Sum('mt629408'))
additionms_629408 = Mca2_629408.objects.aggregate(total=Sum('ms629408'))
additionpa_629408 = Mca2_629408.objects.aggregate(total=Sum('pa629408'))
additioncs_629408 = Mca2_629408.objects.aggregate(total=Sum('cs629408'))
additionps_629408 = Mca2_629408.objects.aggregate(total=Sum('ps629408'))
total_629408 = Mca2_629408.objects.aggregate(total=Sum('pr629408')+Sum('pe629408')+Sum('sk629408')
                                              +Sum('mt629408')+Sum('ms629408')+Sum('pa629408')+
                                              Sum('cs629408')+Sum('ps629408'))
    
#row parameters PR total calculation
totalpr_mca2 = additionpr_629401['total'] + additionpr_629402['total'] + additionpr_629403['total'] + additionpr_629404['total'] + additionpr_629405['total'] + additionpr_629408['total']
#row parameters PE total calculation
totalpe_mca2 = additionpe_629401['total'] + additionpe_629402['total'] + additionpe_629403['total'] + additionpe_629404['total'] + additionpe_629405['total'] + additionpe_629408['total']
#row parameters PR total calculation
totalsk_mca2 = additionsk_629401['total'] + additionsk_629402['total'] + additionsk_629403['total'] + additionsk_629404['total'] + additionsk_629405['total'] + additionsk_629408['total']
#row parameters PE total calculation
totalmt_mca2 = additionmt_629401['total'] + additionmt_629402['total'] + additionmt_629403['total'] + additionmt_629404['total'] + additionmt_629405['total'] + additionmt_629408['total']
#row parameters PR total calculation
totalms_mca2 = additionms_629401['total'] + additionms_629402['total'] + additionms_629403['total'] + additionms_629404['total'] + additionms_629405['total'] + additionms_629408['total']
#row parameters PE total calculation
totalpa_mca2 = additionpa_629401['total'] + additionpa_629402['total'] + additionpa_629403['total'] + additionpa_629404['total'] + additionpa_629405['total'] + additionpa_629408['total']
#row parameters PR total calculation
totalcs_mca2 = additioncs_629401['total'] + additioncs_629402['total'] + additioncs_629403['total'] + additioncs_629404['total'] + additioncs_629405['total'] + additioncs_629408['total']
#row parameters PE total calculation
totalps_mca2 = additionps_629401['total'] + additionps_629402['total'] + additionps_629403['total'] + additionps_629404['total'] + additionps_629405['total'] + additionps_629408['total']

#All Total Of IMCA 8
all_total_mca2 = totalpr_mca2 + totalpe_mca2 + totalsk_mca2 + totalmt_mca2 + totalms_mca2 + totalpa_mca2 + totalcs_mca2 + totalps_mca2
    
#Attend Student
count_mca2 = Mca2_629401.objects.count()
count_mca2-=1

"""-----------------------------------Global variable for Mca 2 Complete----------------------------------------"""

"""----------------------------------- Global variable for Mca 3 ----------------------------------------"""

#calculation for DAA_639401
additionpr_639401 = Mca3_639401.objects.aggregate(total=Sum('pr639401'))
additionpe_639401 = Mca3_639401.objects.aggregate(total=Sum('pe639401'))
additionsk_639401 = Mca3_639401.objects.aggregate(total=Sum('sk639401'))
additionmt_639401 = Mca3_639401.objects.aggregate(total=Sum('mt639401'))
additionms_639401 = Mca3_639401.objects.aggregate(total=Sum('ms639401'))
additionpa_639401 = Mca3_639401.objects.aggregate(total=Sum('pa639401'))
additioncs_639401 = Mca3_639401.objects.aggregate(total=Sum('cs639401'))
additionps_639401 = Mca3_639401.objects.aggregate(total=Sum('ps639401'))
total_639401 = Mca3_639401.objects.aggregate(total=Sum('pr639401')+Sum('pe639401')+Sum('sk639401')
                                              +Sum('mt639401')+Sum('ms639401')+Sum('pa639401')+
                                              Sum('cs639401')+Sum('ps639401'))
    
#calculation for ML_639402
additionpr_639402 = Mca3_639402.objects.aggregate(total=Sum('pr639402'))
additionpe_639402 = Mca3_639402.objects.aggregate(total=Sum('pe639402'))
additionsk_639402 = Mca3_639402.objects.aggregate(total=Sum('sk639402'))
additionmt_639402 = Mca3_639402.objects.aggregate(total=Sum('mt639402'))
additionms_639402 = Mca3_639402.objects.aggregate(total=Sum('ms639402'))
additionpa_639402 = Mca3_639402.objects.aggregate(total=Sum('pa639402'))
additioncs_639402 = Mca3_639402.objects.aggregate(total=Sum('cs639402'))
additionps_639402 = Mca3_639402.objects.aggregate(total=Sum('ps639402'))
total_639402 = Mca3_639402.objects.aggregate(total=Sum('pr639402')+Sum('pe639402')+Sum('sk639402')
                                             +Sum('mt639402')+Sum('ms639402')+Sum('pa639402')+
                                             Sum('cs639402')+Sum('ps639402'))
    
#calculation for SE_639403
additionpr_639403 = Mca3_639403.objects.aggregate(total=Sum('pr639403'))
additionpe_639403 = Mca3_639403.objects.aggregate(total=Sum('pe639403'))
additionsk_639403 = Mca3_639403.objects.aggregate(total=Sum('sk639403'))
additionmt_639403 = Mca3_639403.objects.aggregate(total=Sum('mt639403'))
additionms_639403 = Mca3_639403.objects.aggregate(total=Sum('ms639403'))
additionpa_639403 = Mca3_639403.objects.aggregate(total=Sum('pa639403'))
additioncs_639403 = Mca3_639403.objects.aggregate(total=Sum('cs639403'))
additionps_639403 = Mca3_639403.objects.aggregate(total=Sum('ps639403'))
total_639403 = Mca3_639403.objects.aggregate(total=Sum('pr639403')+Sum('pe639403')+Sum('sk639403')
                                             +Sum('mt639403')+Sum('ms639403')+Sum('pa639403')+
                                             Sum('cs639403')+Sum('ps639403'))
    
#calculation for SP_639404
additionpr_639404 = Mca3_639404.objects.aggregate(total=Sum('pr639404'))
additionpe_639404 = Mca3_639404.objects.aggregate(total=Sum('pe639404'))
additionsk_639404 = Mca3_639404.objects.aggregate(total=Sum('sk639404'))
additionmt_639404 = Mca3_639404.objects.aggregate(total=Sum('mt639404'))
additionms_639404 = Mca3_639404.objects.aggregate(total=Sum('ms639404'))
additionpa_639404 = Mca3_639404.objects.aggregate(total=Sum('pa639404'))
additioncs_639404 = Mca3_639404.objects.aggregate(total=Sum('cs639404'))
additionps_639404 = Mca3_639404.objects.aggregate(total=Sum('ps639404'))
total_639404 = Mca3_639404.objects.aggregate(total=Sum('pr639404')+Sum('pe639404')+Sum('sk639404')
                                             +Sum('mt639404')+Sum('ms639404')+Sum('pa639404')+
                                             Sum('cs639404')+Sum('ps639404'))
    
#calculation for CC_639407
additionpr_639407 = Mca3_639407.objects.aggregate(total=Sum('pr639407'))
additionpe_639407 = Mca3_639407.objects.aggregate(total=Sum('pe639407'))
additionsk_639407 = Mca3_639407.objects.aggregate(total=Sum('sk639407'))
additionmt_639407 = Mca3_639407.objects.aggregate(total=Sum('mt639407'))
additionms_639407 = Mca3_639407.objects.aggregate(total=Sum('ms639407'))
additionpa_639407 = Mca3_639407.objects.aggregate(total=Sum('pa639407'))
additioncs_639407 = Mca3_639407.objects.aggregate(total=Sum('cs639407'))
additionps_639407 = Mca3_639407.objects.aggregate(total=Sum('ps639407'))
total_639407 = Mca3_639407.objects.aggregate(total=Sum('pr639407')+Sum('pe639407')+Sum('sk639407')
                                             +Sum('mt639407')+Sum('ms639407')+Sum('pa639407')+
                                             Sum('cs639407')+Sum('ps639407'))

#calculation for NCS_639410
additionpr_639410 = Mca3_639410.objects.aggregate(total=Sum('pr639410'))
additionpe_639410 = Mca3_639410.objects.aggregate(total=Sum('pe639410'))
additionsk_639410 = Mca3_639410.objects.aggregate(total=Sum('sk639410'))
additionmt_639410 = Mca3_639410.objects.aggregate(total=Sum('mt639410'))
additionms_639410 = Mca3_639410.objects.aggregate(total=Sum('ms639410'))
additionpa_639410 = Mca3_639410.objects.aggregate(total=Sum('pa639410'))
additioncs_639410 = Mca3_639410.objects.aggregate(total=Sum('cs639410'))
additionps_639410 = Mca3_639410.objects.aggregate(total=Sum('ps639410'))
total_639410 = Mca3_639410.objects.aggregate(total=Sum('pr639410')+Sum('pe639410')+Sum('sk639410')
                                              +Sum('mt639410')+Sum('ms639410')+Sum('pa639410')+
                                              Sum('cs639410')+Sum('ps639410'))
    
#row parameters PR total calculation
totalpr_mca3 = additionpr_639401['total'] + additionpr_639402['total'] + additionpr_639403['total'] + additionpr_639404['total'] + additionpr_639407['total'] + additionpr_639410['total']
#row parameters PE total calculation
totalpe_mca3 = additionpe_639401['total'] + additionpe_639402['total'] + additionpe_639403['total'] + additionpe_639404['total'] + additionpe_639407['total'] + additionpe_639410['total']
#row parameters PR total calculation
totalsk_mca3 = additionsk_639401['total'] + additionsk_639402['total'] + additionsk_639403['total'] + additionsk_639404['total'] + additionsk_639407['total'] + additionsk_639410['total']
#row parameters PE total calculation
totalmt_mca3 = additionmt_639401['total'] + additionmt_639402['total'] + additionmt_639403['total'] + additionmt_639404['total'] + additionmt_639407['total'] + additionmt_639410['total']
#row parameters PR total calculation
totalms_mca3 = additionms_639401['total'] + additionms_639402['total'] + additionms_639403['total'] + additionms_639404['total'] + additionms_639407['total'] + additionms_639410['total']
#row parameters PE total calculation
totalpa_mca3 = additionpa_639401['total'] + additionpa_639402['total'] + additionpa_639403['total'] + additionpa_639404['total'] + additionpa_639407['total'] + additionpa_639410['total']
#row parameters PR total calculation
totalcs_mca3 = additioncs_639401['total'] + additioncs_639402['total'] + additioncs_639403['total'] + additioncs_639404['total'] + additioncs_639407['total'] + additioncs_639410['total']
#row parameters PE total calculation
totalps_mca3 = additionps_639401['total'] + additionps_639402['total'] + additionps_639403['total'] + additionps_639404['total'] + additionps_639407['total'] + additionps_639410['total']

#All Total Of IMCA 8
all_total_mca3 = totalpr_mca3 + totalpe_mca3 + totalsk_mca3 + totalmt_mca3 + totalms_mca3 + totalpa_mca3 + totalcs_mca3 + totalps_mca3
    
#Attend Student
count_mca3 = Mca3_639401.objects.count()
count_mca3-=1

"""-----------------------------------Global variable for Mca 3 Complete----------------------------------------"""

"""-----------------------------------Global variable for Imca 10 ----------------------------------------"""

#calculation for SP_4401601
additionpr_4401601 = Ic10_4401601.objects.aggregate(total=Sum('pr4401601'))
additionpe_4401601 = Ic10_4401601.objects.aggregate(total=Sum('pe4401601'))
additionsk_4401601 = Ic10_4401601.objects.aggregate(total=Sum('sk4401601'))
additionmt_4401601 = Ic10_4401601.objects.aggregate(total=Sum('mt4401601'))
additionms_4401601 = Ic10_4401601.objects.aggregate(total=Sum('ms4401601'))
additionpa_4401601 = Ic10_4401601.objects.aggregate(total=Sum('pa4401601'))
additioncs_4401601 = Ic10_4401601.objects.aggregate(total=Sum('cs4401601'))
additionps_4401601 = Ic10_4401601.objects.aggregate(total=Sum('ps4401601'))
total_4401601 = Ic10_4401601.objects.aggregate(total=Sum('pr4401601')+Sum('pe4401601')+Sum('sk4401601')
                                              +Sum('mt4401601')+Sum('ms4401601')+Sum('pa4401601')+
                                              Sum('cs4401601')+Sum('ps4401601'))
    
#row parameters PR total calculation
totalpr_ic10 = additionpr_4401601['total'] 
#row parameters PE total calculation
totalpe_ic10 = additionpe_4401601['total'] 
#row parameters PR total calculation
totalsk_ic10 = additionsk_4401601['total'] 
#row parameters PE total calculation
totalmt_ic10 = additionmt_4401601['total'] 
#row parameters PR total calculation
totalms_ic10 = additionms_4401601['total'] 
#row parameters PE total calculation
totalpa_ic10 = additionpa_4401601['total'] 
#row parameters PR total calculation
totalcs_ic10 = additioncs_4401601['total'] 
#row parameters PE total calculation
totalps_ic10 = additionps_4401601['total'] 
#All Total Of IMCA 2
all_total_ic10 = totalpr_ic10 + totalpe_ic10 + totalsk_ic10 + totalmt_ic10 + totalms_ic10 + totalpa_ic10 + totalcs_ic10 + totalps_ic10
    
#Attend Student
count_ic10 = Ic10_4401601.objects.count()
count_ic10-=1

"""-----------------------------------Global variable for Imca 10 Complete----------------------------------------"""

"""-----------------------------------Global variable for mca 4 ----------------------------------------"""

#calculation for SP_649401
additionpr_649401 = Mca4_649401.objects.aggregate(total=Sum('pr649401'))
additionpe_649401 = Mca4_649401.objects.aggregate(total=Sum('pe649401'))
additionsk_649401 = Mca4_649401.objects.aggregate(total=Sum('sk649401'))
additionmt_649401 = Mca4_649401.objects.aggregate(total=Sum('mt649401'))
additionms_649401 = Mca4_649401.objects.aggregate(total=Sum('ms649401'))
additionpa_649401 = Mca4_649401.objects.aggregate(total=Sum('pa649401'))
additioncs_649401 = Mca4_649401.objects.aggregate(total=Sum('cs649401'))
additionps_649401 = Mca4_649401.objects.aggregate(total=Sum('ps649401'))
total_649401 = Mca4_649401.objects.aggregate(total=Sum('pr649401')+Sum('pe649401')+Sum('sk649401')
                                              +Sum('mt649401')+Sum('ms649401')+Sum('pa649401')+
                                              Sum('cs649401')+Sum('ps649401'))
    
#row parameters PR total calculation
totalpr_mca4 = additionpr_649401['total'] 
#row parameters PE total calculation
totalpe_mca4 = additionpe_649401['total'] 
#row parameters PR total calculation
totalsk_mca4 = additionsk_649401['total'] 
#row parameters PE total calculation
totalmt_mca4 = additionmt_649401['total'] 
#row parameters PR total calculation
totalms_mca4 = additionms_649401['total'] 
#row parameters PE total calculation
totalpa_mca4 = additionpa_649401['total'] 
#row parameters PR total calculation
totalcs_mca4 = additioncs_649401['total'] 
#row parameters PE total calculation
totalps_mca4 = additionps_649401['total'] 
#All Total Of MCA 4
all_total_mca4 = totalpr_mca4 + totalpe_mca4 + totalsk_mca4 + totalmt_mca4 + totalms_mca4 + totalpa_mca4 + totalcs_mca4 + totalps_mca4
    
#Attend Student
count_mca4 = Mca4_649401.objects.count()
count_mca4-=1

"""-----------------------------------Global variable for mca 4 Complete----------------------------------------"""


###############################################################################################################################

def index(request):
    #return HttpResponse("hello world")
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    return render(request, 'index.html', {'sem':sem})

##Sem Serve function for update
def sem_serve(request):
    sem = request.POST['semserve']
    sem_sub = Sem_serve.objects.get(id=1)
    sem_sub.semserve = sem
    sem_sub.save()
    sem1 = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    counts = Student.objects.count()
    show = Myadmin.objects.get(id=1)
    students = Student.objects.all()
    return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})

#for myadmin login function data fetch
def myadmin(request):
    myuser = request.POST['username']
    mypass = request.POST['password']
    user = Myadmin.objects.filter(id=1).values()[0]['username']
    passw = Myadmin.objects.filter(id=1).values()[0]['password']
    show = Myadmin.objects.get(id=1)
    counts = Student.objects.count()
    students = Student.objects.all()
    if myuser == user and mypass == passw:
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    else:     
        return redirect("http://127.0.0.1:8000/")

#for Developer page
def developer(request):
    return render(request, 'developer.html')

#Admin logout
def admin_logout(request):
    if request.method == "POST":
        sem_sub = Sem_serve.objects.get(id=1)
        sem_sub.semserve = 'Offline'
        sem_sub.save()
        
        return render(request, 'logout.html')

def clicklogout(request):
    if request.method == "POST":
        os.system("taskkill /im chrome.exe /f")
        os.system("taskkill /im firefox.exe /f")
        os.system("taskkill /im msedge.exe /f")
        return render(request, 'logout.html')

def change_password(request):
    if request.method == "POST":
        change = Myadmin.objects.get(id=1)
        change.username = request.POST['username']
        change.password = request.POST['password']
        change.save()
        return HttpResponse(myadmin(request))
    
"""-------------------------------------- for student how many student in database ----------------------------"""

def insert_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})

def delete_student(request):
    if request.method == "POST":
        Student.objects.all().delete()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
    
"""------------------------------------- Fetch Faculty for update ----------------------------------------------"""
def update_faculty(request):
    if request.method == "POST":
        #fetch faculty for imca1
        sub_ic1 = Lecturer.objects.filter(id=1).values()
        faculty_name_ic1 = Lecturer.objects.filter(id=11).values()
        
        #fetch faculty for imca2
        sub_ic2 = Lecturer.objects.filter(id=2).values()
        faculty_name_ic2 = Lecturer.objects.filter(id=22).values()
        
        #fetch faculty for imca3
        sub_ic3 = Lecturer.objects.filter(id=3).values()
        faculty_name_ic3 = Lecturer.objects.filter(id=33).values()
        
        #fetch faculty for imca4
        sub_ic4 = Lecturer.objects.filter(id=4).values()
        faculty_name_ic4 = Lecturer.objects.filter(id=44).values()
        
        #fetch faculty for imca5
        sub_ic5 = Lecturer.objects.filter(id=5).values()
        faculty_name_ic5 = Lecturer.objects.filter(id=55).values()
        
        #fetch faculty for imca6
        sub_ic6 = Lecturer.objects.filter(id=6).values()
        faculty_name_ic6 = Lecturer.objects.filter(id=66).values()
        
        #fetch faculty for imca7
        sub_ic7 = Lecturer.objects.filter(id=7).values()
        faculty_name_ic7 = Lecturer.objects.filter(id=77).values()
        
        #fetch faculty for imca8
        sub_ic8 = Lecturer.objects.filter(id=8).values()
        faculty_name_ic8 = Lecturer.objects.filter(id=88).values()
        
        #fetch faculty for imca9
        sub_ic9 = Lecturer.objects.filter(id=9).values()
        faculty_name_ic9 = Lecturer.objects.filter(id=99).values()
        
        #fetch faculty for imca10
        sub_ic10 = Lecturer.objects.filter(id=10).values()
        faculty_name_ic10 = Lecturer.objects.filter(id=100).values()
        
        #fetch faculty for mca1
        sub_mca1 = Lecturer.objects.filter(id=101).values()
        faculty_name_mca1 = Lecturer.objects.filter(id=1011).values()
        
        #fetch faculty for mca2
        sub_mca2 = Lecturer.objects.filter(id=102).values()
        faculty_name_mca2 = Lecturer.objects.filter(id=1022).values()
        
        #fetch faculty for mca3
        sub_mca3 = Lecturer.objects.filter(id=103).values()
        faculty_name_mca3 = Lecturer.objects.filter(id=1033).values()
        
        #fetch faculty for mca4
        sub_mca4 = Lecturer.objects.filter(id=104).values()
        faculty_name_mca4 = Lecturer.objects.filter(id=1044).values()
        
        return render(request,'update.html',{'sub_ic1':sub_ic1,'faculty_name_ic1':faculty_name_ic1,
                                             'sub_ic2':sub_ic2,'faculty_name_ic2':faculty_name_ic2,
                                             'sub_ic3':sub_ic3,'faculty_name_ic3':faculty_name_ic3,
                                             'sub_ic4':sub_ic4,'faculty_name_ic4':faculty_name_ic4,
                                             'sub_ic5':sub_ic5,'faculty_name_ic5':faculty_name_ic5,
                                             'sub_ic6':sub_ic6,'faculty_name_ic6':faculty_name_ic6,
                                             'sub_ic7':sub_ic7,'faculty_name_ic7':faculty_name_ic7,
                                             'sub_ic8':sub_ic8,'faculty_name_ic8':faculty_name_ic8,
                                             'sub_ic9':sub_ic9,'faculty_name_ic9':faculty_name_ic9,
                                             'sub_ic10':sub_ic10,'faculty_name_ic10':faculty_name_ic10,
                                             'sub_mca1':sub_mca1,'faculty_name_mca1':faculty_name_mca1,
                                             'sub_mca2':sub_mca2,'faculty_name_mca2':faculty_name_mca2,
                                             'sub_mca3':sub_mca3,'faculty_name_mca3':faculty_name_mca3,
                                             'sub_mca4':sub_mca4,'faculty_name_mca4':faculty_name_mca4})

"""------------------------------------------ Faculty update ---------------------------------------------------"""

#IMCA1 Update          
def update_ic1(request):
    if request.method == "POST":
        
        #IMCA semester 1 
        sem_code = Lecturer.objects.get(id=1)
        sem_code.subject1 = request.POST['sem_ic1_code_sub1']
        sem_code.subject2 = request.POST['sem_ic1_code_sub2']
        sem_code.subject3 = request.POST['sem_ic1_code_sub3']
        sem_code.subject4 = request.POST['sem_ic1_code_sub4']
        sem_code.subject5 = request.POST['sem_ic1_code_sub5']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=11)
        fac_name.subject1 = request.POST['fac_ic1_sub1']
        fac_name.subject2 = request.POST['fac_ic1_sub2']
        fac_name.subject3 = request.POST['fac_ic1_sub3']
        fac_name.subject4 = request.POST['fac_ic1_sub4']
        fac_name.subject5 = request.POST['fac_ic1_sub5']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA2 Update          
def update_ic2(request):
    if request.method == "POST":
        
        #IMCA semester 2
        sem_code = Lecturer.objects.get(id=2)
        sem_code.subject1 = request.POST['sem_ic2_code_sub1']
        sem_code.subject2 = request.POST['sem_ic2_code_sub2']
        sem_code.subject3 = request.POST['sem_ic2_code_sub3']
        sem_code.subject4 = request.POST['sem_ic2_code_sub4']
        sem_code.subject5 = request.POST['sem_ic2_code_sub5']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=22)
        fac_name.subject1 = request.POST['fac_ic2_sub1']
        fac_name.subject2 = request.POST['fac_ic2_sub2']
        fac_name.subject3 = request.POST['fac_ic2_sub3']
        fac_name.subject4 = request.POST['fac_ic2_sub4']
        fac_name.subject5 = request.POST['fac_ic2_sub5']
        fac_name.save()
        return HttpResponse(update_faculty(request))

#IMCA3 Update          
def update_ic3(request):
    if request.method == "POST":
        
        #IMCA semester 3 
        sem_code = Lecturer.objects.get(id=3)
        sem_code.subject1 = request.POST['sem_ic3_code_sub1']
        sem_code.subject2 = request.POST['sem_ic3_code_sub2']
        sem_code.subject3 = request.POST['sem_ic3_code_sub3']
        sem_code.subject4 = request.POST['sem_ic3_code_sub4']
        sem_code.subject5 = request.POST['sem_ic3_code_sub5']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=33)
        fac_name.subject1 = request.POST['fac_ic3_sub1']
        fac_name.subject2 = request.POST['fac_ic3_sub2']
        fac_name.subject3 = request.POST['fac_ic3_sub3']
        fac_name.subject4 = request.POST['fac_ic3_sub4']
        fac_name.subject5 = request.POST['fac_ic3_sub5']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA4 Update          
def update_ic4(request):
    if request.method == "POST":
        
        #IMCA semester 4 
        sem_code = Lecturer.objects.get(id=4)
        sem_code.subject1 = request.POST['sem_ic4_code_sub1']
        sem_code.subject2 = request.POST['sem_ic4_code_sub2']
        sem_code.subject3 = request.POST['sem_ic4_code_sub3']
        sem_code.subject4 = request.POST['sem_ic4_code_sub4']
        sem_code.subject5 = request.POST['sem_ic4_code_sub5']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=44)
        fac_name.subject1 = request.POST['fac_ic4_sub1']
        fac_name.subject2 = request.POST['fac_ic4_sub2']
        fac_name.subject3 = request.POST['fac_ic4_sub3']
        fac_name.subject4 = request.POST['fac_ic4_sub4']
        fac_name.subject5 = request.POST['fac_ic4_sub5']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA5 Update          
def update_ic5(request):
    if request.method == "POST":
        
        #IMCA semester 5 
        sem_code = Lecturer.objects.get(id=5)
        sem_code.subject1 = request.POST['sem_ic5_code_sub1']
        sem_code.subject2 = request.POST['sem_ic5_code_sub2']
        sem_code.subject3 = request.POST['sem_ic5_code_sub3']
        sem_code.subject4 = request.POST['sem_ic5_code_sub4']
        sem_code.subject5 = request.POST['sem_ic5_code_sub5']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=55)
        fac_name.subject1 = request.POST['fac_ic5_sub1']
        fac_name.subject2 = request.POST['fac_ic5_sub2']
        fac_name.subject3 = request.POST['fac_ic5_sub3']
        fac_name.subject4 = request.POST['fac_ic5_sub4']
        fac_name.subject5 = request.POST['fac_ic5_sub5']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA6 Update          
def update_ic6(request):
    if request.method == "POST":
        
        #IMCA semester 6 
        sem_code = Lecturer.objects.get(id=6)
        sem_code.subject1 = request.POST['sem_ic6_code_sub1']
        sem_code.subject2 = request.POST['sem_ic6_code_sub2']
        sem_code.subject3 = request.POST['sem_ic6_code_sub3']
        sem_code.subject4 = request.POST['sem_ic6_code_sub4']
        sem_code.subject5 = request.POST['sem_ic6_code_sub5']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=66)
        fac_name.subject1 = request.POST['fac_ic6_sub1']
        fac_name.subject2 = request.POST['fac_ic6_sub2']
        fac_name.subject3 = request.POST['fac_ic6_sub3']
        fac_name.subject4 = request.POST['fac_ic6_sub4']
        fac_name.subject5 = request.POST['fac_ic6_sub5']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA7 Update          
def update_ic7(request):
    if request.method == "POST":
        
        #IMCA semester 7 
        sem_code = Lecturer.objects.get(id=7)
        sem_code.subject1 = request.POST['sem_ic7_code_sub1']
        sem_code.subject2 = request.POST['sem_ic7_code_sub2']
        sem_code.subject3 = request.POST['sem_ic7_code_sub3']
        sem_code.subject4 = request.POST['sem_ic7_code_sub4']
        sem_code.subject5 = request.POST['sem_ic7_code_sub5']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=77)
        fac_name.subject1 = request.POST['fac_ic7_sub1']
        fac_name.subject2 = request.POST['fac_ic7_sub2']
        fac_name.subject3 = request.POST['fac_ic7_sub3']
        fac_name.subject4 = request.POST['fac_ic7_sub4']
        fac_name.subject5 = request.POST['fac_ic7_sub5']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA8 Update          
def update_ic8(request):
    if request.method == "POST":
        
        #IMCA semester 8 
        sem_code = Lecturer.objects.get(id=8)
        sem_code.subject1 = request.POST['sem_ic8_code_sub1']
        sem_code.subject2 = request.POST['sem_ic8_code_sub2']
        sem_code.subject3 = request.POST['sem_ic8_code_sub3']
        sem_code.subject4 = request.POST['sem_ic8_code_sub4']
        sem_code.subject5 = request.POST['sem_ic8_code_sub5']
        sem_code.subject6 = request.POST['sem_ic8_code_sub6']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=88)
        fac_name.subject1 = request.POST['fac_ic8_sub1']
        fac_name.subject2 = request.POST['fac_ic8_sub2']
        fac_name.subject3 = request.POST['fac_ic8_sub3']
        fac_name.subject4 = request.POST['fac_ic8_sub4']
        fac_name.subject5 = request.POST['fac_ic8_sub5']
        fac_name.subject6 = request.POST['fac_ic8_sub6']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA9 Update          
def update_ic9(request):
    if request.method == "POST":
        
        #IMCA semester 9 
        sem_code = Lecturer.objects.get(id=9)
        sem_code.subject1 = request.POST['sem_ic9_code_sub1']
        sem_code.subject2 = request.POST['sem_ic9_code_sub2']
        sem_code.subject3 = request.POST['sem_ic9_code_sub3']
        sem_code.subject4 = request.POST['sem_ic9_code_sub4']
        sem_code.subject5 = request.POST['sem_ic9_code_sub5']
        sem_code.subject6 = request.POST['sem_ic9_code_sub6']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=99)
        fac_name.subject1 = request.POST['fac_ic9_sub1']
        fac_name.subject2 = request.POST['fac_ic9_sub2']
        fac_name.subject3 = request.POST['fac_ic9_sub3']
        fac_name.subject4 = request.POST['fac_ic9_sub4']
        fac_name.subject5 = request.POST['fac_ic9_sub5']
        fac_name.subject6 = request.POST['fac_ic9_sub6']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#IMCA10 Update          
def update_ic10(request):
    if request.method == "POST":
        
        #IMCA semester 10 
        sem_code = Lecturer.objects.get(id=10)
        sem_code.subject1 = request.POST['sem_ic10_code_sub1']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=100)
        fac_name.subject1 = request.POST['fac_ic10_sub1']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#MCA1 Update          
def update_mca1(request):
    if request.method == "POST":
        
        #MCA semester 1 
        sem_code = Lecturer.objects.get(id=101)
        sem_code.subject1 = request.POST['sem_mca1_code_sub1']
        sem_code.subject2 = request.POST['sem_mca1_code_sub2']
        sem_code.subject3 = request.POST['sem_mca1_code_sub3']
        sem_code.subject4 = request.POST['sem_mca1_code_sub4']
        sem_code.subject5 = request.POST['sem_mca1_code_sub5']
        sem_code.subject6 = request.POST['sem_mca1_code_sub6']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=1011)
        fac_name.subject1 = request.POST['fac_mca1_sub1']
        fac_name.subject2 = request.POST['fac_mca1_sub2']
        fac_name.subject3 = request.POST['fac_mca1_sub3']
        fac_name.subject4 = request.POST['fac_mca1_sub4']
        fac_name.subject5 = request.POST['fac_mca1_sub5']
        fac_name.subject6 = request.POST['fac_mca1_sub6']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#MCA2 Update          
def update_mca2(request):
    if request.method == "POST":
        
        #MCA semester 2 
        sem_code = Lecturer.objects.get(id=102)
        sem_code.subject1 = request.POST['sem_mca2_code_sub1']
        sem_code.subject2 = request.POST['sem_mca2_code_sub2']
        sem_code.subject3 = request.POST['sem_mca2_code_sub3']
        sem_code.subject4 = request.POST['sem_mca2_code_sub4']
        sem_code.subject5 = request.POST['sem_mca2_code_sub5']
        sem_code.subject6 = request.POST['sem_mca2_code_sub6']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=1022)
        fac_name.subject1 = request.POST['fac_mca2_sub1']
        fac_name.subject2 = request.POST['fac_mca2_sub2']
        fac_name.subject3 = request.POST['fac_mca2_sub3']
        fac_name.subject4 = request.POST['fac_mca2_sub4']
        fac_name.subject5 = request.POST['fac_mca2_sub5']
        fac_name.subject6 = request.POST['fac_mca2_sub6']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#MCA3 Update          
def update_mca3(request):
    if request.method == "POST":
        
        #MCA semester 3 
        sem_code = Lecturer.objects.get(id=103)
        sem_code.subject1 = request.POST['sem_mca3_code_sub1']
        sem_code.subject2 = request.POST['sem_mca3_code_sub2']
        sem_code.subject3 = request.POST['sem_mca3_code_sub3']
        sem_code.subject4 = request.POST['sem_mca3_code_sub4']
        sem_code.subject5 = request.POST['sem_mca3_code_sub5']
        sem_code.subject6 = request.POST['sem_mca3_code_sub6']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=1033)
        fac_name.subject1 = request.POST['fac_mca3_sub1']
        fac_name.subject2 = request.POST['fac_mca3_sub2']
        fac_name.subject3 = request.POST['fac_mca3_sub3']
        fac_name.subject4 = request.POST['fac_mca3_sub4']
        fac_name.subject5 = request.POST['fac_mca3_sub5']
        fac_name.subject6 = request.POST['fac_mca3_sub6']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
#MCA4 Update          
def update_mca4(request):
    if request.method == "POST":
        
        #MCA semester 4 
        sem_code = Lecturer.objects.get(id=104)
        sem_code.subject1 = request.POST['sem_mca4_code_sub1']
        sem_code.save()
        
        fac_name = Lecturer.objects.get(id=1044)
        fac_name.subject1 = request.POST['fac_mca4_sub1']
        fac_name.save()
        return HttpResponse(update_faculty(request))
    
"""----------------------------------- Faculty Update Complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-1 ----------------------------------------"""
#ic1 faculty fetch
def ic1(request):
    sub = Lecturer.objects.filter(id=1).values()
    faculty_name_ic1 = Lecturer.objects.filter(id=11).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA1.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic1':faculty_name_ic1})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
        #return render(request, "index.html", {'context':context})
    
"""------------------------------------ Feedback Insert --------------------------------------"""
##IC1 FCO 2618601 function for feedback insert
def ic1_2618601(request):  
    if request.method == "POST":  
        form = Ic1_2618601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic1_2618601_Form()  
    return render(request,'IMCA1.html',{'form':form})

##IC1 FOW 2618602 function for feedback insert
def ic1_2618602(request):  
    if request.method == "POST":  
        form = Ic1_2618602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic1_2618602_Form()  
    return render(request,'IMCA1.html',{'form':form})

##IC1 FOP 2618603 function for feedback insert
def ic1_2618603(request):  
    if request.method == "POST":  
        form = Ic1_2618603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic1_2618603_Form()  
    return render(request,'IMCA1.html',{'form':form})

##IC1 BM 2618604 function for feedback insert
def ic1_2618604(request):  
    if request.method == "POST":  
        form = Ic1_2618604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic1_2618604_Form()  
    return render(request,'IMCA1.html',{'form':form})

##IC1 CS 2618605 function for feedback insert
def ic1_2618605(request):  
    if request.method == "POST":  
        form = Ic1_2618605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic1_2618605_Form()  
    return render(request,'IMCA1.html',{'form':form})

def successic1(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic1 Main function for insert ############################
def ic1_main(request):
    if request.method == "POST":
        ic1_2618601(request)
        ic1_2618602(request)
        ic1_2618603(request)
        ic1_2618604(request)
        ic1_2618605(request)
        return render(request,'Success.html')
    
################################### Delete IMCA1 Database #############################################
def delete_dbs_ic1(request):
    if request.method == "POST":
        Ic1_2618601.objects.all().delete()
        ic1_2618601 = Ic1_2618601(std_id=0, pr2618601=0, pe2618601=0, sk2618601=0, mt2618601=0, ms2618601=0, pa2618601=0, cs2618601=0, ps2618601=0)
        ic1_2618601.save()
        
        Ic1_2618602.objects.all().delete()
        ic1_2618602 = Ic1_2618602(std_id=0, pr2618602=0, pe2618602=0, sk2618602=0, mt2618602=0, ms2618602=0, pa2618602=0, cs2618602=0, ps2618602=0)
        ic1_2618602.save()    
        
        Ic1_2618603.objects.all().delete()
        ic1_2618603 = Ic1_2618603(std_id=0, pr2618603=0, pe2618603=0, sk2618603=0, mt2618603=0, ms2618603=0, pa2618603=0, cs2618603=0, ps2618603=0)
        ic1_2618603.save()  
          
        Ic1_2618604.objects.all().delete()
        ic1_2618604 = Ic1_2618604(std_id=0, pr2618604=0, pe2618604=0, sk2618604=0, mt2618604=0, ms2618604=0, pa2618604=0, cs2618604=0, ps2618604=0)
        ic1_2618604.save()
          
        Ic1_2618605.objects.all().delete()
        ic1_2618605 = Ic1_2618605(std_id=0, pr2618605=0, pe2618605=0, sk2618605=0, mt2618605=0, ms2618605=0, pa2618605=0, cs2618605=0, ps2618605=0)
        ic1_2618605.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})

################################# imca1 total function ####################################
def imca1total(request):
    if request.method == "POST":
        faculty_name_ic1 = Lecturer.objects.filter(id=11).values()
        sub = Lecturer.objects.filter(id=1).values()
        return render(request,'imca1total.html', {'sub':sub,
                                                  'faculty_name_ic1':faculty_name_ic1,
                                                  'all_total_ic1':all_total_ic1,
                                                  'count_ic1':count_ic1,
                                                  'totalpr_ic1':totalpr_ic1,
                                                  'totalpe_ic1':totalpe_ic1,
                                                  'totalsk_ic1':totalsk_ic1,
                                                  'totalmt_ic1':totalmt_ic1,
                                                  'totalms_ic1':totalms_ic1,
                                                  'totalpa_ic1':totalpa_ic1,
                                                  'totalcs_ic1':totalcs_ic1,
                                                  'totalps_ic1':totalps_ic1,
                                                  
                                                  'total_2618601':total_2618601,
                                                  'additionpr_2618601':additionpr_2618601,
                                                  'additionpe_2618601':additionpe_2618601,
                                                  'additionsk_2618601':additionsk_2618601,
                                                  'additionmt_2618601':additionmt_2618601,
                                                  'additionms_2618601':additionms_2618601,
                                                  'additionpa_2618601':additionpa_2618601,
                                                  'additioncs_2618601':additioncs_2618601,
                                                  'additionps_2618601':additionps_2618601,
                                                  
                                                  'total_2618602':total_2618602,
                                                  'additionpr_2618602':additionpr_2618602,
                                                  'additionpe_2618602':additionpe_2618602,
                                                  'additionsk_2618602':additionsk_2618602,
                                                  'additionmt_2618602':additionmt_2618602,
                                                  'additionms_2618602':additionms_2618602,
                                                  'additionpa_2618602':additionpa_2618602,
                                                  'additioncs_2618602':additioncs_2618602,
                                                  'additionps_2618602':additionps_2618602,
                                                  
                                                  'total_2618603':total_2618603,
                                                  'additionpr_2618603':additionpr_2618603,
                                                  'additionpe_2618603':additionpe_2618603,
                                                  'additionsk_2618603':additionsk_2618603,
                                                  'additionmt_2618603':additionmt_2618603,
                                                  'additionms_2618603':additionms_2618603,
                                                  'additionpa_2618603':additionpa_2618603,
                                                  'additioncs_2618603':additioncs_2618603,
                                                  'additionps_2618603':additionps_2618603,
                                                  
                                                  'total_2618604':total_2618604,
                                                  'additionpr_2618604':additionpr_2618604,
                                                  'additionpe_2618604':additionpe_2618604,
                                                  'additionsk_2618604':additionsk_2618604,
                                                  'additionmt_2618604':additionmt_2618604,
                                                  'additionms_2618604':additionms_2618604,
                                                  'additionpa_2618604':additionpa_2618604,
                                                  'additioncs_2618604':additioncs_2618604,
                                                  'additionps_2618604':additionps_2618604,
                                                  
                                                  'total_2618605':total_2618605,
                                                  'additionpr_2618605':additionpr_2618605,
                                                  'additionpe_2618605':additionpe_2618605,
                                                  'additionsk_2618605':additionsk_2618605,
                                                  'additionmt_2618605':additionmt_2618605,
                                                  'additionms_2618605':additionms_2618605,
                                                  'additionpa_2618605':additionpa_2618605,
                                                  'additioncs_2618605':additioncs_2618605,
                                                  'additionps_2618605':additionps_2618605})
        
############################# ic1_report_2618601 function for report build ###############################
def ic1_report_2618601(request):
    if request.method == "POST":
        sem = 'IMCA-1 SEM'
        count = count_ic1
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic1*100)/whole_sem_score
        highest_score = max(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        lowest_score = min(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=1).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=11).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic1*100)/max_all_score
        pr_total_fac = additionpr_2618601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic1*100)/max_all_score
        pe_total_fac = additionpe_2618601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic1*100)/max_all_score
        sk_total_fac = additionsk_2618601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic1*100)/max_all_score
        mt_total_fac = additionmt_2618601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic1*100)/max_all_score
        ms_total_fac = additionms_2618601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic1*100)/max_all_score
        pa_total_fac = additionpa_2618601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic1*100)/max_all_score
        cs_total_fac = additioncs_2618601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic1*100)/max_all_score
        ps_total_fac = additionps_2618601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic1_report_2618602 function for report build ###############################
def ic1_report_2618602(request):
    if request.method == "POST":
        sem = 'IMCA-1 SEM'
        count = count_ic1
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic1*100)/whole_sem_score
        highest_score = max(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        lowest_score = min(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=1).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=11).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic1*100)/max_all_score
        pr_total_fac = additionpr_2618602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic1*100)/max_all_score
        pe_total_fac = additionpe_2618602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic1*100)/max_all_score
        sk_total_fac = additionsk_2618602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic1*100)/max_all_score
        mt_total_fac = additionmt_2618602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic1*100)/max_all_score
        ms_total_fac = additionms_2618602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic1*100)/max_all_score
        pa_total_fac = additionpa_2618602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic1*100)/max_all_score
        cs_total_fac = additioncs_2618602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic1*100)/max_all_score
        ps_total_fac = additionps_2618602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic1_report_2618603 function for report build ###########################
def ic1_report_2618603(request):
    if request.method == "POST":
        sem = 'IMCA-1 SEM'
        count = count_ic1
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic1*100)/whole_sem_score
        highest_score = max(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        lowest_score = min(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=1).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=11).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic1*100)/max_all_score
        pr_total_fac = additionpr_2618603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic1*100)/max_all_score
        pe_total_fac = additionpe_2618603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic1*100)/max_all_score
        sk_total_fac = additionsk_2618603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic1*100)/max_all_score
        mt_total_fac = additionmt_2618603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic1*100)/max_all_score
        ms_total_fac = additionms_2618603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic1*100)/max_all_score
        pa_total_fac = additionpa_2618603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic1*100)/max_all_score
        cs_total_fac = additioncs_2618603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic1*100)/max_all_score
        ps_total_fac = additionps_2618603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic1_report_2618604 function for report build ##############################
def ic1_report_2618604(request):
    if request.method == "POST":
        sem = 'IMCA-1 SEM'
        count = count_ic1
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic1*100)/whole_sem_score
        highest_score = max(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        lowest_score = min(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=1).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=11).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic1*100)/max_all_score
        pr_total_fac = additionpr_2618604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic1*100)/max_all_score
        pe_total_fac = additionpe_2618604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic1*100)/max_all_score
        sk_total_fac = additionsk_2618604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic1*100)/max_all_score
        mt_total_fac = additionmt_2618604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic1*100)/max_all_score
        ms_total_fac = additionms_2618604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic1*100)/max_all_score
        pa_total_fac = additionpa_2618604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic1*100)/max_all_score
        cs_total_fac = additioncs_2618604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic1*100)/max_all_score
        ps_total_fac = additionps_2618604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic1_report_2618605 function for report build ###############################
def ic1_report_2618605(request):
    if request.method == "POST":
        sem = 'IMCA-1 SEM'
        count = count_ic1
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic1*100)/whole_sem_score
        highest_score = max(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        lowest_score = min(total_2618601['total'], total_2618602['total'], total_2618603['total'], total_2618604['total'], total_2618605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=1).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=11).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic1*100)/max_all_score
        pr_total_fac = additionpr_2618605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic1*100)/max_all_score
        pe_total_fac = additionpe_2618605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic1*100)/max_all_score
        sk_total_fac = additionsk_2618605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic1*100)/max_all_score
        mt_total_fac = additionmt_2618605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic1*100)/max_all_score
        ms_total_fac = additionms_2618605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic1*100)/max_all_score
        pa_total_fac = additionpa_2618605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic1*100)/max_all_score
        cs_total_fac = additioncs_2618605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic1*100)/max_all_score
        ps_total_fac = additionps_2618605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

"""----------------------------------- all functions for Imca-1 complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-2 -------------------0000---------------------"""
#ic2 faculty fetch
def ic2(request):
    sub = Lecturer.objects.filter(id=2).values()
    faculty_name_ic2 = Lecturer.objects.filter(id=22).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA2.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic2':faculty_name_ic2})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
    

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC2 DS 2628601 function for feedback insert
def ic2_2628601(request):  
    if request.method == "POST":  
        form = Ic2_2628601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic2_2628601_Form()  
    return render(request,'IMCA2.html',{'form':form})

##IC2 ADVANCE C 2628602 function for feedback insert
def ic2_2628602(request):  
    if request.method == "POST":  
        form = Ic2_2628602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic2_2628602_Form()  
    return render(request,'IMCA2.html',{'form':form})

##IC2 DBMS 2628603 function for feedback insert
def ic2_2628603(request):  
    if request.method == "POST":  
        form = Ic2_2628603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic2_2628603_Form()  
    return render(request,'IMCA2.html',{'form':form})

##IC2 OS 2628604 function for feedback insert
def ic2_2628604(request):  
    if request.method == "POST":  
        form = Ic2_2628604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic2_2628604_Form()  
    return render(request,'IMCA2.html',{'form':form})

##IC2 SP 2628605 function for feedback insert
def ic2_2628605(request):  
    if request.method == "POST":  
        form = Ic2_2628605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic2_2628605_Form()  
    return render(request,'IMCA2.html',{'form':form})

def successic2(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic2 Main function for insert ############################
def ic2_main(request):
    if request.method == "POST":
        ic2_2628601(request)
        ic2_2628602(request)
        ic2_2628603(request)
        ic2_2628604(request)
        ic2_2628605(request)
        return render(request,'Success.html')
    
################################### Delete IMCA2 Database #############################################
def delete_dbs_ic2(request):
    if request.method == "POST":
        Ic2_2628601.objects.all().delete()
        ic2_2628601 = Ic2_2628601(std_id=0, pr2628601=0, pe2628601=0, sk2628601=0, mt2628601=0, ms2628601=0, pa2628601=0, cs2628601=0, ps2628601=0)
        ic2_2628601.save()
        
        Ic2_2628602.objects.all().delete()
        ic2_2628602 = Ic2_2628602(std_id=0, pr2628602=0, pe2628602=0, sk2628602=0, mt2628602=0, ms2628602=0, pa2628602=0, cs2628602=0, ps2628602=0)
        ic2_2628602.save()    
        
        Ic2_2628603.objects.all().delete()
        ic2_2628603 = Ic2_2628603(std_id=0, pr2628603=0, pe2628603=0, sk2628603=0, mt2628603=0, ms2628603=0, pa2628603=0, cs2628603=0, ps2628603=0)
        ic2_2628603.save()  
          
        Ic2_2628604.objects.all().delete()
        ic2_2628604 = Ic2_2628604(std_id=0, pr2628604=0, pe2628604=0, sk2628604=0, mt2628604=0, ms2628604=0, pa2628604=0, cs2628604=0, ps2628604=0)
        ic2_2628604.save()
          
        Ic2_2628605.objects.all().delete()
        ic2_2628605 = Ic2_2628605(std_id=0, pr2628605=0, pe2628605=0, sk2628605=0, mt2628605=0, ms2628605=0, pa2628605=0, cs2628605=0, ps2628605=0)
        ic2_2628605.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# imca2 total function ####################################
def imca2total(request):
    if request.method == "POST":
        faculty_name_ic2 = Lecturer.objects.filter(id=22).values()
        sub = Lecturer.objects.filter(id=2).values()
        return render(request,'imca2total.html', {'sub':sub,
                                                  'faculty_name_ic2':faculty_name_ic2,
                                                  'all_total_ic2':all_total_ic2,
                                                  'count_ic2':count_ic2,
                                                  'totalpr_ic2':totalpr_ic2,
                                                  'totalpe_ic2':totalpe_ic2,
                                                  'totalsk_ic2':totalsk_ic2,
                                                  'totalmt_ic2':totalmt_ic2,
                                                  'totalms_ic2':totalms_ic2,
                                                  'totalpa_ic2':totalpa_ic2,
                                                  'totalcs_ic2':totalcs_ic2,
                                                  'totalps_ic2':totalps_ic2,
                                                  
                                                  'total_2628601':total_2628601,
                                                  'additionpr_2628601':additionpr_2628601,
                                                  'additionpe_2628601':additionpe_2628601,
                                                  'additionsk_2628601':additionsk_2628601,
                                                  'additionmt_2628601':additionmt_2628601,
                                                  'additionms_2628601':additionms_2628601,
                                                  'additionpa_2628601':additionpa_2628601,
                                                  'additioncs_2628601':additioncs_2628601,
                                                  'additionps_2628601':additionps_2628601,
                                                  
                                                  'total_2628602':total_2628602,
                                                  'additionpr_2628602':additionpr_2628602,
                                                  'additionpe_2628602':additionpe_2628602,
                                                  'additionsk_2628602':additionsk_2628602,
                                                  'additionmt_2628602':additionmt_2628602,
                                                  'additionms_2628602':additionms_2628602,
                                                  'additionpa_2628602':additionpa_2628602,
                                                  'additioncs_2628602':additioncs_2628602,
                                                  'additionps_2628602':additionps_2628602,
                                                  
                                                  'total_2628603':total_2628603,
                                                  'additionpr_2628603':additionpr_2628603,
                                                  'additionpe_2628603':additionpe_2628603,
                                                  'additionsk_2628603':additionsk_2628603,
                                                  'additionmt_2628603':additionmt_2628603,
                                                  'additionms_2628603':additionms_2628603,
                                                  'additionpa_2628603':additionpa_2628603,
                                                  'additioncs_2628603':additioncs_2628603,
                                                  'additionps_2628603':additionps_2628603,
                                                  
                                                  'total_2628604':total_2628604,
                                                  'additionpr_2628604':additionpr_2628604,
                                                  'additionpe_2628604':additionpe_2628604,
                                                  'additionsk_2628604':additionsk_2628604,
                                                  'additionmt_2628604':additionmt_2628604,
                                                  'additionms_2628604':additionms_2628604,
                                                  'additionpa_2628604':additionpa_2628604,
                                                  'additioncs_2628604':additioncs_2628604,
                                                  'additionps_2628604':additionps_2628604,
                                                  
                                                  'total_2628605':total_2628605,
                                                  'additionpr_2628605':additionpr_2628605,
                                                  'additionpe_2628605':additionpe_2628605,
                                                  'additionsk_2628605':additionsk_2628605,
                                                  'additionmt_2628605':additionmt_2628605,
                                                  'additionms_2628605':additionms_2628605,
                                                  'additionpa_2628605':additionpa_2628605,
                                                  'additioncs_2628605':additioncs_2628605,
                                                  'additionps_2628605':additionps_2628605})
        
############################# ic2_report_2628601 function for report build ###############################
def ic2_report_2628601(request):
    if request.method == "POST":
        sem = 'IMCA-2 SEM'
        count = count_ic2
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic2*100)/whole_sem_score
        highest_score = max(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        lowest_score = min(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=2).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=22).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic2*100)/max_all_score
        pr_total_fac = additionpr_2628601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic2*100)/max_all_score
        pe_total_fac = additionpe_2628601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic2*100)/max_all_score
        sk_total_fac = additionsk_2628601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic2*100)/max_all_score
        mt_total_fac = additionmt_2628601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic2*100)/max_all_score
        ms_total_fac = additionms_2628601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic2*100)/max_all_score
        pa_total_fac = additionpa_2628601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic2*100)/max_all_score
        cs_total_fac = additioncs_2628601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic2*100)/max_all_score
        ps_total_fac = additionps_2628601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic2_report_2628602 function for report build ###############################
def ic2_report_2628602(request):
    if request.method == "POST":
        sem = 'IMCA-2 SEM'
        count = count_ic2
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic2*100)/whole_sem_score
        highest_score = max(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        lowest_score = min(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=2).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=22).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic2*100)/max_all_score
        pr_total_fac = additionpr_2628602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic2*100)/max_all_score
        pe_total_fac = additionpe_2628602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic2*100)/max_all_score
        sk_total_fac = additionsk_2628602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic2*100)/max_all_score
        mt_total_fac = additionmt_2628602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic2*100)/max_all_score
        ms_total_fac = additionms_2628602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic2*100)/max_all_score
        pa_total_fac = additionpa_2628602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic2*100)/max_all_score
        cs_total_fac = additioncs_2628602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic2*100)/max_all_score
        ps_total_fac = additionps_2628602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic2_report_2628603 function for report build ###########################
def ic2_report_2628603(request):
    if request.method == "POST":
        sem = 'IMCA-2 SEM'
        count = count_ic2
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic2*100)/whole_sem_score
        highest_score = max(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        lowest_score = min(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=2).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=22).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic2*100)/max_all_score
        pr_total_fac = additionpr_2628603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic2*100)/max_all_score
        pe_total_fac = additionpe_2628603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic2*100)/max_all_score
        sk_total_fac = additionsk_2628603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic2*100)/max_all_score
        mt_total_fac = additionmt_2628603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic2*100)/max_all_score
        ms_total_fac = additionms_2628603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic2*100)/max_all_score
        pa_total_fac = additionpa_2628603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic2*100)/max_all_score
        cs_total_fac = additioncs_2628603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic2*100)/max_all_score
        ps_total_fac = additionps_2628603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic2_report_2628604 function for report build ##############################
def ic2_report_2628604(request):
    if request.method == "POST":
        sem = 'IMCA-2 SEM'
        count = count_ic2
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic2*100)/whole_sem_score
        highest_score = max(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        lowest_score = min(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=2).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=22).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic2*100)/max_all_score
        pr_total_fac = additionpr_2628604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic2*100)/max_all_score
        pe_total_fac = additionpe_2628604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic2*100)/max_all_score
        sk_total_fac = additionsk_2628604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic2*100)/max_all_score
        mt_total_fac = additionmt_2628604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic2*100)/max_all_score
        ms_total_fac = additionms_2628604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic2*100)/max_all_score
        pa_total_fac = additionpa_2628604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic2*100)/max_all_score
        cs_total_fac = additioncs_2628604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic2*100)/max_all_score
        ps_total_fac = additionps_2628604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic2_report_2628605 function for report build ###############################
def ic2_report_2628605(request):
    if request.method == "POST":
        sem = 'IMCA-2 SEM'
        count = count_ic2
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic2*100)/whole_sem_score
        highest_score = max(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        lowest_score = min(total_2628601['total'], total_2628602['total'], total_2628603['total'], total_2628604['total'], total_2628605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=2).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=22).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic2*100)/max_all_score
        pr_total_fac = additionpr_2628605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic2*100)/max_all_score
        pe_total_fac = additionpe_2628605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic2*100)/max_all_score
        sk_total_fac = additionsk_2628605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic2*100)/max_all_score
        mt_total_fac = additionmt_2628605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic2*100)/max_all_score
        ms_total_fac = additionms_2628605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic2*100)/max_all_score
        pa_total_fac = additionpa_2628605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic2*100)/max_all_score
        cs_total_fac = additioncs_2628605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic2*100)/max_all_score
        ps_total_fac = additionps_2628605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
        
        ###########################################################################################

"""----------------------------------- all functions for Imca-2 complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-3 ----------------------------------------"""   

#ic3 faculty fetch
def ic3(request):
    sub = Lecturer.objects.filter(id=3).values()
    faculty_name_ic3 = Lecturer.objects.filter(id=33).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA3.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic3':faculty_name_ic3})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
    
    
"""------------------------------------ Feedback Insert --------------------------------------"""
##IC3 JAVA 2638601 function for feedback insert
def ic3_2638601(request):  
    if request.method == "POST":  
        form = Ic3_2638601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic3_2638601_Form()  
    return render(request,'IMCA3.html',{'form':form})

##IC3 BS 2638602 function for feedback insert
def ic3_2638602(request):  
    if request.method == "POST":  
        form = Ic3_2638602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic3_2638602_Form()  
    return render(request,'IMCA3.html',{'form':form})

##IC3 SOODAM 2638603 function for feedback insert
def ic3_2638603(request):  
    if request.method == "POST":  
        form = Ic3_2638603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic3_2638603_Form()  
    return render(request,'IMCA3.html',{'form':form})

##IC3 WDT 2638604 function for feedback insert
def ic3_2638604(request):  
    if request.method == "POST":  
        form = Ic3_2638604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic3_2638604_Form()  
    return render(request,'IMCA3.html',{'form':form})

##IC3 SPDS 2638605 function for feedback insert
def ic3_2638605(request):  
    if request.method == "POST":  
        form = Ic3_2638605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic3_2638605_Form()  
    return render(request,'IMCA3.html',{'form':form})

def successic3(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic3 Main function for insert ############################
def ic3_main(request):
    if request.method == "POST":
        ic3_2638601(request)
        ic3_2638602(request)
        ic3_2638603(request)
        ic3_2638604(request)
        ic3_2638605(request)
        return render(request,'Success.html')

################################### Delete IMCA3 Database #############################################
def delete_dbs_ic3(request):
    if request.method == "POST":
        Ic3_2638601.objects.all().delete()
        ic3_2638601 = Ic3_2638601(std_id=0, pr2638601=0, pe2638601=0, sk2638601=0, mt2638601=0, ms2638601=0, pa2638601=0, cs2638601=0, ps2638601=0)
        ic3_2638601.save()
        
        Ic3_2638602.objects.all().delete()
        ic3_2638602 = Ic3_2638602(std_id=0, pr2638602=0, pe2638602=0, sk2638602=0, mt2638602=0, ms2638602=0, pa2638602=0, cs2638602=0, ps2638602=0)
        ic3_2638602.save()    
        
        Ic3_2638603.objects.all().delete()
        ic3_2638603 = Ic3_2638603(std_id=0, pr2638603=0, pe2638603=0, sk2638603=0, mt2638603=0, ms2638603=0, pa2638603=0, cs2638603=0, ps2638603=0)
        ic3_2638603.save()  
          
        Ic3_2638604.objects.all().delete()
        ic3_2638604 = Ic3_2638604(std_id=0, pr2638604=0, pe2638604=0, sk2638604=0, mt2638604=0, ms2638604=0, pa2638604=0, cs2638604=0, ps2638604=0)
        ic3_2638604.save()
          
        Ic3_2638605.objects.all().delete()
        ic3_2638605 = Ic3_2638605(std_id=0, pr2638605=0, pe2638605=0, sk2638605=0, mt2638605=0, ms2638605=0, pa2638605=0, cs2638605=0, ps2638605=0)
        ic3_2638605.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})

################################# imca3 total function ####################################
def imca3total(request):
    if request.method == "POST":
        faculty_name_ic3 = Lecturer.objects.filter(id=33).values()
        sub = Lecturer.objects.filter(id=3).values()
        return render(request,'imca3total.html', {'sub':sub,
                                                  'faculty_name_ic3':faculty_name_ic3,
                                                  'all_total_ic3':all_total_ic3,
                                                  'count_ic3':count_ic3,
                                                  'totalpr_ic3':totalpr_ic3,
                                                  'totalpe_ic3':totalpe_ic3,
                                                  'totalsk_ic3':totalsk_ic3,
                                                  'totalmt_ic3':totalmt_ic3,
                                                  'totalms_ic3':totalms_ic3,
                                                  'totalpa_ic3':totalpa_ic3,
                                                  'totalcs_ic3':totalcs_ic3,
                                                  'totalps_ic3':totalps_ic3,
                                                  
                                                  'total_2638601':total_2638601,
                                                  'additionpr_2638601':additionpr_2638601,
                                                  'additionpe_2638601':additionpe_2638601,
                                                  'additionsk_2638601':additionsk_2638601,
                                                  'additionmt_2638601':additionmt_2638601,
                                                  'additionms_2638601':additionms_2638601,
                                                  'additionpa_2638601':additionpa_2638601,
                                                  'additioncs_2638601':additioncs_2638601,
                                                  'additionps_2638601':additionps_2638601,
                                                  
                                                  'total_2638602':total_2638602,
                                                  'additionpr_2638602':additionpr_2638602,
                                                  'additionpe_2638602':additionpe_2638602,
                                                  'additionsk_2638602':additionsk_2638602,
                                                  'additionmt_2638602':additionmt_2638602,
                                                  'additionms_2638602':additionms_2638602,
                                                  'additionpa_2638602':additionpa_2638602,
                                                  'additioncs_2638602':additioncs_2638602,
                                                  'additionps_2638602':additionps_2638602,
                                                  
                                                  'total_2638603':total_2638603,
                                                  'additionpr_2638603':additionpr_2638603,
                                                  'additionpe_2638603':additionpe_2638603,
                                                  'additionsk_2638603':additionsk_2638603,
                                                  'additionmt_2638603':additionmt_2638603,
                                                  'additionms_2638603':additionms_2638603,
                                                  'additionpa_2638603':additionpa_2638603,
                                                  'additioncs_2638603':additioncs_2638603,
                                                  'additionps_2638603':additionps_2638603,
                                                  
                                                  'total_2638604':total_2638604,
                                                  'additionpr_2638604':additionpr_2638604,
                                                  'additionpe_2638604':additionpe_2638604,
                                                  'additionsk_2638604':additionsk_2638604,
                                                  'additionmt_2638604':additionmt_2638604,
                                                  'additionms_2638604':additionms_2638604,
                                                  'additionpa_2638604':additionpa_2638604,
                                                  'additioncs_2638604':additioncs_2638604,
                                                  'additionps_2638604':additionps_2638604,
                                                  
                                                  'total_2638605':total_2638605,
                                                  'additionpr_2638605':additionpr_2638605,
                                                  'additionpe_2638605':additionpe_2638605,
                                                  'additionsk_2638605':additionsk_2638605,
                                                  'additionmt_2638605':additionmt_2638605,
                                                  'additionms_2638605':additionms_2638605,
                                                  'additionpa_2638605':additionpa_2638605,
                                                  'additioncs_2638605':additioncs_2638605,
                                                  'additionps_2638605':additionps_2638605})

############################# ic3_report_2638601 function for report build ###############################
def ic3_report_2638601(request):
    if request.method == "POST":
        sem = 'IMCA-3 SEM'
        count = count_ic3
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic3*100)/whole_sem_score
        highest_score = max(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        lowest_score = min(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=3).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=33).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic3*100)/max_all_score
        pr_total_fac = additionpr_2638601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic3*100)/max_all_score
        pe_total_fac = additionpe_2638601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic3*100)/max_all_score
        sk_total_fac = additionsk_2638601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic3*100)/max_all_score
        mt_total_fac = additionmt_2638601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic3*100)/max_all_score
        ms_total_fac = additionms_2638601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic3*100)/max_all_score
        pa_total_fac = additionpa_2638601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic3*100)/max_all_score
        cs_total_fac = additioncs_2638601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic3*100)/max_all_score
        ps_total_fac = additionps_2638601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic3_report_2638602 function for report build ###############################
def ic3_report_2638602(request):
    if request.method == "POST":
        sem = 'IMCA-3 SEM'
        count = count_ic3
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic3*100)/whole_sem_score
        highest_score = max(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        lowest_score = min(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=3).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=33).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic3*100)/max_all_score
        pr_total_fac = additionpr_2638602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic3*100)/max_all_score
        pe_total_fac = additionpe_2638602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic3*100)/max_all_score
        sk_total_fac = additionsk_2638602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic3*100)/max_all_score
        mt_total_fac = additionmt_2638602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic3*100)/max_all_score
        ms_total_fac = additionms_2638602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic3*100)/max_all_score
        pa_total_fac = additionpa_2638602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic3*100)/max_all_score
        cs_total_fac = additioncs_2638602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic3*100)/max_all_score
        ps_total_fac = additionps_2638602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic3_report_2638603 function for report build ###########################
def ic3_report_2638603(request):
    if request.method == "POST":
        sem = 'IMCA-3 SEM'
        count = count_ic3
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic3*100)/whole_sem_score
        highest_score = max(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        lowest_score = min(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=3).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=33).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic3*100)/max_all_score
        pr_total_fac = additionpr_2638603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic3*100)/max_all_score
        pe_total_fac = additionpe_2638603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic3*100)/max_all_score
        sk_total_fac = additionsk_2638603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic3*100)/max_all_score
        mt_total_fac = additionmt_2638603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic3*100)/max_all_score
        ms_total_fac = additionms_2638603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic3*100)/max_all_score
        pa_total_fac = additionpa_2638603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic3*100)/max_all_score
        cs_total_fac = additioncs_2638603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic3*100)/max_all_score
        ps_total_fac = additionps_2638603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic3_report_2638604 function for report build ##############################
def ic3_report_2638604(request):
    if request.method == "POST":
        sem = 'IMCA-3 SEM'
        count = count_ic3
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic3*100)/whole_sem_score
        highest_score = max(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        lowest_score = min(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=3).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=33).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic3*100)/max_all_score
        pr_total_fac = additionpr_2638604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic3*100)/max_all_score
        pe_total_fac = additionpe_2638604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic3*100)/max_all_score
        sk_total_fac = additionsk_2638604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic3*100)/max_all_score
        mt_total_fac = additionmt_2638604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic3*100)/max_all_score
        ms_total_fac = additionms_2638604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic3*100)/max_all_score
        pa_total_fac = additionpa_2638604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic3*100)/max_all_score
        cs_total_fac = additioncs_2638604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic3*100)/max_all_score
        ps_total_fac = additionps_2638604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic3_report_2638605 function for report build ###############################
def ic3_report_2638605(request):
    if request.method == "POST":
        sem = 'IMCA-3 SEM'
        count = count_ic3
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic3*100)/whole_sem_score
        highest_score = max(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        lowest_score = min(total_2638601['total'], total_2638602['total'], total_2638603['total'], total_2638604['total'], total_2638605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=3).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=33).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic3*100)/max_all_score
        pr_total_fac = additionpr_2638605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic3*100)/max_all_score
        pe_total_fac = additionpe_2638605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic3*100)/max_all_score
        sk_total_fac = additionsk_2638605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic3*100)/max_all_score
        mt_total_fac = additionmt_2638605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic3*100)/max_all_score
        ms_total_fac = additionms_2638605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic3*100)/max_all_score
        pa_total_fac = additionpa_2638605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic3*100)/max_all_score
        cs_total_fac = additioncs_2638605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic3*100)/max_all_score
        ps_total_fac = additionps_2638605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
        
        ###########################################################################################
"""----------------------------------- all functions for Imca-3 Complete ----------------------------------------""" 

"""----------------------------------- all functions for Imca-4 ----------------------------------------"""   

#ic4 faculty fetch
def ic4(request):
    sub = Lecturer.objects.filter(id=4).values()
    faculty_name_ic4 = Lecturer.objects.filter(id=44).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA4.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic4':faculty_name_ic4})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
    

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC4 PY 2648601 function for feedback insert
def ic4_2648601(request):  
    if request.method == "POST":  
        form = Ic4_2648601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic4_2648601_Form()  
    return render(request,'IMCA4.html',{'form':form})

##IC4 OR 2648602 function for feedback insert
def ic4_2648602(request):  
    if request.method == "POST":  
        form = Ic4_2648602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic4_2648602_Form()  
    return render(request,'IMCA4.html',{'form':form})

##IC4 CN 2648603 function for feedback insert
def ic4_2648603(request):  
    if request.method == "POST":  
        form = Ic4_2648603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic4_2648603_Form()  
    return render(request,'IMCA4.html',{'form':form})

##IC4 LR 2648604 function for feedback insert
def ic4_2648604(request):  
    if request.method == "POST":  
        form = Ic4_2648604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic4_2648604_Form()  
    return render(request,'IMCA4.html',{'form':form})

##IC4 SP JAVA 2648605 function for feedback insert
def ic4_2648605(request):  
    if request.method == "POST":  
        form = Ic4_2648605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic4_2648605_Form()  
    return render(request,'IMCA4.html',{'form':form})

def successic4(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic4 Main function for insert ############################
def ic4_main(request):
    if request.method == "POST":
        ic4_2648601(request)
        ic4_2648602(request)
        ic4_2648603(request)
        ic4_2648604(request)
        ic4_2648605(request)
        return render(request,'Success.html')

################################### Delete IMCA4 Database #############################################
def delete_dbs_ic4(request):
    if request.method == "POST":
        Ic4_2648601.objects.all().delete()
        ic4_2648601 = Ic4_2648601(std_id=0, pr2648601=0, pe2648601=0, sk2648601=0, mt2648601=0, ms2648601=0, pa2648601=0, cs2648601=0, ps2648601=0)
        ic4_2648601.save()
        
        Ic4_2648602.objects.all().delete()
        ic4_2648602 = Ic4_2648602(std_id=0, pr2648602=0, pe2648602=0, sk2648602=0, mt2648602=0, ms2648602=0, pa2648602=0, cs2648602=0, ps2648602=0)
        ic4_2648602.save()    
        
        Ic4_2648603.objects.all().delete()
        ic4_2648603 = Ic4_2648603(std_id=0, pr2648603=0, pe2648603=0, sk2648603=0, mt2648603=0, ms2648603=0, pa2648603=0, cs2648603=0, ps2648603=0)
        ic4_2648603.save()  
          
        Ic4_2648604.objects.all().delete()
        ic4_2648604 = Ic4_2648604(std_id=0, pr2648604=0, pe2648604=0, sk2648604=0, mt2648604=0, ms2648604=0, pa2648604=0, cs2648604=0, ps2648604=0)
        ic4_2648604.save()
          
        Ic4_2648605.objects.all().delete()
        ic4_2648605 = Ic4_2648605(std_id=0, pr2648605=0, pe2648605=0, sk2648605=0, mt2648605=0, ms2648605=0, pa2648605=0, cs2648605=0, ps2648605=0)
        ic4_2648605.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# imca4 total function ####################################
def imca4total(request):
    if request.method == "POST":
        faculty_name_ic4 = Lecturer.objects.filter(id=44).values()
        sub = Lecturer.objects.filter(id=4).values()
        return render(request,'imca4total.html', {'sub':sub,
                                                  'faculty_name_ic4':faculty_name_ic4,
                                                  'all_total_ic4':all_total_ic4,
                                                  'count_ic4':count_ic4,
                                                  'totalpr_ic4':totalpr_ic4,
                                                  'totalpe_ic4':totalpe_ic4,
                                                  'totalsk_ic4':totalsk_ic4,
                                                  'totalmt_ic4':totalmt_ic4,
                                                  'totalms_ic4':totalms_ic4,
                                                  'totalpa_ic4':totalpa_ic4,
                                                  'totalcs_ic4':totalcs_ic4,
                                                  'totalps_ic4':totalps_ic4,
                                                  
                                                  'total_2648601':total_2648601,
                                                  'additionpr_2648601':additionpr_2648601,
                                                  'additionpe_2648601':additionpe_2648601,
                                                  'additionsk_2648601':additionsk_2648601,
                                                  'additionmt_2648601':additionmt_2648601,
                                                  'additionms_2648601':additionms_2648601,
                                                  'additionpa_2648601':additionpa_2648601,
                                                  'additioncs_2648601':additioncs_2648601,
                                                  'additionps_2648601':additionps_2648601,
                                                  
                                                  'total_2648602':total_2648602,
                                                  'additionpr_2648602':additionpr_2648602,
                                                  'additionpe_2648602':additionpe_2648602,
                                                  'additionsk_2648602':additionsk_2648602,
                                                  'additionmt_2648602':additionmt_2648602,
                                                  'additionms_2648602':additionms_2648602,
                                                  'additionpa_2648602':additionpa_2648602,
                                                  'additioncs_2648602':additioncs_2648602,
                                                  'additionps_2648602':additionps_2648602,
                                                  
                                                  'total_2648603':total_2648603,
                                                  'additionpr_2648603':additionpr_2648603,
                                                  'additionpe_2648603':additionpe_2648603,
                                                  'additionsk_2648603':additionsk_2648603,
                                                  'additionmt_2648603':additionmt_2648603,
                                                  'additionms_2648603':additionms_2648603,
                                                  'additionpa_2648603':additionpa_2648603,
                                                  'additioncs_2648603':additioncs_2648603,
                                                  'additionps_2648603':additionps_2648603,
                                                  
                                                  'total_2648604':total_2648604,
                                                  'additionpr_2648604':additionpr_2648604,
                                                  'additionpe_2648604':additionpe_2648604,
                                                  'additionsk_2648604':additionsk_2648604,
                                                  'additionmt_2648604':additionmt_2648604,
                                                  'additionms_2648604':additionms_2648604,
                                                  'additionpa_2648604':additionpa_2648604,
                                                  'additioncs_2648604':additioncs_2648604,
                                                  'additionps_2648604':additionps_2648604,
                                                  
                                                  'total_2648605':total_2648605,
                                                  'additionpr_2648605':additionpr_2648605,
                                                  'additionpe_2648605':additionpe_2648605,
                                                  'additionsk_2648605':additionsk_2648605,
                                                  'additionmt_2648605':additionmt_2648605,
                                                  'additionms_2648605':additionms_2648605,
                                                  'additionpa_2648605':additionpa_2648605,
                                                  'additioncs_2648605':additioncs_2648605,
                                                  'additionps_2648605':additionps_2648605})

############################# ic4_report_2648601 function for report build ###############################
def ic4_report_2648601(request):
    if request.method == "POST":
        sem = 'IMCA-4 SEM'
        count = count_ic4
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic4*100)/whole_sem_score
        highest_score = max(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        lowest_score = min(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=4).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=44).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic4*100)/max_all_score
        pr_total_fac = additionpr_2648601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic4*100)/max_all_score
        pe_total_fac = additionpe_2648601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic4*100)/max_all_score
        sk_total_fac = additionsk_2648601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic4*100)/max_all_score
        mt_total_fac = additionmt_2648601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic4*100)/max_all_score
        ms_total_fac = additionms_2648601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic4*100)/max_all_score
        pa_total_fac = additionpa_2648601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic4*100)/max_all_score
        cs_total_fac = additioncs_2648601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic4*100)/max_all_score
        ps_total_fac = additionps_2648601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic4_report_2648602 function for report build ###############################
def ic4_report_2648602(request):
    if request.method == "POST":
        sem = 'IMCA-4 SEM'
        count = count_ic4
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic4*100)/whole_sem_score
        highest_score = max(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        lowest_score = min(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=4).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=44).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic4*100)/max_all_score
        pr_total_fac = additionpr_2648602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic4*100)/max_all_score
        pe_total_fac = additionpe_2648602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic4*100)/max_all_score
        sk_total_fac = additionsk_2648602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic4*100)/max_all_score
        mt_total_fac = additionmt_2648602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic4*100)/max_all_score
        ms_total_fac = additionms_2648602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic4*100)/max_all_score
        pa_total_fac = additionpa_2648602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic4*100)/max_all_score
        cs_total_fac = additioncs_2648602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic4*100)/max_all_score
        ps_total_fac = additionps_2648602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic4_report_2648603 function for report build ###########################
def ic4_report_2648603(request):
    if request.method == "POST":
        sem = 'IMCA-4 SEM'
        count = count_ic4
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic4*100)/whole_sem_score
        highest_score = max(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        lowest_score = min(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=4).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=44).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic4*100)/max_all_score
        pr_total_fac = additionpr_2648603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic4*100)/max_all_score
        pe_total_fac = additionpe_2648603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic4*100)/max_all_score
        sk_total_fac = additionsk_2648603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic4*100)/max_all_score
        mt_total_fac = additionmt_2648603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic4*100)/max_all_score
        ms_total_fac = additionms_2648603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic4*100)/max_all_score
        pa_total_fac = additionpa_2648603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic4*100)/max_all_score
        cs_total_fac = additioncs_2648603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic4*100)/max_all_score
        ps_total_fac = additionps_2648603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic4_report_2648604 function for report build ##############################
def ic4_report_2648604(request):
    if request.method == "POST":
        sem = 'IMCA-4 SEM'
        count = count_ic4
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic4*100)/whole_sem_score
        highest_score = max(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        lowest_score = min(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=4).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=44).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic4*100)/max_all_score
        pr_total_fac = additionpr_2648604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic4*100)/max_all_score
        pe_total_fac = additionpe_2648604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic4*100)/max_all_score
        sk_total_fac = additionsk_2648604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic4*100)/max_all_score
        mt_total_fac = additionmt_2648604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic4*100)/max_all_score
        ms_total_fac = additionms_2648604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic4*100)/max_all_score
        pa_total_fac = additionpa_2648604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic4*100)/max_all_score
        cs_total_fac = additioncs_2648604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic4*100)/max_all_score
        ps_total_fac = additionps_2648604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic4_report_2648605 function for report build ###############################
def ic4_report_2648605(request):
    if request.method == "POST":
        sem = 'IMCA-4 SEM'
        count = count_ic4
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic4*100)/whole_sem_score
        highest_score = max(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        lowest_score = min(total_2648601['total'], total_2648602['total'], total_2648603['total'], total_2648604['total'], total_2648605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=4).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=44).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic4*100)/max_all_score
        pr_total_fac = additionpr_2648605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic4*100)/max_all_score
        pe_total_fac = additionpe_2648605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic4*100)/max_all_score
        sk_total_fac = additionsk_2648605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic4*100)/max_all_score
        mt_total_fac = additionmt_2648605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic4*100)/max_all_score
        ms_total_fac = additionms_2648605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic4*100)/max_all_score
        pa_total_fac = additionpa_2648605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic4*100)/max_all_score
        cs_total_fac = additioncs_2648605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic4*100)/max_all_score
        ps_total_fac = additionps_2648605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

         ###########################################################################################
"""----------------------------------- all functions for Imca-4 Complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-5 ----------------------------------------"""   

#ic5 faculty fetch
def ic5(request):
    sub = Lecturer.objects.filter(id=5).values()
    faculty_name_ic5 = Lecturer.objects.filter(id=55).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA5.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic5':faculty_name_ic5})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
    

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC5 A.JAVA 2658601 function for feedback insert
def ic5_2658601(request):  
    if request.method == "POST":  
        form = Ic5_2658601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic5_2658601_Form()  
    return render(request,'IMCA5.html',{'form':form})

##IC5 MP 2658602 function for feedback insert
def ic5_2658602(request):  
    if request.method == "POST":  
        form = Ic5_2658602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic5_2658602_Form()  
    return render(request,'IMCA5.html',{'form':form})

##IC5 SE 2658603 function for feedback insert
def ic5_2658603(request):  
    if request.method == "POST":  
        form = Ic5_2658603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic5_2658603_Form()  
    return render(request,'IMCA5.html',{'form':form})

##IC5 E.COMM 2658604 function for feedback insert
def ic5_2658604(request):  
    if request.method == "POST":  
        form = Ic5_2658604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic5_2658604_Form()  
    return render(request,'IMCA5.html',{'form':form})

##IC5 SP SPRING 2658605 function for feedback insert
def ic5_2658605(request):  
    if request.method == "POST":  
        form = Ic5_2658605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic5_2658605_Form()  
    return render(request,'IMCA5.html',{'form':form})

def successic5(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic5 Main function for insert ############################
def ic5_main(request):
    if request.method == "POST":
        ic5_2658601(request)
        ic5_2658602(request)
        ic5_2658603(request)
        ic5_2658604(request)
        ic5_2658605(request)
        return render(request,'Success.html')
    
################################### Delete IMCA5 Database #############################################
def delete_dbs_ic5(request):
    if request.method == "POST":
        Ic5_2658601.objects.all().delete()
        ic5_2658601 = Ic5_2658601(std_id=0, pr2658601=0, pe2658601=0, sk2658601=0, mt2658601=0, ms2658601=0, pa2658601=0, cs2658601=0, ps2658601=0)
        ic5_2658601.save()
        
        Ic5_2658602.objects.all().delete()
        ic5_2658602 = Ic5_2658602(std_id=0, pr2658602=0, pe2658602=0, sk2658602=0, mt2658602=0, ms2658602=0, pa2658602=0, cs2658602=0, ps2658602=0)
        ic5_2658602.save()    
        
        Ic5_2658603.objects.all().delete()
        ic5_2658603 = Ic5_2658603(std_id=0, pr2658603=0, pe2658603=0, sk2658603=0, mt2658603=0, ms2658603=0, pa2658603=0, cs2658603=0, ps2658603=0)
        ic5_2658603.save()  
          
        Ic5_2658604.objects.all().delete()
        ic5_2658604 = Ic5_2658604(std_id=0, pr2658604=0, pe2658604=0, sk2658604=0, mt2658604=0, ms2658604=0, pa2658604=0, cs2658604=0, ps2658604=0)
        ic5_2658604.save()
          
        Ic5_2658605.objects.all().delete()
        ic5_2658605 = Ic5_2658605(std_id=0, pr2658605=0, pe2658605=0, sk2658605=0, mt2658605=0, ms2658605=0, pa2658605=0, cs2658605=0, ps2658605=0)
        ic5_2658605.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# imca5 total function ####################################
def imca5total(request):
    if request.method == "POST":
        faculty_name_ic5 = Lecturer.objects.filter(id=55).values()
        sub = Lecturer.objects.filter(id=5).values()
        return render(request,'imca5total.html', {'sub':sub,
                                                  'faculty_name_ic5':faculty_name_ic5,
                                                  'all_total_ic5':all_total_ic5,
                                                  'count_ic5':count_ic5,
                                                  'totalpr_ic5':totalpr_ic5,
                                                  'totalpe_ic5':totalpe_ic5,
                                                  'totalsk_ic5':totalsk_ic5,
                                                  'totalmt_ic5':totalmt_ic5,
                                                  'totalms_ic5':totalms_ic5,
                                                  'totalpa_ic5':totalpa_ic5,
                                                  'totalcs_ic5':totalcs_ic5,
                                                  'totalps_ic5':totalps_ic5,
                                                  
                                                  'total_2658601':total_2658601,
                                                  'additionpr_2658601':additionpr_2658601,
                                                  'additionpe_2658601':additionpe_2658601,
                                                  'additionsk_2658601':additionsk_2658601,
                                                  'additionmt_2658601':additionmt_2658601,
                                                  'additionms_2658601':additionms_2658601,
                                                  'additionpa_2658601':additionpa_2658601,
                                                  'additioncs_2658601':additioncs_2658601,
                                                  'additionps_2658601':additionps_2658601,
                                                  
                                                  'total_2658602':total_2658602,
                                                  'additionpr_2658602':additionpr_2658602,
                                                  'additionpe_2658602':additionpe_2658602,
                                                  'additionsk_2658602':additionsk_2658602,
                                                  'additionmt_2658602':additionmt_2658602,
                                                  'additionms_2658602':additionms_2658602,
                                                  'additionpa_2658602':additionpa_2658602,
                                                  'additioncs_2658602':additioncs_2658602,
                                                  'additionps_2658602':additionps_2658602,
                                                  
                                                  'total_2658603':total_2658603,
                                                  'additionpr_2658603':additionpr_2658603,
                                                  'additionpe_2658603':additionpe_2658603,
                                                  'additionsk_2658603':additionsk_2658603,
                                                  'additionmt_2658603':additionmt_2658603,
                                                  'additionms_2658603':additionms_2658603,
                                                  'additionpa_2658603':additionpa_2658603,
                                                  'additioncs_2658603':additioncs_2658603,
                                                  'additionps_2658603':additionps_2658603,
                                                  
                                                  'total_2658604':total_2658604,
                                                  'additionpr_2658604':additionpr_2658604,
                                                  'additionpe_2658604':additionpe_2658604,
                                                  'additionsk_2658604':additionsk_2658604,
                                                  'additionmt_2658604':additionmt_2658604,
                                                  'additionms_2658604':additionms_2658604,
                                                  'additionpa_2658604':additionpa_2658604,
                                                  'additioncs_2658604':additioncs_2658604,
                                                  'additionps_2658604':additionps_2658604,
                                                  
                                                  'total_2658605':total_2658605,
                                                  'additionpr_2658605':additionpr_2658605,
                                                  'additionpe_2658605':additionpe_2658605,
                                                  'additionsk_2658605':additionsk_2658605,
                                                  'additionmt_2658605':additionmt_2658605,
                                                  'additionms_2658605':additionms_2658605,
                                                  'additionpa_2658605':additionpa_2658605,
                                                  'additioncs_2658605':additioncs_2658605,
                                                  'additionps_2658605':additionps_2658605})
        





    


############################# ic5_report_2658601 function for report build ###############################
def ic5_report_2658601(request):
    if request.method == "POST":
        sem = 'IMCA-5 SEM'
        count = count_ic5
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic5*100)/whole_sem_score
        highest_score = max(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        lowest_score = min(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=5).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=55).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic5*100)/max_all_score
        pr_total_fac = additionpr_2658601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic5*100)/max_all_score
        pe_total_fac = additionpe_2658601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic5*100)/max_all_score
        sk_total_fac = additionsk_2658601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic5*100)/max_all_score
        mt_total_fac = additionmt_2658601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic5*100)/max_all_score
        ms_total_fac = additionms_2658601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic5*100)/max_all_score
        pa_total_fac = additionpa_2658601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic5*100)/max_all_score
        cs_total_fac = additioncs_2658601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic5*100)/max_all_score
        ps_total_fac = additionps_2658601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic5_report_2658602 function for report build ###############################
def ic5_report_2658602(request):
    if request.method == "POST":
        sem = 'IMCA-5 SEM'
        count = count_ic5
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic5*100)/whole_sem_score
        highest_score = max(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        lowest_score = min(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=5).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=55).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic5*100)/max_all_score
        pr_total_fac = additionpr_2658602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic5*100)/max_all_score
        pe_total_fac = additionpe_2658602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic5*100)/max_all_score
        sk_total_fac = additionsk_2658602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic5*100)/max_all_score
        mt_total_fac = additionmt_2658602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic5*100)/max_all_score
        ms_total_fac = additionms_2658602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic5*100)/max_all_score
        pa_total_fac = additionpa_2658602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic5*100)/max_all_score
        cs_total_fac = additioncs_2658602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic5*100)/max_all_score
        ps_total_fac = additionps_2658602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic5_report_2658603 function for report build ###########################
def ic5_report_2658603(request):
    if request.method == "POST":
        sem = 'IMCA-5 SEM'
        count = count_ic5
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic5*100)/whole_sem_score
        highest_score = max(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        lowest_score = min(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=5).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=55).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic5*100)/max_all_score
        pr_total_fac = additionpr_2658603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic5*100)/max_all_score
        pe_total_fac = additionpe_2658603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic5*100)/max_all_score
        sk_total_fac = additionsk_2658603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic5*100)/max_all_score
        mt_total_fac = additionmt_2658603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic5*100)/max_all_score
        ms_total_fac = additionms_2658603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic5*100)/max_all_score
        pa_total_fac = additionpa_2658603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic5*100)/max_all_score
        cs_total_fac = additioncs_2658603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic5*100)/max_all_score
        ps_total_fac = additionps_2658603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic5_report_2658604 function for report build ##############################
def ic5_report_2658604(request):
    if request.method == "POST":
        sem = 'IMCA-5 SEM'
        count = count_ic5
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic5*100)/whole_sem_score
        highest_score = max(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        lowest_score = min(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=5).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=55).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic5*100)/max_all_score
        pr_total_fac = additionpr_2658604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic5*100)/max_all_score
        pe_total_fac = additionpe_2658604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic5*100)/max_all_score
        sk_total_fac = additionsk_2658604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic5*100)/max_all_score
        mt_total_fac = additionmt_2658604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic5*100)/max_all_score
        ms_total_fac = additionms_2658604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic5*100)/max_all_score
        pa_total_fac = additionpa_2658604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic5*100)/max_all_score
        cs_total_fac = additioncs_2658604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic5*100)/max_all_score
        ps_total_fac = additionps_2658604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic5_report_2658605 function for report build ###############################
def ic5_report_2658605(request):
    if request.method == "POST":
        sem = 'IMCA-5 SEM'
        count = count_ic5
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic5*100)/whole_sem_score
        highest_score = max(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        lowest_score = min(total_2658601['total'], total_2658602['total'], total_2658603['total'], total_2658604['total'], total_2658605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=5).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=55).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic5*100)/max_all_score
        pr_total_fac = additionpr_2658605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic5*100)/max_all_score
        pe_total_fac = additionpe_2658605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic5*100)/max_all_score
        sk_total_fac = additionsk_2658605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic5*100)/max_all_score
        mt_total_fac = additionmt_2658605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic5*100)/max_all_score
        ms_total_fac = additionms_2658605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic5*100)/max_all_score
        pa_total_fac = additionpa_2658605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic5*100)/max_all_score
        cs_total_fac = additioncs_2658605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic5*100)/max_all_score
        ps_total_fac = additionps_2658605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

         ###########################################################################################
"""----------------------------------- all functions for Imca-5 Complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-6 ----------------------------------------"""   

#ic6 faculty fetch
def ic6(request):
    sub = Lecturer.objects.filter(id=6).values()
    faculty_name_ic6 = Lecturer.objects.filter(id=66).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA6.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic6':faculty_name_ic6})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
    

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC6 MIS 2668601 function for feedback insert
def ic6_2668601(request):  
    if request.method == "POST":  
        form = Ic6_2668601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic6_2668601_Form()  
    return render(request,'IMCA6.html',{'form':form})

##IC6 ST 2668602 function for feedback insert
def ic6_2668602(request):  
    if request.method == "POST":  
        form = Ic6_2668602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic6_2668602_Form()  
    return render(request,'IMCA6.html',{'form':form})

##IC6 DM 2668603 function for feedback insert
def ic6_2668603(request):  
    if request.method == "POST":  
        form = Ic6_2668603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic6_2668603_Form()  
    return render(request,'IMCA6.html',{'form':form})

##IC6 ES 2668604 function for feedback insert
def ic6_2668604(request):  
    if request.method == "POST":  
        form = Ic6_2668604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic6_2668604_Form()  
    return render(request,'IMCA6.html',{'form':form})

##IC6 SP ASP 2668605 function for feedback insert
def ic6_2668605(request):  
    if request.method == "POST":  
        form = Ic6_2668605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic6_2668605_Form()  
    return render(request,'IMCA6.html',{'form':form})

def successic6(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic6 Main function for insert ############################
def ic6_main(request):
    if request.method == "POST":
        ic6_2668601(request)
        ic6_2668602(request)
        ic6_2668603(request)
        ic6_2668604(request)
        ic6_2668605(request)
        return render(request,'Success.html')

################################### Delete IMCA6 Database #############################################
def delete_dbs_ic6(request):
    if request.method == "POST":
        Ic6_2668601.objects.all().delete()
        ic6_2668601 = Ic6_2668601(std_id=0, pr2668601=0, pe2668601=0, sk2668601=0, mt2668601=0, ms2668601=0, pa2668601=0, cs2668601=0, ps2668601=0)
        ic6_2668601.save()
        
        Ic6_2668602.objects.all().delete()
        ic6_2668602 = Ic6_2668602(std_id=0, pr2668602=0, pe2668602=0, sk2668602=0, mt2668602=0, ms2668602=0, pa2668602=0, cs2668602=0, ps2668602=0)
        ic6_2668602.save()    
        
        Ic6_2668603.objects.all().delete()
        ic6_2668603 = Ic6_2668603(std_id=0, pr2668603=0, pe2668603=0, sk2668603=0, mt2668603=0, ms2668603=0, pa2668603=0, cs2668603=0, ps2668603=0)
        ic6_2668603.save()  
          
        Ic6_2668604.objects.all().delete()
        ic6_2668604 = Ic6_2668604(std_id=0, pr2668604=0, pe2668604=0, sk2668604=0, mt2668604=0, ms2668604=0, pa2668604=0, cs2668604=0, ps2668604=0)
        ic6_2668604.save()
          
        Ic6_2668605.objects.all().delete()
        ic6_2668605 = Ic6_2668605(std_id=0, pr2668605=0, pe2668605=0, sk2668605=0, mt2668605=0, ms2668605=0, pa2668605=0, cs2668605=0, ps2668605=0)
        ic6_2668605.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# imca6 total function ####################################
def imca6total(request):
    if request.method == "POST":
        faculty_name_ic6 = Lecturer.objects.filter(id=66).values()
        sub = Lecturer.objects.filter(id=6).values()
        return render(request,'imca6total.html', {'sub':sub,
                                                  'faculty_name_ic6':faculty_name_ic6,
                                                  'all_total_ic6':all_total_ic6,
                                                  'count_ic6':count_ic6,
                                                  'totalpr_ic6':totalpr_ic6,
                                                  'totalpe_ic6':totalpe_ic6,
                                                  'totalsk_ic6':totalsk_ic6,
                                                  'totalmt_ic6':totalmt_ic6,
                                                  'totalms_ic6':totalms_ic6,
                                                  'totalpa_ic6':totalpa_ic6,
                                                  'totalcs_ic6':totalcs_ic6,
                                                  'totalps_ic6':totalps_ic6,
                                                  
                                                  'total_2668601':total_2668601,
                                                  'additionpr_2668601':additionpr_2668601,
                                                  'additionpe_2668601':additionpe_2668601,
                                                  'additionsk_2668601':additionsk_2668601,
                                                  'additionmt_2668601':additionmt_2668601,
                                                  'additionms_2668601':additionms_2668601,
                                                  'additionpa_2668601':additionpa_2668601,
                                                  'additioncs_2668601':additioncs_2668601,
                                                  'additionps_2668601':additionps_2668601,
                                                  
                                                  'total_2668602':total_2668602,
                                                  'additionpr_2668602':additionpr_2668602,
                                                  'additionpe_2668602':additionpe_2668602,
                                                  'additionsk_2668602':additionsk_2668602,
                                                  'additionmt_2668602':additionmt_2668602,
                                                  'additionms_2668602':additionms_2668602,
                                                  'additionpa_2668602':additionpa_2668602,
                                                  'additioncs_2668602':additioncs_2668602,
                                                  'additionps_2668602':additionps_2668602,
                                                  
                                                  'total_2668603':total_2668603,
                                                  'additionpr_2668603':additionpr_2668603,
                                                  'additionpe_2668603':additionpe_2668603,
                                                  'additionsk_2668603':additionsk_2668603,
                                                  'additionmt_2668603':additionmt_2668603,
                                                  'additionms_2668603':additionms_2668603,
                                                  'additionpa_2668603':additionpa_2668603,
                                                  'additioncs_2668603':additioncs_2668603,
                                                  'additionps_2668603':additionps_2668603,
                                                  
                                                  'total_2668604':total_2668604,
                                                  'additionpr_2668604':additionpr_2668604,
                                                  'additionpe_2668604':additionpe_2668604,
                                                  'additionsk_2668604':additionsk_2668604,
                                                  'additionmt_2668604':additionmt_2668604,
                                                  'additionms_2668604':additionms_2668604,
                                                  'additionpa_2668604':additionpa_2668604,
                                                  'additioncs_2668604':additioncs_2668604,
                                                  'additionps_2668604':additionps_2668604,
                                                  
                                                  'total_2668605':total_2668605,
                                                  'additionpr_2668605':additionpr_2668605,
                                                  'additionpe_2668605':additionpe_2668605,
                                                  'additionsk_2668605':additionsk_2668605,
                                                  'additionmt_2668605':additionmt_2668605,
                                                  'additionms_2668605':additionms_2668605,
                                                  'additionpa_2668605':additionpa_2668605,
                                                  'additioncs_2668605':additioncs_2668605,
                                                  'additionps_2668605':additionps_2668605})


############################# ic6_report_2668601 function for report build ###############################
def ic6_report_2668601(request):
    if request.method == "POST":
        sem = 'IMCA-6 SEM'
        count = count_ic6
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic6*100)/whole_sem_score
        highest_score = max(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        lowest_score = min(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=6).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=66).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic6*100)/max_all_score
        pr_total_fac = additionpr_2668601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic6*100)/max_all_score
        pe_total_fac = additionpe_2668601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic6*100)/max_all_score
        sk_total_fac = additionsk_2668601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic6*100)/max_all_score
        mt_total_fac = additionmt_2668601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic6*100)/max_all_score
        ms_total_fac = additionms_2668601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic6*100)/max_all_score
        pa_total_fac = additionpa_2668601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic6*100)/max_all_score
        cs_total_fac = additioncs_2668601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic6*100)/max_all_score
        ps_total_fac = additionps_2668601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic6_report_2668602 function for report build ###############################
def ic6_report_2668602(request):
    if request.method == "POST":
        sem = 'IMCA-6 SEM'
        count = count_ic6
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic6*100)/whole_sem_score
        highest_score = max(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        lowest_score = min(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=6).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=66).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic6*100)/max_all_score
        pr_total_fac = additionpr_2668602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic6*100)/max_all_score
        pe_total_fac = additionpe_2668602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic6*100)/max_all_score
        sk_total_fac = additionsk_2668602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic6*100)/max_all_score
        mt_total_fac = additionmt_2668602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic6*100)/max_all_score
        ms_total_fac = additionms_2668602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic6*100)/max_all_score
        pa_total_fac = additionpa_2668602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic6*100)/max_all_score
        cs_total_fac = additioncs_2668602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic6*100)/max_all_score
        ps_total_fac = additionps_2668602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic6_report_2668603 function for report build ###########################
def ic6_report_2668603(request):
    if request.method == "POST":
        sem = 'IMCA-6 SEM'
        count = count_ic6
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic6*100)/whole_sem_score
        highest_score = max(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        lowest_score = min(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=6).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=66).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic6*100)/max_all_score
        pr_total_fac = additionpr_2668603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic6*100)/max_all_score
        pe_total_fac = additionpe_2668603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic6*100)/max_all_score
        sk_total_fac = additionsk_2668603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic6*100)/max_all_score
        mt_total_fac = additionmt_2668603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic6*100)/max_all_score
        ms_total_fac = additionms_2668603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic6*100)/max_all_score
        pa_total_fac = additionpa_2668603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic6*100)/max_all_score
        cs_total_fac = additioncs_2668603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic6*100)/max_all_score
        ps_total_fac = additionps_2668603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic6_report_2668604 function for report build ##############################
def ic6_report_2668604(request):
    if request.method == "POST":
        sem = 'IMCA-6 SEM'
        count = count_ic6
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic6*100)/whole_sem_score
        highest_score = max(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        lowest_score = min(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=6).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=66).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic6*100)/max_all_score
        pr_total_fac = additionpr_2668604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic6*100)/max_all_score
        pe_total_fac = additionpe_2668604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic6*100)/max_all_score
        sk_total_fac = additionsk_2668604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic6*100)/max_all_score
        mt_total_fac = additionmt_2668604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic6*100)/max_all_score
        ms_total_fac = additionms_2668604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic6*100)/max_all_score
        pa_total_fac = additionpa_2668604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic6*100)/max_all_score
        cs_total_fac = additioncs_2668604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic6*100)/max_all_score
        ps_total_fac = additionps_2668604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic6_report_2668605 function for report build ###############################
def ic6_report_2668605(request):
    if request.method == "POST":
        sem = 'IMCA-6 SEM'
        count = count_ic6
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic6*100)/whole_sem_score
        highest_score = max(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        lowest_score = min(total_2668601['total'], total_2668602['total'], total_2668603['total'], total_2668604['total'], total_2668605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=6).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=66).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic6*100)/max_all_score
        pr_total_fac = additionpr_2668605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic6*100)/max_all_score
        pe_total_fac = additionpe_2668605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic6*100)/max_all_score
        sk_total_fac = additionsk_2668605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic6*100)/max_all_score
        mt_total_fac = additionmt_2668605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic6*100)/max_all_score
        ms_total_fac = additionms_2668605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic6*100)/max_all_score
        pa_total_fac = additionpa_2668605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic6*100)/max_all_score
        cs_total_fac = additioncs_2668605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic6*100)/max_all_score
        ps_total_fac = additionps_2668605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

         ###########################################################################################
"""----------------------------------- all functions for Imca-6 Complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-7 ----------------------------------------"""   

#ic7 faculty fetch
def ic7(request):
    sub = Lecturer.objects.filter(id=7).values()
    faculty_name_ic7 = Lecturer.objects.filter(id=77).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA7.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic7':faculty_name_ic7})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
    

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC7 ML 2678601 function for feedback insert
def ic7_2678601(request):  
    if request.method == "POST":  
        form = Ic7_2678601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic7_2678601_Form()  
    return render(request,'IMCA7.html',{'form':form})

##IC7 AMP 2678602 function for feedback insert
def ic7_2678602(request):  
    if request.method == "POST":  
        form = Ic7_2678602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic7_2678602_Form()  
    return render(request,'IMCA7.html',{'form':form})

##IC7 CS 2678603 function for feedback insert
def ic7_2678603(request):  
    if request.method == "POST":  
        form = Ic7_2678603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic7_2678603_Form()  
    return render(request,'IMCA7.html',{'form':form})

##IC7 SP 2678604 function for feedback insert
def ic7_2678604(request):  
    if request.method == "POST":  
        form = Ic7_2678604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic7_2678604_Form()  
    return render(request,'IMCA7.html',{'form':form})

##IC7 BCT 2678605 function for feedback insert
def ic7_2678605(request):  
    if request.method == "POST":  
        form = Ic7_2678605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic7_2678605_Form()  
    return render(request,'IMCA7.html',{'form':form})

def successic7(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic7 Main function for insert ############################
def ic7_main(request):
    if request.method == "POST":
        ic7_2678601(request)
        ic7_2678602(request)
        ic7_2678603(request)
        ic7_2678604(request)
        ic7_2678605(request)
        return render(request,'Success.html')
    
################################### Delete IMCA7 Database #############################################
def delete_dbs_ic7(request):
    if request.method == "POST":
        Ic7_2678601.objects.all().delete()
        ic7_2678601 = Ic7_2678601(std_id=0, pr2678601=0, pe2678601=0, sk2678601=0, mt2678601=0, ms2678601=0, pa2678601=0, cs2678601=0, ps2678601=0)
        ic7_2678601.save()
        
        Ic7_2678602.objects.all().delete()
        ic7_2678602 = Ic7_2678602(std_id=0, pr2678602=0, pe2678602=0, sk2678602=0, mt2678602=0, ms2678602=0, pa2678602=0, cs2678602=0, ps2678602=0)
        ic7_2678602.save()    
        
        Ic7_2678603.objects.all().delete()
        ic7_2678603 = Ic7_2678603(std_id=0, pr2678603=0, pe2678603=0, sk2678603=0, mt2678603=0, ms2678603=0, pa2678603=0, cs2678603=0, ps2678603=0)
        ic7_2678603.save()  
          
        Ic7_2678604.objects.all().delete()
        ic7_2678604 = Ic7_2678604(std_id=0, pr2678604=0, pe2678604=0, sk2678604=0, mt2678604=0, ms2678604=0, pa2678604=0, cs2678604=0, ps2678604=0)
        ic7_2678604.save()
          
        Ic7_2678605.objects.all().delete()
        ic7_2678605 = Ic7_2678605(std_id=0, pr2678605=0, pe2678605=0, sk2678605=0, mt2678605=0, ms2678605=0, pa2678605=0, cs2678605=0, ps2678605=0)
        ic7_2678605.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# imca7 total function ####################################
def imca7total(request):
    if request.method == "POST":
        faculty_name_ic7 = Lecturer.objects.filter(id=77).values()
        sub = Lecturer.objects.filter(id=7).values()
        return render(request,'imca7total.html', {'sub':sub,
                                                  'faculty_name_ic7':faculty_name_ic7,
                                                  'all_total_ic7':all_total_ic7,
                                                  'count_ic7':count_ic7,
                                                  'totalpr_ic7':totalpr_ic7,
                                                  'totalpe_ic7':totalpe_ic7,
                                                  'totalsk_ic7':totalsk_ic7,
                                                  'totalmt_ic7':totalmt_ic7,
                                                  'totalms_ic7':totalms_ic7,
                                                  'totalpa_ic7':totalpa_ic7,
                                                  'totalcs_ic7':totalcs_ic7,
                                                  'totalps_ic7':totalps_ic7,
                                                  
                                                  'total_2678601':total_2678601,
                                                  'additionpr_2678601':additionpr_2678601,
                                                  'additionpe_2678601':additionpe_2678601,
                                                  'additionsk_2678601':additionsk_2678601,
                                                  'additionmt_2678601':additionmt_2678601,
                                                  'additionms_2678601':additionms_2678601,
                                                  'additionpa_2678601':additionpa_2678601,
                                                  'additioncs_2678601':additioncs_2678601,
                                                  'additionps_2678601':additionps_2678601,
                                                  
                                                  'total_2678602':total_2678602,
                                                  'additionpr_2678602':additionpr_2678602,
                                                  'additionpe_2678602':additionpe_2678602,
                                                  'additionsk_2678602':additionsk_2678602,
                                                  'additionmt_2678602':additionmt_2678602,
                                                  'additionms_2678602':additionms_2678602,
                                                  'additionpa_2678602':additionpa_2678602,
                                                  'additioncs_2678602':additioncs_2678602,
                                                  'additionps_2678602':additionps_2678602,
                                                  
                                                  'total_2678603':total_2678603,
                                                  'additionpr_2678603':additionpr_2678603,
                                                  'additionpe_2678603':additionpe_2678603,
                                                  'additionsk_2678603':additionsk_2678603,
                                                  'additionmt_2678603':additionmt_2678603,
                                                  'additionms_2678603':additionms_2678603,
                                                  'additionpa_2678603':additionpa_2678603,
                                                  'additioncs_2678603':additioncs_2678603,
                                                  'additionps_2678603':additionps_2678603,
                                                  
                                                  'total_2678604':total_2678604,
                                                  'additionpr_2678604':additionpr_2678604,
                                                  'additionpe_2678604':additionpe_2678604,
                                                  'additionsk_2678604':additionsk_2678604,
                                                  'additionmt_2678604':additionmt_2678604,
                                                  'additionms_2678604':additionms_2678604,
                                                  'additionpa_2678604':additionpa_2678604,
                                                  'additioncs_2678604':additioncs_2678604,
                                                  'additionps_2678604':additionps_2678604,
                                                  
                                                  'total_2678605':total_2678605,
                                                  'additionpr_2678605':additionpr_2678605,
                                                  'additionpe_2678605':additionpe_2678605,
                                                  'additionsk_2678605':additionsk_2678605,
                                                  'additionmt_2678605':additionmt_2678605,
                                                  'additionms_2678605':additionms_2678605,
                                                  'additionpa_2678605':additionpa_2678605,
                                                  'additioncs_2678605':additioncs_2678605,
                                                  'additionps_2678605':additionps_2678605})
        





    



############################# ic7_report_2678601 function for report build ###############################
def ic7_report_2678601(request):
    if request.method == "POST":
        sem = 'IMCA-7 SEM'
        count = count_ic7
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic7*100)/whole_sem_score
        highest_score = max(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        lowest_score = min(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=7).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=77).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic7*100)/max_all_score
        pr_total_fac = additionpr_2678601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic7*100)/max_all_score
        pe_total_fac = additionpe_2678601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic7*100)/max_all_score
        sk_total_fac = additionsk_2678601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic7*100)/max_all_score
        mt_total_fac = additionmt_2678601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic7*100)/max_all_score
        ms_total_fac = additionms_2678601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic7*100)/max_all_score
        pa_total_fac = additionpa_2678601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic7*100)/max_all_score
        cs_total_fac = additioncs_2678601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic7*100)/max_all_score
        ps_total_fac = additionps_2678601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic7_report_2678602 function for report build ###############################
def ic7_report_2678602(request):
    if request.method == "POST":
        sem = 'IMCA-7 SEM'
        count = count_ic7
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic7*100)/whole_sem_score
        highest_score = max(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        lowest_score = min(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=7).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=77).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic7*100)/max_all_score
        pr_total_fac = additionpr_2678602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic7*100)/max_all_score
        pe_total_fac = additionpe_2678602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic7*100)/max_all_score
        sk_total_fac = additionsk_2678602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic7*100)/max_all_score
        mt_total_fac = additionmt_2678602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic7*100)/max_all_score
        ms_total_fac = additionms_2678602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic7*100)/max_all_score
        pa_total_fac = additionpa_2678602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic7*100)/max_all_score
        cs_total_fac = additioncs_2678602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic7*100)/max_all_score
        ps_total_fac = additionps_2678602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic7_report_2678603 function for report build ###########################
def ic7_report_2678603(request):
    if request.method == "POST":
        sem = 'IMCA-7 SEM'
        count = count_ic7
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic7*100)/whole_sem_score
        highest_score = max(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        lowest_score = min(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=7).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=77).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic7*100)/max_all_score
        pr_total_fac = additionpr_2678603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic7*100)/max_all_score
        pe_total_fac = additionpe_2678603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic7*100)/max_all_score
        sk_total_fac = additionsk_2678603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic7*100)/max_all_score
        mt_total_fac = additionmt_2678603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic7*100)/max_all_score
        ms_total_fac = additionms_2678603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic7*100)/max_all_score
        pa_total_fac = additionpa_2678603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic7*100)/max_all_score
        cs_total_fac = additioncs_2678603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic7*100)/max_all_score
        ps_total_fac = additionps_2678603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic7_report_2678604 function for report build ##############################
def ic7_report_2678604(request):
    if request.method == "POST":
        sem = 'IMCA-7 SEM'
        count = count_ic7
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic7*100)/whole_sem_score
        highest_score = max(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        lowest_score = min(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=7).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=77).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic7*100)/max_all_score
        pr_total_fac = additionpr_2678604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic7*100)/max_all_score
        pe_total_fac = additionpe_2678604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic7*100)/max_all_score
        sk_total_fac = additionsk_2678604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic7*100)/max_all_score
        mt_total_fac = additionmt_2678604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic7*100)/max_all_score
        ms_total_fac = additionms_2678604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic7*100)/max_all_score
        pa_total_fac = additionpa_2678604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic7*100)/max_all_score
        cs_total_fac = additioncs_2678604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic7*100)/max_all_score
        ps_total_fac = additionps_2678604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic7_report_2678605 function for report build ###############################
def ic7_report_2678605(request):
    if request.method == "POST":
        sem = 'IMCA-7 SEM'
        count = count_ic7
        total_sub = 5
        total_faculty = 5
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic7*100)/whole_sem_score
        highest_score = max(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        lowest_score = min(total_2678601['total'], total_2678602['total'], total_2678603['total'], total_2678604['total'], total_2678605['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=7).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=77).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic7*100)/max_all_score
        pr_total_fac = additionpr_2678605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic7*100)/max_all_score
        pe_total_fac = additionpe_2678605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic7*100)/max_all_score
        sk_total_fac = additionsk_2678605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic7*100)/max_all_score
        mt_total_fac = additionmt_2678605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic7*100)/max_all_score
        ms_total_fac = additionms_2678605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic7*100)/max_all_score
        pa_total_fac = additionpa_2678605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic7*100)/max_all_score
        cs_total_fac = additioncs_2678605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic7*100)/max_all_score
        ps_total_fac = additionps_2678605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

         ###########################################################################################
"""----------------------------------- all functions for Imca-7 Complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-8 ----------------------------------------"""   

#ic8 faculty fetch
def ic8(request):
    sub = Lecturer.objects.filter(id=8).values()
    faculty_name_ic8 = Lecturer.objects.filter(id=88).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA8.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic8':faculty_name_ic8})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))
    

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC8 BDA 2688601 function for feedback insert
def ic8_2688601(request):  
    if request.method == "POST":  
        form = Ic8_2688601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic8_2688601_Form()  
    return render(request,'IMCA8.html',{'form':form})

##IC8 AML 2688602 function for feedback insert
def ic8_2688602(request):  
    if request.method == "POST":  
        form = Ic8_2688602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic8_2688602_Form()  
    return render(request,'IMCA8.html',{'form':form})

##IC8 DAA 2688603 function for feedback insert
def ic8_2688603(request):  
    if request.method == "POST":  
        form = Ic8_2688603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic8_2688603_Form()  
    return render(request,'IMCA8.html',{'form':form})

##IC8 TW 2688604 function for feedback insert
def ic8_2688604(request):  
    if request.method == "POST":  
        form = Ic8_2688604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic8_2688604_Form()  
    return render(request,'IMCA8.html',{'form':form})

##IC8 SP 2688605 function for feedback insert
def ic8_2688605(request):  
    if request.method == "POST":  
        form = Ic8_2688605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic8_2688605_Form()  
    return render(request,'IMCA8.html',{'form':form})

##IC8 CF 2688607 function for feedback insert
def ic8_2688607(request):
    if request.method == "POST": 
        form = Ic8_2688607_Form(request.POST)
        if form.is_valid():
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic8_2688607_Form()  
    return render(request,'IMCA8.html',{'form':form})

def successic8(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic8 Main function for insert ############################
def ic8_main(request):
    if request.method == "POST":
        ic8_2688601(request)
        ic8_2688602(request)
        ic8_2688603(request)
        ic8_2688604(request)
        ic8_2688605(request)
        ic8_2688607(request)
        return render(request,'Success.html')
    
################################### Delete IMCA8 Database #############################################
def delete_dbs_ic8(request):
    if request.method == "POST":
        Ic8_2688601.objects.all().delete()
        ic8_2688601 = Ic8_2688601(std_id=0, pr2688601=0, pe2688601=0, sk2688601=0, mt2688601=0, ms2688601=0, pa2688601=0, cs2688601=0, ps2688601=0)
        ic8_2688601.save()
        
        Ic8_2688602.objects.all().delete()
        ic8_2688602 = Ic8_2688602(std_id=0, pr2688602=0, pe2688602=0, sk2688602=0, mt2688602=0, ms2688602=0, pa2688602=0, cs2688602=0, ps2688602=0)
        ic8_2688602.save()    
        
        Ic8_2688603.objects.all().delete()
        ic8_2688603 = Ic8_2688603(std_id=0, pr2688603=0, pe2688603=0, sk2688603=0, mt2688603=0, ms2688603=0, pa2688603=0, cs2688603=0, ps2688603=0)
        ic8_2688603.save()  
          
        Ic8_2688604.objects.all().delete()
        ic8_2688604 = Ic8_2688604(std_id=0, pr2688604=0, pe2688604=0, sk2688604=0, mt2688604=0, ms2688604=0, pa2688604=0, cs2688604=0, ps2688604=0)
        ic8_2688604.save()
          
        Ic8_2688605.objects.all().delete()
        ic8_2688605 = Ic8_2688605(std_id=0, pr2688605=0, pe2688605=0, sk2688605=0, mt2688605=0, ms2688605=0, pa2688605=0, cs2688605=0, ps2688605=0)
        ic8_2688605.save()

        Ic8_2688607.objects.all().delete()
        ic8_2688607 = Ic8_2688607(std_id=0, pr2688607=0, pe2688607=0, sk2688607=0, mt2688607=0, ms2688607=0, pa2688607=0, cs2688607=0, ps2688607=0)
        ic8_2688607.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})

################################# imca8 total function ####################################
def imca8total(request):
    if request.method == "POST":
        faculty_name_ic8 = Lecturer.objects.filter(id=88).values()
        sub = Lecturer.objects.filter(id=8).values()
        return render(request,'imca8total.html', {'sub':sub,
                                                  'faculty_name_ic8':faculty_name_ic8,
                                                  'all_total_ic8':all_total_ic8,
                                                  'count_ic8':count_ic8,
                                                  'totalpr_ic8':totalpr_ic8,
                                                  'totalpe_ic8':totalpe_ic8,
                                                  'totalsk_ic8':totalsk_ic8,
                                                  'totalmt_ic8':totalmt_ic8,
                                                  'totalms_ic8':totalms_ic8,
                                                  'totalpa_ic8':totalpa_ic8,
                                                  'totalcs_ic8':totalcs_ic8,
                                                  'totalps_ic8':totalps_ic8,
                                                  
                                                  'total_2688601':total_2688601,
                                                  'additionpr_2688601':additionpr_2688601,
                                                  'additionpe_2688601':additionpe_2688601,
                                                  'additionsk_2688601':additionsk_2688601,
                                                  'additionmt_2688601':additionmt_2688601,
                                                  'additionms_2688601':additionms_2688601,
                                                  'additionpa_2688601':additionpa_2688601,
                                                  'additioncs_2688601':additioncs_2688601,
                                                  'additionps_2688601':additionps_2688601,
                                                  
                                                  'total_2688602':total_2688602,
                                                  'additionpr_2688602':additionpr_2688602,
                                                  'additionpe_2688602':additionpe_2688602,
                                                  'additionsk_2688602':additionsk_2688602,
                                                  'additionmt_2688602':additionmt_2688602,
                                                  'additionms_2688602':additionms_2688602,
                                                  'additionpa_2688602':additionpa_2688602,
                                                  'additioncs_2688602':additioncs_2688602,
                                                  'additionps_2688602':additionps_2688602,
                                                  
                                                  'total_2688603':total_2688603,
                                                  'additionpr_2688603':additionpr_2688603,
                                                  'additionpe_2688603':additionpe_2688603,
                                                  'additionsk_2688603':additionsk_2688603,
                                                  'additionmt_2688603':additionmt_2688603,
                                                  'additionms_2688603':additionms_2688603,
                                                  'additionpa_2688603':additionpa_2688603,
                                                  'additioncs_2688603':additioncs_2688603,
                                                  'additionps_2688603':additionps_2688603,
                                                  
                                                  'total_2688604':total_2688604,
                                                  'additionpr_2688604':additionpr_2688604,
                                                  'additionpe_2688604':additionpe_2688604,
                                                  'additionsk_2688604':additionsk_2688604,
                                                  'additionmt_2688604':additionmt_2688604,
                                                  'additionms_2688604':additionms_2688604,
                                                  'additionpa_2688604':additionpa_2688604,
                                                  'additioncs_2688604':additioncs_2688604,
                                                  'additionps_2688604':additionps_2688604,
                                                  
                                                  'total_2688605':total_2688605,
                                                  'additionpr_2688605':additionpr_2688605,
                                                  'additionpe_2688605':additionpe_2688605,
                                                  'additionsk_2688605':additionsk_2688605,
                                                  'additionmt_2688605':additionmt_2688605,
                                                  'additionms_2688605':additionms_2688605,
                                                  'additionpa_2688605':additionpa_2688605,
                                                  'additioncs_2688605':additioncs_2688605,
                                                  'additionps_2688605':additionps_2688605,
                                                
                                                  'total_2688607':total_2688607,
                                                  'additionpr_2688607':additionpr_2688607,
                                                  'additionpe_2688607':additionpe_2688607,
                                                  'additionsk_2688607':additionsk_2688607,
                                                  'additionmt_2688607':additionmt_2688607,
                                                  'additionms_2688607':additionms_2688607,
                                                  'additionpa_2688607':additionpa_2688607,
                                                  'additioncs_2688607':additioncs_2688607,
                                                  'additionps_2688607':additionps_2688607})
        
############################# ic8_report_2688601 function for report build ###############################
def ic8_report_2688601(request):
    if request.method == "POST":
        sem = 'IMCA-8 SEM'
        count = count_ic8
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic8*100)/whole_sem_score
        highest_score = max(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        lowest_score = min(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=8).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=88).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic8*100)/max_all_score
        pr_total_fac = additionpr_2688601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic8*100)/max_all_score
        pe_total_fac = additionpe_2688601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic8*100)/max_all_score
        sk_total_fac = additionsk_2688601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic8*100)/max_all_score
        mt_total_fac = additionmt_2688601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic8*100)/max_all_score
        ms_total_fac = additionms_2688601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic8*100)/max_all_score
        pa_total_fac = additionpa_2688601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic8*100)/max_all_score
        cs_total_fac = additioncs_2688601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic8*100)/max_all_score
        ps_total_fac = additionps_2688601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic8_report_2688602 function for report build ###############################
def ic8_report_2688602(request):
    if request.method == "POST":
        sem = 'IMCA-8 SEM'
        count = count_ic8
        total_sub = 5 #for rating
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic8*100)/whole_sem_score
        highest_score = max(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        lowest_score = min(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=8).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=88).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic8*100)/max_all_score
        pr_total_fac = additionpr_2688602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic8*100)/max_all_score
        pe_total_fac = additionpe_2688602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic8*100)/max_all_score
        sk_total_fac = additionsk_2688602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic8*100)/max_all_score
        mt_total_fac = additionmt_2688602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic8*100)/max_all_score
        ms_total_fac = additionms_2688602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic8*100)/max_all_score
        pa_total_fac = additionpa_2688602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic8*100)/max_all_score
        cs_total_fac = additioncs_2688602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic8*100)/max_all_score
        ps_total_fac = additionps_2688602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic8_report_2688603 function for report build ###########################
def ic8_report_2688603(request):
    if request.method == "POST":
        sem = 'IMCA-8 SEM'
        count = count_ic8
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic8*100)/whole_sem_score
        highest_score = max(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        lowest_score = min(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=8).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=88).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic8*100)/max_all_score
        pr_total_fac = additionpr_2688603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic8*100)/max_all_score
        pe_total_fac = additionpe_2688603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic8*100)/max_all_score
        sk_total_fac = additionsk_2688603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic8*100)/max_all_score
        mt_total_fac = additionmt_2688603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic8*100)/max_all_score
        ms_total_fac = additionms_2688603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic8*100)/max_all_score
        pa_total_fac = additionpa_2688603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic8*100)/max_all_score
        cs_total_fac = additioncs_2688603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic8*100)/max_all_score
        ps_total_fac = additionps_2688603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic8_report_2688604 function for report build ##############################
def ic8_report_2688604(request):
    if request.method == "POST":
        sem = 'IMCA-8 SEM'
        count = count_ic8
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic8*100)/whole_sem_score
        highest_score = max(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        lowest_score = min(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=8).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=88).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic8*100)/max_all_score
        pr_total_fac = additionpr_2688604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic8*100)/max_all_score
        pe_total_fac = additionpe_2688604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic8*100)/max_all_score
        sk_total_fac = additionsk_2688604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic8*100)/max_all_score
        mt_total_fac = additionmt_2688604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic8*100)/max_all_score
        ms_total_fac = additionms_2688604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic8*100)/max_all_score
        pa_total_fac = additionpa_2688604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic8*100)/max_all_score
        cs_total_fac = additioncs_2688604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic8*100)/max_all_score
        ps_total_fac = additionps_2688604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic8_report_2688605 function for report build ###############################
def ic8_report_2688605(request):
    if request.method == "POST":
        sem = 'IMCA-8 SEM'
        count = count_ic8
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic8*100)/whole_sem_score
        highest_score = max(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        lowest_score = min(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=8).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=88).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic8*100)/max_all_score
        pr_total_fac = additionpr_2688605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic8*100)/max_all_score
        pe_total_fac = additionpe_2688605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic8*100)/max_all_score
        sk_total_fac = additionsk_2688605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic8*100)/max_all_score
        mt_total_fac = additionmt_2688605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic8*100)/max_all_score
        ms_total_fac = additionms_2688605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic8*100)/max_all_score
        pa_total_fac = additionpa_2688605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic8*100)/max_all_score
        cs_total_fac = additioncs_2688605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic8*100)/max_all_score
        ps_total_fac = additionps_2688605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

################################ ic8_report_2688607 function for report build ###############################
def ic8_report_2688607(request):
    if request.method == "POST":
        sem = 'IMCA-8 SEM'
        count = count_ic8
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic8*100)/whole_sem_score
        highest_score = max(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        lowest_score = min(total_2688601['total'], total_2688602['total'], total_2688603['total'], total_2688604['total'], total_2688605['total'], total_2688607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=8).values()[0]['subject6']
        
        #prof name
        prof = Lecturer.objects.filter(id=88).values()[0]['subject6']
        
        #PR calculation
        average_pr_all = (totalpr_ic8*100)/max_all_score
        pr_total_fac = additionpr_2688607['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic8*100)/max_all_score
        pe_total_fac = additionpe_2688607['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic8*100)/max_all_score
        sk_total_fac = additionsk_2688607['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic8*100)/max_all_score
        mt_total_fac = additionmt_2688607['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic8*100)/max_all_score
        ms_total_fac = additionms_2688607['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic8*100)/max_all_score
        pa_total_fac = additionpa_2688607['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic8*100)/max_all_score
        cs_total_fac = additioncs_2688607['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic8*100)/max_all_score
        ps_total_fac = additionps_2688607['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
                                              
         ###########################################################################################
"""----------------------------------- all functions for Imca-8 Complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-9 ----------------------------------------"""   

#ic9 faculty fetch
def ic9(request):
    sub = Lecturer.objects.filter(id=9).values()
    faculty_name_ic9 = Lecturer.objects.filter(id=99).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA9.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic9':faculty_name_ic9})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC9 DP 2698601 function for feedback insert
def ic9_2698601(request):  
    if request.method == "POST":  
        form = Ic9_2698601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic9_2698601_Form()  
    return render(request,'IMCA9.html',{'form':form})

##IC9 FSD 2698602 function for feedback insert
def ic9_2698602(request):  
    if request.method == "POST":  
        form = Ic9_2698602_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic9_2698602_Form()  
    return render(request,'IMCA9.html',{'form':form})

##IC9 EIC 2698603 function for feedback insert
def ic9_2698603(request):  
    if request.method == "POST":  
        form = Ic9_2698603_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic9_2698603_Form()  
    return render(request,'IMCA9.html',{'form':form})

##IC9 PM 2698604 function for feedback insert
def ic9_2698604(request):  
    if request.method == "POST":  
        form = Ic9_2698604_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Ic9_2698604_Form()  
    return render(request,'IMCA9.html',{'form':form})

##IC9 SP 2698605 function for feedback insert
def ic9_2698605(request):  
    if request.method == "POST":  
        form = Ic9_2698605_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic9_2698605_Form()  
    return render(request,'IMCA9.html',{'form':form})

##IC9 IOT 2698607 function for feedback insert
def ic9_2698607(request):
    if request.method == "POST": 
        form = Ic9_2698607_Form(request.POST)
        if form.is_valid():
            try:
                form.save(commit=True)
            except:
                pass
    form = Ic9_2698607_Form()  
    return render(request,'IMCA9.html',{'form':form})

def successic9(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic9 Main function for insert ############################
def ic9_main(request):
    if request.method == "POST":
        ic9_2698601(request)
        ic9_2698602(request)
        ic9_2698603(request)
        ic9_2698604(request)
        ic9_2698605(request)
        ic9_2698607(request)
        return render(request,'Success.html')

################################### Delete IMCA9 Database #############################################
def delete_dbs_ic9(request):
    if request.method == "POST":
        Ic9_2698601.objects.all().delete()
        ic9_2698601 = Ic9_2698601(std_id=0, pr2698601=0, pe2698601=0, sk2698601=0, mt2698601=0, ms2698601=0, pa2698601=0, cs2698601=0, ps2698601=0)
        ic9_2698601.save()
        
        Ic9_2698602.objects.all().delete()
        ic9_2698602 = Ic9_2698602(std_id=0, pr2698602=0, pe2698602=0, sk2698602=0, mt2698602=0, ms2698602=0, pa2698602=0, cs2698602=0, ps2698602=0)
        ic9_2698602.save()    
        
        Ic9_2698603.objects.all().delete()
        ic9_2698603 = Ic9_2698603(std_id=0, pr2698603=0, pe2698603=0, sk2698603=0, mt2698603=0, ms2698603=0, pa2698603=0, cs2698603=0, ps2698603=0)
        ic9_2698603.save()  
          
        Ic9_2698604.objects.all().delete()
        ic9_2698604 = Ic9_2698604(std_id=0, pr2698604=0, pe2698604=0, sk2698604=0, mt2698604=0, ms2698604=0, pa2698604=0, cs2698604=0, ps2698604=0)
        ic9_2698604.save()
          
        Ic9_2698605.objects.all().delete()
        ic9_2698605 = Ic9_2698605(std_id=0, pr2698605=0, pe2698605=0, sk2698605=0, mt2698605=0, ms2698605=0, pa2698605=0, cs2698605=0, ps2698605=0)
        ic9_2698605.save()

        Ic9_2698607.objects.all().delete()
        ic9_2698607 = Ic9_2698607(std_id=0, pr2698607=0, pe2698607=0, sk2698607=0, mt2698607=0, ms2698607=0, pa2698607=0, cs2698607=0, ps2698607=0)
        ic9_2698607.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})

################################# imca9 total function ####################################
def imca9total(request):
    if request.method == "POST":
        faculty_name_ic9 = Lecturer.objects.filter(id=99).values()
        sub = Lecturer.objects.filter(id=9).values()
        return render(request,'imca9total.html', {'sub':sub,
                                                  'faculty_name_ic9':faculty_name_ic9,
                                                  'all_total_ic9':all_total_ic9,
                                                  'count_ic9':count_ic9,
                                                  'totalpr_ic9':totalpr_ic9,
                                                  'totalpe_ic9':totalpe_ic9,
                                                  'totalsk_ic9':totalsk_ic9,
                                                  'totalmt_ic9':totalmt_ic9,
                                                  'totalms_ic9':totalms_ic9,
                                                  'totalpa_ic9':totalpa_ic9,
                                                  'totalcs_ic9':totalcs_ic9,
                                                  'totalps_ic9':totalps_ic9,
                                                  
                                                  'total_2698601':total_2698601,
                                                  'additionpr_2698601':additionpr_2698601,
                                                  'additionpe_2698601':additionpe_2698601,
                                                  'additionsk_2698601':additionsk_2698601,
                                                  'additionmt_2698601':additionmt_2698601,
                                                  'additionms_2698601':additionms_2698601,
                                                  'additionpa_2698601':additionpa_2698601,
                                                  'additioncs_2698601':additioncs_2698601,
                                                  'additionps_2698601':additionps_2698601,
                                                  
                                                  'total_2698602':total_2698602,
                                                  'additionpr_2698602':additionpr_2698602,
                                                  'additionpe_2698602':additionpe_2698602,
                                                  'additionsk_2698602':additionsk_2698602,
                                                  'additionmt_2698602':additionmt_2698602,
                                                  'additionms_2698602':additionms_2698602,
                                                  'additionpa_2698602':additionpa_2698602,
                                                  'additioncs_2698602':additioncs_2698602,
                                                  'additionps_2698602':additionps_2698602,
                                                  
                                                  'total_2698603':total_2698603,
                                                  'additionpr_2698603':additionpr_2698603,
                                                  'additionpe_2698603':additionpe_2698603,
                                                  'additionsk_2698603':additionsk_2698603,
                                                  'additionmt_2698603':additionmt_2698603,
                                                  'additionms_2698603':additionms_2698603,
                                                  'additionpa_2698603':additionpa_2698603,
                                                  'additioncs_2698603':additioncs_2698603,
                                                  'additionps_2698603':additionps_2698603,
                                                  
                                                  'total_2698604':total_2698604,
                                                  'additionpr_2698604':additionpr_2698604,
                                                  'additionpe_2698604':additionpe_2698604,
                                                  'additionsk_2698604':additionsk_2698604,
                                                  'additionmt_2698604':additionmt_2698604,
                                                  'additionms_2698604':additionms_2698604,
                                                  'additionpa_2698604':additionpa_2698604,
                                                  'additioncs_2698604':additioncs_2698604,
                                                  'additionps_2698604':additionps_2698604,
                                                  
                                                  'total_2698605':total_2698605,
                                                  'additionpr_2698605':additionpr_2698605,
                                                  'additionpe_2698605':additionpe_2698605,
                                                  'additionsk_2698605':additionsk_2698605,
                                                  'additionmt_2698605':additionmt_2698605,
                                                  'additionms_2698605':additionms_2698605,
                                                  'additionpa_2698605':additionpa_2698605,
                                                  'additioncs_2698605':additioncs_2698605,
                                                  'additionps_2698605':additionps_2698605,
                                                
                                                  'total_2698607':total_2698607,
                                                  'additionpr_2698607':additionpr_2698607,
                                                  'additionpe_2698607':additionpe_2698607,
                                                  'additionsk_2698607':additionsk_2698607,
                                                  'additionmt_2698607':additionmt_2698607,
                                                  'additionms_2698607':additionms_2698607,
                                                  'additionpa_2698607':additionpa_2698607,
                                                  'additioncs_2698607':additioncs_2698607,
                                                  'additionps_2698607':additionps_2698607})
                
############################# ic9_report_2698601 function for report build ###############################
def ic9_report_2698601(request):
    if request.method == "POST":
        sem = 'IMCA-9 SEM'
        count = count_ic9
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic9*100)/whole_sem_score
        highest_score = max(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        lowest_score = min(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=9).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=99).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic9*100)/max_all_score
        pr_total_fac = additionpr_2698601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic9*100)/max_all_score
        pe_total_fac = additionpe_2698601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic9*100)/max_all_score
        sk_total_fac = additionsk_2698601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic9*100)/max_all_score
        mt_total_fac = additionmt_2698601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic9*100)/max_all_score
        ms_total_fac = additionms_2698601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic9*100)/max_all_score
        pa_total_fac = additionpa_2698601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic9*100)/max_all_score
        cs_total_fac = additioncs_2698601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic9*100)/max_all_score
        ps_total_fac = additionps_2698601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# ic9_report_2698602 function for report build ###############################
def ic9_report_2698602(request):
    if request.method == "POST":
        sem = 'IMCA-9 SEM'
        count = count_ic9
        total_sub = 5 #for rating
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic9*100)/whole_sem_score
        highest_score = max(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        lowest_score = min(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=9).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=99).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_ic9*100)/max_all_score
        pr_total_fac = additionpr_2698602['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic9*100)/max_all_score
        pe_total_fac = additionpe_2698602['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic9*100)/max_all_score
        sk_total_fac = additionsk_2698602['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic9*100)/max_all_score
        mt_total_fac = additionmt_2698602['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic9*100)/max_all_score
        ms_total_fac = additionms_2698602['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic9*100)/max_all_score
        pa_total_fac = additionpa_2698602['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic9*100)/max_all_score
        cs_total_fac = additioncs_2698602['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic9*100)/max_all_score
        ps_total_fac = additionps_2698602['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ ic9_report_2698603 function for report build ###########################
def ic9_report_2698603(request):
    if request.method == "POST":
        sem = 'IMCA-9 SEM'
        count = count_ic9
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic9*100)/whole_sem_score
        highest_score = max(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        lowest_score = min(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=9).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=99).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_ic9*100)/max_all_score
        pr_total_fac = additionpr_2698603['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic9*100)/max_all_score
        pe_total_fac = additionpe_2698603['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic9*100)/max_all_score
        sk_total_fac = additionsk_2698603['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic9*100)/max_all_score
        mt_total_fac = additionmt_2698603['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic9*100)/max_all_score
        ms_total_fac = additionms_2698603['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic9*100)/max_all_score
        pa_total_fac = additionpa_2698603['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic9*100)/max_all_score
        cs_total_fac = additioncs_2698603['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic9*100)/max_all_score
        ps_total_fac = additionps_2698603['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### ic9_report_2698604 function for report build ##############################
def ic9_report_2698604(request):
    if request.method == "POST":
        sem = 'IMCA-9 SEM'
        count = count_ic9
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic9*100)/whole_sem_score
        highest_score = max(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        lowest_score = min(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=9).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=99).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_ic9*100)/max_all_score
        pr_total_fac = additionpr_2698604['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic9*100)/max_all_score
        pe_total_fac = additionpe_2698604['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic9*100)/max_all_score
        sk_total_fac = additionsk_2698604['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic9*100)/max_all_score
        mt_total_fac = additionmt_2698604['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic9*100)/max_all_score
        ms_total_fac = additionms_2698604['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic9*100)/max_all_score
        pa_total_fac = additionpa_2698604['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic9*100)/max_all_score
        cs_total_fac = additioncs_2698604['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic9*100)/max_all_score
        ps_total_fac = additionps_2698604['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ ic9_report_2698605 function for report build ###############################
def ic9_report_2698605(request):
    if request.method == "POST":
        sem = 'IMCA-9 SEM'
        count = count_ic9
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic9*100)/whole_sem_score
        highest_score = max(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        lowest_score = min(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=9).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=99).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_ic9*100)/max_all_score
        pr_total_fac = additionpr_2698605['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic9*100)/max_all_score
        pe_total_fac = additionpe_2698605['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic9*100)/max_all_score
        sk_total_fac = additionsk_2698605['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic9*100)/max_all_score
        mt_total_fac = additionmt_2698605['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic9*100)/max_all_score
        ms_total_fac = additionms_2698605['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic9*100)/max_all_score
        pa_total_fac = additionpa_2698605['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic9*100)/max_all_score
        cs_total_fac = additioncs_2698605['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic9*100)/max_all_score
        ps_total_fac = additionps_2698605['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

################################ ic9_report_2698607 function for report build ###############################
def ic9_report_2698607(request):
    if request.method == "POST":
        sem = 'IMCA-9 SEM'
        count = count_ic9
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic9*100)/whole_sem_score
        highest_score = max(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        lowest_score = min(total_2698601['total'], total_2698602['total'], total_2698603['total'], total_2698604['total'], total_2698605['total'], total_2698607['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=9).values()[0]['subject6']
        
        #prof name
        prof = Lecturer.objects.filter(id=99).values()[0]['subject6']
        
        #PR calculation
        average_pr_all = (totalpr_ic9*100)/max_all_score
        pr_total_fac = additionpr_2698607['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic9*100)/max_all_score
        pe_total_fac = additionpe_2698607['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic9*100)/max_all_score
        sk_total_fac = additionsk_2698607['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic9*100)/max_all_score
        mt_total_fac = additionmt_2698607['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic9*100)/max_all_score
        ms_total_fac = additionms_2698607['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic9*100)/max_all_score
        pa_total_fac = additionpa_2698607['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic9*100)/max_all_score
        cs_total_fac = additioncs_2698607['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic9*100)/max_all_score
        ps_total_fac = additionps_2698607['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
                                              
         ###########################################################################################
"""----------------------------------- all functions for Imca-9 Complete ----------------------------------------"""

"""----------------------------------- all functions for Mca-1 ----------------------------------------"""   

#mca1 faculty fetch
def mca1(request):
    sub = Lecturer.objects.filter(id=101).values()
    faculty_name_mca1 = Lecturer.objects.filter(id=1011).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'MCA1.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_mca1':faculty_name_mca1})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))

"""------------------------------------ Feedback Insert --------------------------------------"""
##MCA1 C-LANG 619401 function for feedback insert
def mca1_619401(request):  
    if request.method == "POST":  
        form = Mca1_619401_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Mca1_619401_Form()  
    return render(request,'MCA1.html',{'form':form})

##MCA1 JAVA 619402 function for feedback insert
def mca1_619402(request):  
    if request.method == "POST":  
        form = Mca1_619402_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca1_619402_Form()  
    return render(request,'MCA1.html',{'form':form})

##MCA1 BM 619403 function for feedback insert
def mca1_619403(request):  
    if request.method == "POST":  
        form = Mca1_619403_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca1_619403_Form()  
    return render(request,'MCA1.html',{'form':form})

##MCA1 RDBMS 619404 function for feedback insert
def mca1_619404(request):  
    if request.method == "POST":  
        form = Mca1_619404_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca1_619404_Form()  
    return render(request,'MCA1.html',{'form':form})

##MCA1 WDT-PHP 619405 function for feedback insert
def mca1_619405(request):  
    if request.method == "POST":  
        form = Mca1_619405_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Mca1_619405_Form()  
    return render(request,'MCA1.html',{'form':form})

##MCA1 BCC 619406 function for feedback insert
def mca1_619406(request):
    if request.method == "POST": 
        form = Mca1_619406_Form(request.POST)
        if form.is_valid():
            try:
                form.save(commit=True)
            except:
                pass
    form = Mca1_619406_Form()  
    return render(request,'MCA1.html',{'form':form})

def successmca1(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# mca1 Main function for insert ############################
def mca1_main(request):
    if request.method == "POST":
        mca1_619401(request)
        mca1_619402(request)
        mca1_619403(request)
        mca1_619404(request)
        mca1_619405(request)
        mca1_619406(request)
        return render(request,'Success.html')

################################### Delete MCA1 Database #############################################
def delete_dbs_mca1(request):
    if request.method == "POST":
        Mca1_619401.objects.all().delete()
        mca1_619401 = Mca1_619401(std_id=0, pr619401=0, pe619401=0, sk619401=0, mt619401=0, ms619401=0, pa619401=0, cs619401=0, ps619401=0)
        mca1_619401.save()
        
        Mca1_619402.objects.all().delete()
        mca1_619402 = Mca1_619402(std_id=0, pr619402=0, pe619402=0, sk619402=0, mt619402=0, ms619402=0, pa619402=0, cs619402=0, ps619402=0)
        mca1_619402.save()    
        
        Mca1_619403.objects.all().delete()
        mca1_619403 = Mca1_619403(std_id=0, pr619403=0, pe619403=0, sk619403=0, mt619403=0, ms619403=0, pa619403=0, cs619403=0, ps619403=0)
        mca1_619403.save()  
          
        Mca1_619404.objects.all().delete()
        mca1_619404 = Mca1_619404(std_id=0, pr619404=0, pe619404=0, sk619404=0, mt619404=0, ms619404=0, pa619404=0, cs619404=0, ps619404=0)
        mca1_619404.save()
          
        Mca1_619405.objects.all().delete()
        mca1_619405 = Mca1_619405(std_id=0, pr619405=0, pe619405=0, sk619405=0, mt619405=0, ms619405=0, pa619405=0, cs619405=0, ps619405=0)
        mca1_619405.save()

        Mca1_619406.objects.all().delete()
        mca1_619406 = Mca1_619406(std_id=0, pr619406=0, pe619406=0, sk619406=0, mt619406=0, ms619406=0, pa619406=0, cs619406=0, ps619406=0)
        mca1_619406.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})

################################# Mca1 total function ####################################
def mca1total(request):
    if request.method == "POST":
        faculty_name_mca1 = Lecturer.objects.filter(id=1011).values()
        sub = Lecturer.objects.filter(id=101).values()
        return render(request,'mca1total.html', {'sub':sub,
                                                  'faculty_name_mca1':faculty_name_mca1,
                                                  'all_total_mca1':all_total_mca1,
                                                  'count_mca1':count_mca1,
                                                  'totalpr_mca1':totalpr_mca1,
                                                  'totalpe_mca1':totalpe_mca1,
                                                  'totalsk_mca1':totalsk_mca1,
                                                  'totalmt_mca1':totalmt_mca1,
                                                  'totalms_mca1':totalms_mca1,
                                                  'totalpa_mca1':totalpa_mca1,
                                                  'totalcs_mca1':totalcs_mca1,
                                                  'totalps_mca1':totalps_mca1,
                                                  
                                                  'total_619401':total_619401,
                                                  'additionpr_619401':additionpr_619401,
                                                  'additionpe_619401':additionpe_619401,
                                                  'additionsk_619401':additionsk_619401,
                                                  'additionmt_619401':additionmt_619401,
                                                  'additionms_619401':additionms_619401,
                                                  'additionpa_619401':additionpa_619401,
                                                  'additioncs_619401':additioncs_619401,
                                                  'additionps_619401':additionps_619401,
                                                  
                                                  'total_619402':total_619402,
                                                  'additionpr_619402':additionpr_619402,
                                                  'additionpe_619402':additionpe_619402,
                                                  'additionsk_619402':additionsk_619402,
                                                  'additionmt_619402':additionmt_619402,
                                                  'additionms_619402':additionms_619402,
                                                  'additionpa_619402':additionpa_619402,
                                                  'additioncs_619402':additioncs_619402,
                                                  'additionps_619402':additionps_619402,
                                                  
                                                  'total_619403':total_619403,
                                                  'additionpr_619403':additionpr_619403,
                                                  'additionpe_619403':additionpe_619403,
                                                  'additionsk_619403':additionsk_619403,
                                                  'additionmt_619403':additionmt_619403,
                                                  'additionms_619403':additionms_619403,
                                                  'additionpa_619403':additionpa_619403,
                                                  'additioncs_619403':additioncs_619403,
                                                  'additionps_619403':additionps_619403,
                                                  
                                                  'total_619404':total_619404,
                                                  'additionpr_619404':additionpr_619404,
                                                  'additionpe_619404':additionpe_619404,
                                                  'additionsk_619404':additionsk_619404,
                                                  'additionmt_619404':additionmt_619404,
                                                  'additionms_619404':additionms_619404,
                                                  'additionpa_619404':additionpa_619404,
                                                  'additioncs_619404':additioncs_619404,
                                                  'additionps_619404':additionps_619404,
                                                  
                                                  'total_619405':total_619405,
                                                  'additionpr_619405':additionpr_619405,
                                                  'additionpe_619405':additionpe_619405,
                                                  'additionsk_619405':additionsk_619405,
                                                  'additionmt_619405':additionmt_619405,
                                                  'additionms_619405':additionms_619405,
                                                  'additionpa_619405':additionpa_619405,
                                                  'additioncs_619405':additioncs_619405,
                                                  'additionps_619405':additionps_619405,
                                                
                                                  'total_619406':total_619406,
                                                  'additionpr_619406':additionpr_619406,
                                                  'additionpe_619406':additionpe_619406,
                                                  'additionsk_619406':additionsk_619406,
                                                  'additionmt_619406':additionmt_619406,
                                                  'additionms_619406':additionms_619406,
                                                  'additionpa_619406':additionpa_619406,
                                                  'additioncs_619406':additioncs_619406,
                                                  'additionps_619406':additionps_619406})
                
############################# mca1_report_619401 function for report build ###############################
def mca1_report_619401(request):
    if request.method == "POST":
        sem = 'MCA-1 SEM'
        count = count_mca1
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca1*100)/whole_sem_score
        highest_score = max(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        lowest_score = min(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=101).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=1011).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_mca1*100)/max_all_score
        pr_total_fac = additionpr_619401['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca1*100)/max_all_score
        pe_total_fac = additionpe_619401['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca1*100)/max_all_score
        sk_total_fac = additionsk_619401['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca1*100)/max_all_score
        mt_total_fac = additionmt_619401['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca1*100)/max_all_score
        ms_total_fac = additionms_619401['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca1*100)/max_all_score
        pa_total_fac = additionpa_619401['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca1*100)/max_all_score
        cs_total_fac = additioncs_619401['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca1*100)/max_all_score
        ps_total_fac = additionps_619401['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# mca1_report_619402 function for report build ###############################
def mca1_report_619402(request):
    if request.method == "POST":
        sem = 'MCA-1 SEM'
        count = count_mca1
        total_sub = 5 #for rating
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca1*100)/whole_sem_score
        highest_score = max(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        lowest_score = min(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=101).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=1011).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_mca1*100)/max_all_score
        pr_total_fac = additionpr_619402['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca1*100)/max_all_score
        pe_total_fac = additionpe_619402['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca1*100)/max_all_score
        sk_total_fac = additionsk_619402['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca1*100)/max_all_score
        mt_total_fac = additionmt_619402['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca1*100)/max_all_score
        ms_total_fac = additionms_619402['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca1*100)/max_all_score
        pa_total_fac = additionpa_619402['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca1*100)/max_all_score
        cs_total_fac = additioncs_619402['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca1*100)/max_all_score
        ps_total_fac = additionps_619402['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ mca1_report_619403 function for report build ###########################
def mca1_report_619403(request):
    if request.method == "POST":
        sem = 'MCA-1 SEM'
        count = count_mca1
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca1*100)/whole_sem_score
        highest_score = max(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        lowest_score = min(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=101).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=1011).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_mca1*100)/max_all_score
        pr_total_fac = additionpr_619403['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca1*100)/max_all_score
        pe_total_fac = additionpe_619403['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca1*100)/max_all_score
        sk_total_fac = additionsk_619403['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca1*100)/max_all_score
        mt_total_fac = additionmt_619403['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca1*100)/max_all_score
        ms_total_fac = additionms_619403['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca1*100)/max_all_score
        pa_total_fac = additionpa_619403['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca1*100)/max_all_score
        cs_total_fac = additioncs_619403['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca1*100)/max_all_score
        ps_total_fac = additionps_619403['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### mca1_report_619404 function for report build ##############################
def mca1_report_619404(request):
    if request.method == "POST":
        sem = 'MCA-1 SEM'
        count = count_mca1
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca1*100)/whole_sem_score
        highest_score = max(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        lowest_score = min(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=101).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=1011).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_mca1*100)/max_all_score
        pr_total_fac = additionpr_619404['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca1*100)/max_all_score
        pe_total_fac = additionpe_619404['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca1*100)/max_all_score
        sk_total_fac = additionsk_619404['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca1*100)/max_all_score
        mt_total_fac = additionmt_619404['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca1*100)/max_all_score
        ms_total_fac = additionms_619404['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca1*100)/max_all_score
        pa_total_fac = additionpa_619404['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca1*100)/max_all_score
        cs_total_fac = additioncs_619404['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca1*100)/max_all_score
        ps_total_fac = additionps_619404['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ mca1_report_619405 function for report build ###############################
def mca1_report_619405(request):
    if request.method == "POST":
        sem = 'MCA-1 SEM'
        count = count_mca1
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca1*100)/whole_sem_score
        highest_score = max(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        lowest_score = min(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=101).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=1011).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_mca1*100)/max_all_score
        pr_total_fac = additionpr_619405['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca1*100)/max_all_score
        pe_total_fac = additionpe_619405['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca1*100)/max_all_score
        sk_total_fac = additionsk_619405['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca1*100)/max_all_score
        mt_total_fac = additionmt_619405['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca1*100)/max_all_score
        ms_total_fac = additionms_619405['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca1*100)/max_all_score
        pa_total_fac = additionpa_619405['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca1*100)/max_all_score
        cs_total_fac = additioncs_619405['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca1*100)/max_all_score
        ps_total_fac = additionps_619405['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

################################ mca1_report_619406 function for report build ###############################
def mca1_report_619406(request):
    if request.method == "POST":
        sem = 'MCA-1 SEM'
        count = count_mca1
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca1*100)/whole_sem_score
        highest_score = max(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        lowest_score = min(total_619401['total'], total_619402['total'], total_619403['total'], total_619404['total'], total_619405['total'], total_619406['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=101).values()[0]['subject6']
        
        #prof name
        prof = Lecturer.objects.filter(id=1011).values()[0]['subject6']
        
        #PR calculation
        average_pr_all = (totalpr_mca1*100)/max_all_score
        pr_total_fac = additionpr_619406['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca1*100)/max_all_score
        pe_total_fac = additionpe_619406['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca1*100)/max_all_score
        sk_total_fac = additionsk_619406['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca1*100)/max_all_score
        mt_total_fac = additionmt_619406['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca1*100)/max_all_score
        ms_total_fac = additionms_619406['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca1*100)/max_all_score
        pa_total_fac = additionpa_619406['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca1*100)/max_all_score
        cs_total_fac = additioncs_619406['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca1*100)/max_all_score
        ps_total_fac = additionps_619406['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
                                              
         ###########################################################################################
"""----------------------------------- all functions for Mca-1 Complete ----------------------------------------"""

"""----------------------------------- all functions for Mca-2 ----------------------------------------"""   

#mca2 faculty fetch
def mca2(request):
    sub = Lecturer.objects.filter(id=102).values()
    faculty_name_mca2 = Lecturer.objects.filter(id=1022).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'MCA2.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_mca2':faculty_name_mca2})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))

"""------------------------------------ Feedback Insert --------------------------------------"""
##MCA2 DS 629401 function for feedback insert
def mca2_629401(request):  
    if request.method == "POST":  
        form = Mca2_629401_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Mca2_629401_Form()  
    return render(request,'MCA2.html',{'form':form})

##MCA2 MP 629402 function for feedback insert
def mca2_629402(request):  
    if request.method == "POST":  
        form = Mca2_629402_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca2_629402_Form()  
    return render(request,'MCA2.html',{'form':form})

##MCA2 PY 629403 function for feedback insert
def mca2_629403(request):  
    if request.method == "POST":  
        form = Mca2_629403_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca2_629403_Form()  
    return render(request,'MCA2.html',{'form':form})

##MCA2 CN 629404 function for feedback insert
def mca2_629404(request):  
    if request.method == "POST":  
        form = Mca2_629404_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca2_629404_Form()  
    return render(request,'MCA2.html',{'form':form})

##MCA2 SP 629405 function for feedback insert
def mca2_629405(request):  
    if request.method == "POST":  
        form = Mca2_629405_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Mca2_629405_Form()  
    return render(request,'MCA2.html',{'form':form})

##MCA2 JWT 629408 function for feedback insert
def mca2_629408(request):
    if request.method == "POST": 
        form = Mca2_629408_Form(request.POST)
        if form.is_valid():
            try:
                form.save(commit=True)
            except:
                pass
    form = Mca2_629408_Form()  
    return render(request,'MCA2.html',{'form':form})

def successmca2(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# mca2 Main function for insert ############################
def mca2_main(request):
    if request.method == "POST":
        mca2_629401(request)
        mca2_629402(request)
        mca2_629403(request)
        mca2_629404(request)
        mca2_629405(request)
        mca2_629408(request)
        return render(request,'Success.html')
    
################################### Delete MCA2 Database #############################################
def delete_dbs_mca2(request):
    if request.method == "POST":
        Mca2_629401.objects.all().delete()
        mca2_629401 = Mca2_629401(std_id=0, pr629401=0, pe629401=0, sk629401=0, mt629401=0, ms629401=0, pa629401=0, cs629401=0, ps629401=0)
        mca2_629401.save()
        
        Mca2_629402.objects.all().delete()
        mca2_629402 = Mca2_629402(std_id=0, pr629402=0, pe629402=0, sk629402=0, mt629402=0, ms629402=0, pa629402=0, cs629402=0, ps629402=0)
        mca2_629402.save()    
        
        Mca2_629403.objects.all().delete()
        mca2_629403 = Mca2_629403(std_id=0, pr629403=0, pe629403=0, sk629403=0, mt629403=0, ms629403=0, pa629403=0, cs629403=0, ps629403=0)
        mca2_629403.save()  
          
        Mca2_629404.objects.all().delete()
        mca2_629404 = Mca2_629404(std_id=0, pr629404=0, pe629404=0, sk629404=0, mt629404=0, ms629404=0, pa629404=0, cs629404=0, ps629404=0)
        mca2_629404.save()
          
        Mca2_629405.objects.all().delete()
        mca2_629405 = Mca2_629405(std_id=0, pr629405=0, pe629405=0, sk629405=0, mt629405=0, ms629405=0, pa629405=0, cs629405=0, ps629405=0)
        mca2_629405.save()

        Mca2_629408.objects.all().delete()
        mca2_629408 = Mca2_629408(std_id=0, pr629408=0, pe629408=0, sk629408=0, mt629408=0, ms629408=0, pa629408=0, cs629408=0, ps629408=0)
        mca2_629408.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# Mca2 total function ####################################
def mca2total(request):
    if request.method == "POST":
        faculty_name_mca2 = Lecturer.objects.filter(id=1022).values()
        sub = Lecturer.objects.filter(id=102).values()
        return render(request,'mca2total.html', {'sub':sub,
                                                  'faculty_name_mca2':faculty_name_mca2,
                                                  'all_total_mca2':all_total_mca2,
                                                  'count_mca2':count_mca2,
                                                  'totalpr_mca2':totalpr_mca2,
                                                  'totalpe_mca2':totalpe_mca2,
                                                  'totalsk_mca2':totalsk_mca2,
                                                  'totalmt_mca2':totalmt_mca2,
                                                  'totalms_mca2':totalms_mca2,
                                                  'totalpa_mca2':totalpa_mca2,
                                                  'totalcs_mca2':totalcs_mca2,
                                                  'totalps_mca2':totalps_mca2,
                                                  
                                                  'total_629401':total_629401,
                                                  'additionpr_629401':additionpr_629401,
                                                  'additionpe_629401':additionpe_629401,
                                                  'additionsk_629401':additionsk_629401,
                                                  'additionmt_629401':additionmt_629401,
                                                  'additionms_629401':additionms_629401,
                                                  'additionpa_629401':additionpa_629401,
                                                  'additioncs_629401':additioncs_629401,
                                                  'additionps_629401':additionps_629401,
                                                  
                                                  'total_629402':total_629402,
                                                  'additionpr_629402':additionpr_629402,
                                                  'additionpe_629402':additionpe_629402,
                                                  'additionsk_629402':additionsk_629402,
                                                  'additionmt_629402':additionmt_629402,
                                                  'additionms_629402':additionms_629402,
                                                  'additionpa_629402':additionpa_629402,
                                                  'additioncs_629402':additioncs_629402,
                                                  'additionps_629402':additionps_629402,
                                                  
                                                  'total_629403':total_629403,
                                                  'additionpr_629403':additionpr_629403,
                                                  'additionpe_629403':additionpe_629403,
                                                  'additionsk_629403':additionsk_629403,
                                                  'additionmt_629403':additionmt_629403,
                                                  'additionms_629403':additionms_629403,
                                                  'additionpa_629403':additionpa_629403,
                                                  'additioncs_629403':additioncs_629403,
                                                  'additionps_629403':additionps_629403,
                                                  
                                                  'total_629404':total_629404,
                                                  'additionpr_629404':additionpr_629404,
                                                  'additionpe_629404':additionpe_629404,
                                                  'additionsk_629404':additionsk_629404,
                                                  'additionmt_629404':additionmt_629404,
                                                  'additionms_629404':additionms_629404,
                                                  'additionpa_629404':additionpa_629404,
                                                  'additioncs_629404':additioncs_629404,
                                                  'additionps_629404':additionps_629404,
                                                  
                                                  'total_629405':total_629405,
                                                  'additionpr_629405':additionpr_629405,
                                                  'additionpe_629405':additionpe_629405,
                                                  'additionsk_629405':additionsk_629405,
                                                  'additionmt_629405':additionmt_629405,
                                                  'additionms_629405':additionms_629405,
                                                  'additionpa_629405':additionpa_629405,
                                                  'additioncs_629405':additioncs_629405,
                                                  'additionps_629405':additionps_629405,
                                                
                                                  'total_629408':total_629408,
                                                  'additionpr_629408':additionpr_629408,
                                                  'additionpe_629408':additionpe_629408,
                                                  'additionsk_629408':additionsk_629408,
                                                  'additionmt_629408':additionmt_629408,
                                                  'additionms_629408':additionms_629408,
                                                  'additionpa_629408':additionpa_629408,
                                                  'additioncs_629408':additioncs_629408,
                                                  'additionps_629408':additionps_629408})

        
############################# mca2_report_629401 function for report build ###############################
def mca2_report_629401(request):
    if request.method == "POST":
        sem = 'MCA-2 SEM'
        count = count_mca2
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca2*100)/whole_sem_score
        highest_score = max(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        lowest_score = min(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=102).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=1022).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_mca2*100)/max_all_score
        pr_total_fac = additionpr_629401['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca2*100)/max_all_score
        pe_total_fac = additionpe_629401['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca2*100)/max_all_score
        sk_total_fac = additionsk_629401['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca2*100)/max_all_score
        mt_total_fac = additionmt_629401['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca2*100)/max_all_score
        ms_total_fac = additionms_629401['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca2*100)/max_all_score
        pa_total_fac = additionpa_629401['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca2*100)/max_all_score
        cs_total_fac = additioncs_629401['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca2*100)/max_all_score
        ps_total_fac = additionps_629401['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# mca2_report_629402 function for report build ###############################
def mca2_report_629402(request):
    if request.method == "POST":
        sem = 'MCA-2 SEM'
        count = count_mca2
        total_sub = 5 #for rating
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca2*100)/whole_sem_score
        highest_score = max(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        lowest_score = min(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=102).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=1022).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_mca2*100)/max_all_score
        pr_total_fac = additionpr_629402['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca2*100)/max_all_score
        pe_total_fac = additionpe_629402['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca2*100)/max_all_score
        sk_total_fac = additionsk_629402['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca2*100)/max_all_score
        mt_total_fac = additionmt_629402['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca2*100)/max_all_score
        ms_total_fac = additionms_629402['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca2*100)/max_all_score
        pa_total_fac = additionpa_629402['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca2*100)/max_all_score
        cs_total_fac = additioncs_629402['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca2*100)/max_all_score
        ps_total_fac = additionps_629402['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ mca2_report_629403 function for report build ###########################
def mca2_report_629403(request):
    if request.method == "POST":
        sem = 'MCA-2 SEM'
        count = count_mca2
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca2*100)/whole_sem_score
        highest_score = max(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        lowest_score = min(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=102).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=1022).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_mca2*100)/max_all_score
        pr_total_fac = additionpr_629403['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca2*100)/max_all_score
        pe_total_fac = additionpe_629403['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca2*100)/max_all_score
        sk_total_fac = additionsk_629403['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca2*100)/max_all_score
        mt_total_fac = additionmt_629403['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca2*100)/max_all_score
        ms_total_fac = additionms_629403['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca2*100)/max_all_score
        pa_total_fac = additionpa_629403['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca2*100)/max_all_score
        cs_total_fac = additioncs_629403['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca2*100)/max_all_score
        ps_total_fac = additionps_629403['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### mca2_report_629404 function for report build ##############################
def mca2_report_629404(request):
    if request.method == "POST":
        sem = 'MCA-2 SEM'
        count = count_mca2
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca2*100)/whole_sem_score
        highest_score = max(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        lowest_score = min(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=102).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=1022).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_mca2*100)/max_all_score
        pr_total_fac = additionpr_629404['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca2*100)/max_all_score
        pe_total_fac = additionpe_629404['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca2*100)/max_all_score
        sk_total_fac = additionsk_629404['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca2*100)/max_all_score
        mt_total_fac = additionmt_629404['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca2*100)/max_all_score
        ms_total_fac = additionms_629404['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca2*100)/max_all_score
        pa_total_fac = additionpa_629404['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca2*100)/max_all_score
        cs_total_fac = additioncs_629404['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca2*100)/max_all_score
        ps_total_fac = additionps_629404['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ mca2_report_629405 function for report build ###############################
def mca2_report_629405(request):
    if request.method == "POST":
        sem = 'MCA-2 SEM'
        count = count_mca2
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca2*100)/whole_sem_score
        highest_score = max(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        lowest_score = min(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=102).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=1022).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_mca2*100)/max_all_score
        pr_total_fac = additionpr_629405['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca2*100)/max_all_score
        pe_total_fac = additionpe_629405['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca2*100)/max_all_score
        sk_total_fac = additionsk_629405['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca2*100)/max_all_score
        mt_total_fac = additionmt_629405['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca2*100)/max_all_score
        ms_total_fac = additionms_629405['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca2*100)/max_all_score
        pa_total_fac = additionpa_629405['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca2*100)/max_all_score
        cs_total_fac = additioncs_629405['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca2*100)/max_all_score
        ps_total_fac = additionps_629405['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

################################ mca2_report_629408 function for report build ###############################
def mca2_report_629408(request):
    if request.method == "POST":
        sem = 'MCA-2 SEM'
        count = count_mca2
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca2*100)/whole_sem_score
        highest_score = max(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        lowest_score = min(total_629401['total'], total_629402['total'], total_629403['total'], total_629404['total'], total_629405['total'], total_629408['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=102).values()[0]['subject6']
        
        #prof name
        prof = Lecturer.objects.filter(id=1022).values()[0]['subject6']
        
        #PR calculation
        average_pr_all = (totalpr_mca2*100)/max_all_score
        pr_total_fac = additionpr_629408['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca2*100)/max_all_score
        pe_total_fac = additionpe_629408['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca2*100)/max_all_score
        sk_total_fac = additionsk_629408['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca2*100)/max_all_score
        mt_total_fac = additionmt_629408['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca2*100)/max_all_score
        ms_total_fac = additionms_629408['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca2*100)/max_all_score
        pa_total_fac = additionpa_629408['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca2*100)/max_all_score
        cs_total_fac = additioncs_629408['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca2*100)/max_all_score
        ps_total_fac = additionps_629408['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
                                              
         ###########################################################################################
"""----------------------------------- all functions for Mca-2 Complete ----------------------------------------"""

"""----------------------------------- all functions for Mca-3 ----------------------------------------"""   

#mca3 faculty fetch
def mca3(request):
    sub = Lecturer.objects.filter(id=103).values()
    faculty_name_mca3 = Lecturer.objects.filter(id=1033).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'MCA3.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_mca3':faculty_name_mca3})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))


"""------------------------------------ Feedback Insert --------------------------------------"""
##MCA3 DAA 639401 function for feedback insert
def mca3_639401(request):  
    if request.method == "POST":  
        form = Mca3_639401_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Mca3_639401_Form()  
    return render(request,'MCA3.html',{'form':form})

##MCA3 ML 639402 function for feedback insert
def mca3_639402(request):  
    if request.method == "POST":  
        form = Mca3_639402_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca3_639402_Form()  
    return render(request,'MCA3.html',{'form':form})

##MCA3 SE 639403 function for feedback insert
def mca3_639403(request):  
    if request.method == "POST":  
        form = Mca3_639403_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca3_639403_Form()  
    return render(request,'MCA3.html',{'form':form})

##MCA3 SP 639404 function for feedback insert
def mca3_639404(request):  
    if request.method == "POST":  
        form = Mca3_639404_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)   
            except:
                pass
    form = Mca3_639404_Form()  
    return render(request,'MCA3.html',{'form':form})

##MCA3 CC 639407 function for feedback insert
def mca3_639407(request):  
    if request.method == "POST":  
        form = Mca3_639407_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)
            except:
                pass
    form = Mca3_639407_Form()  
    return render(request,'MCA3.html',{'form':form})

##MCA3 NCS 639410 function for feedback insert
def mca3_639410(request):
    if request.method == "POST": 
        form = Mca3_639410_Form(request.POST)
        if form.is_valid():
            try:
                form.save(commit=True)
            except:
                pass
    form = Mca3_639410_Form()  
    return render(request,'MCA3.html',{'form':form})

def successmca3(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# mca3 Main function for insert ############################
def mca3_main(request):
    if request.method == "POST":
        mca3_639401(request)
        mca3_639402(request)
        mca3_639403(request)
        mca3_639404(request)
        mca3_639407(request)
        mca3_639410(request)
        return render(request,'Success.html')

################################### Delete MCA3 Database #############################################
def delete_dbs_mca3(request):
    if request.method == "POST":
        Mca3_639401.objects.all().delete()
        mca3_639401 = Mca3_639401(std_id=0, pr639401=0, pe639401=0, sk639401=0, mt639401=0, ms639401=0, pa639401=0, cs639401=0, ps639401=0)
        mca3_639401.save()
        
        Mca3_639402.objects.all().delete()
        mca3_639402 = Mca3_639402(std_id=0, pr639402=0, pe639402=0, sk639402=0, mt639402=0, ms639402=0, pa639402=0, cs639402=0, ps639402=0)
        mca3_639402.save()    
        
        Mca3_639403.objects.all().delete()
        mca3_639403 = Mca3_639403(std_id=0, pr639403=0, pe639403=0, sk639403=0, mt639403=0, ms639403=0, pa639403=0, cs639403=0, ps639403=0)
        mca3_639403.save()  
          
        Mca3_639404.objects.all().delete()
        mca3_639404 = Mca3_639404(std_id=0, pr639404=0, pe639404=0, sk639404=0, mt639404=0, ms639404=0, pa639404=0, cs639404=0, ps639404=0)
        mca3_639404.save()
          
        Mca3_639407.objects.all().delete()
        mca3_639407 = Mca3_639407(std_id=0, pr639407=0, pe639407=0, sk639407=0, mt639407=0, ms639407=0, pa639407=0, cs639407=0, ps639407=0)
        mca3_639407.save()

        Mca3_639410.objects.all().delete()
        mca3_639410 = Mca3_639410(std_id=0, pr639410=0, pe639410=0, sk639410=0, mt639410=0, ms639410=0, pa639410=0, cs639410=0, ps639410=0)
        mca3_639410.save()
        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# Mca3 total function ####################################
def mca3total(request):
    if request.method == "POST":
        faculty_name_mca3 = Lecturer.objects.filter(id=1033).values()
        sub = Lecturer.objects.filter(id=103).values()
        return render(request,'mca3total.html', {'sub':sub,
                                                  'faculty_name_mca3':faculty_name_mca3,
                                                  'all_total_mca3':all_total_mca3,
                                                  'count_mca3':count_mca3,
                                                  'totalpr_mca3':totalpr_mca3,
                                                  'totalpe_mca3':totalpe_mca3,
                                                  'totalsk_mca3':totalsk_mca3,
                                                  'totalmt_mca3':totalmt_mca3,
                                                  'totalms_mca3':totalms_mca3,
                                                  'totalpa_mca3':totalpa_mca3,
                                                  'totalcs_mca3':totalcs_mca3,
                                                  'totalps_mca3':totalps_mca3,
                                                  
                                                  'total_639401':total_639401,
                                                  'additionpr_639401':additionpr_639401,
                                                  'additionpe_639401':additionpe_639401,
                                                  'additionsk_639401':additionsk_639401,
                                                  'additionmt_639401':additionmt_639401,
                                                  'additionms_639401':additionms_639401,
                                                  'additionpa_639401':additionpa_639401,
                                                  'additioncs_639401':additioncs_639401,
                                                  'additionps_639401':additionps_639401,
                                                  
                                                  'total_639402':total_639402,
                                                  'additionpr_639402':additionpr_639402,
                                                  'additionpe_639402':additionpe_639402,
                                                  'additionsk_639402':additionsk_639402,
                                                  'additionmt_639402':additionmt_639402,
                                                  'additionms_639402':additionms_639402,
                                                  'additionpa_639402':additionpa_639402,
                                                  'additioncs_639402':additioncs_639402,
                                                  'additionps_639402':additionps_639402,
                                                  
                                                  'total_639403':total_639403,
                                                  'additionpr_639403':additionpr_639403,
                                                  'additionpe_639403':additionpe_639403,
                                                  'additionsk_639403':additionsk_639403,
                                                  'additionmt_639403':additionmt_639403,
                                                  'additionms_639403':additionms_639403,
                                                  'additionpa_639403':additionpa_639403,
                                                  'additioncs_639403':additioncs_639403,
                                                  'additionps_639403':additionps_639403,
                                                  
                                                  'total_639404':total_639404,
                                                  'additionpr_639404':additionpr_639404,
                                                  'additionpe_639404':additionpe_639404,
                                                  'additionsk_639404':additionsk_639404,
                                                  'additionmt_639404':additionmt_639404,
                                                  'additionms_639404':additionms_639404,
                                                  'additionpa_639404':additionpa_639404,
                                                  'additioncs_639404':additioncs_639404,
                                                  'additionps_639404':additionps_639404,
                                                  
                                                  'total_639407':total_639407,
                                                  'additionpr_639407':additionpr_639407,
                                                  'additionpe_639407':additionpe_639407,
                                                  'additionsk_639407':additionsk_639407,
                                                  'additionmt_639407':additionmt_639407,
                                                  'additionms_639407':additionms_639407,
                                                  'additionpa_639407':additionpa_639407,
                                                  'additioncs_639407':additioncs_639407,
                                                  'additionps_639407':additionps_639407,
                                                
                                                  'total_639410':total_639410,
                                                  'additionpr_639410':additionpr_639410,
                                                  'additionpe_639410':additionpe_639410,
                                                  'additionsk_639410':additionsk_639410,
                                                  'additionmt_639410':additionmt_639410,
                                                  'additionms_639410':additionms_639410,
                                                  'additionpa_639410':additionpa_639410,
                                                  'additioncs_639410':additioncs_639410,
                                                  'additionps_639410':additionps_639410})
        
############################# mca3_report_639401 function for report build ###############################
def mca3_report_639401(request):
    if request.method == "POST":
        sem = 'MCA-3 SEM'
        count = count_mca3
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca3*100)/whole_sem_score
        highest_score = max(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        lowest_score = min(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=103).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=1033).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_mca3*100)/max_all_score
        pr_total_fac = additionpr_639401['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca3*100)/max_all_score
        pe_total_fac = additionpe_639401['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca3*100)/max_all_score
        sk_total_fac = additionsk_639401['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca3*100)/max_all_score
        mt_total_fac = additionmt_639401['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca3*100)/max_all_score
        ms_total_fac = additionms_639401['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca3*100)/max_all_score
        pa_total_fac = additionpa_639401['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca3*100)/max_all_score
        cs_total_fac = additioncs_639401['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca3*100)/max_all_score
        ps_total_fac = additionps_639401['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})


############################# mca3_report_639402 function for report build ###############################
def mca3_report_639402(request):
    if request.method == "POST":
        sem = 'MCA-3 SEM'
        count = count_mca3
        total_sub = 5 #for rating
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca3*100)/whole_sem_score
        highest_score = max(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        lowest_score = min(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=103).values()[0]['subject2']
        
        #prof name
        prof = Lecturer.objects.filter(id=1033).values()[0]['subject2']
        
        #PR calculation
        average_pr_all = (totalpr_mca3*100)/max_all_score
        pr_total_fac = additionpr_639402['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca3*100)/max_all_score
        pe_total_fac = additionpe_639402['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca3*100)/max_all_score
        sk_total_fac = additionsk_639402['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca3*100)/max_all_score
        mt_total_fac = additionmt_639402['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca3*100)/max_all_score
        ms_total_fac = additionms_639402['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca3*100)/max_all_score
        pa_total_fac = additionpa_639402['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca3*100)/max_all_score
        cs_total_fac = additioncs_639402['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca3*100)/max_all_score
        ps_total_fac = additionps_639402['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
############################ mca3_report_639403 function for report build ###########################
def mca3_report_639403(request):
    if request.method == "POST":
        sem = 'MCA-3 SEM'
        count = count_mca3
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca3*100)/whole_sem_score
        highest_score = max(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        lowest_score = min(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=103).values()[0]['subject3']
        
        #prof name
        prof = Lecturer.objects.filter(id=1033).values()[0]['subject3']
        
        #PR calculation
        average_pr_all = (totalpr_mca3*100)/max_all_score
        pr_total_fac = additionpr_639403['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca3*100)/max_all_score
        pe_total_fac = additionpe_639403['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca3*100)/max_all_score
        sk_total_fac = additionsk_639403['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca3*100)/max_all_score
        mt_total_fac = additionmt_639403['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca3*100)/max_all_score
        ms_total_fac = additionms_639403['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca3*100)/max_all_score
        pa_total_fac = additionpa_639403['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca3*100)/max_all_score
        cs_total_fac = additioncs_639403['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca3*100)/max_all_score
        ps_total_fac = additionps_639403['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
########################### mca3_report_639404 function for report build ##############################
def mca3_report_639404(request):
    if request.method == "POST":
        sem = 'MCA-3 SEM'
        count = count_mca3
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca3*100)/whole_sem_score
        highest_score = max(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        lowest_score = min(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=103).values()[0]['subject4']
        
         #prof name
        prof = Lecturer.objects.filter(id=1033).values()[0]['subject4']
        
        #PR calculation
        average_pr_all = (totalpr_mca3*100)/max_all_score
        pr_total_fac = additionpr_639404['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca3*100)/max_all_score
        pe_total_fac = additionpe_639404['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca3*100)/max_all_score
        sk_total_fac = additionsk_639404['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca3*100)/max_all_score
        mt_total_fac = additionmt_639404['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca3*100)/max_all_score
        ms_total_fac = additionms_639404['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca3*100)/max_all_score
        pa_total_fac = additionpa_639404['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca3*100)/max_all_score
        cs_total_fac = additioncs_639404['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca3*100)/max_all_score
        ps_total_fac = additionps_639404['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
    
################################ mca3_report_639407 function for report build ###############################
def mca3_report_639407(request):
    if request.method == "POST":
        sem = 'MCA-3 SEM'
        count = count_mca3
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca3*100)/whole_sem_score
        highest_score = max(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        lowest_score = min(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=103).values()[0]['subject5']
        
        #prof name
        prof = Lecturer.objects.filter(id=1033).values()[0]['subject5']
        
        #PR calculation
        average_pr_all = (totalpr_mca3*100)/max_all_score
        pr_total_fac = additionpr_639407['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca3*100)/max_all_score
        pe_total_fac = additionpe_639407['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca3*100)/max_all_score
        sk_total_fac = additionsk_639407['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca3*100)/max_all_score
        mt_total_fac = additionmt_639407['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca3*100)/max_all_score
        ms_total_fac = additionms_639407['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca3*100)/max_all_score
        pa_total_fac = additionpa_639407['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca3*100)/max_all_score
        cs_total_fac = additioncs_639407['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca3*100)/max_all_score
        ps_total_fac = additionps_639407['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

################################ mca3_report_639410 function for report build ###############################
def mca3_report_639410(request):
    if request.method == "POST":
        sem = 'MCA-3 SEM'
        count = count_mca3
        total_sub = 5
        total_faculty = 6
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca3*100)/whole_sem_score
        highest_score = max(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        lowest_score = min(total_639401['total'], total_639402['total'], total_639403['total'], total_639404['total'], total_639407['total'], total_639410['total'])
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=103).values()[0]['subject6']
        
        #prof name
        prof = Lecturer.objects.filter(id=1033).values()[0]['subject6']
        
        #PR calculation
        average_pr_all = (totalpr_mca3*100)/max_all_score
        pr_total_fac = additionpr_639410['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca3*100)/max_all_score
        pe_total_fac = additionpe_639410['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca3*100)/max_all_score
        sk_total_fac = additionsk_639410['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca3*100)/max_all_score
        mt_total_fac = additionmt_639410['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca3*100)/max_all_score
        ms_total_fac = additionms_639410['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca3*100)/max_all_score
        pa_total_fac = additionpa_639410['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca3*100)/max_all_score
        cs_total_fac = additioncs_639410['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca3*100)/max_all_score
        ps_total_fac = additionps_639410['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
                                              
         ###########################################################################################
"""----------------------------------- all functions for Mca-3 Complete ----------------------------------------"""

"""----------------------------------- all functions for Imca-10 ----------------------------------------"""
#ic10 faculty fetch
def ic10(request):
    sub = Lecturer.objects.filter(id=10).values()
    faculty_name_ic10 = Lecturer.objects.filter(id=100).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'IMCA10.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_ic10':faculty_name_ic10})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))

"""------------------------------------ Feedback Insert --------------------------------------"""
##IC10 SP 4401601 function for feedback insert
def ic10_4401601(request):  
    if request.method == "POST":  
        form = Ic10_4401601_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Ic10_4401601_Form()  
    return render(request,'IMCA10.html',{'form':form})

def successic10(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# ic10 Main function for insert ############################
def ic10_main(request):
    if request.method == "POST":
        ic10_4401601(request)
        return render(request,'Success.html')
    
################################### Delete IMCA10 Database #############################################
def delete_dbs_ic10(request):
    if request.method == "POST":
        Ic10_4401601.objects.all().delete()
        ic10_4401601 = Ic10_4401601(std_id=0, pr4401601=0, pe4401601=0, sk4401601=0, mt4401601=0, ms4401601=0, pa4401601=0, cs4401601=0, ps4401601=0)
        ic10_4401601.save()

        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# imca10 total function ####################################
def imca10total(request):
    if request.method == "POST":
        faculty_name_ic10 = Lecturer.objects.filter(id=100).values()
        sub = Lecturer.objects.filter(id=10).values()
        return render(request,'imca10total.html', {'sub':sub,
                                                  'faculty_name_ic10':faculty_name_ic10,
                                                  'all_total_ic10':all_total_ic10,
                                                  'count_ic10':count_ic10,
                                                  'totalpr_ic10':totalpr_ic10,
                                                  'totalpe_ic10':totalpe_ic10,
                                                  'totalsk_ic10':totalsk_ic10,
                                                  'totalmt_ic10':totalmt_ic10,
                                                  'totalms_ic10':totalms_ic10,
                                                  'totalpa_ic10':totalpa_ic10,
                                                  'totalcs_ic10':totalcs_ic10,
                                                  'totalps_ic10':totalps_ic10,
                                                  
                                                  'total_4401601':total_4401601,
                                                  'additionpr_4401601':additionpr_4401601,
                                                  'additionpe_4401601':additionpe_4401601,
                                                  'additionsk_4401601':additionsk_4401601,
                                                  'additionmt_4401601':additionmt_4401601,
                                                  'additionms_4401601':additionms_4401601,
                                                  'additionpa_4401601':additionpa_4401601,
                                                  'additioncs_4401601':additioncs_4401601,
                                                  'additionps_4401601':additionps_4401601})
        
        
############################# ic10_report_4401601 function for report build ###############################
def ic10_report_4401601(request):
    if request.method == "POST":
        sem = 'IMCA-10 SEM'
        count = count_ic10
        total_sub = 5
        total_faculty = 1
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_ic10*100)/whole_sem_score
        highest_score = total_4401601['total']
        lowest_score = total_4401601['total']
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=10).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=100).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_ic10*100)/max_all_score
        pr_total_fac = additionpr_4401601['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_ic10*100)/max_all_score
        pe_total_fac = additionpe_4401601['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_ic10*100)/max_all_score
        sk_total_fac = additionsk_4401601['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_ic10*100)/max_all_score
        mt_total_fac = additionmt_4401601['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_ic10*100)/max_all_score
        ms_total_fac = additionms_4401601['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_ic10*100)/max_all_score
        pa_total_fac = additionpa_4401601['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_ic10*100)/max_all_score
        cs_total_fac = additioncs_4401601['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_ic10*100)/max_all_score
        ps_total_fac = additionps_4401601['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})
        
"""----------------------------------- all functions for Imca-10 Complete ----------------------------------------"""

"""----------------------------------- all functions for Mca-4 ----------------------------------------"""
#mca4 faculty fetch
def mca4(request):
    sub = Lecturer.objects.filter(id=104).values()
    faculty_name_mca4 = Lecturer.objects.filter(id=1044).values()
    sem = Sem_serve.objects.filter(id=1).values()[0]['semserve']
    userid = request.POST['enrollment']
    
    enrolls = Student.objects.filter(enrollment=userid).exists()
    if enrolls == True:
        return render(request, 'MCA4.html', {'sub':sub, 'userid':userid, 'sem':sem, 'faculty_name_mca4':faculty_name_mca4})
    else:
        context = "Please enter valid enrollment"
        return HttpResponse(index(request))

"""------------------------------------ Feedback Insert --------------------------------------"""
##MCA4 SP 649401 function for feedback insert
def mca4_649401(request):  
    if request.method == "POST":  
        form = Mca4_649401_Form(request.POST)  
        if form.is_valid():  
            try:
                form.save(commit=True)  
            except:
                pass
    form = Mca4_649401_Form()  
    return render(request,'MCA4.html',{'form':form})

def successmca4(request):
    if request.method == "POST":
        return render(request,'Success.html')

################################# mca4 Main function for insert ############################
def mca4_main(request):
    if request.method == "POST":
        mca4_649401(request)
        return render(request,'Success.html')
    
################################### Delete MCA4 Database #############################################
def delete_dbs_mca4(request):
    if request.method == "POST":
        Mca4_649401.objects.all().delete()
        mca4_649401 = Mca4_649401(std_id=0, pr649401=0, pe649401=0, sk649401=0, mt649401=0, ms649401=0, pa649401=0, cs649401=0, ps649401=0)
        mca4_649401.save()

        counts = Student.objects.count()
        show = Myadmin.objects.get(id=1)
        students = Student.objects.all()
        return render(request, 'admin.html',{'counts':counts,'show':show,'students':students})
    
################################# mca4 total function ####################################
def mca4total(request):
    if request.method == "POST":
        faculty_name_mca4 = Lecturer.objects.filter(id=1044).values()
        sub = Lecturer.objects.filter(id=104).values()
        return render(request,'mca4total.html', {'sub':sub,
                                                  'faculty_name_mca4':faculty_name_mca4,
                                                  'all_total_mca4':all_total_mca4,
                                                  'count_mca4':count_mca4,
                                                  'totalpr_mca4':totalpr_mca4,
                                                  'totalpe_mca4':totalpe_mca4,
                                                  'totalsk_mca4':totalsk_mca4,
                                                  'totalmt_mca4':totalmt_mca4,
                                                  'totalms_mca4':totalms_mca4,
                                                  'totalpa_mca4':totalpa_mca4,
                                                  'totalcs_mca4':totalcs_mca4,
                                                  'totalps_mca4':totalps_mca4,
                                                  
                                                  'total_649401':total_649401,
                                                  'additionpr_649401':additionpr_649401,
                                                  'additionpe_649401':additionpe_649401,
                                                  'additionsk_649401':additionsk_649401,
                                                  'additionmt_649401':additionmt_649401,
                                                  'additionms_649401':additionms_649401,
                                                  'additionpa_649401':additionpa_649401,
                                                  'additioncs_649401':additioncs_649401,
                                                  'additionps_649401':additionps_649401})
    
############################# mca4_report_649401 function for report build ###############################
def mca4_report_649401(request):
    if request.method == "POST":
        sem = 'MCA-4 SEM'
        count = count_mca4
        total_sub = 5
        total_faculty = 1
        max_all_score = count * total_sub * total_faculty #all facalty max_score
        whole_sem_score = count * total_sub * total_faculty * 8 #sem maximum possible score
        whole_sem_avg = (all_total_mca4*100)/whole_sem_score
        highest_score = total_649401['total']
        lowest_score = total_649401['total']
        highest_score_avg = (highest_score*100)/(count*5*8)
        lowest_score_avg = (lowest_score*100)/(count*5*8)
        
        today = date.today()
        #for fetch the subject 
        sub = Lecturer.objects.filter(id=104).values()[0]['subject1']
        #prof name
        prof = Lecturer.objects.filter(id=1044).values()[0]['subject1']
        
        #PR calculation
        average_pr_all = (totalpr_mca4*100)/max_all_score
        pr_total_fac = additionpr_649401['total']
        pr_total_fac_avg = (pr_total_fac*100)/(count*total_sub)
        
        #PE calculation
        average_pe_all = (totalpe_mca4*100)/max_all_score
        pe_total_fac = additionpe_649401['total']
        pe_total_fac_avg = (pe_total_fac*100)/(count*total_sub)
        
        #SK calculation
        average_sk_all = (totalsk_mca4*100)/max_all_score
        sk_total_fac = additionsk_649401['total']
        sk_total_fac_avg = (sk_total_fac*100)/(count*total_sub)
        
        #MT calculation
        average_mt_all = (totalmt_mca4*100)/max_all_score
        mt_total_fac = additionmt_649401['total']
        mt_total_fac_avg = (mt_total_fac*100)/(count*total_sub)
        
        #MS calculation
        average_ms_all = (totalms_mca4*100)/max_all_score
        ms_total_fac = additionms_649401['total']
        ms_total_fac_avg = (ms_total_fac*100)/(count*total_sub)
        
        #PA calculation
        average_pa_all = (totalpa_mca4*100)/max_all_score
        pa_total_fac = additionpa_649401['total']
        pa_total_fac_avg = (pa_total_fac*100)/(count*total_sub)
        
        #CS calculation
        average_cs_all = (totalcs_mca4*100)/max_all_score
        cs_total_fac = additioncs_649401['total']
        cs_total_fac_avg = (cs_total_fac*100)/(count*total_sub)
        
        #PS calculation
        average_ps_all = (totalps_mca4*100)/max_all_score
        ps_total_fac = additionps_649401['total']
        ps_total_fac_avg = (ps_total_fac*100)/(count*total_sub)
        
        return render(request,'report.html', {'count':count, 'sem':sem,
                                              'sub':sub,
                                              'prof':prof,
                                              'whole_sem_score':whole_sem_score,
                                              'whole_sem_avg':whole_sem_avg,
                                              'highest_score_avg':highest_score_avg,
                                              'lowest_score_avg':lowest_score_avg,
                                              'today':today,
                                              
                                              'average_pr_all':average_pr_all,
                                              'pr_total_fac':pr_total_fac,
                                              'pr_total_fac_avg':pr_total_fac_avg,
                                              
                                              'average_pe_all':average_pe_all,
                                              'pe_total_fac':pe_total_fac,
                                              'pe_total_fac_avg':pe_total_fac_avg,
                                              
                                              'average_sk_all':average_sk_all,
                                              'sk_total_fac':sk_total_fac,
                                              'sk_total_fac_avg':sk_total_fac_avg,
                                              
                                              'average_mt_all':average_mt_all,
                                              'mt_total_fac':mt_total_fac,
                                              'mt_total_fac_avg':mt_total_fac_avg,
                                              
                                              'average_ms_all':average_ms_all,
                                              'ms_total_fac':ms_total_fac,
                                              'ms_total_fac_avg':ms_total_fac_avg,
                                              
                                              'average_pa_all':average_pa_all,
                                              'pa_total_fac':pa_total_fac,
                                              'pa_total_fac_avg':pa_total_fac_avg,
                                              
                                              'average_cs_all':average_cs_all,
                                              'cs_total_fac':cs_total_fac,
                                              'cs_total_fac_avg':cs_total_fac_avg,
                                              
                                              'average_ps_all':average_ps_all,
                                              'ps_total_fac':ps_total_fac,
                                              'ps_total_fac_avg':ps_total_fac_avg})

"""----------------------------------- all functions for Mca-4 Complete ----------------------------------------"""