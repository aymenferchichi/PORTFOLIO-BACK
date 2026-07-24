from django.db import migrations, models


def seed_journeys(apps, schema_editor):
    Journey = apps.get_model('journeys', 'Journey')
    entries = [
        {
            'slug': 'foundation',
            'year': '2019',
            'title': 'Foundation',
            'eyebrow': 'Front-end beginnings',
            'detail': 'Built the first front-end projects and learned how layout, motion, and code shape perception together.',
            'summary': 'The first stage was about learning how interface structure, typography, and browser behavior combine into a clear visual language.',
            'focus': [
                'Early responsive page builds and interface experiments.',
                'A stronger instinct for spacing, pacing, and clean hierarchy.',
                'The first connection between implementation and design quality.',
            ],
            'accent': '#e1b16f',
            'display_order': 1,
        },
        {
            'slug': 'freelance-momentum',
            'year': '2021',
            'title': 'Freelance momentum',
            'eyebrow': 'Client-facing work',
            'detail': 'Started shipping client-facing work with cleaner structure, stronger interfaces, and more deliberate visual polish.',
            'summary': 'Freelance work pushed the process from experimentation into delivery, where structure, trust, and finish had to become consistent.',
            'focus': [
                'Cleaner delivery across landing pages and presentation surfaces.',
                'More deliberate hierarchy and calmer visual systems.',
                'A tighter bridge between what looks premium and what converts.',
            ],
            'accent': '#7db39e',
            'display_order': 2,
        },
        {
            'slug': 'ui-ux-expansion',
            'year': '2023',
            'title': 'UI / UX expansion',
            'eyebrow': 'Product thinking',
            'detail': 'Moved deeper into product thinking, interaction flow, and scalable visual systems for digital experiences.',
            'summary': 'The work moved beyond individual screens into product behavior, navigation logic, and the kinds of interface decisions that build trust over time.',
            'focus': [
                'More attention to product flow and user confidence.',
                'UI systems that scale beyond a single polished screen.',
                'Sharper balance between aesthetics and decision clarity.',
            ],
            'accent': '#b4c2ff',
            'display_order': 3,
        },
        {
            'slug': 'brand-and-motion',
            'year': '2024',
            'title': 'Brand and motion',
            'eyebrow': 'Visual system expansion',
            'detail': 'Graphic design and video editing became part of one coherent creative workflow instead of separate outputs.',
            'summary': 'Brand direction and motion stopped being side skills and became part of one connected system for shaping how work feels across formats.',
            'focus': [
                'Brand visuals that hold up across digital surfaces.',
                'Motion used to reinforce tone and pacing, not distract.',
                'A stronger authored feel across campaigns, pages, and assets.',
            ],
            'accent': '#f09f89',
            'display_order': 4,
        },
        {
            'slug': 'current-direction',
            'year': 'Now',
            'title': 'Current direction',
            'eyebrow': 'Premium portfolio systems',
            'detail': 'Designing premium portfolio sites, refined digital surfaces, and interactive experiences with a stronger authored edge.',
            'summary': 'The current direction is more selective and more ambitious: premium portfolio experiences, clearer positioning, and interfaces that feel intentional at first glance.',
            'focus': [
                'Portfolio work with stronger visual authority.',
                'Interactive storytelling that feels designed, not assembled.',
                'A tighter mix of code, interface, brand, and motion craft.',
            ],
            'accent': '#f0d6a4',
            'display_order': 5,
        },
    ]

    for entry in entries:
        Journey.objects.update_or_create(slug=entry['slug'], defaults=entry)


def unseed_journeys(apps, schema_editor):
    Journey = apps.get_model('journeys', 'Journey')
    Journey.objects.all().delete()


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('year', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=160)),
                ('eyebrow', models.CharField(max_length=160)),
                ('detail', models.TextField()),
                ('summary', models.TextField()),
                ('focus', models.JSONField(blank=True, default=list)),
                ('accent', models.CharField(max_length=20)),
                ('display_order', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ['display_order'],
            },
        ),
        migrations.RunPython(seed_journeys, unseed_journeys),
    ]