"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()






# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""


    
    db.app = app
    db.init_app(app)






class Playlist(db.Model):
    """ Playlist Model """

    __tablename__ = 'playlist'

    id = db.Column( db.Integer, primary_key = True, nullable = False, autoincrement = True )
    name = db.Column( db.String(45), nullable = False )
    description = db.Column( db.Text, nullable = False )
    
    songs = db.relationship( 'Song', secondary = 'playlist_song', backref = 'playlist')




    @classmethod
    def create_playlist( cls, name, description ):
        """ Creates a new playlist """

        new_playlist = Playlist( name = name, description = description )
        db.session.add(new_playlist)
        db.session.commit()
    
        return new_playlist
    

    def __repr__(self):
        """ Representation Method """
        return f'Playlist {self.id} {self.name} {self.description} >'












class Song(db.Model):
    """ Song """

    __tablename__ = 'songs'

    id = db.Column( db.Integer, primary_key = True, nullable = False, autoincrement = True )
    title = db.Column( db.String(45), unique = True, nullable = False )
    artist = db.Column( db.String(45), nullable = False )

    
    
    


    @classmethod
    def add_song( cls, title, artist ):
        """ Adds a new song to the database """

        add_song = Song( title = title, artist = artist )
        db.session.add(add_song)
        db.session.commit()

        return add_song



    def __repr__(self):
        """ Representation Method """
        return f'Song {self.id} {self.title} {self.artist} >'














class PlaylistSong(db.Model):
    """ Playlist Song Mapping """

    __tablename__ = 'playlist_song'

    id = db.Column( db.Integer, primary_key = True, nullable = False, autoincrement = True )
    playlist_id = db.Column( db.Integer, db.ForeignKey( 'playlist.id' ), primary_key = True )
    song_id = db.Column( db.Integer, db.ForeignKey( 'songs.id' ), primary_key = True )
    



    playlist = db.relationship( 'Playlist', backref = 'playlist_song' )
    song = db.relationship( 'Song', backref = 'song_info' )
  

    def __repr__(self):
        """ Representation Method """
        return f'<PlaylistSong {self.id} {self.playlist_id} {self.song_id} >'
    










