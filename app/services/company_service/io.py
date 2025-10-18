import services.company_service.shemas
import services.company_service.models
import sqlalchemy.ext.asyncio


async def create_company(
    data: services.company_service.shemas.CompanyCreateSchema,
    db: sqlalchemy.ext.asyncio.AsyncSession,
) -> services.company_service.models.CompanyInfo:
    """Создаёт новую компанию в базе данных."""
    new_company = services.company_service.models.CompanyInfo(
        representative_name=data.representative_name,
        representative_surname=data.representative_surname,
        company_name=data.company_name,
        logo=data.logo,
        inn=data.inn,
        contact_number=data.contact_number,
        contact_email=data.contact_email,
    )
    db.add(new_company)
    await db.commit()
    await db.refresh(new_company)
    return new_company


async def update_company(
    data: services.company_service.shemas.CompanyUpdateSchema,
    db: sqlalchemy.ext.asyncio.AsyncSession,
) -> services.company_service.models.CompanyInfo:
    """Обновляет компанию по её ID."""
    result = await db.execute(
        sqlalchemy.select(services.company_service.models.CompanyInfo).where(
            services.company_service.models.CompanyInfo.id == data.id
        )
    )
    company: services.company_service.models.CompanyInfo | None = (
        result.scalar_one_or_none()
    )
    if not company:
        raise ValueError(f"Company with id {data.id} not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(company, field, value)
    await db.commit()
    await db.refresh(company)
    return company


async def delete_company(
    company_id: int, db: sqlalchemy.ext.asyncio.AsyncSession
) -> None:
    result = await db.execute(
        sqlalchemy.select(services.company_service.models.CompanyInfo).where(
            services.company_service.models.CompanyInfo.id == company_id
        )
    )
    company: services.company_service.models.CompanyInfo | None = (
        result.scalar_one_or_none()
    )
    if not company:
        raise ValueError(f"Company with id {company_id} not found")
    await db.delete(company)
    await db.commit()
