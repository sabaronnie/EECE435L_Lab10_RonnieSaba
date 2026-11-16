"""Deploy the greeting application locally and run the deployed copy."""

import argparse
from pathlib import Path
import runpy
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--destination",
        type=Path,
        default=(
            Path.home() / "jenkins_deployments" / "Python-CI-CD_RonnieSaba"
        ),
        help="Directory where app.py will be deployed.",
    )
    args = parser.parse_args()

    source = Path(__file__).resolve().parent / "app.py"
    destination = args.destination.expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)
    deployed_app = destination / "app.py"
    shutil.copy2(source, deployed_app)

    print(f"Deployed application to: {deployed_app}")
    print("Running deployed application:")
    runpy.run_path(str(deployed_app), run_name="__main__")
    print("Local deployment successful.")


if __name__ == "__main__":
    main()
