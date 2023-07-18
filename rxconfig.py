import reflex as rx

class NflfantasygmConfig(rx.Config):
    pass

config = NflfantasygmConfig(
    app_name="nfl_fantasy_gm",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)