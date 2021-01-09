# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import base64, requests, json, datetime


class SpotifyAuthentication(models.Model):
    _name = 'spotify.authentication'
    _description = 'table that stores the authentication record to the spotify API'

    client_id = fields.Char(string='Client ID', required=True)
    client_secret = fields.Char(string='Client Secret', required=True)
    client = fields.Char(string='Client', required=False)
    url = fields.Char(string='Url', required=True, default='https://accounts.spotify.com/api/token')
    grant_type = fields.Char(string='Grant type', required=True, default='client_credentials')
    access_token = fields.Char(string='Access token', required=False)
    token_type = fields.Char(string='Token type', required=False)
    expires_in = fields.Datetime(string='Expires in', required=False)
    scope = fields.Char(string='Scope', required=False)

    @api.onchange('client_id', 'client_secret')
    def _client(self):
        """
        Metodo que crea cadena base64 a partir de client_id y client_secret  para la autenticacion en el API
        """
        for auth in self:
            if auth.client_id and auth.client_secret:
                auth.client = base64.b64encode(str(auth.client_id + ":" + auth.client_secret).encode("UTF-8"))

    def login(self):
        """
        Metodo que consume el API para el logeo obteniendo principalmente un token barer para transaccionalidades dentro del API
        """
        url = self.url
        payload = 'grant_type=' + self.grant_type
        headers = {
            'Authorization': 'Basic ' + self.client,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            res = json.loads(response.text)
            self.access_token = res['access_token']
            self.token_type = res['token_type']
            expires = datetime.datetime.now()
            self.expires_in = expires + datetime.timedelta(seconds=int(res['expires_in']))
            self.scope = res['scope']
        else:
            raise ValidationError(_("Please try again, check your API credentials"))
