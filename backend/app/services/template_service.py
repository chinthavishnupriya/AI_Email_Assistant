from app.database.connection import SessionLocal
from app.database.crud import (
    create_email_template,
    get_all_email_templates,
    get_email_template,
    update_email_template,
    delete_email_template,
)


def create_template(
    user_id: int,
    name: str,
    category: str,
    content: str,
):

    db = SessionLocal()

    try:

        return create_email_template(
            db=db,
            user_id=user_id,
            name=name,
            category=category,
            content=content,
        )

    finally:

        db.close()


def fetch_templates(user_id: int):

    db = SessionLocal()

    try:

        return get_all_email_templates(
            db=db,
            user_id=user_id,
        )

    finally:

        db.close()


def fetch_template(
    user_id: int,
    template_id: int,
):

    db = SessionLocal()

    try:

        return get_email_template(
            db=db,
            template_id=template_id,
            user_id=user_id,
        )

    finally:

        db.close()


def edit_template(
    user_id: int,
    template_id: int,
    name: str,
    category: str,
    content: str,
):

    db = SessionLocal()

    try:

        template = get_email_template(
            db=db,
            template_id=template_id,
            user_id=user_id,
        )

        if not template:
            return None

        return update_email_template(
            db=db,
            template=template,
            name=name,
            category=category,
            content=content,
        )

    finally:

        db.close()


def remove_template(
    user_id: int,
    template_id: int,
):

    db = SessionLocal()

    try:

        template = get_email_template(
            db=db,
            template_id=template_id,
            user_id=user_id,
        )

        if not template:
            return False

        delete_email_template(
            db=db,
            template=template,
        )

        return True

    finally:

        db.close()
