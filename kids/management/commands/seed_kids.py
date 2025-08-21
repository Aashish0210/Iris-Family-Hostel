from django.core.management.base import BaseCommand
from django.utils import timezone
from kids.models import Kid

class Command(BaseCommand):
    help = 'Create 14 sample kids with placeholder data.'

    def handle(self, *args, **options):
        data = [
            ('Aarav Sharma', 'Rahul Sharma', 10, 'A1', '98XXXXXXXX', '2024-04-15'),
            ('Sita Rai', 'Bishal Rai', 11, 'A2', '98XXXXXXXX', '2024-05-10'),
            ('Kiran Thapa', 'Hari Thapa', 9, 'A3', '98XXXXXXXX', '2024-06-05'),
            ('Nisha Karki', 'Ramesh Karki', 10, 'B1', '98XXXXXXXX', '2024-06-20'),
            ('Raju Gurung', 'Manoj Gurung', 12, 'B2', '98XXXXXXXX', '2024-07-01'),
            ('Mina Shrestha', 'Suman Shrestha', 8, 'B3', '98XXXXXXXX', '2024-07-15'),
            ('Sanjay Adhikari', 'Kiran Adhikari', 9, 'C1', '98XXXXXXXX', '2024-08-01'),
            ('Pratiksha Devkota', 'Suraj Devkota', 11, 'C2', '98XXXXXXXX', '2024-08-10'),
            ('Roshan Tamang', 'Nima Tamang', 10, 'C3', '98XXXXXXXX', '2024-08-18'),
            ('Anita Lama', 'Pemba Lama', 9, 'D1', '98XXXXXXXX', '2024-09-03'),
            ('Bibek Magar', 'Dil Magar', 12, 'D2', '98XXXXXXXX', '2024-09-20'),
            ('Kabita Subba', 'Gopal Subba', 8, 'D3', '98XXXXXXXX', '2024-10-05'),
            ('Suresh KC', 'Kamal KC', 11, 'E1', '98XXXXXXXX', '2024-10-20'),
            ('Ritika Joshi', 'Anup Joshi', 10, 'E2', '98XXXXXXXX', '2024-11-01'),
        ]
        created = 0
        for name, parent, age, room, contact, date_str in data:
            obj, was_created = Kid.objects.get_or_create(
                name=name,
                parent_name=parent,
                defaults=dict(
                    age=age,
                    room_number=room,
                    guardian_contact=contact,
                    admission_date=date_str,
                    active=True,
                )
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f'Created {created} kids (or already existed).'))
