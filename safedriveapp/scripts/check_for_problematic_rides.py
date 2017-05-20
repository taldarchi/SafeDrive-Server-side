import django

django.setup()

if __name__ == '__main__':
    from safedriveapp.models import *

    Driver.objects.check_for_duplicate_rides()
    print '\n'
    Driver.objects.check_for_rides_with_closed_gps()