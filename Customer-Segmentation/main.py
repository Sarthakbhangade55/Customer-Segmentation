import os
import subprocess
import sys


def install_requirements():
    print("\nChecking required libraries...")

    try:
        import pandas
        import numpy
        import matplotlib
        import seaborn
        import sklearn

        print("All required libraries are installed.")

    except ImportError:
        print("Installing required libraries...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )


def create_folders():
    folders = [
        "data",
        "outputs",
        "outputs/charts",
        "src"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def run_script(script):
    print("\n" + "=" * 70)
    print(f"Running: {script}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)


def main():

    print("=" * 70)
    print("       CUSTOMER SEGMENTATION PROJECT")
    print("=" * 70)

    create_folders()
    install_requirements()

    run_script("src/data_cleaning.py")
    run_script("src/eda.py")
    run_script("src/segmentation.py")
    run_script("src/insights.py")

    print("\n" + "=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nGenerated files:")

    print("\nData:")
    print("  data/customers.csv")
    print("  outputs/customer_segments.csv")

    print("\nCharts:")
    print("  outputs/charts/")

    print("\nYou can now open the CSV in Excel or Power BI.")


if __name__ == "__main__":
    main()