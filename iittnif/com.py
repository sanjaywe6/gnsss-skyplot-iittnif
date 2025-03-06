
with open('data.csv', 'r') as file:
    data = file.readlines()
i=0
for item in data:
    # Print the contents of the serial data

    try:

        if 'GGA' in item:

            str1 = item.split(',')

            latitude = str1[4].replace('lat=','').replace("'","")
            longitude = str1[6].replace(' lon=','').replace("'","")
            num_sats = str1[9].replace('num_sats=','').replace("'","")
            altitude = str1[11].replace('altitude=','').replace("'","")

            new_data = {
                    'timestamp':[f"{str1[0]},{str1[1]},{str1[2]})"],
                    'latitude':[latitude],
                    'longitude':[longitude],
                    'num_sats':[num_sats],
                    'altitude':[altitude]
                }
                

            print(f"GGA No.: {i}= ", new_data)
        
        elif 'GSV' in item:

            str1 = item.split(',')

            elevation_deg_1 = str1[4].replace('elevation_deg_1=','').replace("'","")
            elevation_deg_2 = str1[8].replace('elevation_deg_2=','').replace("'","")
            elevation_deg_3 = str1[12].replace('elevation_deg_3=','').replace("'","")
            elevation_deg_4 = str1[16].replace('elevation_deg_4=','').replace("'","")
            azimuth_1 = str1[5].replace('azimuth_1=','').replace("'","")
            azimuth_2 = str1[9].replace('azimuth_2=','').replace("'","")
            azimuth_3 = str1[13].replace('azimuth_3=','').replace("'","")
            azimuth_4 = str1[17].replace('azimuth_4=','').replace("'","")
            snr_1 = str1[6].replace('snr_1=','').replace("'","")
            snr_2 = str1[10].replace('snr_2=','').replace("'","")
            snr_3 = str1[14].replace('snr_3=','').replace("'","")
            snr_4 = str1[18].replace('snr_4=','').replace("'","").replace(')','').replace('>','').replace('\n','')

            new_data = {
                    'elevation_deg_1':[elevation_deg_1],
                    'elevation_deg_2':[elevation_deg_2],
                    'elevation_deg_3':[elevation_deg_3],
                    'elevation_deg_4':[elevation_deg_4],
                    'azimuth_1':[azimuth_1],
                    'azimuth_2':[azimuth_2],
                    'azimuth_3':[azimuth_3],
                    'azimuth_4':[azimuth_4],
                    'snr_1':[snr_1],
                    'snr_2':[snr_2],
                    'snr_3':[snr_3],
                    'snr_4':[snr_4],
                }
                

            print(f"GSV No.: {i}= ",new_data)

        elif 'GSA' in item:


            str1 = item.split(',')

            pdop = str1[14].replace('pdop=','').replace("'","")
            hdop = str1[15].replace('hdop=','').replace("'","")
            vdop = str1[16].replace('vdop=','').replace("'","").replace(')','').replace('>','').replace('\n','')

            new_data = {
                    'pdop':[pdop],
                    'hdop':[hdop],
                    'vdop':[vdop],
                }
                
            print(f"GSA No.: {i}= ",new_data)
        
        else:
            print('Unknown')
    
        i = i+1

    except:
        pass