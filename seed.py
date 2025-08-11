from datetime import date
from config import create_app, db
from models import User, Video, Lyrics, Score, SavedSong, VideoStats

# Create the Flask app instance
app = create_app()

def seed_data():
    with app.app_context():
        # Reset database
        db.drop_all()
        db.create_all()

        # --- Users ---
        user1 = User(username="john_doe", email="john@example.com", role="user")
        user1.password_hash = "password123"

        user2 = User(username="admin_girl", email="admin@example.com", role="admin")
        user2.password_hash = "securepass"

        user3 = User(username="choir_leader", email="choir@example.com", role="user")
        user3.password_hash = "sing4joy"

        db.session.add_all([user1, user2, user3])
        db.session.commit()

        # --- Lyrics ---
        lyrics1 = Lyrics(content="Amazing grace, how sweet the sound...", language="English")
        lyrics2 = Lyrics(content="Bwana u mwema...", language="Swahili")

        db.session.add_all([lyrics1, lyrics2])
        db.session.commit()

        # --- Scores ---
        score1 = Score(file_url="https://example.com/scores/amazing_grace.pdf", format="PDF")
        score2 = Score(file_url="https://example.com/scores/bwana_u_mwema.pdf", format="PDF")

        db.session.add_all([score1, score2])
        db.session.commit()

        # --- Videos ---
        video1 = Video(
            title="Amazing Grace",
            description="A heartfelt rendition of Amazing Grace",
            video_url="https://example.com/videos/amazing_grace.mp4",
            uploader_id=user1.id,
            lyrics_id=lyrics1.id,
            score_id=score1.id,
            views=150,
            likes=25
        )

        video2 = Video(
            title="Bwana U Mwema",
            description="Swahili worship song",
            video_url="https://example.com/videos/bwana_u_mwema.mp4",
            uploader_id=user3.id,
            lyrics_id=lyrics2.id,
            score_id=score2.id,
            views=200,
            likes=40
        )

        db.session.add_all([video1, video2])
        db.session.commit()

        # --- Saved Songs ---
        saved1 = SavedSong(user_id=user1.id, video_id=video2.id)
        saved2 = SavedSong(user_id=user3.id, video_id=video1.id)

        db.session.add_all([saved1, saved2])
        db.session.commit()

        # --- Video Stats ---
        stat1 = VideoStats(video_id=video1.id, date=date.today(), views=150, likes=25)
        stat2 = VideoStats(video_id=video2.id, date=date.today(), views=200, likes=40)

        db.session.add_all([stat1, stat2])
        db.session.commit()

        print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
