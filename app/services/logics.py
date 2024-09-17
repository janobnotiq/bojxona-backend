# count of declarations made in particular time period
import datetime
from django.db.models import Q
from ..models import Declaration

def declaration_count(start_date,end_date,user):
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.max.time())

    declarations = Declaration.objects.filter(
        Q(updated_at__gte=start_datetime) & Q(updated_at__lte=end_datetime),
        declarant=user,
        status=Declaration.Status.FINISHED
    )

    return declarations.count()