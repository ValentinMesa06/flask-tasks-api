from config import (
    Config,
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig
)

def test_base_config():
    assert Config.SQLALCHEMY_TRACK_MODIFICATIONS is False

def test_development_config():
    assert DevelopmentConfig.SQLALCHEMY_DATABASE_URI == "sqlite:///tasks.db"

def test_testing_config():
    assert TestingConfig.TESTING is True
    assert TestingConfig.SQLALCHEMY_DATABASE_URI == "sqlite:///:memory:"

def test_production_config():
    assert hasattr(ProductionConfig, "SQLALCHEMY_DATABASE_URI")