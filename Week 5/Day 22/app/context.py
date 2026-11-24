
from jose import jwt, JWTError

from app.config import settings
from app.models import User


async def get_context_value(request, data):
    # Use the database session created for this request.
    db = request.state.db

    # Read the token from the Authorization header.
    authorization = request.headers.get("Authorization")

    current_user = None

    if authorization:
        try:
            scheme, token = authorization.split()

            if scheme.lower() == "bearer":
                # Verify the token and retrieve its payload.
                payload = jwt.decode(
                    token,
                    settings.SECRET_KEY,
                    algorithms=[settings.ALGORITHM]
                )

                user_id = payload.get("sub")

                if user_id is not None:
                    current_user = db.query(User).filter(
                        User.id == int(user_id)
                    ).first()

        except (JWTError, ValueError, TypeError):
            # Treat invalid tokens as unauthenticated requests.
            current_user = None

    return {
        "db": db,
        "current_user": current_user
    }
