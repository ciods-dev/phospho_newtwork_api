from django.db import models

class Gene(models.Model):
    gene = models.CharField(primary_key=True,max_length=255)

    def __str__(self):
        return self.gene

class Phosphosite(models.Model):
    site = models.CharField(primary_key=True,max_length=255)
    def __str__(self):
        return self.site

class Condition(models.Model):
    condition = models.CharField(primary_key=True,max_length=255)

    def __str__(self):
        return self.condition

class GenePhosphosite(models.Model):
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    phosphosite = models.ForeignKey(Phosphosite, on_delete=models.CASCADE)
    conditions = models.ManyToManyField(Condition, through='GenePhosphositeCondition')

    class Meta:
        unique_together = ('gene', 'phosphosite')

    def __str__(self):
        return f"{self.gene} - {self.phosphosite}"

class GenePhosphositeCondition(models.Model):
    gene_phosphosite = models.ForeignKey(GenePhosphosite, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('gene_phosphosite', 'condition')

    def __str__(self):
        return f"{self.gene_phosphosite} under {self.condition}"
