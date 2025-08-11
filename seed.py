from faker import Faker
from random import choice, randint
# from datetime import datetime, timedelta
from app import app, db
from models import User, Video, Lyrics, Score, SavedSong, VideoStats

fake = Faker()

with app.app_context():
    
    db.create_all()
    print("🌱 Seeding database...")
    
    db.session.query(SavedSong).delete()
    db.session.query(VideoStats).delete()
    db.session.query(Video).delete()
    db.session.query(Lyrics).delete()
    db.session.query(Score).delete()
    db.session.query(User).delete()

    roles = ["composer", "artist", "viewer"]
    users = []
    for _ in range(15):
        user = User(
            username=fake.user_name(),
            email=fake.unique.email(),
            password_hash=fake.sha256(),
            role=choice(roles),
            created_at=fake.date_time_this_year()
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()

    
    lyrics_list = []
    for _ in range(15):
        lyric = Lyrics(
            content=fake.paragraph(nb_sentences=5),
            language=choice(["English", "Latin", "Swahili"])
        )
        lyrics_list.append(lyric)
        db.session.add(lyric)
    db.session.commit()

    
    scores_list = []
    for _ in range(15):
        score = Score(
            file_url=f"https://example.com/scores/{fake.word()}.pdf",
            format="PDF"
        )
        scores_list.append(score)
        db.session.add(score)
    db.session.commit()

    
    videos = []
    for _ in range(15):
        video = Video(
            title=fake.sentence(nb_words=4),
            description=fake.paragraph(nb_sentences=3),
            video_url=f"https://example.com/videos/{fake.word()}.mp4",
            uploader_id=choice(users).id,
            upload_date=fake.date_time_this_year(),
            lyrics_id=choice(lyrics_list).id,
            score_id=choice(scores_list).id,
            views=randint(50, 5000),
            likes=randint(10, 2000)
        )
        videos.append(video)
        db.session.add(video)
    db.session.commit()

    
    for _ in range(15):
        saved = SavedSong(
            user_id=choice(users).id,
            video_id=choice(videos).id,
            saved_at=fake.date_time_this_year()
        )
        db.session.add(saved)
    db.session.commit()

    for _ in range(15):
        stat = VideoStats(
            video_id=choice(videos).id,
            date=fake.date_this_year(),
            views=randint(100, 10000),
            likes=randint(10, 500)
        )
        db.session.add(stat)
    db.session.commit()

    print("✅ Seeding complete!")
