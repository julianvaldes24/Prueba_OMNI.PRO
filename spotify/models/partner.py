# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import requests, json


class Partner(models.Model):
    _inherit = "res.partner"

    genres = fields.Many2many(comodel_name='spotify.gender', string='Genres')
    recommended_songs = fields.Many2many(comodel_name='spotify.song', string='Recommended songs')

    @api.onchange('genres')
    def _get_recommended_songs(self):
        """
        Metodo que realiza el consumo del API para la recomendacion de canciones segun un genero o generos.

        """
        for song in self:
            if song.genres:
                auth = self.env['spotify.authentication'].search([])[0]
                genres = ""
                for gen in song.genres:
                    genres += str(gen.name + ",")
                url = "https://api.spotify.com/v1/recommendations?seed_genres=" + genres

                payload = {}
                headers = {
                    'Authorization': 'Bearer ' + auth.access_token
                }

                response = requests.request("GET", url, headers=headers, data=payload)

                if response.status_code == 200:
                    res = json.loads(response.text)
                    songs = []
                    for genre in res['tracks']:
                        artists = ','.join([x['name'] for x in genre['artists']])
                        song_spotify = self.env['spotify.song']
                        song_spotify_res = song_spotify.search([('id_track', '=', genre['id'])])

                        if not song_spotify_res.id:
                            song_spotify_res = song_spotify.create(
                                {'id_track': genre['id'], 'name': genre['name'],
                                 'url': genre['external_urls']['spotify'],
                                 'artist': artists})

                        songs.append(song_spotify_res.id)

                else:
                    raise ValidationError(_("Please try again, check your API credentials"))

                song.recommended_songs = songs
