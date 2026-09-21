from django.db import migrations, models


def seed_portfolio_proof_fields(apps, schema_editor):
    Journey = apps.get_model('journeys', 'Journey')
    updates = {
        'foundation': {
            'title': 'Freelance foundation',
            'eyebrow': 'Early client work',
            'detail': 'Built early freelance websites and landing pages while learning how structure, spacing, and front-end finish affect the way clients judge quality.',
            'summary': 'This stage built the first reliable habits: clearer layouts, calmer visual rhythm, and delivery that felt more client-ready with each project.',
            'client_label': 'Early freelance clients',
            'project_scope': 'Landing pages and portfolio websites',
            'outcome_highlight': 'Built the first projects that felt clear, polished, and ready for real clients.',
            'focus': [
                'Responsive page builds shaped around clarity and clean presentation.',
                'Stronger attention to hierarchy, spacing, and the way details affect trust.',
                'The first freelance projects that connected design decisions with delivery quality.',
            ],
            'deliverables': ['Responsive layouts', 'Front-end implementation', 'Visual cleanup'],
        },
        'freelance-momentum': {
            'title': 'Freelance momentum',
            'eyebrow': 'Client-facing delivery',
            'detail': 'Took on more responsibility in real client work, improving the way projects were planned, presented, and shipped across websites and digital touchpoints.',
            'summary': 'The work moved from experimentation into dependable delivery, where clients needed clearer communication, better structure, and a more polished result.',
            'client_label': 'Growing freelance and agency clients',
            'project_scope': 'Websites, landing pages, and project delivery',
            'outcome_highlight': 'Turned early freelance work into a more consistent and client-trustworthy process.',
            'focus': [
                'Cleaner website delivery across client-facing pages and presentation surfaces.',
                'Better project structure, stronger hierarchy, and more dependable execution.',
                'A clearer bridge between what looks polished and what helps clients feel confident hiring.',
            ],
            'deliverables': ['Website delivery', 'UI refinements', 'Client communication'],
        },
        'ui-ux-expansion': {
            'title': 'UI / UX expansion',
            'eyebrow': 'Interface thinking',
            'detail': 'Moved deeper into interface decisions, user flow, and practical UX work so pages and product surfaces felt easier to understand and use.',
            'summary': 'This stage expanded the work beyond visuals into the decisions that help people move through an interface with more confidence.',
            'client_label': 'Product and service teams',
            'project_scope': 'UI systems and interface refinement',
            'outcome_highlight': 'Improved the balance between polished visuals and interfaces that feel easier to navigate.',
            'focus': [
                'More attention to user flow, clarity, and interface confidence.',
                'UI systems designed to stay organized beyond a single polished screen.',
                'A sharper balance between aesthetics and ease of use.',
            ],
            'deliverables': ['UI systems', 'UX flow improvements', 'Interface polish'],
        },
        'brand-and-motion': {
            'title': 'Brand and motion',
            'eyebrow': 'Visual direction',
            'detail': 'Expanded into brand visuals and motion work so websites, assets, and supporting media felt more cohesive and better presented.',
            'summary': 'Brand and motion became part of one connected workflow, helping the work feel more intentional across pages, campaigns, and presentation materials.',
            'client_label': 'Brands and growing teams',
            'project_scope': 'Visual direction, motion, and supporting assets',
            'outcome_highlight': 'Raised the overall presentation quality by making pages and assets feel more consistent together.',
            'focus': [
                'Brand visuals that hold together across multiple digital surfaces.',
                'Motion used to support tone and pacing without becoming distracting.',
                'A stronger authored feel across websites, assets, and client presentation.',
            ],
            'deliverables': ['Brand visuals', 'Motion support', 'Presentation assets'],
        },
        'current-direction': {
            'title': 'Current direction',
            'eyebrow': 'Premium freelance presentation',
            'detail': 'The current focus is on building cleaner, more polished portfolio websites and digital experiences that help future clients feel the quality quickly.',
            'summary': 'The direction is more selective and more refined: present the work clearly, remove friction, and show enough polish that a future client can trust the process.',
            'client_label': 'Freelance clients and Upwork leads',
            'project_scope': 'Portfolio sites, redesigns, and polished web experiences',
            'outcome_highlight': 'Present the work with enough clarity and finish that future clients feel comfortable hiring.',
            'focus': [
                'Portfolio work with stronger visual authority and cleaner structure.',
                'Interactive storytelling that feels intentional rather than overloaded.',
                'A tighter mix of design, code, brand awareness, and delivery discipline.',
            ],
            'deliverables': ['Portfolio design', 'Front-end delivery', 'Case-study presentation'],
        },
    }

    for slug, defaults in updates.items():
        Journey.objects.update_or_create(slug=slug, defaults=defaults)


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0003_product_marketing_story_refresh'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='client_label',
            field=models.CharField(blank=True, default='', max_length=160),
        ),
        migrations.AddField(
            model_name='journey',
            name='deliverables',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='journey',
            name='outcome_highlight',
            field=models.CharField(blank=True, default='', max_length=240),
        ),
        migrations.AddField(
            model_name='journey',
            name='project_scope',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.RunPython(seed_portfolio_proof_fields, migrations.RunPython.noop),
    ]