# Ishikawa Kazuya Site Clone

Clone of https://ishikawakazuya.net/

## Structure

```
ishikawa-kazuya/
├── templates/
│   └── clone.html              # Main clone template
├── components/                 # Jinja2 macro components
│   ├── base.html
│   ├── header.html
│   ├── hero.html
│   ├── idea.html
│   ├── content.html
│   ├── collaboration.html
│   ├── awards.html
│   ├── books.html
│   ├── community.html
│   ├── media.html
│   ├── sns.html
│   ├── services.html
│   ├── contact.html
│   └── footer.html
├── assets/
│   └── images/                 # Downloaded images from original
│       ├── profile.webp
│       ├── logo.webp
│       ├── idea1-12.webp
│       ├── content1-4.webp
│       ├── collab1-6.webp
│       └── book1-2.webp
└── screenshots/
    ├── original/               # Original site reference
    └── current/                # Current clone state
```

## Pages

| Page | URL | Slug |
|------|-----|------|
| Homepage | / | `home` |

## Sections

- hero, idea, content, collab, awards, books, community, media, sns, services, contact, footer
