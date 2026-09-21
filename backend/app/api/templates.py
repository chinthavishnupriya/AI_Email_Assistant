from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.database.models import User
from app.dependencies import get_current_user
from app.schemas.template import (
    TemplateCreate,
    TemplateUpdate,
    TemplateResponse,
)
from app.services.template_service import (
    create_template,
    fetch_templates,
    fetch_template,
    edit_template,
    remove_template,
)


router = APIRouter(
    prefix="/templates",
    tags=["Templates"]
)

SAFE_ERROR_MESSAGE = "Unable to complete the template operation. Please try again."


@router.post(
    "/",
    response_model=TemplateResponse
)
def create_template_api(
    request: TemplateCreate,
    current_user: User = Depends(get_current_user),
):

    try:

        template = create_template(
            user_id=current_user.id,
            name=request.name,
            category=request.category,
            content=request.content,
        )

        return template

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=SAFE_ERROR_MESSAGE
        )


@router.get(
    "/",
    response_model=List[TemplateResponse]
)
def get_templates(
    current_user: User = Depends(get_current_user),
):

    try:

        return fetch_templates(current_user.id)

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=SAFE_ERROR_MESSAGE
        )


@router.get(
    "/{template_id}",
    response_model=TemplateResponse
)
def get_template(
    template_id: int,
    current_user: User = Depends(get_current_user),
):

    try:

        template = fetch_template(
            user_id=current_user.id,
            template_id=template_id,
        )

        if not template:

            raise HTTPException(
                status_code=404,
                detail="Template not found"
            )

        return template

    except HTTPException:

        raise

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=SAFE_ERROR_MESSAGE
        )


@router.put(
    "/{template_id}",
    response_model=TemplateResponse
)
def update_template(
    template_id: int,
    request: TemplateUpdate,
    current_user: User = Depends(get_current_user),
):

    try:

        template = edit_template(
            user_id=current_user.id,
            template_id=template_id,
            name=request.name,
            category=request.category,
            content=request.content,
        )

        if not template:

            raise HTTPException(
                status_code=404,
                detail="Template not found"
            )

        return template

    except HTTPException:

        raise

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=SAFE_ERROR_MESSAGE
        )


@router.delete(
    "/{template_id}"
)
def delete_template(
    template_id: int,
    current_user: User = Depends(get_current_user),
):

    try:

        deleted = remove_template(
            user_id=current_user.id,
            template_id=template_id,
        )

        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Template not found"
            )

        return {
            "message": "Template deleted successfully"
        }

    except HTTPException:

        raise

    except Exception:

        raise HTTPException(
            status_code=500,
            detail=SAFE_ERROR_MESSAGE
        )
