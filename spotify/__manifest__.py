# -*- coding: utf-8 -*-
{
    'name': "Spotify",
    'description': 'Integration with the Spotify API',
    'summary': 'Integration with the Spotify API',
    'author': "Julián Valdés",
    'website': "",
    'category': 'Music',
    'version': '14.0.1',
    'depends': ['contacts'],
    'application': False,
    'data': [
        'security/ir.model.access.csv',
        'views/spotify_authentication.xml',
        'views/spotify_automation.xml',
        'views/spotify_gender.xml',
        'views/spotify_song.xml',
        'views/partner.xml'
    ],
}
