CREATE TABLE car(
   carSerialNo         integer PRIMARY KEY     NOT NULL,
   manufacturer        VARCHAR(200)    NOT NULL,
   modelName           VARCHAR(200),
   modelVariant        VARCHAR(200),
   weight              INT,
   engineCubicCapacity INT,
   price               INT    NOT NULL,
   resale              BOOLEAN NOT NULL
);

CREATE TABLE customer(
   customerId         SERIAL PRIMARY KEY,
   customerName        VARCHAR(200)    NOT NULL,
   customerPhone       VARCHAR(200)
);

CREATE TABLE salesperson(
   salespersonId         SERIAL PRIMARY KEY,
   salespersonName        VARCHAR(200)    NOT NULL DEFAULT 'admin'
);

CREATE TABLE salesInvoice(
   salesInvoiceId     SERIAL PRIMARY KEY,
   customerId         integer REFERENCES customer,
   carSerialNo        integer REFERENCES car,
   salespersonId      integer REFERENCES salesperson,
   CreatedAt          timestamp NOT NULL DEFAULT  CURRENT_TIMESTAMP
);
