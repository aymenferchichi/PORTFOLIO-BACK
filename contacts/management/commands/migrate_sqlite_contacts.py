import sqlite3
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from contacts.models import ContactMessage


class Command(BaseCommand):
	help = 'Migrate contact messages from a legacy SQLite database into the current Django database.'

	def add_arguments(self, parser):
		parser.add_argument(
			'--sqlite-path',
			default='db.sqlite3',
			help='Path to the legacy SQLite database file.',
		)

	def handle(self, *args, **options):
		sqlite_path = Path(options['sqlite_path'])

		if not sqlite_path.exists():
			raise CommandError(f'SQLite database not found: {sqlite_path}')

		connection = sqlite3.connect(sqlite_path)
		cursor = connection.cursor()

		try:
			cursor.execute(
				'''
				SELECT id, name, email, subject, phone, message, status, created_at, updated_at
				FROM contacts_contactmessage
				ORDER BY id
				'''
			)
		except sqlite3.OperationalError as error:
			raise CommandError(
				'contacts_contactmessage table was not found in the SQLite database.'
			) from error

		rows = cursor.fetchall()
		created_count = 0

		for row in rows:
			contact_message, created = ContactMessage.objects.update_or_create(
				id=row[0],
				defaults={
					'name': row[1],
					'email': row[2],
					'subject': row[3],
					'phone': row[4] or '',
					'message': row[5],
					'status': row[6],
					'created_at': row[7],
					'updated_at': row[8],
				},
			)
			if created:
				created_count += 1

		connection.close()

		self.stdout.write(
			self.style.SUCCESS(
				f'Migrated {len(rows)} contact message(s) from {sqlite_path}. Newly created: {created_count}.'
			)
		)