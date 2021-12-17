https://hackerrank-challenge-pdfs.s3.amazonaws.com/30377-day-of-the-programmer-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1639774887&Signature=gSZhQsFGmp0FBnAIw2UqT8nwXEI%3D&response-content-disposition=inline%3B%20filename%3Dday-of-the-programmer-English.pdf&response-content-type=application%2Fpdf


def dayOfProgrammer(year):
        if year==1918:
            return '26.09.1918'
        if 1700<=year<=1917:
            if year%4==0:
                return '12.09.'+str(year)
            else:
                return '13.09.'+str(year)
        elif year%100==0 and year%400==0 and year%4==0:
            return '12.09.'+str(year)
        elif year%100==0 and year%400==0:
            return '12.09.'+str(year)
        elif year%100!=0 and year%400!=0:
            if year%4==0:
                return '12.09.'+str(year)
            else:
                return '13.09.'+str(year)
        else:
            return '13.09.'+str(year)
