-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "beer_table" (
    "beer_id" INT   NOT NULL,
    "beer_name" VARCHAR   NOT NULL,
    "brewery_name" VARCHAR   NOT NULL,
    "beer_style" VARCHAR   NOT NULL,
    "abv" DECIMAL   NOT NULL,
    "score" INT   NOT NULL,
    "avg_score" DECIMAL   NOT NULL,
    "ratings" INT   NOT NULL,
    "availability" VARCHAR   NOT NULL,
    "brew_state" VARCHAR   NOT NULL,
    "brew_city" VARCHAR   NOT NULL,
    "lat" DECIMAL   NOT NULL,
    "lng" DECIMAL   NOT NULL,
    CONSTRAINT "pk_beer_table" PRIMARY KEY (
        "beer_id"
     )
);

CREATE TABLE "reviews_table" (
    "review_id" INT   NOT NULL,
    "beer_id" INT   NOT NULL,
    "state" VARCHAR   NOT NULL,
    "state_id" INT   NOT NULL,
    CONSTRAINT "pk_reviews_table" PRIMARY KEY (
        "review_id"
     )
);

CREATE TABLE "visitor_log" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR   NOT NULL,
    "style" VARCHAR   NOT NULL,
	"lat" DECIMAL NOT NULL,
	"long" DECIMAL NOT NULL
     );


ALTER TABLE "reviews_table" ADD CONSTRAINT "fk_reviews_table_beer_id" FOREIGN KEY("beer_id")
REFERENCES "beer_table" ("beer_id");

