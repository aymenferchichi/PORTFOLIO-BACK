from django.db import migrations


def refresh_product_marketing_stories(apps, schema_editor):
    Journey = apps.get_model('journeys', 'Journey')
    updates = {
        'foundation': {
            'year': '2020 - 2022',
            'title': 'Freelance Web Delivery Foundations',
            'eyebrow': 'Independent delivery',
            'subcategory': 'experience',
            'detail': 'Built early freelance websites and landing pages with a growing focus on clearer headlines, stronger section flow, and front-end execution that made the offer feel more trustworthy on first view.',
            'summary': 'This stage established the core product-marketing instinct: better page structure and cleaner implementation make even early offers feel easier to trust.',
            'focus': [
                'Shaped early landing pages around clearer messaging and stronger visual hierarchy.',
                'Learned how front-end execution directly affects trust, readability, and conversion intent.',
                'Built the first repeatable habits around responsive presentation and proof-driven sections.',
            ],
            'accent': '#e1b16f',
        },
        'freelance-momentum': {
            'year': '2022 - 2024',
            'title': 'Agency Delivery and Growth Systems',
            'eyebrow': 'Agency leadership',
            'subcategory': 'experience',
            'detail': 'Led delivery and operations with a stronger focus on systems, helping teams ship web projects with clearer process, more reliable implementation, and better alignment between what clients wanted and what the product surface needed to communicate.',
            'summary': 'The outcome was not just better delivery discipline. It was clearer commercial execution: stronger project flow, better stakeholder confidence, and more consistent digital outputs.',
            'focus': [
                'Improved how web projects moved from scope to delivery with less friction.',
                'Introduced tighter review and implementation standards that protected page quality.',
                'Connected technical planning more closely to client-facing outcomes and presentation clarity.',
            ],
            'accent': '#7db39e',
        },
        'ui-ux-expansion': {
            'year': '2023',
            'title': 'AI Product UX and Interface Translation',
            'eyebrow': 'AI-assisted interfaces',
            'subcategory': 'experience',
            'detail': 'Worked on AI-supported product experiences where model output had to become something users could actually understand, trust, and act on through better interface states, clearer feedback, and tighter system-to-UI translation.',
            'summary': 'This stage sharpened the ability to turn technical complexity into product clarity, especially on SaaS surfaces where confidence and comprehension are critical.',
            'focus': [
                'Mapped ML-driven behavior into clearer product states and user-facing feedback.',
                'Reduced ambiguity in interface flow by making automation easier to read and trust.',
                'Strengthened product UX for systems that depend on clarity, confidence, and fast interpretation.',
            ],
            'accent': '#b4c2ff',
        },
        'brand-and-motion': {
            'year': '2024 - 2025',
            'title': 'Design Systems and Marketing Surface Leadership',
            'eyebrow': 'UI/UX and team direction',
            'subcategory': 'experience',
            'detail': 'Led design and development work across marketing pages, supporting visuals, and production flow so launches felt more coherent and digital surfaces carried the same strategic signal across design and implementation.',
            'summary': 'The value here was alignment: stronger hierarchy, better handoff quality, and marketing pages that supported the offer with more consistency.',
            'focus': [
                'Improved the quality of landing pages and supporting campaign surfaces.',
                'Created cleaner design-to-development translation for faster shipping and fewer compromises.',
                'Raised the visual and structural standard of client-facing marketing work.',
            ],
            'accent': '#f09f89',
        },
        'current-direction': {
            'year': '2025 - 2026',
            'title': 'Conversion-Focused Commerce and Growth Delivery',
            'eyebrow': 'Conversion systems',
            'subcategory': 'experience',
            'detail': 'Owned end-to-end digital delivery with a focus on conversion-aware UX, clearer merchandising signals, stronger page structure, and supporting creative that helped the brand feel more credible across web and campaign touchpoints.',
            'summary': 'The current direction is centered on commercially useful design: product and service pages that explain the offer faster, reduce friction, and strengthen the path to action.',
            'focus': [
                'Improved conversion surfaces through clearer structure, stronger proof placement, and cleaner calls to action.',
                'Connected web execution with campaign and brand assets so the offer felt more consistent across channels.',
                'Turned visual polish into something commercially useful by supporting trust and action, not just aesthetics.',
            ],
            'accent': '#f0d6a4',
        },
    }

    for slug, defaults in updates.items():
        Journey.objects.update_or_create(slug=slug, defaults=defaults)


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0002_journey_subcategory_refresh'),
    ]

    operations = [
        migrations.RunPython(
            refresh_product_marketing_stories,
            migrations.RunPython.noop,
        ),
    ]