import pynecone as pc

class NflfantasygmConfig(pc.Config):
    pass

config = NflfantasygmConfig(
    app_name="nfl_fantasy_gm",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)