import time
import yaml
from pathlib import Path


def load_config(config_path: Path) -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def train(config: dict) -> None:
    print("Starting training with config:")
    for k, v in config.items():
        print(f"  {k}: {v}")

    epochs = config.get("epochs", 1)

    for epoch in range(1, epochs + 1):
        print(f"Epoch {epoch}/{epochs} - training...")
        time.sleep(0.5)

    print("Training complete!")


def main():
    config_path = Path("configs/base.yaml")
    config = load_config(config_path)
    train(config)


if __name__ == "__main__":
    main()
