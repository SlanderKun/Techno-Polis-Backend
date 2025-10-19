import services.university_service.models
import services.university_service.shemas
import sqlalchemy.ext.asyncio


async def create_university(
    data: services.university_service.shemas.UniversityCreateSchema,
    db: sqlalchemy.ext.asyncio.AsyncSession,
) -> services.university_service.models.UniversityInfo:
    """Создаёт новый университет в базе данных."""
    new_university = services.university_service.models.UniversityInfo(
        representative_name=data.representative_name,
        representative_surname=data.representative_surname,
        university_name=data.company_name,
        logo=data.logo,
        inn=data.inn,
        contact_number=data.contact_number,
        contact_email=data.contact_email,
    )
    db.add(new_university)
    await db.commit()
    await db.refresh(new_university)
    return new_university


async def update_university(
    data: services.university_service.shemas.UniversityUpdateSchema,
    db: sqlalchemy.ext.asyncio.AsyncSession,
) -> services.university_service.models.UniversityInfo:
    """Обновляет университет по его ID."""
    result = await db.execute(
        sqlalchemy.select(
            services.university_service.models.UniversityInfo
        ).where(
            services.university_service.models.UniversityInfo.id == data.id
        )
    )
    university: services.university_service.models.UniversityInfo | None = (
        result.scalar_one_or_none()
    )
    if not university:
        raise ValueError(f"university with id {data.id} not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(university, field, value)
    await db.commit()
    await db.refresh(university)
    return university


async def delete_university(
    university_id: int, db: sqlalchemy.ext.asyncio.AsyncSession
) -> None:
    result = await db.execute(
        sqlalchemy.select(
            services.university_service.models.UniversityInfo
        ).where(
            services.university_service.models.UniversityInfo.id
            == university_id
        )
    )
    university: services.university_service.models.UniversityInfo | None = (
        result.scalar_one_or_none()
    )
    if not university:
        raise ValueError(f"university with id {university_id} not found")
    await db.delete(university)
    await db.commit()
