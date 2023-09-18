# -*- coding: utf-8 -*-
from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool

config = context.config
target_metadata = None

def run_migrations_offline():
    ...
    # Leave the rest of the content unchanged

def run_migrations_online():
    ...
    # Leave the rest of the content unchanged

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
