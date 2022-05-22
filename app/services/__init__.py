# flake8: noqa F401
from .doc_generator_service import DocGenerator
from .supabase import SupabaseClient, SupabaseMock

doc_generator = DocGenerator()
db = SupabaseClient()
