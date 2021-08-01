from django.db import models

#django class creation, set a character max and default values
class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    courseNumber = models.IntegerField(default=0)
    instructorName = models.CharField(max_length=60)
    duration = models.FloatField(default=0.00)

    objects = models.Manager()

    def __str__(self):
        return self.title

# creating instances of the djangoClasses class

classOne = djangoClasses(title="Early Modern Literature", courseNumber= 302, instructorName="Carey Mulligan", duration= 1.5)
classTwo = djangoClasses(title="Calculus", courseNumber= 140, instructorName="Mark Janeba", duration= 1.5)
classThree = djangoClasses(title="Greeks Romans and Barbarians", courseNumber= 242, instructorName="Rosa Bachvarova", duration= 1.0)

#save objects
classOne.save()
classTwo.save()
classThree.save()






