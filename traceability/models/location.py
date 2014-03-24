from django.db import models

CONTINENTS = (
    ('AF', 'Africa'),
    ('NA', 'North America'),
    ('EU', 'Europe'),
    ('AS', 'Asia'),
    ('OC', 'Oceania'),
    ('SA', 'South America'),
    ('AN', 'Antarctica')
)

AREAS = (
    ('a', 'Another'),
    ('i', 'Island'),
    ('ar', 'Arrondissement'),
    ('at', 'Atoll'),
    ('ai', 'Autonomous island'),
    ('ca', 'Canton'),
    ('cm', 'Commune'),
    ('co', 'County'),
    ('dp', 'Department'),
    ('de', 'Dependency'),
    ('dt', 'District'),
    ('dv', 'Division'),
    ('em', 'Emirate'),
    ('gv', 'Governorate'),
    ('ic', 'Island council'),
    ('ig', 'Island group'),
    ('ir', 'Island region'),
    ('kd', 'Kingdom'),
    ('mu', 'Municipality'),
    ('pa', 'Parish'),
    ('pf', 'Prefecture'),
    ('pr', 'Province'),
    ('rg', 'Region'),
    ('rp', 'Republic'),
    ('sh', 'Sheading'),
    ('st', 'State'),
    ('sd', 'Subdivision'),
    ('sj', 'Subject'),
    ('ty', 'Territory'),
)


class Country(models.Model):
    iso2_code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=255)
    printable_name = models.CharField(max_length=255)
    iso3_code = models.CharField(max_length=3, unique=True)
    active = models.BooleanField(default=True)
    continent = models.CharField(choices=CONTINENTS, max_length=2)
    num_code = models.PositiveSmallIntegerField(null=True, blank=True)
    admin_area = models.CharField(
        choices=AREAS, max_length=2, null=True, blank=True)

    class Meta:
        app_label = 'traceability'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __str__(self):
        return self.printable_name


class AdminArea(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField('Admin Area name', max_length=60, )
    abbrev = models.CharField(
        'Postal Abbreviation', max_length=3, null=True, blank=True)
    active = models.BooleanField('Area is active', default=True)

    class Meta:
        app_label = 'traceability'
        verbose_name = 'Administrative Area'
        verbose_name_plural = 'Administrative Areas'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(max_length=100)
    admin_area = models.ForeignKey(AdminArea)

    class Meta:
        app_label = 'traceability'
        verbose_name = 'Locality'
        verbose_name_plural = 'Localities'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Address(models.Model):
    street_number = models.IntegerField(max_length=255)
    street_name = models.CharField(max_length=255)
    locality = models.ForeignKey(Locality)
    postal_code = models.CharField(max_length=255)

    class Meta:
        app_label = 'traceability'
        verbose_name = 'Address'
        verbose_name_plural = 'Address'
        ordering = ('locality', 'street_name',)

    def __str__(self):
        return '%s %s, %s, %s' % (
            self.street_number,
            self.street_name,
            self.locality,
            self.locality.admin_area)
