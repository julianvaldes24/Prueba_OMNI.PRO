from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import requests, json


class SpotifyAutomation(models.TransientModel):
    _name = 'spotify.automation'
    _description = 'Model used to automate the fetch of data from spotify'

    date = fields.Date(string='Date', required=False)

    def fill_genres_spotify(self):
        """
        Metodo corrido con un cron para obtener generos musicales del API y almacenarlos en un modelo spotify.genres
        :rtype: object
        """
        auth = self.env['spotify.authentication'].search([])[0]

        url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"

        payload = {}
        headers = {
            'Authorization': 'Bearer ' + auth.access_token
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            res = json.loads(response.text)
            for genre in res['genres']:
                self.env['spotify.gender'].create({'name': genre})
        else:
            raise ValidationError(_("Please try again, check your API credentials"))

    def authentication(self):
        """
        Metodo corrido con un cron para renovar el token de auth en el API
        """
        auth = self.env['spotify.authentication'].search([])[0]
        auth.login()
