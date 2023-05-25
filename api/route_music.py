from fastapi import APIRouter, Depends, Request, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from db.models.users import User
from db.sessions import get_db
from db.utils.music import check_file, get_file_path_from_name, save_file
from db.utils.users import get_current_user_from_token

router = APIRouter()


@router.get("/download/{filename}")
def download(
    filename: str,
    user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    path = get_file_path_from_name(filename=filename, user=user, db=db)
    return FileResponse(path=path, filename=filename, media_type="multipart/form-data")


@router.post("/upload/")
def upload_file(
    request: Request,
    file: UploadFile | None = None,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user_from_token),
):
    check_file(file=file)
    file_name = save_file(file=file, db=db, user=user)
    download_url = request.url_for("download", filename=file_name)

    return {"download_url": download_url}
