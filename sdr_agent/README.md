
Ativar o venv

    source venv/bin/activate

Verificar ambiente

    python -c "from dotenv import load_dotenv; import os; print('OPENAI_loaded?'), bool(os.getenv('OPENAI_API_KEY'))"