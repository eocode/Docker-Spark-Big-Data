# Spark Projects with Docker

Project build using: https://github.com/big-data-europe/docker-spark

Supported versions:

* Spark 3.0.0 for Hadoop 3.2 with OpenJDK 8 and Scala 2.12
* Spark 2.4.5 for Hadoop 2.7+ with OpenJDK 8

## How to start

```bash
docker-compose up
```

Master:
http://localhost:8080

Workers:
http://localhost:8081
http://localhost:8082

## Python examples

Run pyspark CLI:

```sh
# Run CLI
./spark/bin/pyspark
# Execute a file
cd home/python/example
./../../../spark/bin/spark-submit example.py data.csv
```

**Spark monitor:**

http://localhost:4040

http://localhost:4041