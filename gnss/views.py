from django.shortcuts import render
from gnss.models import *
from django.http import JsonResponse
import random
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def graphPlot(request):
    return render(request, 'gnss/graph-plot.html')
    
def sendGSVData(request):

    # gps = GPS_data.objects.values().last()
    # glonass = GLONASS_data.objects.values().last()
    # galileo = GALILEO_data.objects.values().last()
    # biedou = Biedou_data.objects.values().last()
    # irnss = IRNSS_data.objects.values().last()


    # random data
    # gps_num = random.randint(1,len(GPS_data.objects.values()))
    # glonas_num = random.randint(1,len(GLONASS_data.objects.values()))
    # galileo_num = random.randint(1,len(GALILEO_data.objects.values()))
    # biedou_num = random.randint(1,len(Biedou_data.objects.values()))
    # irnss_num = random.randint(1,len(IRNSS_data.objects.values()))

    # random data
    gps_num = random.randint(1,707781)
    glonas_num = random.randint(1,454155)
    galileo_num = random.randint(1,567554)
    biedou_num = random.randint(1,191536)
    irnss_num = random.randint(1,35)

    # getting data
    gps = GPS_data.objects.filter(sno = gps_num).values().first()
    glonass = GLONASS_data.objects.filter(sno = glonas_num).values().first()
    galileo = GALILEO_data.objects.filter(sno = galileo_num).values().first()
    biedou = Biedou_data.objects.filter(sno = biedou_num).values().first()
    irnss = IRNSS_data.objects.filter(sno = irnss_num).values().first()
    return JsonResponse({'success':200, 'gps':gps, 'glonass':glonass, 'galileo':galileo, 'biedou': biedou, 'irnss':irnss})

@csrf_exempt
def recievingGSVData(request):
    if request.method == 'POST':

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'code':400, 'msg':'Invalid Json'})
        
        if request.headers.get('Access-Key') == 'hd8687fbdtbvdfsdHGYYBGBgbyugbfFBtftftyfBtfuighuygyu87oihuihi':
            satelite_type = data.get('satelite_type')
            sv_prn_num_1 = data.get('sv_prn_num_1')
            sv_prn_num_2 = data.get('sv_prn_num_2')
            sv_prn_num_3 = data.get('sv_prn_num_3')
            sv_prn_num_4 = data.get('sv_prn_num_4')
            elevation_deg_1 = data.get('elevation_deg_1')
            elevation_deg_2 = data.get('elevation_deg_1')
            elevation_deg_3 = data.get('elevation_deg_1')
            elevation_deg_4 = data.get('elevation_deg_1')
            azimuth_1 = data.get('azimuth_1')
            azimuth_2 = data.get('azimuth_2')
            azimuth_3 = data.get('azimuth_3')
            azimuth_4 = data.get('azimuth_4')
            snr_1 = data.get('snr_1')
            snr_2 = data.get('snr_2')
            snr_3 = data.get('snr_3')
            snr_4 = data.get('snr_4') 
            try:
                if satelite_type == 'GPS':
                    gps_table = GPS_data(sv_prn_num_1=sv_prn_num_1, sv_prn_num_2=sv_prn_num_2, sv_prn_num_3=sv_prn_num_3,sv_prn_num_4=sv_prn_num_4,elevation_deg_1=elevation_deg_1,elevation_deg_2=elevation_deg_2,elevation_deg_3=elevation_deg_3,elevation_deg_4=elevation_deg_4,azimuth_1=azimuth_1,azimuth_2=azimuth_2,azimuth_3=azimuth_3,azimuth_4=azimuth_4,snr_1=snr_1,snr_2=snr_2,snr_3=snr_3,snr_4=snr_4)
                    gps_table.save()

                if satelite_type == 'GLONASS':
                    GLONASS_table = GLONASS_data(sv_prn_num_1=sv_prn_num_1, sv_prn_num_2=sv_prn_num_2, sv_prn_num_3=sv_prn_num_3,sv_prn_num_4=sv_prn_num_4,elevation_deg_1=elevation_deg_1,elevation_deg_2=elevation_deg_2,elevation_deg_3=elevation_deg_3,elevation_deg_4=elevation_deg_4,azimuth_1=azimuth_1,azimuth_2=azimuth_2,azimuth_3=azimuth_3,azimuth_4=azimuth_4,snr_1=snr_1,snr_2=snr_2,snr_3=snr_3,snr_4=snr_4)
                    GLONASS_table.save()

                if satelite_type == 'GALILEO':
                    GALILEO_table = GALILEO_data(sv_prn_num_1=sv_prn_num_1, sv_prn_num_2=sv_prn_num_2, sv_prn_num_3=sv_prn_num_3,sv_prn_num_4=sv_prn_num_4,elevation_deg_1=elevation_deg_1,elevation_deg_2=elevation_deg_2,elevation_deg_3=elevation_deg_3,elevation_deg_4=elevation_deg_4,azimuth_1=azimuth_1,azimuth_2=azimuth_2,azimuth_3=azimuth_3,azimuth_4=azimuth_4,snr_1=snr_1,snr_2=snr_2,snr_3=snr_3,snr_4=snr_4)
                    GALILEO_table.save()

                if satelite_type == 'Biedou':
                    Biedou_table = Biedou_data(sv_prn_num_1=sv_prn_num_1, sv_prn_num_2=sv_prn_num_2, sv_prn_num_3=sv_prn_num_3,sv_prn_num_4=sv_prn_num_4,elevation_deg_1=elevation_deg_1,elevation_deg_2=elevation_deg_2,elevation_deg_3=elevation_deg_3,elevation_deg_4=elevation_deg_4,azimuth_1=azimuth_1,azimuth_2=azimuth_2,azimuth_3=azimuth_3,azimuth_4=azimuth_4,snr_1=snr_1,snr_2=snr_2,snr_3=snr_3,snr_4=snr_4)
                    Biedou_table.save()

                if satelite_type == 'IRNSS':
                    IRNSS_table = IRNSS_data(sv_prn_num_1=sv_prn_num_1, sv_prn_num_2=sv_prn_num_2, sv_prn_num_3=sv_prn_num_3,sv_prn_num_4=sv_prn_num_4,elevation_deg_1=elevation_deg_1,elevation_deg_2=elevation_deg_2,elevation_deg_3=elevation_deg_3,elevation_deg_4=elevation_deg_4,azimuth_1=azimuth_1,azimuth_2=azimuth_2,azimuth_3=azimuth_3,azimuth_4=azimuth_4,snr_1=snr_1,snr_2=snr_2,snr_3=snr_3,snr_4=snr_4)
                    IRNSS_table.save()

            except Exception as e:
                return JsonResponse({'code':403, 'msg':f'The error is: {e}'})

            return JsonResponse({'code':200, 'msg':'Successful'})
        
        else:
            return JsonResponse({'code':403, 'msg':'Invalid Access key'})


def gnss(request):
    return render(request, 'gnss/gnss.html')

def gnssConstillations(request):
    return render(request, 'gnss/gnss-constillations.html')

def gnssStationsWorldwide(request):
    return render(request, 'gnss/gnss-stations-worldwide.html')

def gnssGallery(request):
    return render(request, 'gnss/gnss-gallery.html')

def gnssExperts(request):
    return render(request, 'gnss/gnss-experts.html')
