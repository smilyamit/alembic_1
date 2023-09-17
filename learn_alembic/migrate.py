from alembic import command
from alembic.config import Config

# Modify the path to reflect the location of your alembic.ini
alembic_cfg = Config("alembic.ini")

def upgrade():
    command.upgrade(alembic_cfg, "head")

def downgrade():
    command.downgrade(alembic_cfg, "base")

if __name__ == "__main__":
    # Perform upgrade
    upgrade()

    # Perform downgrade
    downgrade()
