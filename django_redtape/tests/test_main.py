from django.test import TestCase
from django_redtape.models import RedTape
from django_redtape.tools import sanitize
from datetime import timedelta


class StampTestCase(TestCase):
    def setUp(self):
        sanitize.main()

    def test_has_dts(self):
        subject = RedTape.objects.create()
        self.assertFalse(subject.dts_inserted is None)

    def test_not_filtered(self):
        subject = RedTape.objects.create()
        self.assertEqual(RedTape.objects.all().count(), 1)

    def test_future_filtered(self):
        subject = RedTape.objects.create()
        dts = subject.dts_inserted + timedelta(seconds=10)
        subject.dts_activate = dts
        subject.save()
        self.assertEqual(RedTape.objects.all().count(), 0)

    def test_archive_filtered(self):
        subject = RedTape.objects.create()
        dts = subject.dts_inserted - timedelta(seconds=10)
        subject.dts_archived = dts
        subject.save()
        self.assertEqual(RedTape.objects.all().count(), 0)

    def test_all_objects(self):
        self.test_future_filtered()
        self.assertEqual(RedTape.all_objects.all().count(), 1)
