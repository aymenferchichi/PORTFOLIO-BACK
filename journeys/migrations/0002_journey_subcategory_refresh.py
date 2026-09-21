from django.db import migrations, models


def refresh_journey_entries(apps, schema_editor):
    Journey = apps.get_model('journeys', 'Journey')
    Journey.objects.update_or_create(
        slug='foundation',
        defaults={
            'year': '2020 - 2022',
            'title': 'Freelance Web Developer & Designer',
            'eyebrow': 'Independent delivery',
            'subcategory': 'experience',
            'detail': 'Managed freelance web design and development work while finishing computer science studies, balancing client communication, visual polish, and front-end execution across early portfolio and landing-page projects.',
            'summary': 'This stage built the freelance foundation: direct client responsibility, better time management, and a stronger instinct for what makes a digital surface feel more credible and better presented.',
            'focus': [
                'Early freelance website delivery with hands-on client communication.',
                'A stronger mix of design sensitivity and front-end implementation.',
                'The first portfolio and landing-page projects shaped around trust and presentation.',
            ],
            'accent': '#e1b16f',
        },
    )
    Journey.objects.update_or_create(
        slug='freelance-momentum',
        defaults={
            'year': '2022 - 2024',
            'title': 'Technical Lead & Operations Manager',
            'eyebrow': 'Agency leadership',
            'subcategory': 'experience',
            'detail': 'Led delivery and operations at Boujarra IT as a team lead and shareholder, scaling the development team, defining agile workflows, and overseeing full-stack project execution across the agency portfolio.',
            'summary': 'The work expanded from building interfaces into building systems: hiring, reviews, process design, capacity planning, and making technical delivery more consistent and profitable.',
            'focus': [
                'Scaled the web team from 2 to 9 members with clearer onboarding and KPIs.',
                'Introduced code review, CI/CD, and stronger delivery discipline.',
                'Bridged client outcomes with technical planning and team capacity.',
            ],
            'accent': '#7db39e',
        },
    )
    Journey.objects.update_or_create(
        slug='ui-ux-expansion',
        defaults={
            'year': '2023',
            'title': 'Web Developer & AI Integration Specialist',
            'eyebrow': 'AI-assisted interfaces',
            'subcategory': 'experience',
            'detail': 'Worked with leadership and ML engineers at Sentidigital to turn AI model output into usable interface components, backend task orchestration, and live feedback layers that made complex systems easier to read.',
            'summary': 'This stage sharpened how technical systems translate into user-facing clarity, especially when the product surface has to explain automation, status, and confidence in real time.',
            'focus': [
                'Integrated Celery and Django endpoints into ML-driven product flows.',
                'Translated model behavior into practical UI states and feedback loops.',
                'Built a clearer bridge between advanced systems and user trust.',
            ],
            'accent': '#b4c2ff',
        },
    )
    Journey.objects.update_or_create(
        slug='brand-and-motion',
        defaults={
            'year': '2024 - 2025',
            'title': 'Design & Development Team Lead',
            'eyebrow': 'UI/UX and team direction',
            'subcategory': 'experience',
            'detail': 'Led the UI/UX and development team at Sandlist, shaping task flow, improving design handoff quality, and directing WordPress pages and marketing surfaces so they felt more deliberate and easier to ship.',
            'summary': 'The focus moved further into design leadership: clearer visual hierarchy, better Figma-to-development translation, and more polished digital touchpoints tied to product and campaign goals.',
            'focus': [
                'Improved delivery quality across landing pages and campaign surfaces.',
                'Guided cleaner developer handoffs from design to implementation.',
                'Pushed the work toward a more authored and commercially useful visual standard.',
            ],
            'accent': '#f09f89',
        },
    )
    Journey.objects.update_or_create(
        slug='current-direction',
        defaults={
            'year': '2025 - 2026',
            'title': 'E-Commerce Project Lead & Tech Consultant',
            'eyebrow': 'Shopify growth and brand delivery',
            'subcategory': 'experience',
            'detail': 'Owned end-to-end delivery for a US e-commerce brand on Shopify, combining implementation, conversion-focused UX improvements, branding decisions, and creative production across ads and social assets.',
            'summary': 'The current direction is more client-facing and commercially precise: design that sells the right perception, interfaces that improve conversion, and delivery that connects visual polish with business intent.',
            'focus': [
                'Shopify delivery shaped around conversion and brand clarity.',
                'Creative direction across web, ads, and social campaign assets.',
                'A stronger freelance proposition built on both visual craft and execution reliability.',
            ],
            'accent': '#f0d6a4',
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='subcategory',
            field=models.CharField(choices=[('experience', 'Experience'), ('projects', 'Projects')], default='experience', max_length=20),
        ),
        migrations.RunPython(refresh_journey_entries, migrations.RunPython.noop),
    ]