from datetime import datetime
from serializer_mixin import db, SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    videos = db.relationship('Video', backref='uploader', lazy=True)
    saved_songs = db.relationship('SavedSong', backref='user', lazy=True)


class Video(db.Model, SerializerMixin):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    video_url = db.Column(db.String(255), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

    lyrics_id = db.Column(db.Integer, db.ForeignKey('lyrics.id'))
    score_id = db.Column(db.Integer, db.ForeignKey('scores.id'))

    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)


class Lyrics(db.Model, SerializerMixin):
    __tablename__ = 'lyrics'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), default='English')

    videos = db.relationship('Video', backref='lyrics', lazy=True)


class Score(db.Model, SerializerMixin):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    file_url = db.Column(db.String(255), nullable=False)
    format = db.Column(db.String(50), default='PDF')

    videos = db.relationship('Video', backref='score', lazy=True)


class SavedSong(db.Model, SerializerMixin):
    __tablename__ = 'saved_songs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'), nullable=False)
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)

    video = db.relationship('Video', backref='saved_by', lazy=True)


class VideoStats(db.Model, SerializerMixin):
    __tablename__ = 'video_stats'

    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
