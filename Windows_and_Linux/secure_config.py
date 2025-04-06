import os
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional

class SecureConfig:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self.env_prefix = "WRITING_TOOLS_"
        self.load_config()

    def load_config(self) -> None:
        """Load configuration from file and environment variables."""
        try:
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
            
            # Update env prefix if specified in config
            if "secure_config" in self.config:
                self.env_prefix = self.config["secure_config"].get("env_var_prefix", self.env_prefix)

            # Load API keys from environment variables if enabled
            if self.config.get("secure_config", {}).get("use_env_vars", True):
                self._load_env_vars()
        except Exception as e:
            logging.error(f"Error loading config: {e}")
            raise

    def _load_env_vars(self) -> None:
        """Load sensitive data from environment variables."""
        for provider, settings in self.config.get("providers", {}).items():
            if settings.get("use_env", False):
                env_key = f"{self.env_prefix}{provider.upper().replace(' ', '_')}_API_KEY"
                if env_key in os.environ:
                    settings["api_key"] = os.environ[env_key]

    def get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for a provider, checking environment variables first."""
        if provider not in self.config.get("providers", {}):
            return None

        settings = self.config["providers"][provider]
        if settings.get("use_env", False):
            env_key = f"{self.env_prefix}{provider.upper().replace(' ', '_')}_API_KEY"
            return os.environ.get(env_key)
        
        return settings.get("api_key")

    def set_api_key(self, provider: str, api_key: str, use_env: bool = True) -> None:
        """Set API key for a provider, optionally using environment variables."""
        if provider not in self.config.get("providers", {}):
            raise ValueError(f"Provider {provider} not found in config")

        if use_env:
            env_key = f"{self.env_prefix}{provider.upper().replace(' ', '_')}_API_KEY"
            os.environ[env_key] = api_key
            self.config["providers"][provider]["use_env"] = True
            self.config["providers"][provider]["api_key"] = ""
        else:
            self.config["providers"][provider]["use_env"] = False
            self.config["providers"][provider]["api_key"] = api_key

        self._save_config()

    def _save_config(self) -> None:
        """Save configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            logging.error(f"Error saving config: {e}")
            raise

    def get_config(self) -> Dict[str, Any]:
        """Get the current configuration."""
        return self.config.copy() 