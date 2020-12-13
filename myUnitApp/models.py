from django.db import models


class Unit(models.Model):
    # primary key
    UnitId = models.BigAutoField(primary_key=True,
                                 verbose_name="Unique UnitId"
                                 )

    # Name of the Unit e.g. Kilogram
    Name = models.CharField(verbose_name="Name",
                            max_length=200,
                            unique=True
                            )

    # Unit abbreviation e.g. kg
    Abbreviation = models.CharField(verbose_name="Abbreviation",
                                    max_length=3
                                    )

    def __str__(self):
        return self.Name