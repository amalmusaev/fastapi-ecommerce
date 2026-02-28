from fastapi import FastAPI

from app.routers import categories_router, products_router, users_router


# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="0.1.0",
)

# Подключаем маршруты категорий и товаров
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(users_router)


# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}
