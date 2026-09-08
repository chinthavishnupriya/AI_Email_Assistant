from sqlalchemy.orm import Session

from app.database.models import (
    User,
    EmailHistory,
    EmailTemplate,
)


# =====================================
# USER CRUD
# =====================================

def get_user_by_email(
    db: Session,
    email: str,
):

    return db.query(User).filter(
        User.email == email
    ).first()


def create_user(
    db: Session,
    full_name,
    email,
    password,
):

    user = User(
        full_name=full_name,
        email=email,
        password=password,
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


# =====================================
# EMAIL HISTORY CRUD
# =====================================

def create_email_history(
    db: Session,
    user_id: int,
    feature: str,
    user_input: str,
    ai_output: str,
):

    history = EmailHistory(

        user_id=user_id,

        feature=feature,

        user_input=user_input,

        ai_output=ai_output,

    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return history


def get_all_email_history(
    db: Session,
    user_id: int,
):

    return (

        db.query(EmailHistory)

        .filter(EmailHistory.user_id == user_id)

        .order_by(
            EmailHistory.created_at.desc()
        )

        .all()

    )
# =====================================
# EMAIL TEMPLATE CRUD
# =====================================

def create_email_template(
    db: Session,
    user_id: int,
    name: str,
    category: str,
    content: str,
):

    template = EmailTemplate(
        user_id=user_id,
        name=name,
        category=category,
        content=content,
    )

    db.add(template)

    db.commit()

    db.refresh(template)

    return template


def get_all_email_templates(
    db: Session,
    user_id: int,
):

    return (
        db.query(EmailTemplate)
        .filter(
            EmailTemplate.user_id == user_id
        )
        .order_by(
            EmailTemplate.created_at.desc()
        )
        .all()
    )


def get_email_template(
    db: Session,
    template_id: int,
    user_id: int,
):

    return (
        db.query(EmailTemplate)
        .filter(
            EmailTemplate.id == template_id,
            EmailTemplate.user_id == user_id,
        )
        .first()
    )


def update_email_template(
    db: Session,
    template: EmailTemplate,
    name: str,
    category: str,
    content: str,
):

    template.name = name
    template.category = category
    template.content = content

    db.commit()

    db.refresh(template)

    return template


def delete_email_template(
    db: Session,
    template: EmailTemplate,
):

    db.delete(template)

    db.commit()
