from django.core.management.base import BaseCommand

from transaction.models import BranchMaster, DepartmentMaster, CompanyLedgerMaster, ArticleMaster, ColorMaster


class Command(BaseCommand):
    """
    python manage.py update_permissions

    This will update and insert all permissions added in FRONTEND_PERMISSIONS
    and will enter it in department as specified in FRONTEND_DEPARTMENT_PERMISSIONS
    """
    help = 'Checks and updates frontend permissions in connected database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Inserting data for masters'))
        branch1 = BranchMaster.objects.create(short_name="SUN", contact_person_name="Ramesh",
                                              address1="Some address", pin_code=335009,
                                              gst_number="24AAFFG8339R1ZQ")
        branch2 = BranchMaster.objects.create(short_name="MOON", contact_person_name="Suresh",
                                              address1="Some more address", pin_code=335009,
                                              gst_number="24AAFFG8339R1ZQ")
        department1 = DepartmentMaster.objects.create(name="Warp Knitting")
        department2 = DepartmentMaster.objects.create(name="DPV")

        company1 = CompanyLedgerMaster.objects.create(
            name="Ace", gst_number="23453554", supplier_status=True, address1="4325 Bahubali Nagar", pin_code="123456",
            mobile=9864596945)

        article_1 = ArticleMaster.objects.create(name='YarnArticle1', short_name='YA1', blend_pct="CT50PY50",
                                                 twists=50)
        color_1_1 = ColorMaster.objects.create(article=article_1, name="White", short_name="WT")
        color_1_2 = ColorMaster.objects.create(article=article_1, name="Black", short_name="BL")
        color_1_3 = ColorMaster.objects.create(article=article_1, name="Red", short_name="RD")
        color_1_4 = ColorMaster.objects.create(article=article_1, name="Green", short_name="GR")

        article_2 = ArticleMaster.objects.create(name='YarnArticle2', short_name='YA2',
                                                 blend_pct="CT50PY25RY25",
                                                 twists=200)

        color_2_1 = ColorMaster.objects.create(article=article_2, name="White", short_name="WT")
        color_2_2 = ColorMaster.objects.create(article=article_2, name="Yellow", short_name="YL")
        color_2_3 = ColorMaster.objects.create(article=article_2, name="Orange", short_name="OR")
        color_2_4 = ColorMaster.objects.create(article=article_2, name="Blue", short_name="BL")
        self.stdout.write(self.style.SUCCESS('Its done'))
