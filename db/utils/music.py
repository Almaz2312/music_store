import os

from fastapi import HTTPException, UploadFile, status
from pydub import AudioSegment
from sqlalchemy.orm import Session

from core.config import settings
from db.models.music import Music
from db.models.users import User


def save_file(file: UploadFile, db: Session, user: User):
    mp3_file_name = convert_to_mp3(file=file, user=user)

    music = Music(filename=mp3_file_name, owner=user)
    get_file_path(music=music, user=user)
    db.add(music)
    db.commit()
    db.refresh(music)

    return mp3_file_name


def check_file(file: UploadFile):
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No file sent"
        )
    if file.content_type != "audio/wav":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only WAV files are allowed",
        )

    return file


def get_file_path_from_name(filename: str, user: User):
    os.makedirs(settings.BASE_DIR / "media" / user.username, exist_ok=True)
    filepath = settings.BASE_DIR / "media" / user.username / filename
    return filepath


def get_file_path(music, user: User):
    os.makedirs(settings.BASE_DIR / "media" / user.username, exist_ok=True)
    path = settings.BASE_DIR / "media" / user.username / music.filename
    return path


def convert_to_mp3(file: UploadFile, user: User):
    mp3_filename = os.path.splitext(file.filename)[0] + ".mp3"
    mp3_file_path = get_file_path_from_name(mp3_filename, user=user)

    audio = AudioSegment.from_file(file.file, format="png")
    audio.export(mp3_file_path, format="mp3")

    return mp3_filename
