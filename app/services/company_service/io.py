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
