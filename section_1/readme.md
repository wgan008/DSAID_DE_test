# README

## Assumption
1. The input file is available at `s3://mybucket/input_data/dataset.csv` at 1am on daily basis
2. Airflow has write access to destination directory `s3://mybucket/output_data/`

## Sync python script to airflow file directory via CI
```
cp section1.py /home/airflow/airflow/dags/scripts/
```

## How it works
After airflow job is enabled, the job will read the input file at 1am everyday and process it. A result file will be written once completion.