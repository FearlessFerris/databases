"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length







class PlaylistForm(FlaskForm):
    """ Form for adding playlists """

    name = StringField('Playlist Name', validators = [InputRequired(), Length( min = 1 )], render_kw = { 'placeholder' : 'Ex. Notorious B.I.G.' })
    description = StringField('Description', validators = [InputRequired(), Length( min = 1, max = 250 )], render_kw = { 'placeholder' : 'Ex. This is a chill vibes playlist' })









class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form

    title = StringField( 'Song Title', validators = [InputRequired(), Length( min = 1, max = 40 )], render_kw = { 'placeholder' : 'Ex. Wish You Were Here' })
    artist = StringField( 'Artist Name', validators = [InputRequired(), Length( min = 1, max = 40 )], render_kw = { 'placeholder' : 'Ex. Pink Floyd' })









# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField( 'Song To Add', coerce = int )
