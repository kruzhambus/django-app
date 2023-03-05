from django.core.management.base import BaseCommand
import time

from psycopg2 import OperationalError as Psycopg2OperationalError

from django.db.utils import OperationalError as DjangoOperationalError
from django.core.management.base import BaseCommand # noqa

class Command(BaseCommand): # noqa
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = False
        while db_conn is False:
            try:
                self.check(databases=['default'])
                db_conn = True
            except (Psycopg2OperationalError, DjangoOperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
