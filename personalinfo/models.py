from django.db import models
from django.contrib.auth.models import AbstractUser
from extensions.utils import jalali_converter, full_jalali_converter
from translated_fields import TranslatedField
from django.utils import timezone


# Create your models here.


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'مهارت ها'
        verbose_name = 'مهارت'
    
    name = TranslatedField(
         models.CharField(max_length=20, blank=True, null=True),
         {"fa":{"verbose_name":" عنوان مهارت در سايت فارسي "},
         "en":{"verbose_name":" عنوان مهارت در سايت انگليسي "},
         }
    )
    score = models.IntegerField(default=80, blank=True, null=True, verbose_name = 'امتياز')
    is_key_skill = models.BooleanField(default=True, verbose_name = 'فعال/غيرفعال')
    
    def __str__(self):
        return self.name


class User(AbstractUser):

    class Meta:
        verbose_name_plural = 'پروفايل كاربري'
        verbose_name = 'پروفايل'
    
    first_name = TranslatedField(
        models.CharField(max_length=30, blank=True, null=True),
         {"fa":{"verbose_name":"نام در سايت فارسي "},
         "en":{"verbose_name":" نام در سايت انگليسي "},
         }
    )

    last_name = TranslatedField(
        models.CharField(max_length=30, blank=True, null=True),
         {"fa":{"verbose_name":"نام خانوادگي در سايت فارسي "},
         "en":{"verbose_name":" نام خانوادگي در سايت انگليسي "},
         }
    )

    avatar = models.ImageField(blank=True, null=True, upload_to="avatar", default='avatar/no-img.png' , verbose_name = 'تصوير')

    title = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {"fa":{"verbose_name":" عنوان تخصص در سايت فارسي "},
         "en":{"verbose_name":" عنوان تخصص در سايت انگليسي "},
         }
    )

    birthday = models.DateTimeField(blank=True, null=True, verbose_name = 'تاريخ تولد', default=timezone.now())

    bio = TranslatedField(
        models.TextField(blank=True, null=True),
         {"fa":{"verbose_name":"  توضيحات درباره من در سايت فارسي "},
         "en":{"verbose_name":" توضيحات  درباره من در سايت انگليسي "},
         }
    )

    skills = models.ManyToManyField(Skill, blank=True, verbose_name = 'مهارت ها')

    cv = TranslatedField(
        models.FileField(blank=True, null=True, upload_to="cv", default='avatar/no-img.png'),
         {"fa":{"verbose_name":" فايل رزومه براي سايت فارسي "},
         "en":{"verbose_name":" فايل رزومه براي سايت انگليسي "},
         }
    )

    UnderDiploma = 1
    Diploma = 2
    Bachelor = 3
    Master = 4
    Phd = 5
    UpperPhd = 6
    Degree = (
        (UnderDiploma, 'زير ديپلم'),
        (Diploma, 'ديپلم'),
        (Bachelor, 'كارشناسي'),
        (Master, 'كارشناسي ارشد'),
        (Phd, 'دكترا'),
        (UpperPhd, 'فوق دكترا'),
    )

    ENDegree = (
        (UnderDiploma, 'High School'),
        (Diploma, 'Diploma'),
        (Bachelor, 'BA/BSc'),
        (Master, 'MA/MSc'),
        (Phd, 'PhD'),
        (UpperPhd, 'Post Doctoral'),
    )

    last_degree = TranslatedField(
         models.IntegerField( default=Bachelor),
         {
            "fa":{"verbose_name":"آخرين مدرك در سايت فارسي ", "choices": Degree ,},
            "en":{"verbose_name":" آخرين مدرك در سايت انگليسي ", "choices": ENDegree ,},
         }
    )
    course = TranslatedField(
         models.CharField(max_length=200, blank=True, null=True),
         {"fa":{"verbose_name":" رشته تحصيلي در سايت فارسي "},
         "en":{"verbose_name":" رشته تحصيلي در سايت انگليسي "},
         }
    )
    
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="شماره تماس")
    
    city = TranslatedField(
        models.CharField(max_length=50, blank=True, null=True),
         {"fa":{"verbose_name":" شهر محل زندگي در سايت فارسي "},
         "en":{"verbose_name":" شهر محل زندگي در سايت انگليسي "},
         }
    )

    country = TranslatedField(
        models.CharField(max_length=50, blank=True, null=True),
         {"fa":{"verbose_name":" كشور محل زندگي در سايت فارسي "},
         "en":{"verbose_name":"كشور محل زندگي در سايت انگليسي "},
         }
    )

    freelancer = models.BooleanField(default=True, verbose_name = 'امكان فريلنسري')

    github = models.CharField(max_length=100, blank=True, null=True, verbose_name=" يوزرنيم گيت هاب")
            
    instagram = models.CharField(max_length=100, blank=True, null=True, verbose_name=" يوزرنيم اينستاگرام")

    whatsapp = models.CharField(max_length=100, blank=True, null=True, verbose_name="  شماره واتس اپ")

    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name=" يوزرنيم تلگرام")

    twitter = models.CharField(max_length=100, blank=True, null=True, verbose_name=" يوزرنيم توييتر")

    youtube = models.CharField(max_length=100, blank=True, null=True, verbose_name=" كانال يوتوب")

    skype = models.CharField(max_length=100, blank=True, null=True, verbose_name=" يوزرنيم اسكايپ")

    linkedin = models.CharField(max_length=100, blank=True, null=True, verbose_name=" يوزرنيم لينكدين")

    googlescholar = models.CharField(max_length=100, blank=True, null=True, verbose_name=" يوزرنيم گوگل اسكولار")


    def __str__(self):
        if self.get_full_name():
            return f'{self.first_name} {self.last_name}'
        return f'{self.username}'  


    def jbirthday(self):
        return jalali_converter(self.birthday)

    jbirthday.short_description = " تاريخ تولد"
    

    def Mbirthday(self):
        return f'{self.birthday.year}/{self.birthday.month}'

    Mbirthday.short_description = " تاريخ تولد"


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'تماس ها '
        verbose_name = 'تماس'
        ordering = ["-timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name = 'تاريخ و زمان ارسال')

    name = models.CharField(max_length=100, verbose_name = 'نام و نام خانوادگي')

    title = models.CharField(max_length=100, verbose_name = 'عنوان پيام')

    email = models.EmailField( verbose_name = 'آدرس ايميل')

    message = models.TextField( verbose_name = 'پيام ارسالي')


    def __str__(self):
        return f'{self.name}'  

    def jtimestamp(self):
        return full_jalali_converter(self.timestamp)

    jtimestamp.short_description = " تاريخ ارسال"     


class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'مراجع'
        verbose_name = 'مرجع'
       

    name = TranslatedField(
         models.CharField(max_length=200, blank=True, null=True),
         {"fa":{"verbose_name":"  نام و نام خانوادگي در سايت فارسي "},
         "en":{"verbose_name":"  نام و نام خانوادگي در سايت انگليسي "},
         }
    )

    role = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {"fa":{"verbose_name":" عنوان سمت شغلي در سايت فارسي "},
         "en":{"verbose_name":" عنوان سمت شغلي در سايت انگليسي "},
         }
    )

    email = models.EmailField( verbose_name = 'آدرس ايميل')

    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name = 'شماره تماس')

    web_site = models.CharField(max_length=200, blank=True, null=True, verbose_name = ' وب سايت')

    describtion = TranslatedField(
        models.TextField(blank=True, null=True),
         {"fa":{"verbose_name":" توضيحات در سايت فارسي "},
         "en":{"verbose_name":"  توضيحات در سايت انگليسي "},
         }
    )

    is_active = models.BooleanField(default=True, verbose_name = 'فعال/غيرفعال')

    def __str__(self):
        return self.name              


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'سرتيفيكيت ها'
        verbose_name = 'سرتيفيكت'

  
    thumbnail = models.ImageField(blank=True, null=True, upload_to="certificate", verbose_name = 'تصوير')
    
    date = models.DateTimeField(blank=True, null=True, verbose_name = 'تاريخ دريافت')
    
    name = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {"fa":{"verbose_name":" عنوان مدرك در سايت فارسي "},
         "en":{"verbose_name":" عنوان مدرك در سايت انگليسي "},
         }
    )

    location = TranslatedField(
         models.CharField(max_length=200, blank=True, null=True),
         {"fa":{"verbose_name":" دريافتي از سازمان , دانشگاه,... در سايت فارسي "},
         "en":{"verbose_name":" دريافتي از سازمان , دانشگاه,... در سايت انگليسي "},
         }
    )

    verify_link = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'لينك اعتبار سنجي')
   
    is_active = models.BooleanField(default=True, verbose_name = 'فعال/غيرفعال')

  
    def __str__(self):
        return self.name

    def Mdate(self):
        return f'{self.date.year}/{self.date.month}'

    Mdate.short_description = " تاريخ دريافت"


class Interested(models.Model):

    title = TranslatedField(
        models.CharField(max_length=120),
         {"fa":{"verbose_name":" عنوان در سايت فارسي "},
         "en":{"verbose_name":" عنوان در سايت انگليسي "},
         }
    )

    active = models.BooleanField(verbose_name='فعال/غیر فعال', default=True)
   

    class Meta:
        verbose_name_plural = 'علاقه مندي ها'
        verbose_name = 'علاقه مندي'

    def __str__(self):
        return self.title        


class Academic(models.Model):

    class Meta:
        verbose_name_plural = 'سوابق تحصيلي'
        verbose_name = 'سابقه تحصيل'
        ordering = ['position']


    thumbnail = models.ImageField(blank=True, null=True, upload_to="certificate", verbose_name = 'تصوير')

    start = models.DateTimeField(blank=True, null=True, verbose_name = 'تاريخ شروع')

    end = models.DateTimeField(blank=True, null=True, verbose_name = 'تاريخ پايان')

    describtion =  TranslatedField(
        models.TextField(blank=True, null=True),
         {"fa":{"verbose_name":" توضيحات در سايت فارسي "},
         "en":{"verbose_name":" توضيحات در سايت انگليسي "},
         }
    )

    UnderDiploma = 1
    Diploma = 2
    Bachelor = 3
    Master = 4
    Phd = 5
    UpperPhd = 6
    Degree = (
        (UnderDiploma, 'زير ديپلم'),
        (Diploma, 'ديپلم'),
        (Bachelor, 'كارشناسي'),
        (Master, 'كارشناسي ارشد'),
        (Phd, 'دكترا'),
        (UpperPhd, 'فوق دكترا'),
    )

    ENDegree = (
        (UnderDiploma, 'High School'),
        (Diploma, 'Diploma'),
        (Bachelor, 'BA/BSc'),
        (Master, 'MA/MSc'),
        (Phd, 'PhD'),
        (UpperPhd, 'Post Doctoral'),
    )

    degree = TranslatedField(
         models.IntegerField( default=Bachelor),
         {
            "fa":{"verbose_name":" مدرك در سايت فارسي ", "choices": Degree ,},
            "en":{"verbose_name":" مدرك در سايت انگليسي ", "choices": ENDegree ,},
         }
    )

    gpa = TranslatedField(
        models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=2),
         {
            "fa":{"verbose_name":"معدل در سايت فارسي "},
            "en":{"verbose_name":" معدل در سايت انگليسي "},
         }
    )

    course = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {
            "fa":{"verbose_name":"رشته تحصيلي در سايت فارسي "},
            "en":{"verbose_name":" رشته تحصيلي در سايت انگليسي "},
         }
    )

    university = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {
            "fa":{"verbose_name":"دانشگاه محل تحصيل در سايت فارسي "},
            "en":{"verbose_name":" دانشگاه محل تحصيل در سايت انگليسي "},
         }
    )     

    city_university = TranslatedField(
        models.CharField(max_length=50, blank=True, null=True),
         {
            "fa":{"verbose_name":"شهر دانشگاه محل تحصيل در سايت فارسي "},
            "en":{"verbose_name":" شهر دانشگاه محل تحصيل در سايت انگليسي "},
         }
    )     

    country_university = TranslatedField(
        models.CharField(max_length=50, blank=True, null=True),
         {
            "fa":{"verbose_name":"كشور دانشگاه محل تحصيل در سايت فارسي "},
            "en":{"verbose_name":" كشور دانشگاه محل تحصيل در سايت انگليسي "},
         }
    )     

    position = models.IntegerField(verbose_name='پوزیشن') 

    def __str__(self):
        return f'{self.university}'  


    def jstart(self):
        return jalali_converter(self.start)

    jstart.short_description = " تاريخ شروع"
    

    def jend(self):
        return jalali_converter(self.end)

    jend.short_description = " تاريخ پايان"
    

    def Mstart(self):
        return f'{self.start.year}/{self.start.month}'

    Mstart.short_description = " تاريخ شروع"


    def Mend(self):
        return f'{self.end.year}/{self.end.month}'

    Mend.short_description = " تاريخ پايان"


class Job(models.Model):

    class Meta:
        verbose_name_plural = 'سوابق شغلي'
        verbose_name = 'سابقه شغل'
        ordering = ['position']


    job_title = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True, verbose_name = 'عنوان شغل'),
         {
            "fa":{"verbose_name":"عنوان شغل در سايت فارسي "},
            "en":{"verbose_name":" عنوان شغل در سايت انگليسي "},
         }
    )     

    company = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {
            "fa":{"verbose_name":"كمپاني در سايت فارسي "},
            "en":{"verbose_name":"كمپاني در سايت انگليسي "},
         }
    )     
    
    city_company = TranslatedField(
        models.CharField(max_length=50, blank=True, null=True),
         {
            "fa":{"verbose_name":"شهر كمپاني در سايت فارسي "},
            "en":{"verbose_name":"شهر كمپاني در سايت انگليسي "},
         }
    )     

    country_company = TranslatedField(
        models.CharField(max_length=50, blank=True, null=True),
         {
            "fa":{"verbose_name":"كشور كمپاني در سايت فارسي "},
            "en":{"verbose_name":"كشور كمپاني در سايت انگليسي "},
         }
    )     

    start = models.DateTimeField(blank=True, null=True, verbose_name = 'تاريخ شروع')

    end = models.DateTimeField(blank=True, null=True, verbose_name = 'تاريخ پايان')

    describtion = TranslatedField(
        models.TextField(blank=True, null=True),
         {
            "fa":{"verbose_name":"توضيحات در سايت فارسي "},
            "en":{"verbose_name":"توضيحات در سايت انگليسي "},
         }
    )     

    position = models.IntegerField(verbose_name='پوزیشن') 

    def __str__(self):
        return f'{self.job_title}'  


    def jstart(self):
        return jalali_converter(self.start)

    jstart.short_description = " تاريخ شروع"
    

    def jend(self):
        return jalali_converter(self.end)

    jend.short_description = " تاريخ پايان"


    def Mstart(self):
        return f'{self.start.year}/{self.start.month}'

    Mstart.short_description = " تاريخ شروع"


    def Mend(self):
        return f'{self.end.year}/{self.end.month}'

    Mend.short_description = " تاريخ پايان"


class Publication(models.Model):

    class Meta:
        verbose_name_plural = 'مقالات'
        verbose_name = ' مقاله'
        ordering = ['position']

    date = models.DateTimeField(blank=True, null=True, verbose_name = 'تاريخ انتشار')

    title = TranslatedField(
        models.TextField(blank=True, null=True),
         {
            "fa":{"verbose_name":"عنوان مقاله در سايت فارسي "},
            "en":{"verbose_name":"عنوان مقاله در سايت انگليسي "},
         }
    )     

    link = models.CharField(max_length=200, blank=True, null=True, verbose_name = 'لينك')

    status = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {
            "fa":{"verbose_name":"وضعيت مقاله در سايت فارسي "},
            "en":{"verbose_name":"وضعيت مقاله در سايت انگليسي "},
         }
    )     


    position = models.IntegerField(verbose_name='پوزیشن') 

    def __str__(self):
        return f'{self.title}'  


    def jdate(self):
        return jalali_converter(self.date)

    jdate.short_description = "تاريخ انتشار"


    def Mdate(self):
        return f'{self.date.year}/{self.date.month}'

    Mdate.short_description = " تاريخ انتشار"

    
class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'پرتفوليو'
        verbose_name = 'پروژه'
        

    title = TranslatedField(
        models.CharField(max_length=200, blank=True, null=True),
         {
            "fa":{"verbose_name":"عنوان پروژه در سايت فارسي "},
            "en":{"verbose_name":"عنوان پروژه در سايت انگليسي "},
         }
    )     
    
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name = 'لينك پروژه')

    cover = models.ImageField(blank=True, null=True, upload_to="project", verbose_name = 'كاور پروژه')

    describtion = TranslatedField(
        models.TextField(blank=True, null=True),
         {
            "fa":{"verbose_name":"توضيحات پروژه در سايت فارسي "},
            "en":{"verbose_name":"توضيحات پروژه در سايت انگليسي "},
         }
    )     
    
    def __str__(self):
        return f'{self.title}'  




 