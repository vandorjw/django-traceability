from django.db import models
from django.core.urlresolvers import reverse


class Incident(models.Model):
    CRITICAL = 0
    MAJOR = 1
    MINOR = 2
    ENQUIRY = 3

    SEVERITY_LEVEL = (
        (CRITICAL, 'Critical'),
        (MAJOR, 'Major'),
        (MINOR, 'Minor'),
        (ENQUIRY, 'Enquiry'),
    )
    date_time = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    text = models.TextField()
    severity_level = models.IntegerField(
        max_length=1,
        choices=SEVERITY_LEVEL,
        default=0)

    class Meta:
        app_label = 'traceability'
        ordering = ['severity_level','date_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'traceability:incident:incident_detail',
            args=[self.id], )

    def get_severity_level(self):
        return self.SEVERITY_LEVEL[self.severity_level][1]


class Update(models.Model):
    incident = models.ForeignKey(Incident)
    date_time = models.DateTimeField(auto_now=True)
    text = models.TextField()

    class Meta:
        app_label = 'traceability'
        ordering = ['incident', 'date_time']
    
    def __str__(self):
        return "%s-%s" % (self.incident, self.date_time)


