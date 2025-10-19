import services.resume_service.models
import services.resume_service.shemas
import sqlalchemy.ext.asyncio


async def create_resume(
    data: services.resume_service.shemas.ResumeCreateInfo,
    db: sqlalchemy.ext.asyncio.AsyncSession,
) -> services.resume_service.models.Resume:
    """Создаёт новое резюме в базе данных."""
    new_resume = services.resume_service.models.Resume(
        name=data.name,
        phone=data.phone,
        resume_link=data.resume_link,
        email=data.email,
        confidencial=data.confidencial,
        mallings=data.mallings,
        sms_ad=data.sms_ad,
        external_id=data.external_id,
    )
    db.add(new_resume)
    await db.commit()
    await db.refresh(new_resume)
    return new_resume


async def update_resume(
    data: services.resume_service.shemas.ResumeUpdate,
    db: sqlalchemy.ext.asyncio.AsyncSession,
) -> services.resume_service.models.Resume:
    """Обновляет резюме по его ID."""
    result = await db.execute(
        sqlalchemy.select(services.resume_service.models.Resume).where(
            services.resume_service.models.Resume.id == data.id
        )
    )
    resume: services.resume_service.models.Resume | None = (
        result.scalar_one_or_none()
    )
    if not resume:
        raise ValueError(f"Resume with id {data.id} not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(resume, field, value)
    await db.commit()
    await db.refresh(resume)
    return resume


async def delete_resume(
    resume_id: int, db: sqlalchemy.ext.asyncio.AsyncSession
) -> None:
    result = await db.execute(
        sqlalchemy.select(services.resume_service.models.Resume).where(
            services.resume_service.models.Resume.id == resume_id
        )
    )
    resume: services.resume_service.models.Resume | None = (
        result.scalar_one_or_none()
    )
    if not resume:
        raise ValueError(f"Resume with id {resume_id} not found")
    await db.delete(resume)
    await db.commit()
