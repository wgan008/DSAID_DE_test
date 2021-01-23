# Readme
## Build the docker image under `section_2` directory
```
docker build .
```

## Start a container form the new image
```
docker run -e POSTGRES_PASSWORD=password -p 5432:5432 <your image tag>
```


## Connect to postgres instance
```
docker exec -it <your container ID> bash
```


## Run psql commands
```
psql -h localhost -p 5432 -U postgres
```

show table `car`:

```
postgres=# \d car;
                              Table "public.car"
       Column        |          Type          | Collation | Nullable | Default
---------------------+------------------------+-----------+----------+---------
 carserialno         | integer                |           | not null |
 manufacturer        | character varying(200) |           | not null |
 modelname           | character varying(200) |           |          |
 modelvariant        | character varying(200) |           |          |
 weight              | integer                |           |          |
 enginecubiccapacity | integer                |           |          |
 price               | integer                |           | not null |
 resale              | boolean                |           | not null |
Indexes:
    "car_pkey" PRIMARY KEY, btree (carserialno)
Referenced by:
    TABLE "salesinvoice" CONSTRAINT "salesinvoice_carserialno_fkey" FOREIGN KEY (carserialno) REFERENCES car(carserialno)
```
